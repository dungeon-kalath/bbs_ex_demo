# -*- coding: utf-8 -*-
# @File    : __init__.py.py
# @Theme  ： create application object
# @Time    : 2020/1/7 17:46
# @Author  : Kalath
from flask import Flask

from App.bbs_background import register_bp_back
from App.bbs_foreground import register_bp_front
from App.extensions import app_init
from App.settings import config
from App.models import *


def create_app():
    app = Flask(__name__)
    # load configurations
    app.config.from_object(config.get("development", "default"))

    # load extensions
    app_init(app)

    # register blueprints
    register_bp_back(app)
    register_bp_front(app)

    return app
