"""Draws entry.png: one page summing up the world news of Wednesday 18 November 2026.

Run: python art/draw.py  (needs Pillow and the Windows fonts Georgia and Segoe UI).
Everything is drawn at 2x and scaled down for clean edges, then saved as a palette PNG.
"""
import math
import os
import sys

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content as C  # noqa: E402

K = 2
W = H = 1024
FONTS = "C:/Windows/Fonts/"
SERIF_B, SERIF = "georgiab.ttf", "georgia.ttf"
SANS, SANS_B, SANS_SB = "segoeui.ttf", "segoeuib.ttf", "seguisb.ttf"

BG = (250, 247, 240)
INK = (24, 24, 28)
GREY = (95, 95, 100)
RULE = (200, 196, 186)
RED = (190, 30, 40)
NAVY = (22, 34, 66)
REGION_COL = {
    "EUROPE": (40, 90, 170), "AMERICAS": (36, 128, 70), "ASIA": (120, 50, 160),
    "AFRICA": (214, 120, 20), "MIDDLE EAST": (190, 40, 50), "OCEANIA": (20, 130, 140),
    "GLOBAL": (80, 80, 90),
}

_fc = {}


def font(name, size):
    key = (name, size)
    if key not in _fc:
        _fc[key] = ImageFont.truetype(FONTS + name, int(round(size * K)))
    return _fc[key]


img = Image.new("RGB", (W * K, H * K), BG)
d = ImageDraw.Draw(img)


def S(v):
    return int(round(v * K))


def R(x, y, w, h, fill=None, outline=None, width=1, r=0):
    box = [S(x), S(y), S(x + w) - 1, S(y + h) - 1]
    if r:
        d.rounded_rectangle(box, S(r), fill=fill, outline=outline, width=S(width))
    else:
        d.rectangle(box, fill=fill, outline=outline, width=S(width) if outline else 0)


def T(x, y, s, f, fill=INK, anchor="la"):
    d.text((S(x), S(y)), s, font=f, fill=fill, anchor=anchor)


def tw(s, f):
    return d.textlength(s, font=f) / K


def poly(pts, fill=None, outline=None, width=1):
    d.polygon([(S(a), S(b)) for a, b in pts], fill=fill, outline=outline, width=S(width) if outline else 0)


def L(pts, fill=INK, width=1):
    d.line([(S(a), S(b)) for a, b in pts], fill=fill, width=max(1, S(width)), joint="curve")


def E(cx, cy, rx, ry=None, fill=None, outline=None, width=1):
    ry = rx if ry is None else ry
    d.ellipse([S(cx - rx), S(cy - ry), S(cx + rx), S(cy + ry)], fill=fill, outline=outline,
              width=S(width) if outline else 0)


def dashed(x1, y1, x2, y2, fill, width=1.5, dash=6, gap=4):
    n = math.hypot(x2 - x1, y2 - y1)
    if n == 0:
        return
    ux, uy = (x2 - x1) / n, (y2 - y1) / n
    t = 0
    while t < n:
        e = min(n, t + dash)
        L([(x1 + ux * t, y1 + uy * t), (x1 + ux * e, y1 + uy * e)], fill, width)
        t += dash + gap


def wrap(s, f, maxw):
    words, lines, cur = s.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if tw(t, f) <= maxw or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def fit(s, name, size, maxw, maxlines, minsize):
    while True:
        f = font(name, size)
        lines = wrap(s, f, maxw)
        if (len(lines) <= maxlines and all(tw(l_, f) <= maxw for l_ in lines)) or size <= minsize:
            return f, lines, size
        size -= 0.5


def star(cx, cy, r, fill, points=5, inner=0.45, rot=-90):
    pts = []
    for i in range(points * 2):
        rr = r if i % 2 == 0 else r * inner
        a = math.radians(rot + i * 180 / points)
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    poly(pts, fill)


def burst(cx, cy, r, fill=(255, 200, 40), core=(255, 245, 200)):
    star(cx, cy, r, fill, points=9, inner=0.5)
    E(cx, cy, r * 0.35, fill=core)


# ---------------------------------------------------------------- flags
def flag(code, x, y, w, h):
    stripes_h = {
        "UA": [(0, 87, 183), (255, 213, 0)], "RU": [(255, 255, 255), (0, 57, 166), (213, 43, 30)],
        "DE": [(0, 0, 0), (221, 0, 0), (255, 206, 0)], "IN": [(255, 153, 51), (255, 255, 255), (19, 136, 8)],
        "IR": [(35, 159, 64), (255, 255, 255), (218, 0, 0)], "CO": [(252, 209, 22), (0, 56, 147), (206, 17, 38)],
        "NL": [(174, 28, 40), (255, 255, 255), (33, 70, 139)], "HU": [(205, 42, 62), (255, 255, 255), (67, 111, 77)],
        "SD": [(210, 16, 52), (255, 255, 255), (0, 0, 0)], "AR": [(116, 172, 223), (255, 255, 255), (116, 172, 223)],
        "ID": [(206, 17, 38), (255, 255, 255)], "PL": [(255, 255, 255), (220, 20, 60)],
        "AT": [(237, 41, 57), (255, 255, 255), (237, 41, 57)], "EG": [(206, 17, 38), (255, 255, 255), (0, 0, 0)],
        "VE": [(255, 204, 0), (0, 36, 125), (207, 20, 43)],
    }
    stripes_v = {
        "FR": [(0, 85, 164), (255, 255, 255), (239, 65, 53)], "IT": [(0, 146, 70), (255, 255, 255), (206, 43, 55)],
        "NG": [(0, 135, 81), (255, 255, 255), (0, 135, 81)], "IE": [(22, 155, 98), (255, 255, 255), (255, 136, 62)],
        "MX": [(0, 104, 71), (255, 255, 255), (206, 17, 38)], "PE": [(217, 16, 35), (255, 255, 255), (217, 16, 35)],
        "BE": [(0, 0, 0), (253, 218, 36), (239, 51, 64)],
    }
    if code in stripes_h:
        cols = stripes_h[code]
        for i, c in enumerate(cols):
            R(x, y + h * i / len(cols), w, h / len(cols) + 0.5, fill=c)
    elif code in stripes_v:
        cols = stripes_v[code]
        for i, c in enumerate(cols):
            R(x + w * i / len(cols), y, w / len(cols) + 0.5, h, fill=c)
    elif code == "CN":
        R(x, y, w, h, fill=(222, 41, 16))
        star(x + w * 0.2, y + h * 0.3, h * 0.2, (255, 222, 0))
        for i, (a, b) in enumerate([(0.38, 0.12), (0.45, 0.25), (0.45, 0.43), (0.38, 0.55)]):
            star(x + w * a, y + h * b, h * 0.07, (255, 222, 0))
    elif code == "US":
        for i in range(7):
            R(x, y + h * i * 2 / 13, w, h / 13 + 0.3, fill=(178, 34, 52))
            R(x, y + h * (i * 2 + 1) / 13, w, h / 13 + 0.3, fill=(255, 255, 255)) if i < 6 else None
        R(x, y, w * 0.42, h * 7 / 13, fill=(60, 59, 110))
    elif code == "EU":
        R(x, y, w, h, fill=(0, 51, 153))
        for i in range(12):
            a = math.radians(i * 30)
            star(x + w / 2 + h * 0.33 * math.cos(a), y + h / 2 + h * 0.33 * math.sin(a), h * 0.06, (255, 204, 0))
    elif code == "JP":
        R(x, y, w, h, fill=(255, 255, 255))
        E(x + w / 2, y + h / 2, h * 0.3, fill=(188, 0, 45))
    elif code == "UK":
        R(x, y, w, h, fill=(1, 33, 105))
        L([(x, y), (x + w, y + h)], (255, 255, 255), h * 0.18)
        L([(x + w, y), (x, y + h)], (255, 255, 255), h * 0.18)
        R(x + w * 0.42, y, w * 0.16, h, fill=(255, 255, 255))
        R(x, y + h * 0.36, w, h * 0.28, fill=(255, 255, 255))
        R(x + w * 0.45, y, w * 0.1, h, fill=(200, 16, 46))
        R(x, y + h * 0.4, w, h * 0.2, fill=(200, 16, 46))
    elif code == "BR":
        R(x, y, w, h, fill=(0, 156, 59))
        poly([(x + w * 0.5, y + h * 0.1), (x + w * 0.92, y + h * 0.5), (x + w * 0.5, y + h * 0.9),
              (x + w * 0.08, y + h * 0.5)], (255, 223, 0))
        E(x + w / 2, y + h / 2, h * 0.22, fill=(0, 39, 118))
    elif code == "IL":
        R(x, y, w, h, fill=(255, 255, 255))
        R(x, y + h * 0.12, w, h * 0.12, fill=(0, 56, 184))
        R(x, y + h * 0.76, w, h * 0.12, fill=(0, 56, 184))
        star(x + w / 2, y + h / 2, h * 0.16, (0, 56, 184), points=6, inner=0.6)
    elif code == "KR":
        R(x, y, w, h, fill=(255, 255, 255))
        E(x + w / 2, y + h / 2, h * 0.22, fill=(205, 46, 58))
        d.pieslice([S(x + w / 2 - h * 0.22), S(y + h / 2 - h * 0.22), S(x + w / 2 + h * 0.22),
                    S(y + h / 2 + h * 0.22)], 0, 180, fill=(0, 71, 160))
    else:
        R(x, y, w, h, fill=(200, 200, 200))
    R(x, y, w, h, outline=(60, 60, 60), width=0.6)


