import threading

from PIL.ImageDraw import ImageDraw


class WMouse:
    WIDTH = 128

    def __init__(self, mouse_device, window_size, color):
        self.x = window_size[0] / 2
        self.y = window_size[1] / 2
        self.window_size = window_size
        self.color = color
        self.mouse = open(mouse_device, 'rb')
        self.update_thread = threading.Thread(target=self.update)
        self.update_thread.daemon = True
        self.update_thread.start()

    def update(self):
        while True:
            try:
                a = int.from_bytes(self.mouse.read(1), byteorder='big', signed=False)
                dx = int.from_bytes(self.mouse.read(1), byteorder='big', signed=False)
                dy = int.from_bytes(self.mouse.read(1), byteorder='big', signed=False)

                x = self.x
                y = self.y

                if a & 0b10000 == 0:
                    x += dx
                else:
                    x -= 0xFF - dx

                if a & 0b100000 != 0:
                    y += 0xFF - dy
                else:
                    y -= dy

                self.x = max(0, min(self.window_size[0] - self.WIDTH, x))
                self.y = max(0, min(self.window_size[1] - self.WIDTH, y))
            except ValueError:
                break

    def draw(self, pencil: ImageDraw):
        pencil.ellipse((self.x, self.y, self.x + self.WIDTH, self.y + self.WIDTH), fill=self.color)

    def finish(self):
        self.mouse.close()
