# -*- coding: utf-8 -*-
# @File    : category.py
# @Theme   ： sections of forum
# @Time    : 2020/1/7 18:40
# @Author  : Kalath
from flask import Blueprint

sections = Blueprint("sections", __name__, url_prefix="/admin")


@sections.route("/sec/")
def section_index():
    return "sections of forum"
