"""Render the front page for Tuesday 24 November 2026.

Everything here is drawn from scratch with Pillow: no stock photos, no
external images. Headlines were checked against Reuters / AP / BBC / ESA
reporting from 23-24 November 2026.
"""

from PIL import Image, ImageDraw, ImageFont

PAGE = 1024
BG = (247, 242, 231)
DARK = (22, 22, 22)
NAVY = (18, 34, 60)
CREAM = (239, 233, 219)
GOLD = (214, 162, 60)
BRICK = (170, 34, 28)
FOREST = (32, 110, 70)
OCEAN = (30, 72, 136)
PINE = (14, 106, 104)
MUTED = (92, 88, 80)
LINECOL = (201, 193, 173)

FONTDIR = "/usr/share/fonts/truetype/dejavu/"
SERIF_HEAVY = FONTDIR + "DejaVuSerif-Bold.ttf"
SERIF_PLAIN = FONTDIR + "DejaVuSerif.ttf"
SANS_HEAVY = FONTDIR + "DejaVuSans-Bold.ttf"
SANS_PLAIN = FONTDIR + "DejaVuSans.ttf"


def load(path, size):
    return ImageFont.truetype(path, size)


def split_lines(canvas, text, font, limit):
    """Greedy wrap: pack as many words per line as fit inside limit."""
    out = []
    current = ""
    for word in text.split():
        trial = (current + " " + word).strip()
        if canvas.textlength(trial, font=font) <= limit:
            current = trial
        else:
            if current:
                out.append(current)
            current = word
    if current:
        out.append(current)
    return out


def paint_lines(canvas, lines, x, top, font, colour, leading=5):
    """Draw stacked lines; return the y just below the last one."""
    y = top
    for line in lines:
        canvas.text((x, y), line, font=font, fill=colour)
        y += font.size + leading
    return y


def story_card(canvas, x, y, w, h, accent, tag, headline, standfirst):
    """One of the four boxed stories in the middle grid."""
    canvas.rectangle([x, y, x + w, y + h], outline=LINECOL, width=2)
    canvas.rectangle([x, y, x + 136, y + 30], fill=accent)
    canvas.text((x + 68, y + 15), tag, font=load(SANS_HEAVY, 18),
                fill=(255, 255, 255), anchor="mm")
    after_head = paint_lines(
        canvas,
        split_lines(canvas, headline, load(SANS_HEAVY, 26), w - 28),
        x + 14, y + 42, load(SANS_HEAVY, 26), DARK, leading=3)
    paint_lines(
        canvas,
        split_lines(canvas, standfirst, load(SANS_PLAIN, 19), w - 28),
        x + 14, after_head + 4, load(SANS_PLAIN, 19), MUTED, leading=3)


def globe_mark(canvas, left, top, size):
    """Cracked-globe illustration with a NO DEAL stamp, all shapes."""
    canvas.rectangle([left, top, left + size, top + 300], fill=NAVY)
    canvas.rectangle([left, top, left + size, top + 300],
                     outline=GOLD, width=4)
    cx = left + size // 2
    cy = top + 132
    r = 92
    canvas.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(46, 110, 160))
    for (dx, dy, w, h) in [(-52, -58, 46, 40), (8, 6, 50, 46),
                           (-58, 28, 40, 34), (22, -66, 38, 36)]:
        canvas.ellipse([cx + dx, cy + dy, cx + dx + w, cy + dy + h],
                       fill=FOREST)
    crack = [(cx - 8, cy - 92), (cx + 12, cy - 48), (cx - 14, cy - 10),
             (cx + 16, cy + 30), (cx - 6, cy + 66), (cx + 10, cy + 92)]
    canvas.line(crack, fill=BRICK, width=7, joint="curve")
    stamp = [left + 62, top + 300 - 56, left + size - 62, top + 300 - 16]
    canvas.rectangle(stamp, outline=GOLD, width=3)
    canvas.text((cx, top + 300 - 50), "NO DEAL", font=load(SANS_HEAVY, 26),
                fill=GOLD, anchor="ma")


