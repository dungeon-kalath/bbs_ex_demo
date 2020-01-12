# -*- coding: utf-8 -*-
# @File    : views.py
# @Theme   ： foreground view
# @Time    : 2020/1/7 18:40
# @Author  : Kalath
import datetime

from flask import Blueprint, render_template, request, redirect, url_for, session, make_response
from flask_login import login_required
from sqlalchemy import func, and_

from App.extensions import db
from App.models import Category, User, Link, Sponsor, Post
from App.tools import VerifyCode

bbs = Blueprint("bbs", __name__)


@bbs.route("/")
@bbs.route("/<int:cid>/")
def bbs_index(cid=0):
    """

    :param cid: default value is 0, show every section. For other values, show specified section.
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

    # if cid not equal to 0, find the specified section
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


@bbs.route("/list/<int:cid>/<int:page>/")
def list_category(cid, page=1):
    #  sponsor object
    sponsor = Sponsor.query.first()
    # current date
    current_year = datetime.datetime.now().year
    time_now = datetime.datetime.now().strftime("%m-%d %H:%M")

    # query to find the specified sub-section
    other_layer = Category.query.filter(Category.cid == cid).all()
    other_layer_name = other_layer[0].classname
    other_layer_parent = other_layer[0].parentid

    # find first-level section according to the sub-section
    first_layer = Category.query.filter(and_(Category.parentid == 0, Category.cid == other_layer_parent)).all()
    first_layer_name = first_layer[0].classname
    first_layer_cid = first_layer[0].cid

    compere_name = other_layer[0].compere
    post_num = other_layer[0].postcount

    classid =cid

    # query first level data
    first_layer_category = Category.query.filter(Category.parentid == 0).all()
    # query other levels data
    other_layer_category = Category.query.filter(Category.parentid != 0).all()

    # Show posts by pagination
    pagenation = Post.query.paginate(page, 10)
    data = {
        # Data list of current page
        'posts': pagenation.items,
        # Current page number
        'current': pagenation.page,
        # Number of posts per page
        'per_page': pagenation.per_page,
        # Total number of pages
        'pages': pagenation.pages,
        # Next page number
        'next': pagenation.next_num,
        # Previous page number
        'pre': pagenation.prev_num
    }
    posts = data["posts"]
    return render_template("foreground/list.html", **locals())


@bbs.route("/publish/<int:cid>/", methods=["GET", "POST"])
# login required to publish a post
@login_required
def publish_post(cid):
    sponsor = Sponsor.query.first()
    # current date
    current_year = datetime.datetime.now().year
    time_now = datetime.datetime.now().strftime("%m-%d %H:%M")

    # query to find the specified sub-section
    other_layer = Category.query.filter(Category.cid == cid).all()
    other_layer_name = other_layer[0].classname
    other_layer_parent = other_layer[0].parentid

    # find first-level section according to the sub-section
    first_layer = Category.query.filter(and_(Category.parentid == 0, Category.cid == other_layer_parent)).all()
    first_layer_name = first_layer[0].classname
    first_layer_cid = first_layer[0].cid

    if request.method == "GET":
        return render_template("foreground/addc.html", **locals())
    else:
        # add a record of the post to the database
        post_title = request.form.get("subject")
        post_content = request.form.get("content")
        post_price = request.form.get("price")
        post = Post()
        post.authorid = session['user_id']
        post.title = post_title
        post.content = post_content
        post.addtime = int(datetime.datetime.now().strftime("%Y%m%d"))
        post.addip = 1123133
        post.classid = cid
        post.replycount = 0
        post.hits = 0
        post.istop = 0
        post.elite = 0
        post.ishot = 0
        post.rate = 0
        post.isdel = 0
        post.isdisplay = 0
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("bbs.list_category", cid=cid))


@bbs.route("/login/")
def bbs_login():
    # the login page
    sponsor = Sponsor.query.first()
    # current date
    current_year = datetime.datetime.now().year
    time_now = datetime.datetime.now().strftime("%m-%d %H:%M")
    return render_template("foreground/addc-login.html", **locals())


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