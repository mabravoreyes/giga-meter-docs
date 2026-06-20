"""
Daily stats updater for giga-meter-docs README.md.
Fetches live counts from the Giga Meter API and regenerates the country flag grid PNG.
Renders at 2x resolution (1440px wide) for crisp display on retina screens.
"""

import io
import os
import re
import sys

import requests
from PIL import Image, ImageDraw, ImageFont

API_BASE = "https://uni-ooi-giga-meter-backend.azurewebsites.net"
API_KEY = os.environ.get("GIGA_API_KEY", "")
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

README_PATH = "README.md"
GRID_PATH = "docs/assets/country-grid.png"

# Brand colours (matches gigabrand.vercel.app social media card)
GIGA_BLUE     = (39, 122, 255)   # #277AFF
GIGA_BLUE_MID = (26,  95, 212)   # #1A5FD4 — placeholder flag tint
WHITE         = (255, 255, 255)

# ── Layout (all values are source pixels at 2x; display size is half) ──────
CANVAS_W   = 1440
GRID_COLS  = 10
H_PAD      = 40                                 # left/right margin
FLAG_W     = 110                                # → 55px visual
FLAG_H     = 73                                 # → 36px visual (≈3:2 ratio)
CELL_GAP_H = 14                                 # horizontal gap between cells
CELL_GAP_V = 14                                 # vertical gap between cells
CELL_W     = (CANVAS_W - H_PAD * 2 - CELL_GAP_H * (GRID_COLS - 1)) // GRID_COLS
CELL_H     = FLAG_H + CELL_GAP_V
HEADER_H   = 64
GRID_PAD_T = 16
BOTTOM_PAD = 20


# ── Font loading ────────────────────────────────────────────────────────────

def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = []
    if bold:
        candidates += [
            "/usr/share/fonts/truetype/open-sans/OpenSans-SemiBold.ttf",
            "/usr/share/fonts/truetype/open-sans/OpenSans-Bold.ttf",
            "/usr/share/fonts/truetype/lato/Lato-Bold.ttf",
        ]
    else:
        candidates += [
            "/usr/share/fonts/truetype/open-sans/OpenSans-Regular.ttf",
            "/usr/share/fonts/truetype/lato/Lato-Regular.ttf",
        ]
    candidates.append("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
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


def fetch_school_count() -> int:
    page, total = 0, 0
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
        total += len(batch)
        page += 1
        if page % 10 == 0:
            print(f"  Schools paginated: {total} so far (page {page})")
    print(f"  Schools total: {total}")
    return total


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
    # Use w160 for high quality; scale down to FLAG_W × FLAG_H
    url = f"https://flagcdn.com/w160/{iso2.lower()}.png"
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            return (
                Image.open(io.BytesIO(resp.content))
                .convert("RGBA")
                .resize((FLAG_W, FLAG_H), Image.LANCZOS)
            )
    except Exception:
        pass
    return None


# ── Country grid ─────────────────────────────────────────────────────────────

def generate_grid(countries: list[dict]) -> Image.Image:
    countries_sorted = sorted(countries, key=lambda c: c.get("name", ""))
    n = len(countries_sorted)
    rows = (n + GRID_COLS - 1) // GRID_COLS

    total_h = HEADER_H + GRID_PAD_T + rows * CELL_H + BOTTOM_PAD
    img = Image.new("RGB", (CANVAS_W, total_h), GIGA_BLUE)
    draw = ImageDraw.Draw(img)

    # Header: "Deployed in X countries"
    font_header = load_font(26, bold=True)
    draw.text((H_PAD, (HEADER_H - 30) // 2), f"Deployed in {n} countries",
              font=font_header, fill=WHITE)

    # Divider
    draw.line([(0, HEADER_H - 1), (CANVAS_W, HEADER_H - 1)],
              fill=(80, 148, 255), width=1)

    grid_y0 = HEADER_H + GRID_PAD_T

    for i, country in enumerate(countries_sorted):
        col = i % GRID_COLS
        row = i // GRID_COLS
        x = H_PAD + col * (CELL_W + CELL_GAP_H)
        y = grid_y0 + row * CELL_H

        flag = fetch_flag(country.get("code", ""))
        if flag:
            img.paste(flag, (x, y), flag)
        else:
            draw.rectangle([(x, y), (x + FLAG_W, y + FLAG_H)], fill=GIGA_BLUE_MID)

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
    schools = fetch_school_count()

    print("Fetching measurement count...")
    measurements = fetch_measurement_count()

    print("Generating country grid image...")
    grid_img = generate_grid(countries)
    os.makedirs("docs/assets", exist_ok=True)
    grid_img.save(GRID_PATH, "PNG", optimize=True)
    print(f"  Saved: {GRID_PATH} ({grid_img.size[0]}×{grid_img.size[1]}px)")

    print("Updating README.md...")
    update_readme(len(countries), schools, measurements)

    print("Done.")


if __name__ == "__main__":
    main()
