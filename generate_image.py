#!/usr/bin/env python3
"""Draw the front page of THE WORLD for Thursday 19 November 2026.

Standard library plus Pillow only. Deterministic: same input, same PNG.
Run from the repository root; writes entry.png next to this file.
"""

import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MARGIN = 40
INK = (18, 18, 18)
PAPER = (250, 247, 238)
GREY = (112, 108, 98)
PANEL = (233, 229, 218)
RULE = (18, 18, 18)
RED = (150, 30, 30)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def serif_b(size):
    return font("DejaVuSerif-Bold.ttf", size)


def serif(size):
    return font("DejaVuSerif.ttf", size)


def sans_b(size):
    return font("DejaVuSans-Bold.ttf", size)


def sans(size):
    return font("DejaVuSans.ttf", size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, max_w, leading, color=INK):
    """Draw a wrapped paragraph; returns the y just below it."""
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


def hline(draw, y, x0, x1, width=2):
    draw.line([(x0, y), (x1, y)], fill=RULE, width=width)


def draw_page():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    left, right = MARGIN, W - MARGIN
    y = 28

    # --- Masthead -------------------------------------------------------
    title = "THE WORLD"
    tf = serif_b(88)
    tw = d.textlength(title, font=tf)
    d.text(((W - tw) / 2, y), title, font=tf, fill=INK)
    y += 104
    hline(d, y, left, right, 3)
    y += 8
    dateline = "THURSDAY 19 NOVEMBER 2026"
    df = sans_b(26)
    dw = d.textlength(dateline, font=df)
    d.text(((W - dw) / 2, y), dateline, font=df, fill=INK)
    y += 36
    tag = "One day's world news, in one page"
    tagf = serif(20)
    tgw = d.textlength(tag, font=tagf)
    d.text(((W - tgw) / 2, y), tag, font=tagf, fill=GREY)
    y += 30
    hline(d, y, left, right, 2)
    y += 16

    # --- Lead story -----------------------------------------------------
    d.text((left, y), "SUMMIT IN SHENZHEN", font=sans_b(24), fill=RED)
    y += 32
    head = "Trump, Xi and Putin hold first three-way summit"
    y = para(d, left, y, head, serif_b(40), right - left, 50)
    y += 6
    sub = ("The three leaders meet in Shenzhen on the APEC sidelines, with "
           "Ukraine, Iran and nuclear arms control on the agenda.")
    y = para(d, left, y, sub, serif(24), right - left, 31)
    y += 16
    hline(d, y, left, right, 2)
    y += 16

    # --- Flashpoints panel ----------------------------------------------
    panel_top = y
    d.rectangle([left, panel_top, right, panel_top + 140], fill=PANEL)
    y += 12
    d.text((left + 16, y), "FLASHPOINTS", font=sans_b(22), fill=INK)
    y += 34
    cols = [
        ("SHENZHEN", "Trilateral summit opens"),
        ("KERCH", "Bridge hit again"),
        ("THE GULF", "Iran\u2013U.S. strikes"),
    ]
    col_w = (right - left - 32) / 3
    for i, (place, line) in enumerate(cols):
        cx = left + 16 + i * col_w
        d.text((cx, y), place, font=sans_b(24), fill=RED)
        d.text((cx, y + 32), line, font=sans(21), fill=INK)
    y = panel_top + 140 + 16
    hline(d, y, left, right, 2)
    y += 16

    # --- Two columns ------------------------------------------------------
    col_w = (right - left - 28) / 2
    col_top = y
    stories = [
        ("THE HAGUE",
         "ICJ rules on Rohingya case",
         "The world court rules on Gambia's genocide case against "
         "Myanmar over the Rohingya."),
        ("MARKETS",
         "Anthropic's $83 IPO debut",
         "Shares debut at $83, above the $70\u2013$78 range set for the "
         "AI company's listing."),
    ]
    bottom = col_top
    for i, (kicker, headline, body) in enumerate(stories):
        cx = left + i * (col_w + 28)
        cy = col_top
        d.text((cx, cy), kicker, font=sans_b(20), fill=RED)
        cy += 30
        cy = para(d, cx, cy, headline, serif_b(26), col_w, 32)
        cy += 4
        cy = para(d, cx, cy, body, serif(20), col_w, 26)
        bottom = max(bottom, cy)
    y = bottom + 14
    hline(d, y, left, right, 2)
    y += 14

    # --- Also today ---------------------------------------------------------
    d.text((left, y), "ALSO TODAY", font=sans_b(22), fill=INK)
    y += 30
    items = [
        "Ukraine hits the Crimea bridge a third time in a week",
        "Iran fires at U.S. bases in the Gulf; U.S. hits Qeshm Island",
        "COP31 ministers meet in Antalya",
        "Bangladesh unrest: Yunus's home torched",
        "Van Gogh sells for $190.4M, an artist record",
        "IAEA: North Korea expanded uranium enrichment",
    ]
    bf = sans(20)
    for item in items:
        d.text((left, y), "\u2022", font=bf, fill=INK)
        y = para(d, left + 24, y, item, bf, right - left - 24, 26)
        y += 1
    y += 4
    hline(d, y, left, right, 2)
    y += 10
    foot = "THE WORLD  \u2022  19 November 2026"
    ff = sans(18)
    fw = d.textlength(foot, font=ff)
    d.text(((W - fw) / 2, y), foot, font=ff, fill=GREY)
    return img


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "entry.png")
    draw_page().save(out, "PNG")
    print("wrote", out)


if __name__ == "__main__":
    main()