# ---------------------------------------------------------------- scenes
def person(cx, base, hgt, suit, skin=(236, 196, 160), arm=None):
    head = hgt * 0.13
    E(cx, base - hgt + head, head, fill=skin)
    R(cx - hgt * 0.15, base - hgt + head * 2.1, hgt * 0.3, hgt * 0.5, fill=suit, r=hgt * 0.06)
    R(cx - hgt * 0.12, base - hgt * 0.42, hgt * 0.1, hgt * 0.42, fill=suit)
    R(cx + hgt * 0.02, base - hgt * 0.42, hgt * 0.1, hgt * 0.42, fill=suit)
    poly([(cx - hgt * 0.03, base - hgt + head * 2.1), (cx + hgt * 0.03, base - hgt + head * 2.1),
          (cx, base - hgt * 0.62)], (255, 255, 255))
    if arm is not None:
        L([(cx, base - hgt * 0.68), (arm, base - hgt * 0.55)], suit, hgt * 0.07)


def drone(cx, cy, s, fill=(40, 40, 46)):
    poly([(cx - s, cy), (cx + s, cy - s * 0.35), (cx + s * 0.6, cy), (cx + s, cy + s * 0.35)], fill)


def skyline(x, y, w, h, fill):
    import random
    rnd = random.Random(int(x * 7 + y))
    cx = x
    while cx < x + w:
        bw = rnd.uniform(w * 0.05, w * 0.11)
        bh = rnd.uniform(h * 0.25, h * 0.7)
        R(cx, y + h - bh, min(bw, x + w - cx), bh, fill=fill)
        cx += bw + 1


