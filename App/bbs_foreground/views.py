# -*- coding: utf-8 -*-
# @File    : views.py
# 描述     ：
# @Time    : 2020/1/7 18:40
# @Author  : Kalath
from flask import Blueprint, render_template
from sqlalchemy import func

from App.extensions import db
from App.models import Category, User

bbs = Blueprint("bbs", __name__)


@bbs.route("/")
@bbs.route("/<int:cid>/")
def bbs_index(cid=0):
    """

    :param cid: default value is 0, show every section. For other values, show specific section.
    :return:
    """
    big_category = Category.query.filter(Category.parentid == 0).all()
    small_category = Category.query.filter(Category.parentid != 0).all()

    posts = db.session.query(func.sum(Category.postcount)).group_by(Category.parentid).having(Category.parentid == 0).all()[0][0]
    replies = db.session.query(func.sum(Category.replycount)).group_by(Category.parentid).having(Category.parentid == 0).all()[0][0]

    user_count = User.query.count()

    new_user = User.query.order_by(-User.id).limit(1).first()


    if cid != 0:
        for big in big_category:
            if big.cid == cid:
                the_big = big
                break
        return render_template("foreground/index.html", **locals())
    else:
        # return render_template("foreground/index.html", big_category=big_category, cid=cid,
        #                        small_category=small_category)
        return render_template("foreground/index.html", **locals())

@bbs.route("/list/<int:cid>/")
def list_category(cid):
    return "post list"
