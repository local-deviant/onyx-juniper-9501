#!/usr/bin/env python3
"""The World in One Day — front page for Thursday 19 November 2026.
Drawn entirely in code with Pillow. No photograph, no network, no API.
Every illustration is an original drawing; every word written for this page.
Deterministic: same input -> same bytes.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (26, 26, 26)
RED = (178, 35, 27)
NAVY = (30, 58, 95)
BLUE = (43, 94, 167)
GOLD = (200, 155, 60)
GRAY = (107, 107, 107)
LINE = (216, 210, 196)
GREEN = (31, 110, 63)
SKY = (183, 214, 232)
SAND = (232, 220, 188)

HERE = os.path.dirname(os.path.abspath(__file__))
F = os.path.join(HERE, "fonts")


def font(name, size):
    return ImageFont.truetype(os.path.join(F, name), size)


GLOOCK = lambda s: font("Gloock-Regular.ttf", s)
LORA = lambda s: font("Lora-Regular.ttf", s)
LORA_B = lambda s: font("Lora-Bold.ttf", s)
LORA_I = lambda s: font("Lora-Italic.ttf", s)
SANS = lambda s: font("InstrumentSans-Regular.ttf", s)
SANS_B = lambda s: font("InstrumentSans-Bold.ttf", s)
MONO = lambda s: font("JetBrainsMono-Regular.ttf", s)
MONO_B = lambda s: font("JetBrainsMono-Bold.ttf", s)


def text_w(d, text, f):
    return d.textlength(text, font=f)


def wrap(d, text, f, max_w):
    """Word-wrap text to lines that fit max_w. Returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if text_w(d, trial, f) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(d, x, y, text, f, max_w, leading, fill=INK):
    lines = wrap(d, text, f, max_w)
    for ln in lines:
        d.text((x, y), ln, font=f, fill=fill)
        y += leading
    return y


def check_mark(d, x, y, s, color, width=3):
    """Hand-drawn check mark (no glyph, avoids tofu)."""
    d.line([(x, y + s * 0.55), (x + s * 0.38, y + s * 0.9),
            (x + s, y + s * 0.1)], fill=color, width=width)


def rule(d, x0, y, x1, w=1, fill=INK):
    d.line([(x0, y), (x1, y)], fill=fill, width=w)


# ---------------------------------------------------------------- art pieces
def art_globe(d, cx, cy, r):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=RED, width=3)
    d.ellipse([cx - r * 0.55, cy - r, cx + r * 0.55, cy + r], outline=RED, width=2)
    d.line([(cx - r, cy), (cx + r, cy)], fill=RED, width=2)
    d.arc([cx - r, cy - r * 0.55, cx + r, cy + r * 0.55], 0, 360, fill=RED, width=2)
    d.line([(cx, cy - r), (cx, cy + r)], fill=RED, width=2)


def art_skyline(d, x, y, w, h):
    """Shenzhen skyline at dusk + three flags. (x,y) top-left."""
    d.rectangle([x, y, x + w, y + h], fill=(250, 232, 196))
    # sun
    d.ellipse([x + w - 52, y + 8, x + w - 16, y + 44], fill=(232, 120, 48))
    # buildings, back row (lighter)
    backs = [(0, 0.45, 0.16), (0.18, 0.30, 0.14), (0.34, 0.52, 0.15),
             (0.52, 0.34, 0.13), (0.68, 0.48, 0.15), (0.84, 0.38, 0.16)]
    for fx, fh, fw in backs:
        bx = x + fx * w
        bw = fw * w
        bh = fh * h
        d.rectangle([bx, y + h - bh, bx + bw, y + h], fill=(120, 138, 158))
    # front row (dark)
    fronts = [(0.05, 0.62, 0.13), (0.22, 0.78, 0.12), (0.40, 0.58, 0.13),
              (0.58, 0.72, 0.12), (0.75, 0.60, 0.12), (0.90, 0.70, 0.10)]
    for fx, fh, fw in fronts:
        bx = x + fx * w
        bw = fw * w
        bh = fh * h
        d.rectangle([bx, y + h - bh, bx + bw, y + h], fill=(44, 62, 86))
        # windows
        for wy in range(3):
            for wx in range(2):
                wx0 = bx + 5 + wx * (bw - 10) / 2
                wy0 = y + h - bh + 8 + wy * 16
                d.rectangle([wx0, wy0, wx0 + 4, wy0 + 6], fill=(250, 214, 120))
    # three flag poles on three towers, one flag each
    for i, (fx, c) in enumerate([(0.22, RED), (0.40, BLUE), (0.58, NAVY)]):
        px = x + fx * w + 0.06 * w
        d.line([(px, y + h * 0.24), (px, y + h * 0.02)], fill=INK, width=2)
        d.rectangle([px + 2, y + h * 0.02, px + 24, y + h * 0.02 + 10], fill=c)
        # small white band on the middle flag
        if i == 1:
            d.rectangle([px + 2, y + h * 0.02 + 3, px + 24, y + h * 0.02 + 6],
                        fill=(255, 255, 255))
    # ground line
    d.line([(x, y + h - 1), (x + w, y + h - 1)], fill=INK, width=2)


