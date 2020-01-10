# -*- coding: utf-8 -*-
# @File    : tools.py
# @Theme   ：
# @Time    : 2020/1/10 20:12
# @Author  :
import random
import string

from PIL import ImageFont, ImageDraw, Image
from six import BytesIO


class VerifyCode:
    def __init__(self, width=50, height=25, size=4):
        self.width = width
        self.height = height
        self.size = size

    @property
    def code(self):
        return self.__code

    def generate(self):
        self.im = Image.new("RGB", (self.width, self.height), self.__rand_color(200, 250))
        self.pen = ImageDraw.Draw(self.im)
        res = self.rand_string()
        self.draw_code()
        self.__draw_point()
        self.__draw_line()
        buf = BytesIO()
        self.im.save("App/static/foreground/images/vc.png")

        # binary = buf.getvalue()
        buf.close()
        # return binary
        return res


    def rand_string(self):
        chr_s = string.ascii_letters + string.digits
        self.__code = "".join(random.sample(chr_s, self.size))
        print(self.__code)
        return self.__code

    def draw_code(self):
        font_c = ImageFont.truetype("simkai.ttf", size=18, encoding="utf-8")
        width_c = (self.width - 5) / self.size
        for i in range(self.size):
            x = 2 + width_c * i
            y = 5
            self.pen.text((x, y), self.__code[i], font=font_c, fill=self.__rand_color(0, 0))

    def __draw_point(self):
        for i in range(200):
            x = random.randint(1, self.width - 1)
            y = random.randint(1, self.height - 1)
            self.pen.point((x, y), fill=self.__rand_color(120, 180))

    def __draw_line(self):
        for i in range(5):
            x1 = random.randint(1, self.width - 1)
            x2 = random.randint(1, self.width - 1)
            y1 = random.randint(1, self.height - 1)
            y2 = random.randint(1, self.height - 1)
            self.pen.line([(x1, y1), (x2, y2)], fill=self.__rand_color(150, 180), width=1)

    def __rand_color(self, low, high):
        return random.randint(low, high), random.randint(low, high), random.randint(low, high)