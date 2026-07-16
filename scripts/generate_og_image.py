"""Generate the branded 1200x630 social-preview image."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "static" / "og-image.png"

PAPER = "#f6f2e8"
INK = "#211c16"
INK_MUTE = "#8a8170"
ANCHOR = "#1f4636"
ANCHOR_DARK = "#163528"
ACCENT = "#d99b1f"
ACCENT_DARK = "#b87f12"
HIGHLIGHT = "#f4d98a"
ON_ANCHOR = "#f3efe2"


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(Path("C:/Windows/Fonts") / name, size=size)


def main() -> None:
    image = Image.new("RGB", (1200, 630), PAPER)
    draw = ImageDraw.Draw(image)

    display = font("georgia.ttf", 70)
    display_bold = font("georgiab.ttf", 70)
    body_bold = font("arialbd.ttf", 25)
    utility = font("consola.ttf", 20)

    # Kicker and title block.
    draw.rounded_rectangle((72, 70, 99, 74), radius=2, fill=ACCENT)
    draw.text((112, 57), "A DC YOUTH JUSTICE COALITION", font=utility, fill=INK_MUTE)

    draw.text((72, 130), "A smaller, fairer,", font=display, fill=INK)
    draw.rectangle((70, 283, 420, 315), fill=HIGHLIGHT)
    draw.text((72, 208), "more just system", font=display_bold, fill=INK)
    draw.text((72, 286), "for DC’s young", font=display, fill=INK)
    draw.text((72, 364), "people.", font=display, fill=INK)

    draw.text((74, 548), "Youth Justice Project", font=body_bold, fill=ANCHOR)

    # The site's sunrise mark, enlarged into a social-card signature.
    center_x = 955
    baseline = 574
    for radius, color in (
        (225, ANCHOR_DARK),
        (174, ANCHOR),
        (122, ACCENT_DARK),
        (70, ACCENT),
    ):
        draw.pieslice(
            (center_x - radius, baseline - radius, center_x + radius, baseline + radius),
            start=180,
            end=360,
            fill=color,
        )
    draw.line((716, baseline, 1180, baseline), fill=INK, width=3)
    draw.ellipse((925, 196, 985, 256), fill=HIGHLIGHT)
    draw.ellipse((915, 186, 995, 266), outline="#edcf72", width=7)

    # A quiet frame makes the cream card legible against white feeds.
    draw.rectangle((0, 0, 1199, 629), outline="#d7ccb6", width=2)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    image.save(OUTPUT, format="PNG", optimize=True)


if __name__ == "__main__":
    main()