def scene(kind, x, y, w, h, o):
    """Draw illustration `kind` into the box. o: options (labels, flags, colours)."""
    d0 = d
    R(x, y, w, h, fill=o.get("bg", (230, 225, 210)))
    cx, cy = x + w / 2, y + h / 2
    if kind == "summit":
        for i in range(int(h)):
            t = i / h
            R(x, y + i, w, 1.2, fill=(int(250 - 30 * t), int(200 - 40 * t), int(140 - 50 * t)))
        E(x + w * 0.8, y + h * 0.28, h * 0.16, fill=(240, 120, 60))
        skyline(x, y + h * 0.35, w, h * 0.35, (205, 150, 120))
        R(x, y + h * 0.7, w, h * 0.3, fill=(150, 140, 130))
        poly([(cx - w * 0.06, y + h * 0.7), (cx + w * 0.06, y + h * 0.7), (cx + w * 0.22, y + h), (cx - w * 0.22, y + h)],
             (190, 30, 40))
        # plane
        px, py = x + w * 0.05, y + h * 0.42
        R(px, py, w * 0.36, h * 0.12, fill=(245, 245, 250), r=h * 0.06)
        R(px + w * 0.02, py + h * 0.035, w * 0.3, h * 0.025, fill=(60, 90, 160))
        poly([(px + w * 0.15, py + h * 0.1), (px + w * 0.24, py + h * 0.1), (px + w * 0.1, py + h * 0.22)], (220, 220, 228))
        person(cx - h * 0.1, y + h * 0.95, h * 0.6, (35, 35, 45), arm=cx)
        person(cx + h * 0.1, y + h * 0.95, h * 0.6, (30, 40, 70), arm=cx)
        for nm, px_ in ((o.get("n1"), cx - h * 0.16), (o.get("n2"), cx + h * 0.16)):
            if nm:
                nf = font(SANS_B, h * 0.1)
                bw2 = tw(nm, nf) + 8
                R(px_ - bw2 / 2, y + h * 0.17, bw2, h * 0.14, fill=(255, 255, 255), r=2)
                T(px_, y + h * 0.24, nm, nf, INK, "mm")
                poly([(px_ - 4, y + h * 0.31), (px_ + 4, y + h * 0.31), (px_, y + h * 0.35)], (255, 255, 255))
        flag(o.get("f1", "CN"), x + w * 0.66, y + h * 0.5, h * 0.24, h * 0.16)
        flag(o.get("f2", "US"), x + w * 0.66 + h * 0.3, y + h * 0.5, h * 0.24, h * 0.16)
    elif kind == "gulf":
        R(x, y, w, h, fill=(120, 180, 215))
        poly([(x, y + h * 0.55), (x + w * 0.2, y + h * 0.4), (x + w * 0.38, y + h * 0.5), (x + w * 0.5, y + h * 0.78),
              (x + w * 0.62, y + h * 0.8), (x + w * 0.75, y + h), (x, y + h)], (232, 210, 160))
        poly([(x + w * 0.25, y), (x + w, y), (x + w, y + h * 0.62), (x + w * 0.8, y + h * 0.5), (x + w * 0.55, y + h * 0.3),
              (x + w * 0.35, y + h * 0.12)], (214, 190, 140))
        T(x + w * 0.72, y + h * 0.12, "IRAN", font(SANS_B, h * 0.13), (110, 80, 50))
        for (lx, ly, nm) in o.get("targets", []):
            E(x + w * lx, y + h * ly, h * 0.035, fill=RED)
            T(x + w * lx - h * 0.02, y + h * ly + h * 0.05, nm, font(SANS_B, h * 0.085), (70, 50, 30), "ra")
        for (lx, ly) in o.get("targets_xy", []):
            pass
        sx, sy = x + w * 0.78, y + h * 0.36
        for (lx, ly, nm) in o.get("targets", []):
            tx, ty = x + w * lx, y + h * ly
            dashed(sx, sy, tx + (sx - tx) * 0.25, ty + (sy - ty) * 0.25, (90, 30, 30), 1.3)
            drone(tx + (sx - tx) * 0.3, ty + (sy - ty) * 0.3, h * 0.06)
            burst(tx + (sx - tx) * 0.2, ty + (sy - ty) * 0.2, h * 0.08)
    elif kind == "space":
        R(x, y, w, h, fill=(12, 16, 40))
        import random
        rnd = random.Random(7)
        for _ in range(60):
            E(x + rnd.uniform(0, w), y + rnd.uniform(0, h), rnd.uniform(0.4, 1.1), fill=(230, 230, 255))
        E(x + w * 0.1, y + h * 0.62, h * 0.12, fill=(50, 120, 220))
        E(x + w * 0.08, y + h * 0.6, h * 0.05, h * 0.07, fill=(70, 170, 90))
        T(x + w * 0.1, y + h * 0.8, "EARTH", font(SANS_B, h * 0.07), (200, 210, 240), "ma")
        dashed(x + w * 0.18, y + h * 0.62, x + w * 0.74, y + h * 0.55, (255, 210, 80), 1.6)
        px, py = x + w * 0.83, y + h * 0.5
        E(px - h * 0.04, py, h * 0.05, h * 0.16, fill=(230, 230, 235))
        R(px, py - h * 0.05, h * 0.12, h * 0.1, fill=(200, 170, 80))
        L([(px + h * 0.12, py), (px + h * 0.3, py - h * 0.12)], (200, 200, 210), 1.4)
        L([(px + h * 0.06, py + h * 0.05), (px + h * 0.1, py + h * 0.28)], (200, 200, 210), 1.4)
    elif kind == "drones_night":
        R(x, y, w, h, fill=(28, 32, 58))
        for i in range(3):
            L([(x + w * (0.2 + 0.3 * i), y + h), (x + w * (0.35 + 0.25 * i), y + h * 0.1)], (230, 230, 150), 0.9)
        skyline(x, y + h * 0.55, w, h * 0.45, (14, 16, 30))
        for i, (a, b) in enumerate([(0.15, 0.2), (0.3, 0.35), (0.45, 0.18), (0.6, 0.3), (0.75, 0.15), (0.88, 0.32),
                                     (0.22, 0.48), (0.68, 0.45)]):
            drone(x + w * a, y + h * b, h * 0.05, (200, 205, 215))
        burst(x + w * 0.53, y + h * 0.4, h * 0.08)
        burst(x + w * 0.38, y + h * 0.25, h * 0.06)
    elif kind == "money":
        R(x, y, w, h, fill=o.get("bg", (225, 232, 245)))
        flag(o.get("f1", "EU"), x + w * 0.08, y + h * 0.22, h * 0.6 * 1.5, h * 0.6)
        flag(o.get("f2", "UA"), x + w * 0.92 - h * 0.6 * 1.5, y + h * 0.22, h * 0.6 * 1.5, h * 0.6)
        ax1, ax2 = x + w * 0.08 + h * 0.9 + 6, x + w * 0.92 - h * 0.9 - 6
        L([(ax1, cy), (ax2 - 6, cy)], NAVY, 3)
        poly([(ax2, cy), (ax2 - 10, cy - 7), (ax2 - 10, cy + 7)], NAVY)
        if o.get("amt"):
            f = font(SERIF_B, h * 0.2)
            T((ax1 + ax2) / 2, cy - h * 0.06, o["amt"], f, NAVY, "md")
    elif kind == "chart_down" or kind == "chart_up":
        up = kind == "chart_up"
        R(x, y, w, h, fill=o.get("bg", (238, 240, 236)))
        n = 9
        for i in range(n):
            bh = h * (0.25 + 0.06 * (i if up else n - i) + (0.05 if i % 2 else 0))
            R(x + w * 0.08 + i * w * 0.09, y + h * 0.9 - bh, w * 0.06, bh, fill=(180, 190, 200))
        col = (30, 140, 70) if up else RED
        pts = [(x + w * (0.08 + 0.09 * i), y + h * (0.65 - 0.05 * i if up else 0.25 + 0.05 * i + (0.06 if i % 2 else 0)))
               for i in range(n)]
        L(pts, col, 3)
        ex, ey = pts[-1]
        poly([(ex + 10, ey + (-8 if up else 8)), (ex - 6, ey - 2), (ex + 2, ey + (-14 if up else 14))], col)
        R(x, y + h * 0.9, w, h * 0.1, fill=(150, 150, 150))
    elif kind == "cyclone":
        R(x, y, w, h, fill=(70, 120, 170))
        poly([(x + w * 0.62, y), (x + w, y), (x + w, y + h), (x + w * 0.8, y + h), (x + w * 0.72, y + h * 0.5)],
             (150, 175, 110))
        ccx, ccy = x + w * 0.38, y + h * 0.55
        for i in range(4):
            r = h * (0.12 + 0.1 * i)
            d.arc([S(ccx - r), S(ccy - r), S(ccx + r), S(ccy + r)], 200 + i * 40, 200 + i * 40 + 230,
                  fill=(240, 245, 250), width=S(3))
        E(ccx, ccy, h * 0.05, fill=(240, 245, 250))
        L([(ccx + h * 0.2, ccy - h * 0.1), (x + w * 0.66, y + h * 0.3)], (255, 220, 80), 2)
        poly([(x + w * 0.68, y + h * 0.27), (x + w * 0.64, y + h * 0.26), (x + w * 0.66, y + h * 0.33)], (255, 220, 80))
        if o.get("land"):
            lf = font(SANS_B, h * 0.11)
            T(x + w * 0.86, y + h * 0.85, o["land"], lf, (40, 60, 30), "mm")
    elif kind == "court":
        R(x, y, w, h, fill=o.get("bg", (226, 220, 205)))
        bx, bw_ = cx - h * 0.6, h * 1.2
        poly([(bx - 6, y + h * 0.32), (cx, y + h * 0.1), (bx + bw_ + 6, y + h * 0.32)], (200, 190, 170))
        for i in range(5):
            R(bx + i * bw_ / 4.6, y + h * 0.36, h * 0.07, h * 0.42, fill=(245, 240, 230))
        R(bx - 8, y + h * 0.78, bw_ + 16, h * 0.08, fill=(190, 180, 160))
        R(x + w * 0.75, y + h * 0.55, h * 0.3, h * 0.1, fill=(110, 70, 40), r=2)
        L([(x + w * 0.75 + h * 0.15, y + h * 0.65), (x + w * 0.75 + h * 0.25, y + h * 0.85)], (110, 70, 40), 3)
    elif kind == "ballot":
        R(x, y, w, h, fill=o.get("bg", (225, 232, 240)))
        R(cx - h * 0.35, y + h * 0.4, h * 0.7, h * 0.5, fill=(40, 70, 130), r=3)
        R(cx - h * 0.2, y + h * 0.39, h * 0.4, h * 0.03, fill=(15, 20, 40))
        poly([(cx - h * 0.14, y + h * 0.4), (cx - h * 0.08, y + h * 0.08), (cx + h * 0.18, y + h * 0.12),
              (cx + h * 0.12, y + h * 0.4)], (255, 255, 255), (80, 80, 80), 1)
        L([(cx - h * 0.04, y + h * 0.22), (cx + h * 0.0, y + h * 0.28), (cx + h * 0.1, y + h * 0.15)], RED, 2.5)
        if o.get("f1"):
            flag(o["f1"], x + w * 0.06, y + h * 0.1, h * 0.36, h * 0.24)
    elif kind == "virus":
        R(x, y, w, h, fill=(220, 238, 236))
        for i in range(12):
            a = math.radians(i * 30)
            L([(cx + h * 0.22 * math.cos(a), cy + h * 0.22 * math.sin(a)),
               (cx + h * 0.33 * math.cos(a), cy + h * 0.33 * math.sin(a))], (200, 60, 70), 2)
            E(cx + h * 0.34 * math.cos(a), cy + h * 0.34 * math.sin(a), h * 0.035, fill=(200, 60, 70))
        E(cx, cy, h * 0.24, fill=(225, 90, 90))
        R(x + w * 0.08, y + h * 0.3, h * 0.28, h * 0.08, fill=RED)
        R(x + w * 0.08 + h * 0.1, y + h * 0.2, h * 0.08, h * 0.28, fill=RED)
    elif kind == "quake":
        R(x, y, w, h, fill=(236, 228, 214))
        pts = []
        for i in range(60):
            t = i / 59
            amp = h * 0.25 * math.exp(-((t - 0.45) ** 2) / 0.01)
            pts.append((x + w * t, y + h * 0.35 + amp * math.sin(i * 2.1)))
        L(pts, RED, 1.6)
        R(x, y + h * 0.65, w, h * 0.35, fill=(160, 130, 100))
        L([(cx - h * 0.4, y + h * 0.65), (cx - h * 0.1, y + h * 0.8), (cx - h * 0.2, y + h * 0.9),
           (cx + h * 0.1, y + h)], (60, 40, 30), 2)
    elif kind == "flood":
        R(x, y, w, h, fill=(150, 170, 185))
        for i in range(4):
            hx = x + w * (0.1 + 0.22 * i)
            R(hx, y + h * 0.35, h * 0.28, h * 0.35, fill=(230, 220, 200))
            poly([(hx - 3, y + h * 0.36), (hx + h * 0.14, y + h * 0.18), (hx + h * 0.28 + 3, y + h * 0.36)], (160, 60, 50))
        R(x, y + h * 0.58, w, h * 0.42, fill=(110, 90, 60))
        for j in range(3):
            pts = [(x + w * i / 30, y + h * (0.6 + 0.1 * j) + 3 * math.sin(i + j)) for i in range(31)]
            L(pts, (180, 200, 215), 1.5)
    elif kind == "fire":
        R(x, y, w, h, fill=(60, 40, 40))
        poly([(x, y + h), (x + w * 0.3, y + h * 0.55), (x + w * 0.6, y + h * 0.75), (x + w, y + h * 0.5), (x + w, y + h)],
             (30, 25, 25))
        for i in range(6):
            fx = x + w * (0.1 + 0.15 * i)
            poly([(fx - h * 0.1, y + h * 0.8), (fx, y + h * (0.3 + 0.08 * (i % 3))), (fx + h * 0.1, y + h * 0.8)],
                 (240, 120, 30))
            poly([(fx - h * 0.05, y + h * 0.8), (fx, y + h * (0.5 + 0.06 * (i % 3))), (fx + h * 0.05, y + h * 0.8)],
                 (255, 210, 60))
    elif kind == "sport":
        R(x, y, w, h, fill=(60, 140, 70))
        for i in range(6):
            R(x + i * w / 6, y, w / 12, h, fill=(70, 150, 80))
        L([(cx, y), (cx, y + h)], (240, 240, 240), 1.5)
        E(cx, cy, h * 0.22, outline=(240, 240, 240), width=1.5)
        b = o.get("ball", "football")
        if b == "tennis":
            R(x, y, w, h, fill=(60, 110, 170))
            R(x + w * 0.1, y + h * 0.15, w * 0.8, h * 0.7, outline=(255, 255, 255), width=1.5)
            L([(cx, y + h * 0.15), (cx, y + h * 0.85)], (240, 240, 240), 2)
            E(cx + w * 0.2, cy - h * 0.1, h * 0.1, fill=(220, 240, 60))
        elif b == "trophy":
            poly([(cx - h * 0.2, y + h * 0.15), (cx + h * 0.2, y + h * 0.15), (cx + h * 0.12, y + h * 0.5),
                  (cx - h * 0.12, y + h * 0.5)], (240, 200, 60))
            R(cx - h * 0.04, y + h * 0.5, h * 0.08, h * 0.2, fill=(220, 180, 40))
            R(cx - h * 0.15, y + h * 0.7, h * 0.3, h * 0.1, fill=(120, 80, 30))
        else:
            E(cx + w * 0.22, cy, h * 0.13, fill=(255, 255, 255))
            star(cx + w * 0.22, cy, h * 0.06, (30, 30, 30), points=5, inner=0.8)
    elif kind == "chip":
        R(x, y, w, h, fill=(30, 40, 60))
        for i in range(10):
            L([(x, y + h * (0.1 * i)), (x + w, y + h * (0.1 * i))], (45, 58, 85), 1)
        R(cx - h * 0.28, cy - h * 0.28, h * 0.56, h * 0.56, fill=(70, 80, 100), r=4)
        for i in range(6):
            off = -h * 0.22 + i * h * 0.088
            L([(cx + off, cy - h * 0.38), (cx + off, cy - h * 0.28)], (200, 180, 90), 1.5)
            L([(cx + off, cy + h * 0.28), (cx + off, cy + h * 0.38)], (200, 180, 90), 1.5)
            L([(cx - h * 0.38, cy + off), (cx - h * 0.28, cy + off)], (200, 180, 90), 1.5)
            L([(cx + h * 0.28, cy + off), (cx + h * 0.38, cy + off)], (200, 180, 90), 1.5)
        T(cx, cy, o.get("chiptext", "AI"), font(SANS_B, h * 0.2), (230, 240, 255), "mm")
    elif kind == "rocket":
        R(x, y, w, h, fill=(30, 50, 90))
        rx = cx
        poly([(rx, y + h * 0.08), (rx + h * 0.08, y + h * 0.25), (rx + h * 0.08, y + h * 0.6), (rx - h * 0.08, y + h * 0.6),
              (rx - h * 0.08, y + h * 0.25)], (240, 240, 245))
        poly([(rx - h * 0.06, y + h * 0.6), (rx + h * 0.06, y + h * 0.6), (rx, y + h * 0.85)], (255, 160, 40))
        R(x, y + h * 0.85, w, h * 0.15, fill=(90, 90, 100))
    elif kind == "protest":
        R(x, y, w, h, fill=o.get("bg", (238, 225, 205)))
        import random
        rnd = random.Random(3)
        for row in range(3):
            for i in range(14):
                px = x + w * (i / 13) + rnd.uniform(-4, 4)
                py = y + h * (0.5 + 0.12 * row)
                E(px, py, h * 0.06, fill=(rnd.randint(40, 120), rnd.randint(30, 80), rnd.randint(30, 70)))
                R(px - h * 0.07, py + h * 0.05, h * 0.14, h * 0.2, fill=(60, 60, 80))
        for i, a in enumerate([0.6, 0.83] if o.get("badge") else [0.15, 0.45, 0.75]):
            L([(x + w * a + 10, y + h * 0.3), (x + w * a + 10, y + h * 0.6)], (110, 80, 50), 1.5)
            pw_ = 50 if o.get("sign") else 36
            R(x + w * a + 10 - pw_ / 2, y + h * 0.1, pw_, h * 0.22, fill=(255, 255, 255), outline=(60, 60, 60), width=0.8)
            if o.get("sign"):
                T(x + w * a + 10, y + h * 0.21, o["sign"], font(SANS_B, h * 0.12), RED, "mm")
    elif kind == "oil":
        R(x, y, w, h, fill=(240, 220, 170))
        L([(x + w * 0.2, y + h * 0.9), (x + w * 0.3, y + h * 0.15), (x + w * 0.4, y + h * 0.9)], (60, 50, 40), 2)
        for i in range(4):
            yy = y + h * (0.3 + 0.15 * i)
            L([(x + w * 0.3 - (yy - y - h * 0.15) * 0.14, yy), (x + w * 0.3 + (yy - y - h * 0.15) * 0.14, yy)], (60, 50, 40), 1.2)
        for i in range(3):
            R(x + w * (0.55 + 0.13 * i), y + h * 0.45, h * 0.3, h * 0.45, fill=(40, 40, 50), r=3)
            R(x + w * (0.55 + 0.13 * i), y + h * 0.55, h * 0.3, h * 0.04, fill=(200, 160, 40))
    elif kind == "military":
        R(x, y, w, h, fill=o.get("bg", (210, 200, 170)))
        R(x, y + h * 0.78, w, h * 0.22, fill=(150, 130, 90))
        tx, ty = x + w * 0.3, y + h * 0.5
        R(tx, ty, h * 0.9, h * 0.2, fill=(80, 90, 60), r=4)
        R(tx + h * 0.2, ty - h * 0.14, h * 0.4, h * 0.16, fill=(90, 100, 66), r=3)
        L([(tx + h * 0.55, ty - h * 0.07), (tx + h * 1.15, ty - h * 0.12)], (70, 80, 55), 3)
        R(tx - 4, ty + h * 0.18, h * 0.9 + 8, h * 0.12, fill=(40, 40, 40), r=6)
    elif kind == "plane":
        R(x, y, w, h, fill=o.get("bg", (200, 220, 240)))
        px, py = cx - h * 0.6, cy
        R(px, py - h * 0.07, h * 1.2, h * 0.14, fill=(250, 250, 252), r=h * 0.07)
        poly([(px + h * 0.5, py), (px + h * 0.8, py), (px + h * 0.45, py + h * 0.4)], (225, 225, 232))
        poly([(px + h * 0.5, py), (px + h * 0.8, py), (px + h * 0.45, py - h * 0.4)], (225, 225, 232))
        poly([(px, py), (px + h * 0.12, py), (px - h * 0.05, py - h * 0.25)], (225, 225, 232))
    elif kind == "ship":
        R(x, y, w, h, fill=(140, 190, 220))
        R(x, y + h * 0.62, w, h * 0.38, fill=(40, 90, 140))
        poly([(cx - h * 0.6, y + h * 0.5), (cx + h * 0.7, y + h * 0.5), (cx + h * 0.55, y + h * 0.7), (cx - h * 0.5, y + h * 0.7)],
             (120, 40, 40))
        R(cx - h * 0.2, y + h * 0.32, h * 0.5, h * 0.18, fill=(240, 240, 240))
    elif kind == "parliament":
        R(x, y, w, h, fill=o.get("bg", (230, 228, 240)))
        E(cx, y + h * 0.42, h * 0.22, fill=(235, 235, 240))
        R(cx - h * 0.6, y + h * 0.42, h * 1.2, h * 0.4, fill=(240, 240, 244))
        for i in range(7):
            R(cx - h * 0.55 + i * h * 0.17, y + h * 0.48, h * 0.06, h * 0.3, fill=(200, 200, 210))
        R(cx - h * 0.7, y + h * 0.82, h * 1.4, h * 0.06, fill=(170, 170, 180))
        if o.get("f1"):
            L([(cx, y + h * 0.2), (cx, y + h * 0.05)], (60, 60, 60), 1)
            flag(o["f1"], cx, y + h * 0.04, h * 0.18, h * 0.12)
    elif kind == "game":
        R(x, y, w, h, fill=(70, 30, 90))
        R(cx - h * 0.4, cy - h * 0.18, h * 0.8, h * 0.36, fill=(240, 240, 245), r=h * 0.16)
        R(cx - h * 0.28, cy - h * 0.03, h * 0.16, h * 0.06, fill=(70, 30, 90))
        R(cx - h * 0.23, cy - h * 0.08, h * 0.06, h * 0.16, fill=(70, 30, 90))
        E(cx + h * 0.2, cy - h * 0.04, h * 0.035, fill=(70, 30, 90))
        E(cx + h * 0.28, cy + h * 0.04, h * 0.035, fill=(70, 30, 90))
    elif kind == "factory":
        R(x, y, w, h, fill=(220, 215, 205))
        poly([(x + w * 0.1, y + h * 0.9), (x + w * 0.1, y + h * 0.5), (x + w * 0.3, y + h * 0.35), (x + w * 0.3, y + h * 0.5),
              (x + w * 0.5, y + h * 0.35), (x + w * 0.5, y + h * 0.5), (x + w * 0.7, y + h * 0.35), (x + w * 0.7, y + h * 0.9)],
             (110, 110, 120))
        R(x + w * 0.76, y + h * 0.15, w * 0.05, h * 0.75, fill=(110, 110, 120))
        for i in range(3):
            E(x + w * (0.8 + 0.03 * i), y + h * (0.1 - 0.03 * i), h * (0.05 + 0.02 * i), fill=(180, 180, 185))
    elif kind == "map":
        R(x, y, w, h, fill=(170, 205, 225))
        for blob in o.get("land", []):
            poly([(x + w * a, y + h * b) for a, b in blob], (225, 215, 180))
        for (lx, ly, nm) in o.get("places", []):
            E(x + w * lx, y + h * ly, h * 0.035, fill=RED)
            T(x + w * lx + h * 0.05, y + h * ly, nm, font(SANS_B, h * 0.085), (40, 40, 40), "lm")
    elif kind == "bridge":
        for i in range(int(h * 0.55)):
            t = i / (h * 0.55)
            R(x, y + i, w, 1.2, fill=(int(60 + 120 * t), int(70 + 90 * t), int(110 + 60 * t)))
        R(x, y + h * 0.55, w, h * 0.45, fill=(40, 80, 120))
        dy = y + h * 0.5
        R(x, dy, w, h * 0.06, fill=(70, 70, 78))
        for i in range(9):
            px = x + w * (0.04 + 0.12 * i)
            R(px, dy + h * 0.06, w * 0.02, h * 0.3, fill=(80, 80, 88))
            d.arc([S(px), S(dy - h * 0.18), S(px + w * 0.12), S(dy + h * 0.14)], 180, 360, fill=(90, 90, 98), width=S(1.5))
        burst(x + w * 0.56, dy - h * 0.05, h * 0.2, (255, 150, 40), (255, 240, 180))
        for i in range(4):
            E(x + w * (0.52 + 0.04 * i), dy - h * (0.28 + 0.07 * i), h * (0.06 + 0.02 * i), fill=(90, 85, 85))
        R(x + w * 0.78, dy - h * 0.25, h * 0.4, h * 0.16, fill=RED, r=2)
        T(x + w * 0.78 + h * 0.2, dy - h * 0.17, "CLOSED", font(SANS_B, h * 0.09), (255, 255, 255), "mm")
    elif kind == "police":
        R(x, y, w, h, fill=(40, 40, 60))
        skyline(x, y + h * 0.2, w, h * 0.5, (25, 25, 38))
        R(x, y + h * 0.75, w, h * 0.25, fill=(70, 70, 75))
        vx, vy = x + w * 0.22, y + h * 0.5
        R(vx, vy, h * 1.1, h * 0.26, fill=(30, 50, 40), r=4)
        R(vx + h * 0.15, vy - h * 0.14, h * 0.6, h * 0.16, fill=(30, 50, 40), r=3)
        E(vx + h * 0.22, vy + h * 0.27, h * 0.08, fill=(15, 15, 15))
        E(vx + h * 0.88, vy + h * 0.27, h * 0.08, fill=(15, 15, 15))
        R(vx + h * 0.3, vy - h * 0.2, h * 0.12, h * 0.06, fill=(220, 40, 40))
        R(vx + h * 0.42, vy - h * 0.2, h * 0.12, h * 0.06, fill=(40, 90, 230))
        for i in range(5):
            L([(x + w * (0.7 + 0.05 * i), y + h * (0.3 + 0.08 * i)), (x + w * (0.66 + 0.05 * i), y + h * (0.32 + 0.08 * i))],
              (255, 220, 80), 1.2)
    elif kind == "strip":
        R(x, y, w, h, fill=(150, 195, 220))
        poly([(x + w * 0.42, y), (x + w, y), (x + w, y + h), (x + w * 0.6, y + h)], (225, 210, 170))
        poly([(x + w * 0.42, y), (x + w * 0.52, y), (x + w * 0.7, y + h), (x + w * 0.6, y + h)], (240, 200, 160))
        L([(x + w * 0.52, y), (x + w * 0.7, y + h)], (90, 90, 90), 1.2)
        R(x + w * 0.49, y + h * 0.42, w * 0.12, h * 0.18, fill=(200, 60, 50))
        lf = font(SANS_B, h * 0.12)
        lab = o.get("area", "CENTRAL GAZA")
        R(x + w * 0.64, y + h * 0.18, tw(lab, lf) + 8, h * 0.18, fill=(255, 255, 255), r=2)
        T(x + w * 0.64 + 4, y + h * 0.27, lab, lf, (150, 30, 30), "lm")
        for i in range(3):
            L([(x + w * (0.8 - 0.04 * i), y + h * (0.55 + 0.1 * i)), (x + w * (0.64 - 0.02 * i), y + h * (0.53 + 0.05 * i))],
              (60, 70, 40), 2)
            poly([(x + w * (0.63 - 0.02 * i), y + h * (0.53 + 0.05 * i)), (x + w * (0.66 - 0.02 * i), y + h * (0.5 + 0.05 * i)),
                  (x + w * (0.66 - 0.02 * i), y + h * (0.56 + 0.05 * i))], (60, 70, 40))
        T(x + w * 0.2, y + h * 0.5, "MEDITERRANEAN", font(SANS_B, h * 0.08), (60, 100, 140), "mm")
    elif kind == "art":
        R(x, y, w, h, fill=(120, 30, 40))
        fx, fy, fw, fh = cx - h * 0.55, y + h * 0.1, h * 1.1, h * 0.75
        R(fx - 6, fy - 6, fw + 12, fh + 12, fill=(200, 160, 60))
        R(fx, fy, fw, fh, fill=(120, 170, 200))
        R(fx, fy + fh * 0.7, fw, fh * 0.3, fill=(110, 140, 60))
        import random
        rnd = random.Random(5)
        for tx_ in (0.3, 0.7):
            R(fx + fw * tx_ - 2, fy + fh * 0.45, 4, fh * 0.3, fill=(90, 60, 40))
            for _ in range(28):
                E(fx + fw * tx_ + rnd.uniform(-fw * 0.15, fw * 0.15), fy + fh * (0.3 + rnd.uniform(-0.15, 0.15)),
                  rnd.uniform(2, 4.5), fill=rnd.choice([(250, 250, 245), (240, 200, 210), (90, 140, 70)]))
        R(cx - h * 0.25, y + h * 0.9, h * 0.5, h * 0.08, fill=(240, 230, 200))
    elif kind == "strike":
        R(x, y, w, h, fill=(70, 75, 95))
        for i in range(3):
            E(x + w * (0.55 + 0.08 * i), y + h * (0.32 - 0.08 * i), h * (0.14 + 0.05 * i), fill=(105, 100, 105))
        bx_ = x + w * 0.08
        R(bx_, y + h * 0.35, w * 0.84, h * 0.65, fill=(225, 205, 165))
        for i in range(7):
            for j in range(2):
                wx = bx_ + w * 0.05 + i * w * 0.11
                wy = y + h * (0.45 + 0.25 * j)
                R(wx, wy, w * 0.05, h * 0.16, fill=(80, 80, 95), r=w * 0.02)
        R(bx_ - 3, y + h * 0.33, w * 0.84 + 6, h * 0.05, fill=(190, 170, 130))
        poly([(x + w * 0.5, y + h * 0.33), (x + w * 0.62, y + h * 0.5), (x + w * 0.72, y + h * 0.36), (x + w * 0.78, y + h * 0.6),
              (x + w * 0.68, y + h * 0.75), (x + w * 0.56, y + h * 0.62)], (60, 50, 50))
        burst(x + w * 0.64, y + h * 0.42, h * 0.16, (255, 140, 30), (255, 230, 160))
        if o.get("place"):
            lf = font(SANS_B, h * 0.12)
            R(x + w * 0.08, y + h * 0.78, tw(o["place"], lf) + 10, h * 0.17, fill=(255, 255, 255), r=2)
            T(x + w * 0.08 + 5, y + h * 0.865, o["place"], lf, INK, "lm")
    elif kind == "pact":
        R(x, y, w, h, fill=o.get("bg", (228, 232, 240)))
        fh = h * 0.42
        flag(o.get("f1", "US"), x + w * 0.05, y + h * 0.18, fh * 1.5, fh)
        flag(o.get("f2", "VE"), x + w * 0.95 - fh * 1.5, y + h * 0.18, fh * 1.5, fh)
        R(cx - h * 0.3, y + h * 0.1, h * 0.6, h * 0.8, fill=(255, 255, 255), outline=(120, 120, 130), width=1)
        for i in range(5):
            R(cx - h * 0.22, y + h * (0.2 + 0.09 * i), h * (0.44 if i % 2 else 0.36), h * 0.03, fill=(170, 170, 180))
        L([(cx - h * 0.2, y + h * 0.76), (cx - h * 0.1, y + h * 0.7), (cx, y + h * 0.77), (cx + h * 0.1, y + h * 0.69),
           (cx + h * 0.2, y + h * 0.75)], NAVY, 1.6)
        L([(cx + h * 0.22, y + h * 0.82), (cx + h * 0.38, y + h * 0.58)], (40, 40, 40), 2.5)
    elif kind == "health":
        R(x, y, w, h, fill=(225, 238, 245))
        R(cx - h * 0.1, cy - h * 0.3, h * 0.2, h * 0.6, fill=(40, 140, 120))
        R(cx - h * 0.3, cy - h * 0.1, h * 0.6, h * 0.2, fill=(40, 140, 120))
        R(x + w * 0.72, y + h * 0.2, h * 0.12, h * 0.5, fill=(255, 255, 255), outline=(120, 120, 130), width=1, r=3)
        R(x + w * 0.72, y + h * 0.45, h * 0.12, h * 0.25, fill=(200, 60, 70), r=3)
    elif kind == "bank":
        R(x, y, w, h, fill=o.get("bg", (232, 236, 228)))
        poly([(cx - h * 0.55, y + h * 0.32), (cx, y + h * 0.1), (cx + h * 0.55, y + h * 0.32)], (90, 100, 110))
        for i in range(5):
            R(cx - h * 0.48 + i * h * 0.22, y + h * 0.36, h * 0.08, h * 0.38, fill=(150, 160, 170))
        R(cx - h * 0.6, y + h * 0.74, h * 1.2, h * 0.08, fill=(90, 100, 110))
        if o.get("sign"):
            T(cx, y + h * 0.26, o["sign"], font(SANS_B, h * 0.09), (255, 255, 255), "mm")
    if o.get("cflag"):
        flag(o["cflag"], x + w - h * 0.42 - 6, y + 6, h * 0.42, h * 0.28)
    # optional text badge
    if o.get("badge"):
        f = font(SANS_B, o.get("bsize", 11))
        bw_ = tw(o["badge"], f) + 12
        R(x + 6, y + 6, bw_, o.get("bsize", 11) * 1.55, fill=o.get("bcol", (20, 20, 24)), r=3)
        T(x + 12, y + 6 + o.get("bsize", 11) * 0.77, o["badge"], f, (255, 255, 255), "lm")
    if o.get("badge2"):
        f = font(SANS_B, o.get("bsize", 11))
        bw_ = tw(o["badge2"], f) + 12
        R(x + 6, y + 10 + o.get("bsize", 11) * 1.55, bw_, o.get("bsize", 11) * 1.55, fill=(255, 210, 40), r=3)
        T(x + 12, y + 10 + o.get("bsize", 11) * 2.32, o["badge2"], f, (20, 20, 24), "lm")
    if o.get("caption"):
        f = font(SANS_B, o.get("csize", 9.5))
        ch = o.get("csize", 9.5) * 1.7
        R(x, y + h - ch, w, ch, fill=(0, 0, 0))
        T(x + w / 2, y + h - ch / 2, o["caption"], f, (255, 255, 255), "mm")
    _ = d0


