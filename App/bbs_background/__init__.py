# -*- coding: utf-8 -*-
# @File    : __init__.py.py
# 描述     ：
# @Time    : 2020/1/7 18:01
# @Author  : Kalath
from App.bbs_background.category import sections


def register_bp_back(app):
    app.register_blueprint(sections)
