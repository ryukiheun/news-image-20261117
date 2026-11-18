#!/usr/bin/env python3
"""Draw the news-image-20261117 infographic (1024x1024 PNG).

Run: python3 draw_image.py
Writes entry.png next to this script. All artwork is drawn with
PIL shapes and DejaVu text; no photographs are used.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "entry.png"

NAVY = (20, 33, 61)
GOLD = (244, 201, 93)
PAPER = (247, 245, 239)
CARD = (255, 255, 255)
BORDER = (214, 211, 203)
INK = (24, 30, 42)
GREY = (84, 90, 102)
WHITE = (255, 255, 255)

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(size, bold=False):
    return ImageFont.truetype(FONT_B if bold else FONT, size)


def wrap(text, fnt, max_w):
    """Split text into lines that fit max_w pixels."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if fnt.getlength(trial) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_globe(d, cx, cy, r, color):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=4)
    d.ellipse([cx - r // 2, cy - r, cx + r // 2, cy + r], outline=color, width=3)
    d.line([cx - r, cy, cx + r, cy], fill=color, width=3)
    d.arc([cx - r, cy - r // 2, cx + r, cy + r // 2], 0, 360, fill=color, width=3)


def draw_bridge(d, x, y, s, color):
    # deck, arc and two towers of a suspension bridge
    d.line([x, y + s * 0.62, x + s, y + s * 0.62], fill=color, width=5)
    d.arc([x + s * 0.12, y + s * 0.08, x + s * 0.88, y + s * 0.95],
          180, 360, fill=color, width=5)
    for tx in (x + s * 0.22, x + s * 0.72):
        d.line([tx, y + s * 0.2, tx, y + s * 0.62], fill=color, width=5)
    for hx in (x + s * 0.36, x + s * 0.5, x + s * 0.64):
        d.line([hx, y + s * 0.34, hx, y + s * 0.62], fill=color, width=3)


def draw_radar(d, x, y, s, color):
    cx, cy, r = x + s // 2, y + s // 2, s // 2 - 3
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=4)
    d.ellipse([cx - r // 2, cy - r // 2, cx + r // 2, cy + r // 2],
              outline=color, width=3)
    d.line([cx, cy, cx + r * 0.7, cy - r * 0.7], fill=color, width=4)
    d.ellipse([cx + r * 0.28 - 4, cy - r * 0.3 - 4,
               cx + r * 0.28 + 4, cy - r * 0.3 + 4], fill=color)
    d.ellipse([cx - r * 0.45 - 4, cy + r * 0.25 - 4,
               cx - r * 0.45 + 4, cy + r * 0.25 + 4], fill=color)


def draw_flags(d, x, y, s, color):
    # three small flags on poles, each a rectangle with a swallowtail cut
    for i, fx in enumerate((x + s * 0.10, x + s * 0.40, x + s * 0.70)):
        d.line([fx, y + s * 0.14, fx, y + s * 0.88], fill=color, width=4)
        d.polygon([(fx, y + s * 0.14), (fx + s * 0.26, y + s * 0.14),
                   (fx + s * 0.26, y + s * 0.38), (fx, y + s * 0.38)],
                  fill=color)
        d.polygon([(fx + s * 0.26, y + s * 0.14), (fx + s * 0.26, y + s * 0.38),
                   (fx + s * 0.18, y + s * 0.26)], fill=color)


def draw_ledger(d, x, y, s, color):
    d.rectangle([x + s * 0.2, y + s * 0.12, x + s * 0.8, y + s * 0.88],
                outline=color, width=4)
    for i, ly in enumerate((0.3, 0.48, 0.66)):
        d.line([x + s * 0.3, y + s * ly, x + s * 0.7, y + s * ly],
               fill=color, width=3)
    # cross mark inside the page: two short diagonal strokes
    d.line([x + s * 0.6, y + s * 0.6, x + s * 0.78, y + s * 0.78],
           fill=color, width=5)
    d.line([x + s * 0.78, y + s * 0.6, x + s * 0.6, y + s * 0.78],
           fill=color, width=5)


def draw_chip(d, x, y, s, color):
    d.rectangle([x + s * 0.26, y + s * 0.26, x + s * 0.74, y + s * 0.74],
                outline=color, width=4)
    d.rectangle([x + s * 0.42, y + s * 0.42, x + s * 0.58, y + s * 0.58],
                fill=color)
    for i in range(3):
        t = s * (0.34 + i * 0.16)
        d.line([x + s * 0.26, y + t, x + s * 0.1, y + t], fill=color, width=3)
        d.line([x + s * 0.74, y + t, x + s * 0.9, y + t], fill=color, width=3)
        d.line([x + t, y + s * 0.26, x + t, y + s * 0.1], fill=color, width=3)
        d.line([x + t, y + s * 0.74, x + t, y + s * 0.9], fill=color, width=3)


def draw_jet(d, x, y, s, color):
    d.polygon([(x + s * 0.5, y + s * 0.1), (x + s * 0.86, y + s * 0.62),
               (x + s * 0.5, y + s * 0.5), (x + s * 0.14, y + s * 0.62)],
              fill=color)
    d.polygon([(x + s * 0.5, y + s * 0.5), (x + s * 0.72, y + s * 0.9),
               (x + s * 0.5, y + s * 0.72), (x + s * 0.28, y + s * 0.9)],
              fill=color)


ICONS = {
    "bridge": draw_bridge,
    "radar": draw_radar,
    "flags": draw_flags,
    "ledger": draw_ledger,
    "chip": draw_chip,
    "jet": draw_jet,
}

STORIES = [
    ("EUROPE", (192, 57, 43), "bridge",
     "Ukraine hits Crimea bridge again",
     "Kyiv strikes the Kerch Bridge a second day; Russia hits two Kyiv bridges, cutting heat and power."),
    ("MIDDLE EAST", (211, 84, 0), "radar",
     "Iran fires at US radar in Bahrain",
     "Drones target a US base radar; tankers hit mines near Hormuz as a third US carrier arrives."),
    ("ASIA", (14, 124, 123), "flags",
     "Xi, Trump and Putin to meet",
     "China confirms the first three-way summit, set for Thursday in Shenzhen at APEC."),
    ("UNITED STATES", (93, 109, 126), "ledger",
     "US runs nationwide alert test",
     "FEMA's 2:20 p.m. test interrupts TV and radio as officials debunk a viral 90-day blackout hoax."),
    ("TECH & TRADE", (108, 52, 131), "chip",
     "US closes AI chip loophole",
     "New rules stop China renting US computing power; Beijing calls it economic coercion."),
    ("ASIA-PACIFIC", (36, 113, 163), "jet",
     "Japan scrambles jets on Russian planes",
     "Two suspected Russian aircraft enter airspace near Okinoshima; Tokyo lodges a stern protest."),
]


def draw_card(d, x, y, w, h, tag, accent, icon, headline, summary):
    d.rounded_rectangle([x, y, x + w, y + h], radius=14, fill=CARD,
                        outline=BORDER, width=2)
    d.rounded_rectangle([x, y, x + w, y + 7], radius=3, fill=accent)
    # icon chip
    ix, iy, s = x + 18, y + 18, 58
    d.rounded_rectangle([ix, iy, ix + s, iy + s], radius=12, fill=accent)
    ICONS[icon](d, ix + 6, iy + 6, s - 12, WHITE)
    tx = x + 90
    d.text((tx, y + 16), tag, font=font(16, bold=True), fill=accent)
    head_lines = wrap(headline, font(27, bold=True), w - 90 - 18)[:2]
    hy = y + 40
    for line in head_lines:
        d.text((tx, hy), line, font=font(27, bold=True), fill=INK)
        hy += 33
    sum_lines = wrap(summary, font(21), w - 36)[:3]
    sy = y + 116
    for line in sum_lines:
        d.text((x + 18, sy), line, font=font(21), fill=GREY)
        sy += 27


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # masthead
    d.rectangle([0, 0, W, 168], fill=NAVY)
    d.text((28, 26), "17 NOVEMBER 2026", font=font(64, bold=True), fill=WHITE)
    d.text((30, 108), "TUESDAY  ·  THE WORLD IN ONE DAY",
           font=font(25, bold=True), fill=GOLD)
    d.line([28, 152, 620, 152], fill=GOLD, width=3)
    draw_globe(d, 920, 84, 56, GOLD)

    # story grid: 2 columns x 3 rows
    margin, gap = 28, 18
    top, bottom = 188, 958
    cw = (W - 2 * margin - gap) // 2
    ch = (bottom - top - 2 * gap) // 3
    for i, (tag, accent, icon, headline, summary) in enumerate(STORIES):
        row, col = divmod(i, 2)
        x = margin + col * (cw + gap)
        y = top + row * (ch + gap)
        draw_card(d, x, y, cw, ch, tag, accent, icon, headline, summary)

    # footer: sources
    d.text((W // 2, 976),
           "Reported on 17 November 2026  ·  Sources: Reuters, Al Jazeera, AP, Bloomberg, Kyodo News, FEMA",
           font=font(17), fill=GREY, anchor="ma")

    img.save(OUT, optimize=True)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