# ---------------------------------------------------------------- world map
LAND = [  # (lat_top, [(lon_from, lon_to), ...]) in 5-degree bands
    (85, [(-65, -20)]), (80, [(-120, -65), (-70, -20), (10, 30), (45, 65), (95, 105)]),
    (75, [(-125, -70), (-60, -20), (50, 60), (80, 115), (130, 150)]),
    (70, [(-165, -140), (-140, -60), (-55, -25), (15, 30), (30, 180)]),
    (65, [(-165, -140), (-140, -60), (-50, -40), (-25, -15), (5, 30), (30, 180)]),
    (60, [(-160, -135), (-130, -95), (-80, -60), (-7, -2), (5, 20), (20, 160)]),
    (55, [(-130, -55), (-10, 2), (0, 40), (40, 140), (155, 160)]),
    (50, [(-125, -55), (-5, 40), (40, 135), (140, 145)]),
    (45, [(-125, -70), (-10, 3), (5, 28), (41, 50), (50, 130), (140, 145)]),
    (40, [(-125, -75), (-10, 0), (-10, 10), (12, 27), (26, 45), (45, 122), (125, 130), (130, 142)]),
    (35, [(-120, -80), (-10, 32), (32, 36), (38, 62), (62, 122), (130, 135)]),
    (30, [(-115, -97), (-82, -80), (-15, 35), (35, 57), (57, 68), (68, 122)]),
    (25, [(-106, -97), (-85, -75), (-17, 37), (38, 60), (68, 92), (92, 110)]),
    (20, [(-105, -88), (-17, 40), (42, 55), (72, 85), (95, 110), (120, 125)]),
    (15, [(-92, -83), (-75, -60), (-17, 45), (45, 51), (75, 80), (98, 109), (122, 126)]),
    (10, [(-83, -52), (-13, 10), (10, 45), (40, 50), (100, 104), (122, 126)]),
    (5, [(-80, -50), (8, 42), (95, 105), (109, 118), (120, 125)]),
    (0, [(-80, -35), (9, 40), (100, 117), (132, 150)]),
    (-5, [(-80, -35), (12, 40), (105, 115), (140, 150)]),
    (-10, [(-77, -37), (13, 40), (44, 50), (130, 142)]),
    (-15, [(-75, -39), (12, 37), (44, 50), (122, 146)]),
    (-20, [(-70, -40), (13, 35), (43, 48), (114, 152)]),
    (-25, [(-70, -48), (15, 32), (114, 153)]),
    (-30, [(-72, -52), (18, 30), (115, 125), (135, 152), (173, 178)]),
    (-35, [(-73, -57), (140, 150), (173, 178)]),
    (-40, [(-74, -63), (145, 148), (168, 175)]),
    (-45, [(-75, -66), (166, 170)]),
    (-50, [(-75, -68), (-61, -58)]),
    (-55, [(-70, -66)]),
]