def build():
    sheet = Image.new("RGB", (PAGE, PAGE), BG)
    pen = ImageDraw.Draw(sheet)

    # Masthead
    pen.rectangle([0, 0, PAGE, 118], fill=NAVY)
    pen.text((512, 14), "THE WORLD IN ONE IMAGE",
             font=load(SERIF_HEAVY, 58), fill=CREAM, anchor="ma")
    pen.text((512, 78), "T U E S D A Y   2 4   N O V E M B E R   2 0 2 6",
             font=load(SANS_HEAVY, 26), fill=GOLD, anchor="ma")
    pen.rectangle([0, 118, PAGE, 124], fill=GOLD)

    # Lead story
    pen.text((40, 140), "CLIMATE  \u2022  ANTALYA",
             font=load(SANS_HEAVY, 22), fill=BRICK)
    y = 176
    for line in ("COP31 ENDS", "WITH NO DEAL"):
        pen.text((40, y), line, font=load(SERIF_HEAVY, 54), fill=DARK)
        y += 62
    y += 8
    y = paint_lines(
        pen,
        split_lines(pen, "Climate talks collapse over fossil fuels \u2014 "
                    "the first summit to fail since Copenhagen in 2009.",
                    load(SANS_HEAVY, 27), 560),
        40, y, load(SANS_HEAVY, 27), DARK, leading=4)
    y += 10
    paint_lines(
        pen,
        split_lines(pen, "The EU and 130-plus nations reject a text that "
                    "never names coal, oil or gas. The UN chief says he is "
                    "\u201cdeeply disappointed\u201d.",
                    load(SANS_PLAIN, 20), 560),
        40, y, load(SANS_PLAIN, 20), (62, 60, 54), leading=4)

    globe_mark(pen, 640, 140, 344)
    # Divider sits a touch lower now so the lead body text can breathe.
    pen.line([40, 478, 984, 478], fill=LINECOL, width=2)

    # Middle grid of four stories
    stories = [
        (BRICK, "SECURITY", "Ukraine sinks Russian warship off Libya",
         "Zelenskyy says sea drones sank the corvette Merkury at "
         "Benghazi and hit the cargo ship Angara."),
        (NAVY, "EUROPE", "Odesa in the dark",
         "Russian strikes leave 240,000 without heat; schools shut "
         "as crews race to repair the lines."),
        (PINE, "MARKETS", "Nvidia soars as Huang returns",
         "Shares end nearly a third higher as the founder "
         "retakes the helm."),
        (FOREST, "WORLD", "6.5 quake near Vanuatu",
         "Deep tremor in the South Pacific; no tsunami threat "
         "and no damage reported."),
    ]
    gx, gy, cw, ch, gap = 40, 492, 462, 176, 20
    for i, (accent, tag, head, deck) in enumerate(stories):
        story_card(pen, gx + (i % 2) * (cw + gap),
                   gy + (i // 2) * (ch + gap), cw, ch,
                   accent, tag, head, deck)

    # Also-today strip
    strip_y = 878
    pen.rectangle([0, strip_y, PAGE, strip_y + 96], fill=NAVY)
    pen.text((40, strip_y + 12), "ALSO TODAY",
             font=load(SANS_HEAVY, 22), fill=GOLD)
    extras = ["BepiColombo reaches Mercury after eight years",
              "EU plans sports ban in new Russia sanctions",
              "14 nations back ICJ genocide ruling on Rohingya",
              "Delta outage delays 2,000 flights"]
    row_y = strip_y + 44
    for i in range(0, 4, 2):
        pen.text((40, row_y), extras[i], font=load(SANS_PLAIN, 18),
                 fill=CREAM)
        pen.text((532, row_y), extras[i + 1], font=load(SANS_PLAIN, 18),
                 fill=CREAM)
        row_y += 26

    # Footer
    pen.text((512, 988), "Sources: Reuters, AP, BBC, ESA  \u2022  "
             "24 November 2026", font=load(SANS_PLAIN, 17), fill=MUTED,
             anchor="ma")
    return sheet


if __name__ == "__main__":
    page = build()
    page.save("news.png")
    print("saved news.png", page.size)
