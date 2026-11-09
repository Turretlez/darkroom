# draws the Darkroom app icon: a little cream disposable camera on a warm orange tile
from PIL import Image, ImageDraw, ImageFilter
S = 1024
im = Image.new('RGB', (S, S), (226, 87, 43))
d = ImageDraw.Draw(im)
for y in range(S):  # soft vertical gradient
    t = y / S
    d.line([(0, y), (S, y)], fill=(int(240 - 40*t), int(120 - 50*t), int(58 - 20*t)))
sh = Image.new('L', (S, S), 0); ImageDraw.Draw(sh).rounded_rectangle([170, 330, 870, 790], 70, fill=150)
im.paste((120, 40, 15), (0, 0), sh.filter(ImageFilter.GaussianBlur(30)))
d = ImageDraw.Draw(im)
d.rounded_rectangle([150, 290, 874, 760], 70, fill=(244, 234, 216))          # body
d.rounded_rectangle([150, 640, 874, 760], 70, fill=(226, 211, 186))          # lower band
d.rectangle([150, 640, 874, 700], fill=(226, 211, 186))
d.rounded_rectangle([210, 345, 380, 455], 22, fill=(27, 23, 20))             # viewfinder
d.rounded_rectangle([225, 360, 365, 440], 14, fill=(64, 80, 92))
d.rounded_rectangle([640, 345, 820, 430], 18, fill=(255, 238, 190))          # flash
d.ellipse([400, 370, 700, 670], fill=(27, 23, 20))                           # lens
d.ellipse([440, 410, 660, 630], fill=(58, 48, 40))
d.ellipse([485, 455, 615, 585], fill=(20, 24, 30))
d.ellipse([505, 470, 555, 520], fill=(160, 175, 190))
d.rounded_rectangle([690, 240, 800, 300], 16, fill=(196, 60, 24))            # shutter
im.save('icons/icon-512.png'.replace('512', '1024-src'))  # unused, kept small below
for n, z in [('icon-512.png', 512), ('icon-192.png', 192), ('apple-touch-icon.png', 180)]:
    im.resize((z, z), Image.LANCZOS).save('icons/' + n)