def world_map(x, y, w, h, pins):
    R(x, y, w, h, fill=(226, 234, 240))
    lat_top, lat_bot = 82, -58
    sx = w / 360.0
    sy = h / (lat_top - lat_bot)

    def proj(lat, lon):
        return x + (lon + 180) * sx, y + (lat_top - lat) * sy

    step = 2.5
    for top, ranges in LAND:
        for sub in (0, step):
            lat = top - sub - step / 2
            if lat > lat_top or lat < lat_bot:
                continue
            for a, b in ranges:
                lon = a + step / 2
                while lon < b:
                    px, py = proj(lat, lon)
                    E(px, py, min(sx, sy) * step * 0.36, fill=(150, 160, 170))
                    lon += step
    for num, lat, lon, col in pins:
        px, py = proj(lat, lon)
        E(px, py, 7.2, fill=col, outline=(255, 255, 255), width=1.2)
        T(px, py, str(num), font(SANS_B, 8.5), (255, 255, 255), "mm")


# ---------------------------------------------------------------- page
M = 16


def masthead():
    R(0, 0, W, 112, fill=NAVY)
    R(M, 14, 84, 84, fill=RED, r=6)
    R(M, 14, 84, 22, fill=(255, 255, 255), r=6)
    R(M, 28, 84, 8, fill=(255, 255, 255))
    T(M + 42, 25, "NOV", font(SANS_B, 15), RED, "mm")
    T(M + 42, 63, "18", font(SERIF_B, 40), (255, 255, 255), "mm")
    T(M + 42, 88, "WED · 2026", font(SANS_B, 10), (255, 255, 255), "mm")
    T(116, 12, C.KICKER, font(SANS_B, 12.5), (255, 200, 80))
    T(W - M, 12, C.COUNTS, font(SANS_B, 12.5), (255, 200, 80), "ra")
    f, _, _ = fit(C.TITLE, SERIF_B, 64, W - 116 - M, 1, 30)
    T(116, 30, C.TITLE, f, (255, 255, 255))
    T(116, 92, C.SUBTITLE, font(SERIF, 13.5), (215, 222, 240))


