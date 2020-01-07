# -*- coding: utf-8 -*-
# @File    : views.py
# 描述     ：
# @Time    : 2020/1/7 18:40
# @Author  : Kalath
from flask import Blueprint


bbs = Blueprint("bbs", __name__)


@bbs.route("/")
def bbs_index():
    return "bbs index"
