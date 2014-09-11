from PIL import Image, ImageDraw, ImageFilter
import os
import time


IMAGE_PATH = 'image.bmp'

def camera():
    print('Smile...')
    print(w)
    os.system('CommandCam.exe')
    print()
    print(w)
    time.sleep(4)

w = '=' * 60

print('Press space to start', end='')
a = input()

print(w)

if a == ' ':
    camera()
    text = open('text.txt', 'w')
    img = Image.open(IMAGE_PATH)
    img = img.filter(ImageFilter.BLUR)
    width2 = int(424)
    height2 = int(240 * 0.666)
    img = img.resize((width2, height2))
    img.save('image-size-good.bmp', 'BMP')

    width1, height1 = img.size

    image = Image.open("image-size-good.bmp")
    draw = ImageDraw.Draw(image)
    width3, height3 = image.size
    pix = image.load()
    main_dict = {(str(x) + '-' + str(y)): str(s) for x, y, s in zip(range(0, 260, 10), range(9, 260, 10), 'MNABDEW0RD9X1L2T3VZGC8576 ')}
    str_width = ''

    for y in range(height3):
        for x in range(width3):
            r = pix[x, y][0]
            g = pix[x, y][1]
            b = pix[x, y][2]
            c = int(0.3*r + 0.59*g + 0.11*b)
            draw.point((x, y), (c, c, c))
            q = str(c // 10 * 10) + '-' + str(c // 10 * 10 + 9)

            b = c if b < c else b

            str_width += main_dict[q]

        with open('text.txt', 'a') as text:
            text.write(str(str_width) + '\n')
        str_width = ''

    image.save('image-black.bmp', 'BMP')
    del draw
    print('Done!')
    print(w)
    os.system('text.txt')

else:
    print('Error')

print (b)