def art_gulf(d, x, y, w, h):
    """Strait of Hormuz: sea, land, Qeshm island, jets."""
    d.rectangle([x, y, x + w, y + h], fill=SKY)
    # land (Iran, top) and Arabia (bottom)
    d.polygon([(x, y), (x + w, y), (x + w, y + h * 0.30),
               (x + w * 0.55, y + h * 0.42), (x, y + h * 0.34)], fill=SAND)
    d.polygon([(x, y + h), (x + w, y + h), (x + w, y + h * 0.78),
               (x + w * 0.45, y + h * 0.66), (x, y + h * 0.74)], fill=SAND)
    # Qeshm island (red dot + label)
    qx, qy = x + w * 0.58, y + h * 0.52
    d.ellipse([qx - 7, qy - 4, qx + 7, qy + 4], fill=RED)
    d.text((qx + 10, qy - 12), "QESHM", font=MONO_B(10), fill=INK)
    d.text((x + 4, y + h - 14), "HORMUZ", font=MONO_B(10), fill=NAVY)
    # jets (small triangles)
    for jx, jy in [(x + w * 0.30, y + h * 0.42), (x + w * 0.38, y + h * 0.36)]:
        d.polygon([(jx, jy - 6), (jx - 5, jy + 5), (jx + 5, jy + 5)], fill=INK)


def art_btc(d, x, y, w, h):
    """Bitcoin 7-day line chart, falling."""
    d.rectangle([x, y, x + w, y + h], fill=(255, 255, 255))
    pts = [74, 72, 70, 68, 66, 64, 63]  # $k, 7 days
    lo, hi = 60, 76
    xs = [x + 8 + i * (w - 16) / 6 for i in range(7)]
    ys = [y + 8 + (hi - p) / (hi - lo) * (h - 26) for p in pts]
    d.line(list(zip(xs, ys)), fill=RED, width=3)
    for px, py in zip(xs, ys):
        d.ellipse([px - 2, py - 2, px + 2, py + 2], fill=RED)
    d.text((x + 4, y + 2), "$63,048", font=MONO_B(11), fill=INK)
    pct = "-14.8% WK"
    d.text((x + w - 4 - text_w(d, pct, MONO_B(10)), y + h - 14), pct,
           font=MONO_B(10), fill=RED)


def art_ipo(d, x, y, w, h):
    """IPO proceeds bars: SpaceX $75bn vs Anthropic $81.3bn."""
    d.rectangle([x, y, x + w, y + h], fill=(255, 255, 255))
    base = y + h - 18
    maxv = 90.0
    bw = 24
    # SpaceX bar (left)
    sx = x + 10
    sh = (75.0 / maxv) * (h - 40)
    d.rectangle([sx, base - sh, sx + bw, base], fill=(150, 150, 150))
    v1 = "$75B"
    d.text((sx + bw / 2 - text_w(d, v1, MONO_B(10)) / 2, base - sh - 13),
           v1, font=MONO_B(10), fill=GRAY)
    n1 = "SPACEX"
    d.text((sx + bw / 2 - text_w(d, n1, MONO(8)) / 2, base + 3),
           n1, font=MONO(8), fill=GRAY)
    # Anthropic bar (right)
    ax = x + w - 10 - bw
    ah = (81.3 / maxv) * (h - 40)
    d.rectangle([ax, base - ah, ax + bw, base], fill=BLUE)
    v2 = "$81.3B"
    d.text((ax + bw / 2 - text_w(d, v2, MONO_B(10)) / 2, base - ah - 13),
           v2, font=MONO_B(10), fill=BLUE)
    n2 = "ANTHROPIC"
    d.text((ax + bw / 2 - text_w(d, n2, MONO(8)) / 2, base + 3),
           n2, font=MONO(8), fill=GRAY)


