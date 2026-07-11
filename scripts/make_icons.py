"""Generate icon.svg, favicon.png, and apple-touch-icon.png for the DS23 guides site.
One-time icon builder. Run from the project root.
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

ROOT = Path(__file__).parent
ACCENT_1 = (13, 77, 122)
ACCENT_2 = (21, 101, 192)
WHITE = (255, 255, 255)


def gradient_bg(size):
    img = Image.new("RGB", (size, size), ACCENT_1)
    draw = ImageDraw.Draw(img)
    for y in range(size):
        t = y / max(1, size - 1)
        r = int(ACCENT_1[0] * (1 - t) + ACCENT_2[0] * t)
        g = int(ACCENT_1[1] * (1 - t) + ACCENT_2[1] * t)
        b = int(ACCENT_1[2] * (1 - t) + ACCENT_2[2] * t)
        draw.line([(0, y), (size, y)], fill=(r, g, b))
    return img


def pick_font(size_px):
    candidates = [
        "C:/Windows/Fonts/segoeuib.ttf",
        "C:/Windows/Fonts/seguibl.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
        "C:/Windows/Fonts/arial.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size_px)
    return ImageFont.load_default()


def draw_text_centered(draw, text, font, cx, cy, fill=WHITE):
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    draw.text((cx - w / 2 - bbox[0], cy - h / 2 - bbox[1]), text, font=font, fill=fill)


def render_icon(size):
    img = gradient_bg(size).convert("RGBA")
    draw = ImageDraw.Draw(img)

    book_font = pick_font(int(size * 0.42))
    ds_font = pick_font(int(size * 0.30))
    nb_font = pick_font(int(size * 0.21))

    # 📚 emoji rarely renders in PIL on Windows. Use clean typography instead:
    # Row 1: "DS"  (large)
    # Row 2: "23"  (smaller)
    # Underline bar between them for graph-feel.

    cx = size / 2
    cy_ds = size * 0.36
    cy_23 = size * 0.72

    draw_text_centered(draw, "DS", ds_font, cx, cy_ds)

    # accent bar
    bar_w = size * 0.42
    bar_h = max(2, int(size * 0.022))
    bar_x0 = cx - bar_w / 2
    bar_y0 = size * 0.54
    draw.rectangle(
        [bar_x0, bar_y0, bar_x0 + bar_w, bar_y0 + bar_h],
        fill=(255, 255, 255, 200),
    )

    draw_text_centered(draw, "23", nb_font, cx, cy_23)

    return img.convert("RGB")


def write_svg():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 180">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#0D4D7A"/>
      <stop offset="1" stop-color="#1565C0"/>
    </linearGradient>
  </defs>
  <rect width="180" height="180" rx="36" ry="36" fill="url(#g)"/>
  <text x="90" y="78" text-anchor="middle"
        font-family="Segoe UI, Arial, sans-serif" font-weight="800"
        font-size="58" fill="#ffffff" letter-spacing="-1">DS</text>
  <rect x="52" y="92" width="76" height="4" rx="2" fill="#ffffff" opacity="0.85"/>
  <text x="90" y="138" text-anchor="middle"
        font-family="Segoe UI, Arial, sans-serif" font-weight="700"
        font-size="40" fill="#ffffff" letter-spacing="-1">23</text>
</svg>
"""
    (ROOT / "icon.svg").write_text(svg, encoding="utf-8")


def main():
    write_svg()

    apple = render_icon(180)
    apple.save(ROOT / "apple-touch-icon.png", "PNG", optimize=True)

    fav = render_icon(192)
    fav.save(ROOT / "favicon.png", "PNG", optimize=True)

    # 32x32 fallback favicon for browsers that prefer it
    small = render_icon(64)
    small.save(ROOT / "favicon-32.png", "PNG", optimize=True)

    print("wrote: icon.svg, favicon.png, favicon-32.png, apple-touch-icon.png")


if __name__ == "__main__":
    main()
