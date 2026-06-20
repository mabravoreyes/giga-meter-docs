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

GIGA_BLUE = "#00A3E0"
GIGA_NAVY = "#1a2142"
GRID_COLS = 8
CANVAS_WIDTH = 780
CELL_PADDING_H = 20  # total horizontal padding (10 each side)
CELL_WIDTH = (CANVAS_WIDTH - CELL_PADDING_H * 2) // GRID_COLS  # ~92px
FLAG_W, FLAG_H = 40, 28
CELL_HEIGHT = FLAG_H + 4 + 13 + 10  # flag + gap + text + bottom pad


# ---------------------------------------------------------------------------
# Font loading
# ---------------------------------------------------------------------------

def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = []
    if bold:
        candidates += [
            "/usr/share/fonts/truetype/lato/Lato-Bold.ttf",
            "/usr/share/fonts/truetype/lato/Lato-Regular.ttf",
        ]
    else:
        candidates += [
            "/usr/share/fonts/truetype/lato/Lato-Regular.ttf",
            "/usr/share/fonts/truetype/lato/Lato-Bold.ttf",
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
    resp = requests.get(
        f"{API_BASE}/api/v1/dailycheckapp_countries",
        params={"size": 200},
        headers=HEADERS,
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json().get("data", [])
    print(f"  Countries fetched: {len(data)}")
    return data


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
    print(f"  Measurement count (approx): {count:,}")
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


# ---------------------------------------------------------------------------
# Country grid image
# ---------------------------------------------------------------------------

def generate_grid(countries: list[dict]) -> Image.Image:
    countries_sorted = sorted(countries, key=lambda c: c.get("name", ""))
    n = len(countries_sorted)
    rows = (n + GRID_COLS - 1) // GRID_COLS

    # Heights
    accent_h = 4
    subtitle_h = 32
    grid_top_pad = 8
    grid_h = rows * CELL_HEIGHT
    bottom_pad = 16
    total_h = accent_h + subtitle_h + grid_top_pad + grid_h + bottom_pad

    img = Image.new("RGBA", (CANVAS_WIDTH, total_h), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Top accent bar
    draw.rectangle([(0, 0), (CANVAS_WIDTH, accent_h)], fill=GIGA_BLUE)

    # Subtitle
    font_subtitle = load_font(12, bold=True)
    subtitle_y = accent_h + (subtitle_h - 14) // 2
    draw.text((20, subtitle_y), f"Deployed in {n} countries", font=font_subtitle, fill=GIGA_NAVY)

    # Grid
    font_label = load_font(9, bold=False)
    grid_y0 = accent_h + subtitle_h + grid_top_pad

    for i, country in enumerate(countries_sorted):
        col = i % GRID_COLS
        row = i // GRID_COLS
        cell_x = CELL_PADDING_H + col * CELL_WIDTH
        cell_y = grid_y0 + row * CELL_HEIGHT

        # Flag
        flag_x = cell_x + (CELL_WIDTH - FLAG_W) // 2
        flag = fetch_flag(country.get("code", ""))
        if flag:
            img.paste(flag, (flag_x, cell_y), flag)
        else:
            draw.rectangle(
                [(flag_x, cell_y), (flag_x + FLAG_W, cell_y + FLAG_H)],
                fill="#d0d0d0",
            )

        # Country name
        name = country.get("name", "")
        if len(name) > 12:
            name = name[:11] + "…"
        text_y = cell_y + FLAG_H + 4
        bbox = draw.textbbox((0, 0), name, font=font_label)
        text_w = bbox[2] - bbox[0]
        text_x = cell_x + (CELL_WIDTH - text_w) // 2
        draw.text((text_x, text_y), name, font=font_label, fill=GIGA_NAVY)

    return img.convert("RGB")


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

    # Stats block
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

    # Country grid block
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

    print(f"  README updated: {countries_count} countries, {schools_count:,} schools, {measurements_count:,} measurements")


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
