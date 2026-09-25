"""Render assets/og-card.png, the 1200x630 link-preview card, in Midnight.

Run from the repository root: `python tools/make-og-card.py`. Needs Pillow, and
reads Georgia and Segoe UI from the Windows font folder.

The page itself paints a radial "low light from above" glow over a dark base;
this does the same with a vertical falloff so the card reads as the same
surface as the site it links to.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1200, 630
BASE = (11, 15, 29)       # --bg-base #0B0F1D
TOP = (26, 36, 64)        # --bg-top  #1A2440
INK = (238, 241, 248)     # --ink
INK2 = (238, 241, 248)
ACCENT = (237, 179, 92)   # --accent #EDB35C

card = Image.new("RGB", (W, H), BASE)
px = card.load()

# Radial glow centred above the top edge, falling off to the base colour.
cx, cy, radius = W * 0.5, -H * 0.25, H * 1.55
for y in range(H):
    for x in range(0, W, 4):
        d = (((x - cx) ** 2 + (y - cy) ** 2) ** 0.5) / radius
        t = max(0.0, 1.0 - d) ** 1.6
        c = tuple(int(BASE[i] + (TOP[i] - BASE[i]) * t) for i in range(3))
        for xx in range(x, min(x + 4, W)):
            px[xx, y] = c
card = card.filter(ImageFilter.GaussianBlur(2))
draw = ImageDraw.Draw(card)

# App icon, squircle-cropped the way both stores round it.
icon = Image.open("assets/app-icon.png").convert("RGB").resize((236, 236), Image.LANCZOS)
mask = Image.new("L", (236 * 4, 236 * 4), 0)
ImageDraw.Draw(mask).rounded_rectangle([0, 0, 236 * 4 - 1, 236 * 4 - 1], radius=58 * 4, fill=255)
icon.putalpha(mask.resize((236, 236), Image.LANCZOS))
IX, IY = 96, 197
card.paste(icon, (IX, IY), icon)

TX = IX + 236 + 72
name = ImageFont.truetype("C:/Windows/Fonts/georgiab.ttf", 92)
tag = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 38)
label = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 22)

draw.text((TX, 196), "FAMILY HEALTH, QUIETLY", font=label, fill=ACCENT)
draw.text((TX, 232), "Bellwether", font=name, fill=INK)
draw.text((TX, 352), "Know how they're doing", font=tag, fill=INK2)
draw.text((TX, 400), "before you ask.", font=tag, fill=INK2)

# The accent hairline the site uses under its eyebrows.
draw.rectangle([TX, 470, TX + 96, 473], fill=ACCENT)
draw.text((TX, 496), "iOS  ·  Android", font=tag.font_variant(size=26), fill=(160, 170, 190))

card.save("assets/og-card.png", optimize=True)
print(card.size)
