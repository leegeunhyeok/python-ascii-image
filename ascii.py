from PIL import Image
import sys
import os

fill = [" ", ".", "-", ":", "*", "+", "=", "%", "@", "#"]

class color:
    BLACK = '\033[30m'
    RED ='\033[31m'
    GREEN ='\033[32m'
    ORANGE ='\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    PINK = '\033[95m'
    LIGHTBLUE = '\033[94m'
    LIGHTGREEN = '\033[92m'
    YELLOW = '\033[93m'
    LIGHTRED = '\033[91m'
    RESET = '\033[0m'

class converter(color):
    def __init__(self, dir):
        self.dir = dir
        self.size = (100, 100)

    def create_gray(self):
        try:
            with Image.open(self.dir) as img:

                if img.mode != "L":
                    img = img.convert("L")

                img.thumbnail(self.size)
                img.show()

                pixels = img.load()
                width, height = img.size
                print(img.size)
                
                for h in range(height):
                    for w in range(width):
                        print(self.get_ascii(pixels[w, h]), end="")
                    print()
        except Exception as e:
            print("작업 중 오류가 발생하였습니다:", e)

    def create_color(self):
        # TODO: 색상 추출
        try:
            with Image.open(self.dir) as img:

                if img.mode != "RGB":
                    img = img.convert("RGB")

                img.thumbnail(self.size)
                img.show()

                pixels = img.load()
                width, height = img.size
                print(img.size)
                
                for h in range(height):
                    for w in range(width):
                        pixel = pixels[w, h]
                        print(self.get_color(pixel), end="")
                    print()
        except Exception as e:
            print("작업 중 오류가 발생하였습니다:", e)

    def get_ascii(self, value):
        return fill[int(value / 25) - 1] * 2

    def get_color(self, rgb):
        pixel_values = rgb[0] + rgb[1] + rgb[2]
        c = fill[int(pixel_values / 76) - 1] * 2
        return c


mode_check = False
img_dir = sys.argv[1]
try:
    mode = sys.argv[2].lower()
    mode_check = True
except:
    pass

if os.path.isfile(img_dir):
    c = converter(img_dir)

    if mode == "-grey":
        c.create_gray()
    elif mode == "-color":
        c.create_color()
    else:
        if mode_check:
            print("알 수 없는 모드입니다. {}".format(mode))
        else:
            c.create_gray()
else:
    print("{} 파일이 없습니다.".format(img_dir))