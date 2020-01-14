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
from App.models import Category, User, Link, Sponsor, Post, Reply
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
        post_l = Post.query.filter(Post.classid == subcat_id[i]).order_by(-Post.addtime).first()
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
    pagenation = Post.query.filter(Post.classid == cid).paginate(page, 10)
    data = {
        # Total number of posts
        'total':pagenation.total,
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
    length = len(posts)

    # last reply info
    # authors = db.session.query(User, Post).filter(User.id == Post.authorid).all()
    # print(authors)
    # author_name_dict = dict()
    # for post in posts:
    #     # author_name = db.session.query(User, Post).filter(User.id == Post.authorid).group_by(User.id).having(Post.authorid == post.authorid).order_by(-Post.addtime).limit(1).first()
    #     # if author_name:
    #     #     author_name_dict[author_name.username] = post.authorid
    #     #     print(author_name[1].authorid)
    #     for author in authors:
    #         print(author[0].id)
    #         if author[0].id == post.authorid:
    #             author_name_dict[author.username] = post.authorid
    #             break
    # print(author_name_dict)

    # replies = db.session.query(Reply, Post).filter(Reply.tid == Post.id).all()
    reply_dict = dict()
    # print(replies)
    for post in posts:
        # replies = db.session.query(Reply, Post).filter(Reply.tid == Post.id).group_by(Post.id).having(Post.authorid == post.authorid).order_by(-Reply.addtime).limit(1).first()
        rep = Reply.query.filter(Reply.tid == post.id).order_by(-Reply.addtime).limit(1).first()
        if rep:
            reply_dict[post.id] = list()
            reply_dict[post.id].append(rep.authorid)
            reply_dict[post.id].append(rep.addtime)
        else:
            reply_dict[post.id] = list()

    # print(reply_dict)
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
    # query first level data
    first_layer_category = Category.query.filter(Category.parentid == 0).all()
    # query other levels data
    other_layer_category = Category.query.filter(Category.parentid != 0).all()
    # the login page
    sponsor = Sponsor.query.first()
    # current date
    current_year = datetime.datetime.now().year
    time_now = datetime.datetime.now().strftime("%m-%d %H:%M")
    return render_template("foreground/addc-login.html", **locals())


@bbs.route('/notice/')
def login_notice():
    # query first level data
    first_layer_category = Category.query.filter(Category.parentid == 0).all()
    # query other levels data
    other_layer_category = Category.query.filter(Category.parentid != 0).all()
    # the login page
    sponsor = Sponsor.query.first()
    # current date
    current_year = datetime.datetime.now().year
    time_now = datetime.datetime.now().strftime("%m-%d %H:%M")
    message = "Login successfully"
    return render_template("foreground/notice.html", **locals())


@bbs.route('/fail/')
def fail_notice():
    # query first level data
    first_layer_category = Category.query.filter(Category.parentid == 0).all()
    # query other levels data
    other_layer_category = Category.query.filter(Category.parentid != 0).all()
    # the login page
    sponsor = Sponsor.query.first()
    # current date
    current_year = datetime.datetime.now().year
    time_now = datetime.datetime.now().strftime("%m-%d %H:%M")
    message = "Incorrect username or password, please try again "
    return render_template("foreground/notice_fail.html", **locals())


@bbs.route('/deletedpost/<int:ptid>')
def deleted_post(ptid):
    # query first level data
    first_layer_category = Category.query.filter(Category.parentid == 0).all()
    # query other levels data
    other_layer_category = Category.query.filter(Category.parentid != 0).all()
    # the login page
    sponsor = Sponsor.query.first()
    # current date
    current_year = datetime.datetime.now().year
    time_now = datetime.datetime.now().strftime("%m-%d %H:%M")
    message = "The post you viewed does not exist or has been deleted"
    if Post.query.filter(Post.id == ptid).first().isdel == 0:
        return redirect(url_for("bbs.list_detail", cid=ptid, page=1))
    else:
        return render_template("foreground/notice_post.html", **locals())


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


@bbs.route("/detail/<int:postid>/<int:page>/")
def list_detail(postid, page=1):
    the_post = Post.query.filter(Post.id == postid).first()
    the_author = User.query.filter(User.id == the_post.authorid).first()
    cid = Post.query.filter(Post.id == postid).first().classid

    # query first level data
    first_layer_category = Category.query.filter(Category.parentid == 0).all()
    # query other levels data
    other_layer_category = Category.query.filter(Category.parentid != 0).all()
    # the login page
    sponsor = Sponsor.query.first()
    # current date
    current_year = datetime.datetime.now().year
    time_now = datetime.datetime.now().strftime("%m-%d %H:%M")

    other_layer_id = Post.query.filter(Post.id == postid).first()
    # query to find the specified sub-section
    other_layer = Category.query.filter(Category.cid == other_layer_id.classid).all()
    other_layer_name = other_layer[0].classname
    other_layer_parent = other_layer[0].parentid

    # find first-level section according to the sub-section
    first_layer = Category.query.filter(and_(Category.parentid == 0, Category.cid == other_layer_parent)).all()
    first_layer_name = first_layer[0].classname
    first_layer_cid = first_layer[0].cid

    the_replies = Reply.query.filter(Reply.tid == the_post.id).all()
    print(the_replies)

    # Show posts by pagination
    pagenation = Reply.query.filter(Reply.tid == postid).paginate(page, 10)
    data = {
        # Total number of posts
        'total': pagenation.total,
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
    reply_s = data["posts"]
    length = len(reply_s)

    classid = postid

    # res = db.session.execute("select * from bbs_reply inner join bbs_user on bbs_reply.authorid=bbs_user.uid ")
    # print(res.fetchall())

    rep_user = dict()

    for rep in the_replies:
        print(rep)
        rep_user[rep.authorid] = User.query.filter(User.id == rep.authorid).first()
    print(rep_user)
    if the_post.isdel == 0:
        return render_template("foreground/detail.html", **locals())
    else:
        return


@bbs.route("/essence/<int:ptid>")
def post_essence(ptid):
    #
    post = Post.query.filter(Post.id == ptid).first()
    post.elite = 1 - post.elite
    db.session.commit()
    return redirect(url_for("bbs.list_detail", postid=ptid, page=1))


@bbs.route("/essence/<int:ptid>")
def post_pin(ptid):
    #
    post = Post.query.filter(Post.id == ptid).first()
    post.istop = 1 - post.istop
    db.session.commit()
    return redirect(url_for("bbs.list_detail", postid=ptid, page=1))


@bbs.route("/highlight/<int:ptid>")
def post_highlight(ptid):
    #
    post = Post.query.filter(Post.id == ptid).first()
    post.ishot = 1 - post.ishot
    db.session.commit()
    return redirect(url_for("bbs.list_detail", postid=ptid, page=1))


@bbs.route("/essence/<int:ptid>")
def post_delete(ptid):
    #
    post = Post.query.filter(Post.id == ptid).first()
    post.isdel = 1 - post.isdel
    db.session.commit()
    return redirect(url_for("bbs.list_detail", postid=ptid, page=1))