def art_senate(d, x, y, w, h):
    """Senate split 56-44 horizontal bars."""
    d.rectangle([x, y, x + w, y + h], fill=(255, 255, 255))
    d.text((x + 4, y + 4), "DEM 56", font=MONO_B(12), fill=BLUE)
    d.rectangle([x + 4, y + 22, x + 4 + (w - 8) * 56 / 100, y + 40], fill=BLUE)
    d.text((x + 4, y + 46), "GOP 44", font=MONO_B(12), fill=RED)
    d.rectangle([x + 4, y + 64, x + 4 + (w - 8) * 44 / 100, y + 82], fill=RED)


def art_cyclone(d, x, y, w, h):
    """Cyclone spiral."""
    d.rectangle([x, y, x + w, y + h], fill=(232, 240, 248))
    cx, cy = x + w / 2, y + h / 2
    for r in range(6, int(min(w, h) / 2), 7):
        d.arc([cx - r, cy - r, cx + r, cy + r], 20 + r * 6, 300 + r * 6,
              fill=NAVY, width=3)
    d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=RED)


def art_ebola(d, x, y, w, h):
    """Case dots grid."""
    d.rectangle([x, y, x + w, y + h], fill=(255, 255, 255))
    import random
    rng = random.Random(1911)
    for i in range(10):
        for j in range(4):
            px = x + 10 + i * (w - 20) / 9
            py = y + 10 + j * (h - 20) / 3
            c = RED if rng.random() < 0.55 else (90, 90, 90)
            d.ellipse([px - 4, py - 4, px + 4, py + 4], fill=c)


def art_dow(d, x, y, w, h):
    """Dow bars falling + Nvidia tag."""
    d.rectangle([x, y, x + w, y + h], fill=(255, 255, 255))
    vals = [100, 92, 84, 76, 66]
    bw = (w - 24) / 5
    base = y + h - 16
    for i, v in enumerate(vals):
        bh = v / 100 * (h - 30)
        bx = x + 8 + i * bw
        d.rectangle([bx, base - bh, bx + bw - 5, base], fill=RED if i == 4 else (120, 120, 120))
    d.text((x + 4, y + 2), "DOW -561", font=MONO_B(11), fill=RED)


def art_gta(d, x, y, w, h):
    """Night skyline + big 99."""
    d.rectangle([x, y, x + w, y + h], fill=(18, 22, 38))
    # stars
    for sx, sy in [(0.12, 0.2), (0.3, 0.12), (0.55, 0.22), (0.8, 0.1), (0.92, 0.3)]:
        d.ellipse([x + sx * w - 1, y + sy * h - 1, x + sx * w + 1, y + sy * h + 1],
                  fill=(255, 255, 255))
    # buildings
    for fx, fh, fw in [(0.02, 0.45, 0.18), (0.22, 0.62, 0.16), (0.42, 0.5, 0.18),
                       (0.62, 0.68, 0.16), (0.80, 0.55, 0.18)]:
        bx = x + fx * w
        bw = fw * w
        bh = fh * h
        d.rectangle([bx, y + h - bh, bx + bw, y + h], fill=(52, 64, 96))
        for wy in range(2):
            for wx in range(2):
                d.rectangle([bx + 4 + wx * 8, y + h - bh + 6 + wy * 12,
                             bx + 7 + wx * 8, y + h - bh + 10 + wy * 12],
                            fill=(250, 214, 120))
    d.text((x + w - 46, y + 4), "99", font=GLOOCK(26), fill=GOLD)


def art_icj(d, x, y, w, h):
    """Scales of justice."""
    d.rectangle([x, y, x + w, y + h], fill=(255, 255, 255))
    cx = x + w / 2
    d.line([(cx, y + 8), (cx, y + h - 14)], fill=INK, width=3)
    d.line([(cx - 26, y + 14), (cx + 26, y + 14)], fill=INK, width=3)
    for s in (-1, 1):
        px = cx + s * 26
        d.line([(px, y + 14), (px, y + 30)], fill=INK, width=2)
        d.pieslice([px - 12, y + 28, px + 12, y + 40], 0, 180, fill=GOLD)
    d.rectangle([cx - 16, y + h - 14, cx + 16, y + h - 8], fill=INK)


