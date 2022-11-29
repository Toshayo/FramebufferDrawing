import math
import os
import random
import sys

from PIL import Image, ImageFont, ImageDraw

from WFrameBufferHelper import WFrameBufferHelper
from WMouse import WMouse

FONT_SIZE = 32


if __name__ == "__main__":
    if os.path.exists('/tmp/ttyback.png') and (len(sys.argv) == 1 or sys.argv[1] == 'show'):
        # Disable blinking cursor
        print('\033[?25l')

        font = ImageFont.truetype('Ubuntu-L.ttf', size=FONT_SIZE)
        with Image.open('/tmp/ttyback.png') as img_original, open('/dev/fb0', 'wb') as fb:
            mice = []
            for file in os.listdir('/dev/input'):
                if file.startswith('mouse'):
                    mice.append(
                        WMouse(
                            '/dev/input/' + file,
                            (img_original.width, img_original.height),
                            random.randint(0, 0xFFFFFF)
                        )
                    )
            img = img_original.copy()

            pencil = ImageDraw.Draw(img)
            # pencil.text((0, 0), "HEY", font=font, fill='red', size=FONT_SIZE)

            fb.seek(0)
            fb.write(img.tobytes('raw', 'BGRA'))

            try:
                while True:
                    img.paste(img_original)

                    for mouse in mice:
                        mouse.draw(pencil)

                    fb.seek(0)
                    fb.write(img.tobytes('raw', 'BGRA'))
            except KeyboardInterrupt:
                # Enable blinking cursor
                print('\033[?25h')
                print('Move your ' + ('mice' if len(mice) > 1 else 'mouse') + ' to exit!')
                for mouse in mice:
                    mouse.finish()
    elif sys.argv[1] == 'load':
        path = input('Image path : ')
        with open('/dev/fb0', 'wb') as fb:
            fb_size = WFrameBufferHelper(fb).get_size()
        with Image.open(path) as img, Image.new('RGBA', fb_size, 'black') as image:
            new_size = fb_size
            if img.width > img.height:
                new_size = fb_size[0], math.ceil(img.height * fb_size[0] / img.width)
            else:
                new_size = math.ceil(img.width * fb_size[1] / img.height), fb_size[1]
            margin_left = (fb_size[0] - new_size[0]) // 2
            margin_right = margin_left + new_size[0]
            margin_top = (fb_size[1] - new_size[1]) // 2
            margin_bottom = margin_top + new_size[1]
            image.paste(img.resize(new_size), (margin_left, margin_top))
            image.save('/tmp/ttyback.png')
            image.close()
