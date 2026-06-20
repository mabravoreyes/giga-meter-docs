"""
Daily stats updater for giga-meter-docs README.md.
Fetches live counts from the Giga Meter API and regenerates the country flag grid PNG.
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
GIGA_BLUE = "#277AFF"
GIGA_BLUE_DARK = "#1A5FD4"   # silhouette tint — slightly darker than background
WHITE = "#FFFFFF"

GRID_COLS = 8
CANVAS_WIDTH = 780
H_PAD = 20
CELL_WIDTH = (CANVAS_WIDTH - H_PAD * 2) // GRID_COLS  # ~92px
FLAG_W, FLAG_H = 40, 28
NAME_H = 13
CELL_HEIGHT = FLAG_H + 4 + NAME_H + 10   # flag + gap + text + bottom pad


# ---------------------------------------------------------------------------
# Font loading — try Open Sans (matches brand), fall back to DejaVuSans
# ---------------------------------------------------------------------------

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
    candidates += ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]
    for path in candidates:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


# ---------------------------------------------------------------------------
# API helpers
# ---------------------------------------------------------------------------

def fetch_countries() -> list[dict]:
    """Paginate countries endpoint (max size=100 per page)."""
    all_countries: list[dict] = []
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
        all_countries.extend(batch)
        page += 1
    print(f"  Countries fetched: {len(all_countries)}")
    return all_countries


def fetch_school_count() -> int:
    page = 0
    total = 0
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


# ---------------------------------------------------------------------------
# Flag fetching
# ---------------------------------------------------------------------------

def fetch_flag(iso2: str) -> Image.Image | None:
    url = f"https://flagcdn.com/w40/{iso2.lower()}.png"
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            return Image.open(io.BytesIO(resp.content)).convert("RGBA").resize(
                (FLAG_W, FLAG_H), Image.LANCZOS
            )
    except Exception:
        pass
    return None


def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    h = hex_color.lstrip("#")
    return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


# ---------------------------------------------------------------------------
# Country grid image — Giga-branded: blue background, white text
# ---------------------------------------------------------------------------

def generate_grid(countries: list[dict]) -> Image.Image:
    countries_sorted = sorted(countries, key=lambda c: c.get("name", ""))
    n = len(countries_sorted)
    rows = (n + GRID_COLS - 1) // GRID_COLS

    # Layout heights
    header_h = 52          # logo strip + "Deployed in X countries"
    grid_top_pad = 12
    grid_h = rows * CELL_HEIGHT
    bottom_pad = 20
    total_h = header_h + grid_top_pad + grid_h + bottom_pad

    bg_rgb = hex_to_rgb(GIGA_BLUE)
    img = Image.new("RGB", (CANVAS_WIDTH, total_h), bg_rgb)
    draw = ImageDraw.Draw(img)

    # Header: "Deployed in X countries" — white, semibold
    font_header = load_font(14, bold=True)
    header_text = f"Deployed in {n} countries"
    header_y = (header_h - 18) // 2
    draw.text((H_PAD, header_y), header_text, font=font_header, fill=WHITE)

    # Subtle divider line below header
    divider_y = header_h - 1
    draw.line([(0, divider_y), (CANVAS_WIDTH, divider_y)], fill=(255, 255, 255, 40), width=1)

    # Grid of flags + country names
    font_label = load_font(9, bold=False)
    grid_y0 = header_h + grid_top_pad

    for i, country in enumerate(countries_sorted):
        col = i % GRID_COLS
        row = i // GRID_COLS
        cell_x = H_PAD + col * CELL_WIDTH
        cell_y = grid_y0 + row * CELL_HEIGHT

        # Flag — centred in cell
        flag_x = cell_x + (CELL_WIDTH - FLAG_W) // 2
        flag = fetch_flag(country.get("code", ""))
        if flag:
            # Paste with alpha mask
            img.paste(flag, (flag_x, cell_y), flag)
        else:
            # Placeholder: slightly lighter blue rectangle
            dark_rgb = hex_to_rgb(GIGA_BLUE_DARK)
            draw.rectangle(
                [(flag_x, cell_y), (flag_x + FLAG_W, cell_y + FLAG_H)],
                fill=dark_rgb,
            )

        # Country name — white, centred
        name = country.get("name", "")
        if len(name) > 12:
            name = name[:11] + "…"
        text_y = cell_y + FLAG_H + 4
        bbox = draw.textbbox((0, 0), name, font=font_label)
        text_w = bbox[2] - bbox[0]
        text_x = cell_x + (CELL_WIDTH - text_w) // 2
        draw.text((text_x, text_y), name, font=font_label, fill=WHITE)

    return img


# ---------------------------------------------------------------------------
# README updater
# ---------------------------------------------------------------------------

def update_readme(
    countries_count: int,
    schools_count: int,
    measurements_count: int,
) -> None:
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
        stats_block,
        content,
        flags=re.DOTALL,
    )

    grid_block = (
        "<!-- country-grid-start -->\n"
        "![](docs/assets/country-grid.png)\n"
        "<!-- country-grid-end -->"
    )
    content = re.sub(
        r"<!-- country-grid-start -->.*?<!-- country-grid-end -->",
        grid_block,
        content,
        flags=re.DOTALL,
    )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(
        f"  README updated: {countries_count} countries, "
        f"{schools_count:,} schools, {measurements_count:,} measurements"
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    if not API_KEY:
        print("ERROR: GIGA_API_KEY environment variable not set", file=sys.stderr)
        sys.exit(1)

    print("Fetching countries...")
    countries = fetch_countries()

    print("Fetching school count (paginating)...")
    schools = fetch_school_count()

    print("Fetching measurement count...")
    measurements = fetch_measurement_count()

    print("Generating country grid image...")
    grid_img = generate_grid(countries)
    os.makedirs("docs/assets", exist_ok=True)
    grid_img.save(GRID_PATH, "PNG", optimize=True)
    print(f"  Saved: {GRID_PATH}")

    print("Updating README.md...")
    update_readme(len(countries), schools, measurements)

    print("Done.")


if __name__ == "__main__":
    main()
