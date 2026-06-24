"""
Daily stats updater for giga-meter-docs README.md.
Fetches live counts from the Giga Meter API and regenerates the country flag grid PNG.
Renders at 2x resolution (1440px wide) for crisp display on retina screens.
"""

import io
import math
import os
import re
import sys

import requests
from PIL import Image, ImageDraw, ImageFont

API_BASE = "https://uni-ooi-giga-meter-backend.azurewebsites.net"
API_KEY = os.environ.get("GIGA_API_KEY", "")
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

README_PATH = "README.md"
GRID_PATH = ".gitbook/assets/country-grid.png"

# Brand colours
GIGA_BLUE     = (39, 122, 255)   # #277AFF
GIGA_BLUE_MID = (26,  95, 212)   # placeholder flag tint
WHITE         = (255, 255, 255)

CANVAS_W = 1440


# ── Font loading ────────────────────────────────────────────────────────────

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MANROPE_BOLD = os.path.join(SCRIPT_DIR, "Manrope-Bold.ttf")

def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = []
    if bold:
        candidates += [
            MANROPE_BOLD,  # bundled — works on both macOS and Linux
            "/usr/share/fonts/truetype/open-sans/OpenSans-SemiBold.ttf",
            "/usr/share/fonts/truetype/open-sans/OpenSans-Bold.ttf",
            "/usr/share/fonts/truetype/lato/Lato-Bold.ttf",
            "/Library/Fonts/Arial Unicode.ttf",
        ]
    else:
        candidates += [
            MANROPE_BOLD,
            "/usr/share/fonts/truetype/open-sans/OpenSans-Regular.ttf",
            "/usr/share/fonts/truetype/lato/Lato-Regular.ttf",
            "/Library/Fonts/Arial Unicode.ttf",
        ]
    candidates += [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for path in candidates:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


# ── API helpers ─────────────────────────────────────────────────────────────

def fetch_countries() -> list[dict]:
    """Paginate countries endpoint (max size=100 per page). Deduplicate by ISO2."""
    all_countries: list[dict] = []
    seen_iso2: set[str] = set()
    page = 0
    while True:
        resp = requests.get(
            f"{API_BASE}/api/v1/dailycheckapp_countries",
            params={"size": 100, "page": page},
            headers=HEADERS,
            timeout=30,
        )
        resp.raise_for_status()
        batch = resp.json().get("data", [])
        if not batch:
            break
        for c in batch:
            iso2 = c.get("code", "").upper()
            if iso2 and iso2 not in seen_iso2:
                seen_iso2.add(iso2)
                all_countries.append(c)
        page += 1
    print(f"  Countries fetched (deduplicated): {len(all_countries)}")
    return all_countries


def fetch_school_count(active_countries: list[dict]) -> int:
    """Count unique giga_id_school values in countries that have measurements."""
    active_iso2 = {c.get("code", "").upper() for c in active_countries}
    seen: set[str] = set()
    page = 0
    while True:
        resp = requests.get(
            f"{API_BASE}/api/v1/dailycheckapp_schools",
            params={"size": 100, "page": page},
            headers=HEADERS,
            timeout=30,
        )
        resp.raise_for_status()
        batch = resp.json().get("data", [])
        if not batch:
            break
        for school in batch:
            if school.get("country_code", "").upper() not in active_iso2:
                continue
            giga_id = school.get("giga_id_school")
            if giga_id:
                seen.add(str(giga_id))
        page += 1
        if page % 10 == 0:
            print(f"  Schools paginated: page {page}, {len(seen)} unique so far")
    print(f"  Schools total (unique giga_id_school, active countries): {len(seen)}")
    return len(seen)


def fetch_measurement_count() -> int:
    resp = requests.get(
        f"{API_BASE}/api/v1/measurements",
        params={"size": 1, "orderBy": "-timestamp"},
        headers=HEADERS,
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json().get("data", [])
    if not data:
        return 0
    count = int(data[0].get("id", 0))
    print(f"  Measurement count (approx via latest ID): {count:,}")
    return count


def filter_countries_with_measurements(countries: list[dict]) -> list[dict]:
    """Keep only countries that have at least one measurement record."""
    active = []
    for c in countries:
        iso3 = c.get("code_iso3", "")
        if not iso3:
            continue
        try:
            resp = requests.get(
                f"{API_BASE}/api/v1/measurements",
                params={"size": 1, "country_iso3_code": iso3},
                headers=HEADERS,
                timeout=15,
            )
            resp.raise_for_status()
            if resp.json().get("data"):
                active.append(c)
            else:
                print(f"  Skipping {c.get('name', iso3)} — no measurements")
        except Exception as e:
            print(f"  Warning: could not check {iso3}: {e}")
    print(f"  Active countries (with measurements): {len(active)}")
    return active


# ── Flag fetching ────────────────────────────────────────────────────────────

def fetch_flag(iso2: str) -> Image.Image | None:
    url = f"https://flagcdn.com/w160/{iso2.lower()}.png"
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            return Image.open(io.BytesIO(resp.content)).convert("RGBA")
    except Exception:
        pass
    return None


def round_corners(img: Image.Image, radius: int) -> Image.Image:
    img = img.convert("RGBA")
    mask = Image.new("L", img.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        [(0, 0), (img.width - 1, img.height - 1)], radius=radius, fill=255
    )
    img.putalpha(mask)
    return img


# ── Country grid ─────────────────────────────────────────────────────────────

def generate_grid(countries: list[dict], schools: int = 0, measurements: int = 0) -> Image.Image:
    countries_sorted = sorted(countries, key=lambda c: c.get("name", ""))
    n = len(countries_sorted)

    # Layout
    OUTER_H = 44          # left/right outer margin
    OUTER_V = 28          # top/bottom outer margin
    LEFT_COL_W = 260      # text column width
    COL_GAP = 32          # gap between text col and flags
    RIGHT_PAD = 32
    GRID_ROWS = 4
    CELL_GAP_H = 10
    CELL_GAP_V = 12
    CORNER_R = 5

    flags_x0 = OUTER_H + LEFT_COL_W + COL_GAP
    flag_area_w = CANVAS_W - flags_x0 - RIGHT_PAD
    grid_cols = math.ceil(n / GRID_ROWS)
    flag_w = (flag_area_w - CELL_GAP_H * (grid_cols - 1)) // grid_cols
    flag_h = flag_w * 2 // 3
    cell_h = flag_h + CELL_GAP_V
    total_h = OUTER_V * 2 + GRID_ROWS * cell_h

    img = Image.new("RGB", (CANVAS_W, total_h), GIGA_BLUE)
    draw = ImageDraw.Draw(img)

    # Left column: "Deployed in\nX countries"
    line1, line2 = "Deployed in", f"{n} countries"
    font_size = 56
    font = load_font(font_size, bold=True)
    while font_size > 18:
        font = load_font(font_size, bold=True)
        w1 = draw.textbbox((0, 0), line1, font=font)[2]
        w2 = draw.textbbox((0, 0), line2, font=font)[2]
        if max(w1, w2) <= LEFT_COL_W:
            break
        font_size -= 2

    b1 = draw.textbbox((0, 0), line1, font=font)
    b2 = draw.textbbox((0, 0), line2, font=font)
    h1, h2 = b1[3] - b1[1], b2[3] - b2[1]
    line_gap = 6
    text_total_h = h1 + line_gap + h2
    text_y = (total_h - text_total_h) // 2

    draw.text((OUTER_H, text_y), line1, font=font, fill=WHITE)
    draw.text((OUTER_H, text_y + h1 + line_gap), line2, font=font, fill=WHITE)

    # Flags grid
    for i, country in enumerate(countries_sorted):
        col = i % grid_cols
        row = i // grid_cols
        x = flags_x0 + col * (flag_w + CELL_GAP_H)
        y = OUTER_V + row * cell_h

        flag = fetch_flag(country.get("code", ""))
        if flag:
            flag = round_corners(flag.resize((flag_w, flag_h), Image.LANCZOS), CORNER_R)
            img.paste(flag, (x, y), flag)
        else:
            draw.rounded_rectangle(
                [(x, y), (x + flag_w, y + flag_h)], radius=CORNER_R, fill=GIGA_BLUE_MID
            )

    return img


# ── README updater ───────────────────────────────────────────────────────────

def update_readme(countries_count: int, schools_count: int, measurements_count: int) -> None:
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    stats_block = (
        "<!-- stats-start -->\n"
        "{% columns %}\n"
        "{% column %}\n"
        f"## {countries_count:,}\n\n"
        "Countries\n"
        "{% endcolumn %}\n\n"
        "{% column %}\n"
        f"## {schools_count:,}\n\n"
        "Schools\n"
        "{% endcolumn %}\n\n"
        "{% column %}\n"
        f"## {measurements_count:,}\n\n"
        "Measurements\n"
        "{% endcolumn %}\n"
        "{% endcolumns %}\n"
        "<!-- stats-end -->"
    )
    content = re.sub(
        r"<!-- stats-start -->.*?<!-- stats-end -->",
        stats_block, content, flags=re.DOTALL,
    )

    grid_block = (
        "<!-- country-grid-start -->\n"
        "![](docs/assets/country-grid.png)\n"
        "<!-- country-grid-end -->"
    )
    content = re.sub(
        r"<!-- country-grid-start -->.*?<!-- country-grid-end -->",
        grid_block, content, flags=re.DOTALL,
    )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"  README updated: {countries_count} countries, {schools_count:,} schools, {measurements_count:,} measurements")


# ── Main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    if not API_KEY:
        print("ERROR: GIGA_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    print("Fetching countries...")
    countries = fetch_countries()

    print("Filtering to countries with measurements...")
    countries = filter_countries_with_measurements(countries)

    print("Fetching school count...")
    schools = fetch_school_count(countries)

    print("Fetching measurement count...")
    measurements = fetch_measurement_count()

    print("Generating country grid image...")
    grid_img = generate_grid(countries, schools, measurements)
    os.makedirs(".gitbook/assets", exist_ok=True)
    grid_img.save(GRID_PATH, "PNG", optimize=True)
    print(f"  Saved: {GRID_PATH} ({grid_img.size[0]}×{grid_img.size[1]}px)")

    print("Updating README.md...")
    update_readme(len(countries), schools, measurements)

    print("Done.")


if __name__ == "__main__":
    main()