def region_bar(y):
    span = W - 2 * M
    raw = [max(n / sum(k for _, k in C.REGIONS) * span, 92) for _, n in C.REGIONS]
    scale = span / sum(raw)
    x = M
    for (name, n), rw in zip(C.REGIONS, raw):
        w = rw * scale
        R(x, y, w + 0.5, 18, fill=REGION_COL[name])
        T(x + w / 2, y + 9, f"{name} {n}", font(SANS_B, 10.5), (255, 255, 255), "mm")
        x += w


def utc_strip(y, h=40):
    R(M, y, W - 2 * M, h, fill=(255, 255, 255), outline=RULE, width=1)
    R(M, y, 70, h, fill=RED)
    T(M + 35, y + h / 2 - 7, "THE DAY", font(SANS_B, 10.5), (255, 255, 255), "mm")
    T(M + 35, y + h / 2 + 7, "IN ORDER", font(SANS_B, 10.5), (255, 255, 255), "mm")
    n = len(C.UTC)
    cw = (W - 2 * M - 70) / n
    for i, (t, line) in enumerate(C.UTC):
        x = M + 70 + i * cw
        if i:
            L([(x, y + 5), (x, y + h - 5)], RULE, 1)
        T(x + 6, y + 5, t, font(SANS_B, 10.5), RED)
        f, lines, _ = fit(line, SANS, 10, cw - 10, 2, 8.5)
        for j, l_ in enumerate(lines[:2]):
            T(x + 6, y + 18 + j * 11, l_, f, INK)


