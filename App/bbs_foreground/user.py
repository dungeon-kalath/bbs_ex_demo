# -*- coding: utf-8 -*-
# @File    : user.py
# @Theme   ： manage user information, maintenance, registration, logging actions of users
# @Time    : 2020/1/7 18:40
# @Author  : Kalath
import datetime
from hashlib import md5

from flask_login import login_user, logout_user

from App.models import User, Sponsor, Category
from App.extensions import db
from flask import Blueprint, request, redirect, url_for, render_template, session

from App.tools import RegisterForm

user_info = Blueprint("user_info", __name__, url_prefix="/user")


@user_info.route("/login/", methods=["GET", "POST"])
def user_login():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # password = md5(password.encode("utf8")).hexdigest()
        # query user in database
        user = User.query.filter(User.username == username).first()
        # user must exist and complete password verification
        if user and user.check_password(password):
            # write user info into session
            login_user(user)
            return redirect(url_for("bbs.login_notice"))
        # jump to index page
        else:
            return redirect(url_for("bbs.fail_notice"))
        # return "login page!!!"
    else:
        # show login page
        return redirect(url_for("bbs.bbs_login"))


@user_info.route("/logout/")
def user_logout():
    # log out
    logout_user()
    return redirect(url_for("bbs.bbs_index"))


@user_info.route("/register/", methods=["GET", "POST"])
def user_register():
    formm = RegisterForm()

    # query first level data
    first_layer_category = Category.query.filter(Category.parentid == 0).all()
    # query other levels data
    other_layer_category = Category.query.filter(Category.parentid != 0).all()
    #  sponsor object
    sponsor = Sponsor.query.first()
    # current date
    current_year = datetime.datetime.now().year
    time_now = datetime.datetime.now().strftime("%m-%d %H:%M")

    if request.method == "GET":
        # v_code = VerifyCode().generate()
        return render_template("foreground/reg.html", **locals())
    else:
        # check whether the form information filled by the user meets all of the restrictions
        if formm.validate_on_submit():
            # data = request.form
            # uname = data.get("username")
            # upsw = data.get("password")
            # upsw_r = data.get("repassword")
            # umail = data.get("mail")
            # v_code = request.form.get("yzm")
            # only if all restrictions are met , get user information
            uname = formm.username.data
            upsw = formm.password.data
            upsw_r = formm.confirm.data
            umail = formm.email.data
            # v_code = formm.verificationcode.data
            # print(v_code, session['code'])
            # Determine whether the verification code is correct
            # if session['code'] != v_code:
            #     war = "Wrong verification code"
            #     return render_template("foreground/reg.html", **locals())
            if (not User.query.filter(User.username == uname).first()) and upsw == upsw_r:
                # save user information and insert data into the database
                user = User()
                user.username = uname
                user.password = upsw
                user.email = umail
                user.portrait = "foreground/images/avatar_blank.gif"
                db.session.add(user)
                db.session.commit()
                return redirect(url_for("bbs.bbs_index"))
            else:
                return render_template("foreground/reg.html", **locals())
        else:
            return render_template("foreground/reg.html", **locals())