def art_worldmap(d, x, y, w, h):
    """Dotted world map strip; red dots mark Shenzhen, the Gulf, Alaska."""
    dots = []
    # North America
    for dx in range(0, 150, 10):
        for dy in range(0, 26, 10):
            dots.append((x + 18 + dx, y + 4 + dy))
    # South America
    for dx in range(0, 48, 10):
        for dy in range(0, 22, 10):
            dots.append((x + 200 + dx, y + 14 + dy))
    # Europe
    for dx in range(0, 60, 10):
        for dy in range(0, 16, 10):
            dots.append((x + 430 + dx, y + 2 + dy))
    # Africa
    for dx in range(0, 72, 10):
        for dy in range(0, 30, 10):
            dots.append((x + 450 + dx, y + 12 + dy))
    # Asia
    for dx in range(0, 210, 10):
        for dy in range(0, 28, 10):
            dots.append((x + 540 + dx, y + 2 + dy))
    # Australia
    for dx in range(0, 48, 10):
        for dy in range(0, 12, 10):
            dots.append((x + 760 + dx, y + 20 + dy))
    for px, py in dots:
        d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=(120, 142, 168))
    # red markers: Shenzhen, Gulf, Alaska
    for mx, my in [(x + 700, y + 16), (x + 560, y + 14), (x + 60, y + 6)]:
        d.ellipse([mx - 4, my - 4, mx + 4, my + 4], fill=RED)


# ---------------------------------------------------------------- content
LEAD_DEK = ("First three-way summit with Putin opens at Kylin Villa; "
            "nuclear arms, trade and the wars in Ukraine and Iran on the agenda.")

MEDIUMS = [
    ("GULF", "U.S. JETS HIT IRGC SITE",
     "Iran answers with drones at U.S. bases in Bahrain and Kuwait; "
     "three carrier groups now in the Gulf.", "gulf"),
    ("MARKETS", "BITCOIN FALLS TO $63,048",
     "Down 2.9% in a day and 14.8% in a week; fear index at 10 as "
     "ETFs shed $240 million.", "btc"),
    ("BUSINESS", "ANTHROPIC DEBUTS AT $81 BILLION",
     "Priced at $83, the largest debut on record; shares start trading "
     "on Nasdaq today under ANT.", "ipo"),
    ("AMERICAS", "PELTOLA TAKES ALASKA",
     "Democrat unseats Sullivan; Senate goes 56-44, the largest "
     "majority since 2009.", "senate"),
]

ART_BRIEFS = [
    ("AKVAN NEARS INDIA",
     "Landfall due Friday; 50,000 moved out in Odisha.", "cyclone"),
    ("EBOLA TOPS 11,500",
     "Cases pass 11,500 in Congo; 5,630 dead, children hit hardest.", "ebola"),
    ("DOW FALLS 561",
     "Nvidia beats with $115.8bn sales, yet shares fall 2.9%.", "dow"),
    ("GTA VI ARRIVES WITH A 99",
     "Rockstar sequel launches today; score ties the highest on record.", "gta"),
    ("ICJ RULES ON ROHINGYA",
     "Court hands down its judgment on the Myanmar genocide case today.", "icj"),
]

REGIONS = [
    ("ASIA", [
        "Bangladesh: Yunus home torched; 28 districts hit",
        "Russian bombers land in Vietnam amid tensions",
        "Taiwan spots Russian aircraft near island again",
        "S. Korea's Lee hopes NK talks bring lasting peace",
        "Fires ravage 3m hectares in Indonesia",
        "North Korea expands uranium site, UN agency says",
    ]),
    ("EUROPE", [
        "EU proposes \u20ac45bn loan to Ukraine for 2027 funding gap",
        "COP31: ministers meet in Antalya to unblock climate deal",
        "Crimea bridge hit for a third time this week; traffic halted",
        "Van Gogh sells for $190.4m, a record for the artist",
        "EU approves Indonesia trade pact to offset U.S. tariffs",
    ]),
    ("MIDDLE EAST", [
        "Israeli forces cross Gaza ceasefire line into central Gaza",
        "Saudi PIF tower hit by Houthi rocket debris",
        "Yemen coalition reports missile threat towards Riyadh",
        "NSA outage disrupts Middle East intelligence links",
    ]),
    ("AMERICAS", [
        "U.S. asks top court to lift stay on Venezuela TPS",
        "Panama: second arrest over attack on journalist's home",
        "U.S. and Philippines pursue loan package over $2bn",
        "House stands at 254-170 as Democrats hold big majority",
        "Fed signals December hike; dollar at 19-month high",
    ]),
    ("AFRICA", [
        "Ethiopia and Eritrea mass troops along their border",
        "Kenya milk shortage deepens as drought cuts output",
        "Somalia faces crisis as reforms spark federal tensions",
        "Boat carrying 100 migrants sinks off Senegal",
    ]),
    ("OCEANIA", [
        "Fiji declares national disaster over El Ni\u00f1o drought",
        "Cyclone Xavier: 100-knot winds hit Cook Islands",
        "Albanese joins Putin and Trump in APEC group photo",
    ]),
    ("GLOBAL", [
        "Islam to be largest religion by 2035, Pew says",
        "589m children lived in conflict zones in 2025, report says",
        "Drug-resistant infections tied to 4.7m deaths",
    ]),
]

