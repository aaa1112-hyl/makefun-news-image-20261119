#!/usr/bin/env python3
"""Generate entry.png: a front-page-style summary of 19 November 2026 world news.

Dev-time generator only (needs Pillow + DejaVu fonts on this machine). The
submitted program is main.py, which copies the generated entry.png to
/output/entry.png. Re-run: python3 generate_image.py
Sources (checked 2026-11-19): One Turn daily brief on the Shenzhen summit,
Crimea bridge and Gulf strikes; Horizon daily brief on the ICJ Rohingya
ruling, COP31, Bangladesh unrest and the Van Gogh sale; FeedCast daily brief
on the Anthropic IPO, Netanyahu's Iran push and the IMF inflation warning;
Open Chronicle global brief on the Shenzhen summit and IAEA North Korea
warning.
"""
import textwrap

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (248, 244, 234)
INK = (24, 24, 24)
NAVY = (26, 46, 74)
RED = (176, 42, 30)
TEAL = (14, 110, 110)
GOLD = (176, 132, 24)
MUTED = (90, 90, 90)
RULE = (24, 24, 24)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap measured in pixels, not characters."""
    out = []
    for para in text.split("\n"):
        words = para.split(" ")
        line = ""
        for word in words:
            trial = (line + " " + word).strip()
            if draw.textlength(trial, font=fnt) <= width or not line:
                line = trial
            else:
                out.append(line)
                line = word
        if line:
            out.append(line)
    return out


def text_block(draw, x, y, text, fnt, fill, width, leading=6):
    lines = wrap(draw, text, fnt, width)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + leading
    return y


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    # border
    d.rectangle([10, 10, W - 11, H - 11], outline=RULE, width=3)

    # ---- masthead ----
    y = 24
    d.text((W // 2, y), "THE WORLD", font=font(SERIF_B, 88),
           fill=INK, anchor="ma")
    y = 126
    d.line([40, y, W - 40, y], fill=RULE, width=3)
    y += 10
    d.text((W // 2, y), "THURSDAY  •  19 NOVEMBER 2026  •  THE DAY IN ONE IMAGE",
           font=font(SANS_B, 23), fill=NAVY, anchor="ma")
    y += 34
    d.line([40, y, W - 40, y], fill=RULE, width=2)
    y += 12

    # ---- lead story ----
    d.text((40, y), "DIPLOMACY  —  SHENZHEN", font=font(SANS_B, 22), fill=RED)
    y += 30
    y = text_block(d, 40, y, "THREE LEADERS, ONE TABLE",
                   font(SERIF_B, 58), INK, W - 80, leading=4)
    y += 2
    y = text_block(
        d, 40, y,
        "Trump, Xi and Putin hold the first three-way summit of the "
        "United States, China and Russia on the sidelines of APEC — "
        "Ukraine, Iran and nuclear arms control on the agenda.",
        font(SERIF, 25), INK, W - 80, leading=5)
    y += 12

    # ---- map panel: three flashpoints ----
    panel_y0, panel_y1 = y, y + 160
    d.rectangle([40, panel_y0, W - 40, panel_y1], fill=NAVY)
    d.text((W // 2, panel_y0 + 12), "THREE FLASHPOINTS, ONE DAY",
           font=font(SANS_B, 21), fill=(232, 220, 180), anchor="ma")
    cities = [
        ("SHENZHEN", "Trilateral summit", 200, 0.30),
        ("KERCH", "Bridge hit again", 512, 0.42),
        ("THE GULF", "Iran–U.S. strikes", 824, 0.32),
    ]
    for name, label, cx, frac in cities:
        cy = panel_y0 + 70 + int(30 * frac)
        d.ellipse([cx - 11, cy - 11, cx + 11, cy + 11], fill=RED,
                  outline=(255, 255, 255), width=3)
        d.text((cx, cy + 18), name, font=font(SANS_B, 23),
               fill=(255, 255, 255), anchor="ma")
        d.text((cx, cy + 42), label, font=font(SANS, 19),
               fill=(200, 210, 225), anchor="ma")
    # arcs between the points (kept below the title)
    for (x1, x2) in [(200, 512), (512, 824)]:
        d.arc([x1, panel_y0 + 64, x2, panel_y0 + 148], start=200, end=340,
              fill=(120, 140, 170), width=3)
    y = panel_y1 + 16

    # ---- two-column stories ----
    col_w = (W - 80 - 36) // 2
    left_x, right_x = 40, 40 + col_w + 36
    d.line([W // 2, y, W // 2, y + 200], fill=(180, 175, 160), width=2)

    d.text((left_x, y), "JUSTICE  —  THE HAGUE", font=font(SANS_B, 20),
           fill=RED)
    y1 = text_block(d, left_x, y + 28, "Court rules on\nMyanmar genocide case",
                    font(SERIF_B, 33), INK, col_w, leading=2)
    y1 = text_block(
        d, left_x, y1 + 4,
        "The International Court of Justice rules on Gambia's genocide "
        "claim against Myanmar over the Rohingya.",
        font(SERIF, 22), INK, col_w, leading=4)

    d.text((right_x, y), "BUSINESS  —  NEW YORK", font=font(SANS_B, 20),
           fill=RED)
    y2 = text_block(d, right_x, y + 28, "Anthropic's $83\nIPO debut",
                    font(SERIF_B, 33), INK, col_w, leading=2)
    y2 = text_block(
        d, right_x, y2 + 4,
        "The AI company behind Claude prices its Nasdaq debut at $83 a "
        "share, above its $70–$78 range, in a record AI listing.",
        font(SERIF, 22), INK, col_w, leading=4)
    y = max(y1, y2) + 10
    d.line([40, y, W - 40, y], fill=RULE, width=2)
    y += 10

    # ---- also today ----
    d.text((40, y), "ALSO TODAY", font=font(SANS_B, 23), fill=NAVY)
    y += 30
    items = [
        ("Ukraine hits the Crimea bridge for a third time in a week.",
         TEAL),
        ("Iran fires at U.S. bases in the Gulf; the U.S. hits Qeshm Island.",
         RED),
        ("COP31 ministers meet in Antalya to unblock climate talks.", NAVY),
        ("Bangladesh unrest: Yunus's ancestral home set on fire.", GOLD),
        ("Van Gogh sells for $190.4M — a record for the artist.", TEAL),
        ("IAEA: North Korea expanded uranium enrichment.", RED),
    ]
    col2_w = (W - 80 - 36) // 2
    for i, (text, color) in enumerate(items):
        x = 40 if i % 2 == 0 else 40 + col2_w + 36
        yy = y + (i // 2) * 44
        d.ellipse([x, yy + 7, x + 13, yy + 20], fill=color)
        text_block(d, x + 22, yy, text, font(SERIF, 20), INK, col2_w - 22,
                   leading=3)
    y += 3 * 44 + 2
    d.line([40, y, W - 40, y], fill=RULE, width=2)
    y += 8
    d.text((W // 2, y), "Compiled 19 November 2026 from world news reports",
           font=font(SANS, 18), fill=MUTED, anchor="ma")

    img.save("entry.png", optimize=True)
    print("saved entry.png")


if __name__ == "__main__":
    main()
