from PIL import Image
from colorama import init, Fore
import sys
import colorsys
import os

fill = [" ", ".", "-", ":", "*", "+", "%", "&", "@", "#"]

print("Image to ASCII @ Developed by Leegeunhyeok (2018.07)")

class converter():
    def __init__(self, dir):
        self.dir = dir
        self.size = (50, 50)
        init(autoreset=True)

    def create_gray(self):
        try:
            with Image.open(self.dir) as img:
                # 이미지 모드를 흑백으로 변환
                if img.mode != "L":
                    img = img.convert("L")

                # 이미지를 size에 맞게 축소 (썸네일)
                img.thumbnail(self.size)

                # 이미지의 모든 픽셀 정보 로드
                pixels = img.load()

                # 이미지의 폭, 높이 가져오기
                width, height = img.size
                
                # 1픽셀씩 반복하며 출력
                for h in range(height):
                    for w in range(width):
                        print(self.get_ascii(pixels[w, h]), end="")
                    # 개행
                    print()

        except Exception as e:
            print("작업 중 오류가 발생하였습니다:", e)

    def create_color(self):
        # TODO: 색상 추출
        try:

            with Image.open(self.dir) as img:
                
                # 이미지 모드가 RGB가 아닌 경우 RGB 모드로 변환
                if img.mode != "RGB":
                    img = img.convert("RGB")

                # 이미지를 size에 맞게 축소 (썸네일)
                img.thumbnail(self.size)

                # 이미지의 모든 픽셀 정보 로드
                pixels = img.load()

                # 이미지의 폭, 높이 가져오기
                width, height = img.size
                
                # 1픽셀씩 반복하며 출력
                for h in range(height):
                    for w in range(width):
                        print(self.get_color_ascii(pixels[w, h]), end="")
                    # 개행
                    print()

        except Exception as e:
            print("작업 중 오류가 발생하였습니다:", e)
    
    # 0 ~ 255 사이의 값을 받은 후 0 ~ 9 범위로 변환
    def get_ascii(self, value):
        return fill[int(value / 25) - 1] * 2

    def get_color_ascii(self, rgb):
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]

        # rgb 색상 데이터를 모두 더한다
        pixel_values = r + g + b

        # 모두 더한 색상 데이터를 범위 10으로 제한 (765 -> 10)
        c = fill[int(pixel_values / 76.5) - 1] * 2

        # 기본 색상은 리셋
        color = Fore.RESET

        # rgb 색상 데이터를 hsv로 변환
        # 변환할 rgb 데이터의 범위는 0 ~ 1 이어야 함
        h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)

        # h에 따른 색상
        if h >= 0 and h <= 0.07: # 0 ~ 30
            color = Fore.RED
        elif h > 0.07 and h <= 0.20: # 31 ~ 70
            color = Fore.YELLOW
        elif h > 0.20 and h <= 0.45: # 71 ~ 160
            color = Fore.GREEN
        elif h > 0.45 and h <= 0.55: # 161 ~ 200
            color = Fore.CYAN
        elif h > 0.55 and h <= 0.72: # 201 ~ 260
            color = Fore.BLUE
        elif h > 0.72 and h <= 0.92: # 261 ~ 330
            color = Fore.MAGENTA
        else:
            color = Fore.RED

        # v, s에 따라 검정, 흰색으로 변경
        if v >= 0.75 or s <= 0.25:
            color = Fore.WHITE

        if v <= 0.25:
            color = Fore.BLACK
        
        # 색상과 출력할 문자를 합쳐서 전달
        return color + c


# 모드 입력 확인
mode_check = False
try:
    # 이미지 경로
    img_dir = sys.argv[1]
except:
    print("이미지 경로를 찾을 수 없습니다.")
    exit()

try:
    # 실행 모드
    mode = sys.argv[2].lower()
    mode_check = True
except:
    pass

if os.path.isfile(img_dir):
    c = converter(img_dir)

    if mode_check:
        if mode == "-grey":
            c.create_gray()
        elif mode == "-color":
            c.create_color()
        else:
            print("알 수 없는 모드입니다. {}".format(mode))
    else:
        # 모드를 입력하지 않았으면 흑백모드로 진행
        c.create_gray()
        
else:
    print("{} 파일이 없습니다.".format(img_dir))