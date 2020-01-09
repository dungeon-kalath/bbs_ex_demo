# -*- coding: utf-8 -*-
# @File    : user.py
# @Theme   ： manage user information, maintenance, registration, logging actions of users
# @Time    : 2020/1/7 18:40
# @Author  : Kalath
from hashlib import md5

from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash

from App.models import User
from App.extensions import db
from flask import Blueprint, request, redirect, url_for, render_template

user_info = Blueprint("user_info", __name__, url_prefix="/user")


@user_info.route("/login/", methods=["GET", "POST"])
def user_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        password = md5(password.encode("utf8")).hexdigest()
        # query user in database
        user = User.query.filter(User.username == username, User.password_hash == password).first()
        if user:
            # write user info into session
            login_user(user)
        # jump to index page
        return redirect(url_for("bbs.bbs_index"))
        # return "login page!!!"
    else:
        # show login page
        return "login page"


@user_info.route("/logout/")
def user_logout():
    # log out
    logout_user()
    return redirect(url_for("bbs.bbs_index"))


@user_info.route("/register/", methods=["GET", "POST"])
def register_user():
    if request.method == "GET":
        return render_template("foreground/reg.html")
    else:
        data = request.form
        uname = data.get("username")
        upsw = data.get("password")
        umail = data.get("mail")

        user = User()
        user.username = uname
        user.password_hash = generate_password_hash(upsw)
        user.email = umail
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("bbs.bbs_index"))