def card(s, num, x, y, w, ih, hsize, hlines, dsize, dlines, total_h):
    scene(s["art"], x, y, w, ih, s.get("o", {}))
    R(x, y - 3, w, 3, fill=REGION_COL[s["region"]])
    ty = y + ih + 6
    col = REGION_COL[s["region"]]
    E(x + 8, ty + 6, 7.5, fill=col)
    T(x + 8, ty + 6, str(num), font(SANS_B, 9.5), (255, 255, 255), "mm")
    tag = s["tag"]
    tf = font(SANS_B, 8.5 if hsize < 20 else 9.5)
    tagw = tw(tag, tf) + 8
    ks = 9.5 if hsize < 20 else 10.5
    while tw(s["kicker"], font(SANS_B, ks)) > w - tagw - 26 and ks > 7.5:
        ks -= 0.25
    T(x + 20, ty + 6, s["kicker"], font(SANS_B, ks), col, "lm")
    tagcol = (30, 120, 60) if tag.startswith("CONFIRMED") else (200, 110, 0)
    R(x + w - tagw, ty, tagw, 13, fill=tagcol, r=2)
    T(x + w - tagw / 2, ty + 6.5, tag, tf, (255, 255, 255), "mm")
    hf, hl, hs = fit(s["head"], SERIF_B, hsize, w - 4, hlines, hsize * 0.72)
    yy = ty + 16
    for l_ in hl:
        T(x, yy, l_, hf, INK)
        yy += hs * 1.14
    df, dl, ds = fit(s["dek"], SANS, dsize, w - 4, dlines, dsize * 0.8)
    yy += 2
    for l_ in dl:
        T(x, yy, l_, df, (60, 60, 66))
        yy += ds * 1.25


