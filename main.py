import math
import subprocess
import sys
import time
from subprocess import Popen

from PIL import Image, ImageFont, ImageDraw

FB_SIZE = (640, 480)
FONT_SIZE = 16

if __name__ == "__main__":
    if len(sys.argv) == 1 or sys.argv[1] == 'show':
        # Disable blinking cursor
        # print('\033[?25l')
        p = Popen(['bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False, bufsize=0)
        font = ImageFont.load_default()
        with Image.open('/tmp/ttyback.png') as img, open('/dev/fb0', 'wb') as fb:
            pencil = ImageDraw.Draw(img)
            pencil.text((0, 0), "HEY", font=font, fill='red', size=16)
            fb.seek(0)
            fb.write(img.tobytes('raw', 'BGRA'))
            try:
                while True:
                    time.sleep(1)
                    i = 20
                    p.stdin.write(input('Enter bash command : ').encode('utf-8'))
                    for line in iter(p.stdout.readline, b''):
                        pencil.text((0, i), line, font=font, fill='red', size=FONT_SIZE)
                    i += FONT_SIZE
                    # raw_file.seek(0)
                    fb.seek(0)
                    # fb.write(raw_file.read(raw_file_length))
                    fb.write(img.tobytes('raw', 'BGRA'))
                    p.terminate()
            except KeyboardInterrupt:
                pass
        # Enable blinking cursor
        # print('\033[?25h')
    elif sys.argv[1] == 'load':
        path = input('Image path : ')
        with Image.open(path) as img, Image.new('RGBA', FB_SIZE, 'black') as image:
            new_size = FB_SIZE
            if img.width > img.height:
                new_size = FB_SIZE[0], math.ceil(img.height * FB_SIZE[0] / img.width)
            else:
                new_size = math.ceil(img.width * FB_SIZE[1] / img.height), FB_SIZE[1]
            margin_left = (FB_SIZE[0] - new_size[0]) // 2
            margin_right = margin_left + new_size[0]
            margin_top = (FB_SIZE[1] - new_size[1]) // 2
            margin_bottom = margin_top + new_size[1]
            image.paste(img.resize(new_size), (margin_left, margin_top))
            image.save('/tmp/ttyback.png')
            image.close()