TIMELINE = ("00:00 BTC $63,048  \u00b7  02:37 Anthropic prices IPO at $83  \u00b7  "
            "05:16 Trump-Putin talks end  \u00b7  06:30 Three-way summit meets")
NUMBERS = ("BTC $63,048  \u00b7  ANT $83  \u00b7  GTA 99  \u00b7  SENATE 56-44  \u00b7  "
           "AKVAN 110 KM/H  \u00b7  EU \u20ac45BN")


def draw_page():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    MX = 28
    CW = W - 2 * MX  # 968

    # ---- masthead ----
    d.text((MX, 16), "THURSDAY, 19 NOVEMBER 2026", font=SANS_B(13), fill=INK)
    right = "No. 323 \u2014 PRICE $2.50"
    d.text((W - MX - text_w(d, right, SANS_B(13)), 16), right,
           font=SANS_B(13), fill=INK)
    art_globe(d, MX + 30, 62, 24)
    title = "THE WORLD IN ONE DAY"
    tf = GLOOCK(56)
    d.text(((W - text_w(d, title, tf)) / 2, 30), title, font=tf, fill=INK)
    sub = "I N T E R N A T I O N A L   E D I T I O N"
    sf = SANS(11)
    d.text(((W - text_w(d, sub, sf)) / 2, 92), sub, font=sf, fill=INK)
    count = "40 STORIES \u00b7 7 REGIONS \u00b7 12 DRAWN ILLUSTRATIONS"
    cf = SANS_B(12)
    d.text(((W - text_w(d, count, cf)) / 2, 106), count, font=cf, fill=RED)
    rule(d, MX, 124, W - MX, 2)

    # ---- UTC timeline strip ----
    d.rectangle([MX, 130, W - MX, 156], fill=NAVY)
    d.text((MX + 10, 137), "UTC TIMELINE", font=MONO_B(11), fill=GOLD)
    tlf = MONO(11)
    tw = text_w(d, TIMELINE, tlf)
    tx = MX + 10 + text_w(d, "UTC TIMELINE", MONO_B(11)) + 18
    if tx + tw > W - MX - 8:
        tlf = MONO(10)
        tw = text_w(d, TIMELINE, tlf)
    d.text((tx, 138), TIMELINE, font=tlf, fill=(255, 255, 255))

    # ---- lead ----
    ly = 166
    d.text((MX, ly), "SUMMIT IN SHENZHEN", font=SANS_B(14), fill=RED)
    hf = GLOOCK(50)
    d.text((MX, ly + 20), "TRUMP MEETS XI", font=hf, fill=INK)
    d.text((MX, ly + 74), "IN SHENZHEN", font=hf, fill=INK)
    dek_y = draw_wrapped(d, MX, ly + 132, LEAD_DEK, LORA(15), 600, 21)
    check_mark(d, MX, dek_y + 8, 13, GREEN, 3)
    proof = "DATE-CHECKED  \u00b7  REUTERS / AFP / AP"
    d.text((MX + 20, dek_y + 6), proof, font=MONO_B(11), fill=GREEN)
    # lead art
    ax, ay, aw, ah = 656, 166, 340, 158
    art_skyline(d, ax, ay, aw, ah)
    draw_wrapped(d, ax, ay + ah + 6,
                 "Shenzhen: Trump and Xi meet at Kylin Villa; Putin joins "
                 "for the first three-way summit.",
                 LORA_I(11), aw, 15, fill=GRAY)
    rule(d, MX, 368, W - MX, 1)

    # ---- mediums 2x2 ----
    art_fn = {"gulf": art_gulf, "btc": art_btc, "ipo": art_ipo, "senate": art_senate}
    my = 376
    cell_w = (CW - 24) // 2
    cell_h = 96
    for i, (kick, head, dek, kind) in enumerate(MEDIUMS):
        col = i % 2
        row = i // 2
        cx = MX + col * (cell_w + 24)
        cy = my + row * (cell_h + 8)
        art_fn[kind](d, cx, cy, 92, 92)
        tx = cx + 104
        tw = cell_w - 104
        d.text((tx, cy + 2), kick, font=SANS_B(10), fill=RED)
        hy = draw_wrapped(d, tx, cy + 18, head, LORA_B(18), tw, 22)
        draw_wrapped(d, tx, hy + 2, dek, LORA(12), tw, 16, fill=(60, 60, 60))
    rule(d, MX, 582, W - MX, 1)
    # vertical divider between medium columns
    d.line([(MX + cell_w + 12, my), (MX + cell_w + 12, my + 2 * cell_h + 8)],
           fill=LINE, width=1)

    # ---- art briefs row (5) ----
    by = 590
    col_w = (CW - 4 * 8) // 5
    art_fn2 = {"cyclone": art_cyclone, "ebola": art_ebola, "dow": art_dow,
               "gta": art_gta, "icj": art_icj}
    for i, (head, dek, kind) in enumerate(ART_BRIEFS):
        bx = MX + i * (col_w + 8)
        art_fn2[kind](d, bx, by, col_w, 58)
        hy = draw_wrapped(d, bx, by + 64, head, LORA_B(13), col_w, 16)
        draw_wrapped(d, bx, hy + 2, dek, LORA(11), col_w, 13, fill=(60, 60, 60))
    rule(d, MX, 702, W - MX, 1)

    # ---- day in numbers ----
    d.text((MX, 710), "DAY IN NUMBERS", font=SANS_B(11), fill=RED)
    nf = MONO_B(13)
    nw = text_w(d, NUMBERS, nf)
    nx = MX + text_w(d, "DAY IN NUMBERS", SANS_B(11)) + 16
    if nx + nw > W - MX:
        nf = MONO_B(12)
        nw = text_w(d, NUMBERS, nf)
    d.text((nx, 710), NUMBERS, font=nf, fill=INK)
    rule(d, MX, 732, W - MX, 1)

    # ---- region grid (3 columns) ----
    col_w3 = (CW - 2 * 14) // 3
    cols = [
        [REGIONS[0], REGIONS[1]],
        [REGIONS[2], REGIONS[3]],
        [REGIONS[4], REGIONS[5], REGIONS[6]],
    ]
    brief_f = SANS(12)
    for ci, groups in enumerate(cols):
        gx = MX + ci * (col_w3 + 14)
        gy = 740
        for name, items in groups:
            d.text((gx, gy), name, font=SANS_B(12), fill=RED)
            gy += 18
            for it in items:
                lines = wrap(d, it, brief_f, col_w3)
                for ln in lines:
                    d.text((gx, gy), ln, font=brief_f, fill=INK)
                    gy += 15
            gy += 5
        if ci < 2:
            d.line([(gx + col_w3 + 7, 740), (gx + col_w3 + 7, gy)],
                   fill=LINE, width=1)

    # ---- world map strip ----
    rule(d, MX, 960, W - MX, 1)
    art_worldmap(d, MX, 964, CW, 30)

    # ---- footer ----
    f1 = "ILLUSTRATIONS ARE ORIGINAL DRAWINGS, NOT PHOTOGRAPHS."
    ff = SANS_B(10)
    d.text(((W - text_w(d, f1, ff)) / 2, 998), f1, font=ff, fill=INK)
    f2 = "DATE-CHECKED 19 NOVEMBER 2026 \u00b7 40 STORIES \u00b7 7 REGIONS \u00b7 12 DRAWN"
    d.text(((W - text_w(d, f2, SANS(10))) / 2, 1012), f2, font=SANS(10), fill=GRAY)
    return img


def main():
    img = draw_page()
    img.save(os.path.join(HERE, "entry.png"), optimize=True)
    print("rendered", os.path.join(HERE, "entry.png"))


if __name__ == "__main__":
    main()