def briefs(x, y, w, h, start):
    cols = 3
    cw = (w - (cols - 1) * 12) / cols
    per = math.ceil(len(C.BRIEFS) / cols)
    lh = h / per
    for i, (place, text, region) in enumerate(C.BRIEFS):
        c, r = divmod(i, per)
        bx, by = x + c * (cw + 12), y + r * lh
        n = start + i
        T(bx, by + lh / 2, f"{n}", font(SANS_B, 10), REGION_COL[region], "lm")
        pf = font(SANS_B, 10.5)
        T(bx + 18, by + lh / 2, place + ":", pf, INK, "lm")
        pw = tw(place + ": ", pf)
        f, lines, sz = fit(text, SANS, 10.5, cw - 18 - pw, 1, 9.5)
        if len(lines) > 1 or sz < 10:
            print("brief too long:", place, "|", text, "| size", sz, "lines", len(lines))
        T(bx + 18 + pw, by + lh / 2, lines[0], f, (45, 45, 50), "lm")


def main():
    masthead()
    region_bar(118)
    utc_strip(142)
    # leads
    y0 = 196
    lw = (W - 2 * M - 2 * 12) / 3
    for i, s in enumerate(C.LEADS):
        card(s, i + 1, M + i * (lw + 12), y0, lw, 132, 22.5, 2, 12.5, 2, 0)
    # tiles
    y1 = 444
    tw_ = (W - 2 * M - 3 * 12) / 4
    for i, s in enumerate(C.TILES):
        r, c = divmod(i, 4)
        card(s, len(C.LEADS) + i + 1, M + c * (tw_ + 12), y1 + r * 164, tw_, 72, 16, 2, 10.5, 2, 0)
    # bottom: map + briefs
    yb = 778
    L([(M, yb - 6), (W - M, yb - 6)], INK, 1.5)
    T(M, yb, "WHERE IT HAPPENED", font(SANS_B, 11.5), INK)
    mw = 286
    pins = []
    for i, s in enumerate(C.LEADS + C.TILES):
        lat, lon = s["pin"]
        pins.append((i + 1, lat, lon, REGION_COL[s["region"]]))
    world_map(M, yb + 18, mw, 146, pins)
    T(M, yb + 167, C.MAPNOTE, font(SANS, 9.5), GREY)
    bx = M + mw + 16
    T(bx, yb, C.ALSO, font(SANS_B, 11.5), INK)
    briefs(bx, yb + 17, W - M - bx, 163, len(C.LEADS) + len(C.TILES) + 1)
    # date check
    yd = 962
    R(M, yd, W - 2 * M, 36, fill=(253, 240, 238), outline=RED, width=1.2)
    T(M + 10, yd + 12, "DATE CHECK", font(SANS_B, 11.5), RED, "lm")
    f, lines, _ = fit(C.DATECHECK, SANS, 10.5, W - 2 * M - 120, 2, 8.5)
    for j, l_ in enumerate(lines):
        T(M + 108, yd + 4 + j * 14, l_, f, INK)
    T(M, 1006, C.FOOTER_L, font(SANS, 9.5), GREY, "lm")
    T(W - M, 1006, C.FOOTER_R, font(SANS_SB, 9.5), INK, "rm")

    out = img.resize((W, H), Image.LANCZOS)
    dest = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "entry.png")
    q = out.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
    q.save(dest, optimize=True)
    print(dest, os.path.getsize(dest))


if __name__ == "__main__":
    main()
