# -*- coding: utf-8 -*-
# @File    : tools.py
# @Theme   ：
# @Time    : 2020/1/10 20:12
# @Author  :
import random
import string

from PIL import ImageFont, ImageDraw, Image
from flask_wtf import FlaskForm
from six import BytesIO
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class VerifyCode:
    # Class initialization
    def __init__(self, width=80, height=20, size=4):
        # the width，height of the verification code
        self.width = width
        self.height = height
        # the number of characters in the verification code
        self.size = size

    @property
    def code(self):
        return self.__code

    # generate a verification code
    def generate(self):
        # create a new image with the given mode, size and color.
        # size is given as a (width, height)-tuple, in pixels.
        self.im = Image.new("RGB", (self.width, self.height), self.__rand_color(200, 250))
        # create an object that can be used to draw in the given image.
        self.pen = ImageDraw.Draw(self.im)
        # generate a random string with fixed length
        self.rand_string()
        # draw verification code
        self.draw_code()
        # draw points
        self.__draw_point()
        # draw lines
        self.__draw_line()
        # save verification code image into buffer
        buf = BytesIO()
        # self.im.save("App/static/foreground/images/vc.png")
        self.im.save(buf, 'png')
        binary = buf.getvalue()
        buf.close()
        return binary

    def rand_string(self):
        # Character set with uppercase and lowercase letters and numbers
        chr_s = string.ascii_letters + string.digits
        # obtain the verification code
        self.__code = "".join(random.sample(chr_s, self.size))
        return self.__code

    def draw_code(self):
        # load a TrueType font file, and create a font object using the given encoding.
        font_c = ImageFont.truetype("App/static/foreground/font/simkai.ttf", size=18, encoding="utf-8")
        # Set the spacing and position of characters
        # width_c means the width of each character
        width_c = (self.width - 5) / self.size
        for i in range(self.size):
            x = 5 + width_c * i
            y = 2
            # position tuple, the character, font, character color are used to draw the code
            self.pen.text((x, y), self.__code[i], font=font_c, fill=self.__rand_color(0, 0))

    def __draw_point(self):
        # draw 200 interference points
        for i in range(200):
            x = random.randint(1, self.width - 1)
            y = random.randint(1, self.height - 1)
            self.pen.point((x, y), fill=self.__rand_color(120, 180))

    def __draw_line(self):
        # draw five interference lines
        for i in range(5):
            # two points are used to draw one line
            x1 = random.randint(1, self.width - 1)
            x2 = random.randint(1, self.width - 1)
            y1 = random.randint(1, self.height - 1)
            y2 = random.randint(1, self.height - 1)
            self.pen.line([(x1, y1), (x2, y2)], fill=self.__rand_color(150, 180), width=1)

    # Generate a random color
    def __rand_color(self, low, high):
        # RGB color style
        return random.randint(low, high), random.randint(low, high), random.randint(low, high)


class RegisterForm(FlaskForm):
    # Registration form contains five fields
    username = StringField(validators=[DataRequired("User name must be entered"), Length(min=3, max=12, message="User name must contain 3 to 12 characters")])
    password = PasswordField(validators=[DataRequired("Password must be entered"), Length(min=3, max=12, message="Password must contain 3 to 12 characters")])
    confirm = PasswordField(validators=[DataRequired("Password must be entered"), EqualTo("password", message="Two password entries do not match")])
    email = StringField(validators=[DataRequired("Please enter your email address"), Email(message="Invalid mailbox format")])
    verification_code = StringField(validators=[DataRequired("Please enter verification code"), Length(min=4, max=4, message="Wrong verification code length")])