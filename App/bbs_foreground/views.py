# -*- coding: utf-8 -*-
# @File    : views.py
# @Theme   ： foreground view
# @Time    : 2020/1/7 18:40
# @Author  : Kalath
import datetime

from flask import Blueprint, render_template, request, redirect, url_for, session, make_response
from flask_login import login_required
from sqlalchemy import func

from App.extensions import db
from App.models import Category, User, Link, Sponsor, Post
from App.tools import VerifyCode, RegisterForm

bbs = Blueprint("bbs", __name__)


@bbs.route("/")
@bbs.route("/<int:cid>/")
def bbs_index(cid=0):
    """

    :param cid: default value is 0, show every section. For other values, show specific section.
    :return:
    """
    # query first level data
    first_layer_category = Category.query.filter(Category.parentid == 0).all()
    # query other levels data
    other_layer_category = Category.query.filter(Category.parentid != 0).all()

    # number of posts
    posts = db.session.query(func.sum(Category.postcount)).group_by(Category.parentid).having(Category.parentid == 0).all()[0][0]
    res = db.session.execute("select sum(replycount) from bbs_category")
    # print(res.fetchall())

    # number of replies
    replies = db.session.query(func.sum(Category.replycount)).group_by(Category.parentid).having(Category.parentid == 0).all()[0][0]
    # number of users
    user_count = User.query.count()
    # name of new user
    new_user = User.query.order_by(-User.id).limit(1).first()
    # all links
    links = Link.query.order_by(-Link.displayorder).all()
    #  sponsor object
    sponsor = Sponsor.query.first()
    # current date
    current_year = datetime.datetime.now().year
    time_now = datetime.datetime.now().strftime("%m-%d %H:%M")

    # last post part
    subcat_nums = len(Category.query.filter(Category.parentid != 0).all())
    subcat_id = [x.cid for x in Category.query.filter(Category.parentid != 0).all()]
    post_s = list()
    for i in range(subcat_nums):
        post_l = Post.query.filter(Post.classid == subcat_id[i]).first()
        post_s.append(post_l)

    # if cid not equal to 0, find the specific section
    if cid != 0:
        for sub_category in first_layer_category:
            if sub_category.cid == cid:
                the_category = sub_category
                break
        return render_template("foreground/index.html", **locals())
    # cid equals to 0, show every section
    else:
        # return render_template("foreground/index1.html", big_category=big_category, cid=cid,
        #                        small_category=small_category)
        return render_template("foreground/index.html", **locals())


@bbs.route("/list/<int:cid>/")
def list_category(cid):
    return "post list"


@bbs.route("/publish/")
# login required to publish a post
@login_required
def publish_post():
    return "post"


@bbs.route("/login/")
def bbs_login():
    return "login page"


@bbs.route("/code/")
def show_code():
    # generate verification code
    vc = VerifyCode()
    res = vc.generate()
    # save the verification code into the session
    session['code'] = vc.code
    response = make_response(res)
    response.headers['content-type'] = 'image/png'
    return response