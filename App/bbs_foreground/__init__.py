# -*- coding: utf-8 -*-
# @File    : __init__.py.py
# @Theme   ：
# @Time    : 2020/1/7 18:01
# @Author  : Kalath
from App.bbs_foreground.user import user_info
from App.bbs_foreground.views import bbs


def register_bp_front(app):
    app.register_blueprint(user_info)
    app.register_blueprint(bbs)
