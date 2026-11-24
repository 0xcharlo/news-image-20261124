"""Draw the front page for Tuesday 24 November 2026 with Pillow.

Every headline below was checked against reporting from 23-24 November
2026 (Reuters, AP, BBC, ESA, TASS, France 24, Al Jazeera). All shapes and
text are drawn fresh here; no external images are used.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 242, 231)
INK = (22, 22, 22)
NAVY = (18, 34, 60)
GOLD = (214, 162, 60)
RED = (170, 34, 28)
GREEN = (32, 110, 70)
BLUE = (30, 72, 136)
TEAL = (14, 106, 104)
GREY = (92, 88, 80)
RULE = (201, 193, 173)
LIGHT = (239, 233, 219)

FD = "/usr/share/fonts/truetype/dejavu/"
SERIF_B = FD + "DejaVuSerif-Bold.ttf"
SERIF = FD + "DejaVuSerif.ttf"
SANS_B = FD + "DejaVuSans-Bold.ttf"
SANS = FD + "DejaVuSans.ttf"


def fnt(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, font, width):
    """Greedy word wrap: lines that fit `width` pixels."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=font) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def put_lines(draw, lines, x, y, font, fill, gap=6):
    for ln in lines:
        draw.text((x, y), ln, font=font, fill=fill)
        y += font.size + gap
    return y


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---- Masthead -------------------------------------------------------
d.rectangle([0, 0, W, 118], fill=NAVY)
d.text((512, 14), "THE WORLD IN ONE IMAGE", font=fnt(SERIF_B, 58),
       fill=LIGHT, anchor="ma")
d.text((512, 78), "T U E S D A Y   2 4   N O V E M B E R   2 0 2 6",
       font=fnt(SANS_B, 26), fill=GOLD, anchor="ma")
d.rectangle([0, 118, W, 124], fill=GOLD)

# ---- Lead story: COP31 ----------------------------------------------
d.text((40, 140), "CLIMATE  \u2022  ANTALYA", font=fnt(SANS_B, 22), fill=RED)
y = 176
for ln in ("COP31 ENDS", "WITH NO DEAL"):
    d.text((40, y), ln, font=fnt(SERIF_B, 54), fill=INK)
    y += 62
y += 8
sub = ("Climate talks collapse over fossil fuels \u2014 the first "
       "summit to fail since Copenhagen in 2009.")
y = put_lines(d, wrap(d, sub, fnt(SANS_B, 27), 560), 40, y,
              fnt(SANS_B, 27), INK, gap=4)
y += 10
body = ("The EU and 130-plus nations reject a text that never names "
        "coal, oil or gas. The UN chief says he is \u201cdeeply "
        "disappointed\u201d.")
y = put_lines(d, wrap(d, body, fnt(SANS, 20), 560), 40, y,
              fnt(SANS, 20), (62, 60, 54), gap=4)

# Lead illustration: a cracked globe stamped NO DEAL
PX, PY, PW, PH = 640, 140, 344, 300
d.rectangle([PX, PY, PX + PW, PY + PH], fill=NAVY)
d.rectangle([PX, PY, PX + PW, PY + PH], outline=GOLD, width=4)
cx, cy, r = PX + PW // 2, PY + 132, 92
d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(46, 110, 160))
d.ellipse([cx - 52, cy - 58, cx - 6, cy - 18], fill=GREEN)
d.ellipse([cx + 8, cy + 6, cx + 58, cy + 52], fill=GREEN)
d.ellipse([cx - 58, cy + 28, cx - 18, cy + 62], fill=GREEN)
d.ellipse([cx + 22, cy - 66, cx + 60, cy - 30], fill=GREEN)
crack = [(cx - 8, cy - 92), (cx + 12, cy - 48), (cx - 14, cy - 10),
         (cx + 16, cy + 30), (cx - 6, cy + 66), (cx + 10, cy + 92)]
d.line(crack, fill=RED, width=7, joint="curve")
d.rectangle([PX + 62, PY + PH - 56, PX + PW - 62, PY + PH - 16],
            outline=GOLD, width=3)
d.text((PX + PW // 2, PY + PH - 50), "NO DEAL", font=fnt(SANS_B, 26),
       fill=GOLD, anchor="ma")

d.line([40, 470, 984, 470], fill=RULE, width=2)

# ---- 2x2 grid --------------------------------------------------------
GRID = [
    (RED, "SECURITY",
     "Ukraine sinks Russian warship off Libya",
     "Zelenskyy says sea drones sank the corvette Merkury at "
     "Benghazi and hit the cargo ship Angara."),
    (NAVY, "EUROPE",
     "Odesa in the dark",
     "Russian strikes leave 240,000 without heat; schools shut "
     "as crews race to repair the lines."),
    (TEAL, "MARKETS",
     "Nvidia soars as Huang returns",
     "Shares end nearly a third higher as the founder "
     "retakes the helm."),
    (GREEN, "WORLD",
     "6.5 quake near Vanuatu",
     "Deep tremor in the South Pacific; no tsunami threat "
     "and no damage reported."),
]
GX, GY, CW, CH, GAP = 40, 492, 462, 176, 20
for i, (color, label, head, deck) in enumerate(GRID):
    x = GX + (i % 2) * (CW + GAP)
    y = GY + (i // 2) * (CH + GAP)
    d.rectangle([x, y, x + CW, y + CH], outline=RULE, width=2)
    d.rectangle([x, y, x + 132, y + 30], fill=color)
    d.text((x + 66, y + 15), label, font=fnt(SANS_B, 18),
           fill=(255, 255, 255), anchor="mm")
    hy = put_lines(d, wrap(d, head, fnt(SANS_B, 26), CW - 28), x + 14,
                   y + 42, fnt(SANS_B, 26), INK, gap=3)
    put_lines(d, wrap(d, deck, fnt(SANS, 19), CW - 28), x + 14, hy + 4,
              fnt(SANS, 19), GREY, gap=3)

# ---- Also today ------------------------------------------------------
AY = 878
d.rectangle([0, AY, W, AY + 96], fill=NAVY)
d.text((40, AY + 12), "ALSO TODAY", font=fnt(SANS_B, 22), fill=GOLD)
also = [
    "BepiColombo reaches Mercury after eight years",
    "EU plans sports ban in new Russia sanctions",
    "14 nations back ICJ genocide ruling on Rohingya",
    "Delta outage delays 2,000 flights",
]
ay = AY + 44
for i in range(0, 4, 2):
    d.text((40, ay), also[i], font=fnt(SANS, 18), fill=LIGHT)
    d.text((532, ay), also[i + 1], font=fnt(SANS, 18), fill=LIGHT)
    ay += 26

# ---- Footer ----------------------------------------------------------
d.text((512, 988), "Sources: Reuters, AP, BBC, ESA  \u2022  24 November 2026",
       font=fnt(SANS, 17), fill=GREY, anchor="ma")

img.save("news.png")
print("saved news.png", img.size)
