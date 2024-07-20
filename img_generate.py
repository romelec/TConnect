from PIL import Image, ImageFont, ImageDraw

red   = (0xa3, 0x00, 0x00)
green = (0x08, 0x41, 0x00)
blue  = (0x00, 0x00, 0x94)
gray  = (0x4a, 0x49, 0x4a)
black  = (0x00, 0x00, 0x00)


def img_large(text, bg):
    font_size = 172
    font_filepath = "NotoSansMono-Regular.ttf"
    color = (255,255,255)
    font = ImageFont.truetype(font_filepath, size=font_size)

    img = Image.new(size=(230, 140), mode='RGB',color=bg[1])
    draw = ImageDraw.Draw(img)
    draw.text((13,-52), text ,color, font)

    file = f"Lfonts/{bg[0]}{text}.png"
    print(file)

    img.save(file)

def img_small(text, bg):
    font_size = 92
    font_filepath = "NotoSansMono-Regular.ttf"
    color = (255,255,255)
    font = ImageFont.truetype(font_filepath, size=font_size)

    img = Image.new(size=(112, 82), mode='RGB',color=bg[1])
    draw = ImageDraw.Draw(img)
    draw.text((0,-26), text ,color, font)

    file = f"Sfonts/{bg[0]}{text}.png"
    print(file)

    img.save(file)

#img_large("88", ['g', gray])
#exit()

Lcolors = [['r', red], ['n', black], ['b', blue]]
for c in Lcolors:
    img_large("-", c)
    img_large("--", c)
    for t in range(5,41):
        temp = f"{t:02d}"
        img_large(temp, c)
Scolors = [['g', gray], ['b', black]]
for c in Scolors:
    img_small("-", c)
    img_small("--", c)
    for t in range(-9,41):
        temp = f"{t:02d}"
        img_small(temp, c)

