# -*- coding: utf-8 -*-
# @File    : user.py
# 描述     ： manage user information, maintenance, registration, logging actions of users
# @Time    : 2020/1/7 18:40
# @Author  : Kalath
from flask import Blueprint

user_info = Blueprint("user_info", __name__, url_prefix="/user")


@user_info.route("/login/")
def user_login():
    return "login page!!!"
