# -*- coding: utf-8 -*-
# @File    : models.py
# 描述     ：
# @Time    : 2020/1/7 18:37
# @Author  :
from App.extensions import db


class BbsUser(db.Model):
    __tablename__= "bbs_user"
    uid = db.Column(db.Integer(11), primary_key=True, nullable=False, autoincrement=True)
    username = db.Column(db.CHAR(16), nullable=False)
    password = db.Column(db.CHAR(32), nullable=False)
    email = db.Column(db.CHAR(30), nullable=False)
    udertype = db.Column(db.SmallInteger(2), nullable=False)
    regtime = db.Column(db.Integer(12), nullable=False)
    lasttime = db.Column(db.Integer(12), nullable=False)
    regip = db.Column(db.Integer(12), nullable=False)
    picture = db.Column(db.VARCHAR(255), nullable=False, default="static/img/portrait.jpg")
    grade = db.Column(db.Integer(10), nullable=True, default=0)
    problem = db.Column(db.VARCHAR(200), nullable=True, default="NULL")
    result = db.Column(db.VARCHAR(200), nullable=True, default="NULL")
    realname = db.Column(db.CHAR(50), nullable=True, default="NULL")
    sex = db.Column(db.SmallInteger(4), nullable=True, default=2)
    birthday = db.Column(db.VARCHAR(20), nullable=True, default="NULL")
    place = db.Column(db.VARCHAR(50), nullable=True, default="NULL")
    qq = db.Column(db.CHAR(13), nullable=True, default="NULL")
    autograph = db.Column(db.VARCHAR(500), nullable=True, default="NULL")
    allowlogin = db.Column(db.SmallInteger(2), nullable=False, default=0)


class BbsCloseip(db.Model):
    id = db.Column(db.Integer(10), primary_key=True, nullable=False, autoincrement=True)
    ip = db.Column(db.Integer(10), nullable=False)
    addtime = db.Column(db.Integer(10), nullable=False)
    overtime = db.Column(db.Integer(10), nullable=True, default="NULL")


class BbsLink():
    lid = db.Column(db.SmallInteger(6), primary_key=True, nullable=False, autoincrement=True)
    displayorder = db.Column(db.SmallInteger(2), nullable=False, default=0)
    name = db.Column(db.VARCHAR(30), nullable=False)
    url = db.Column(db.VARCHAR(255), nullable=False)
    description = db.Column(db.TEXT(0), nullable=True, default="NULL")
    logo = db.Column(db.VARCHAR(255), nullable=True, default="NULL")
    addtime = db.Column(db.Integer(12), nullable=False)


class BbsCategory(db.Model):
    cid = db.Column(db.Integer(10), primary_key=True, nullable=False, autoincrement=True)
    classname = db.Column(db.VARCHAR(60), nullable=False)
    parentid = db.Column(db.Integer(10), nullable=False)
    classpath = db.Column(db.CHAR(20), nullable=True, default="NULL")
    relycount = db.Column(db.Integer(10), nullable=False, default=0)
    motifcount = db.Column(db.Integer(10), nullable=False, default=0)
    compare = db.Column(db.CHAR(10), nullable=True, default="NULL")
    classpic = db.Column(db.VARCHAR(255), nullable=False)
    description = db.Column(db.TEXT(0), nullable=True, default="NULL")
    orderby = db.Column(db.SmallInteger(6), nullable=False, default=0)
    lastpost = db.Column(db.VARCHAR(255), nullable=True, default="NULL")
    namestyle = db.Column(db.CHAR(10), nullable=True, default="NULL")
    ispass = db.Column(db.SmallInteger(2), nullable=False, default=1)


class BbsDetails(db.Model):
    id = db.Column(db.Integer(10), primary_key=True, nullable=False, autoincrement=True)
    # first = db.Column(db.SmallInteger(1), nullable=False, default=0)
    tid = db.Column(db.Integer(10), nullable=False)
    authorid = db.Column(db.INTEGER(10), nullable=False)
    title = db.Column(db.VARCHAR(600), nullable=False)
    content = db.Column(db.TEXT(0), nullable=False)
    addtime = db.Column(db.INTEGER(12), nullable=False)
    addip = db.Column(db.INTEGER(12), nullable=False)
    classid = db.Column(db.INTEGER(10), nullable=False)
    replycount = db.Column(db.INTEGER(12), nullable=False, default=0)
    hits = db.Column(db.INTEGER(12), nullable=False, default=0)
    istop = db.Column(db.SmallInteger(2), nullable=False, default=0)
    elite = db.Column(db.SmallInteger(2), nullable=False, default=0)
    ishot = db.Column(db.SmallInteger(2), nullable=False, default=0)
    rate = db.Column(db.SmallInteger(3), nullable=False, default=0)
    attachment = db.Column(db.SmallInteger(3), nullable=True, default="NULL")
    isdel = db.Column(db.Integer(2), nullable=False, default=0)
    style = db.Column(db.CHAR(10), nullable=True, default="NULL")
    isdisplay = db.Column(db.Integer(2), nullable=False, default=0)


class BbsComments(db.Model):
    coid = db.Column(db.Integer(10), primary_key=True, nullable=False, autoincrement=True)
    # first = db.Column(db.SmallInteger(1), nullable=False, default=0)
    ctid = db.Column(db.Integer(10), nullable=False)
    commentid = db.Column(db.INTEGER(10), nullable=False)
    ccontent = db.Column(db.TEXT(0), nullable=False)
    commenttime = db.Column(db.INTEGER(12), nullable=False)
    commentip = db.Column(db.INTEGER(12), nullable=False)



class BbsOrder(db.Model):
    lid = db.Column(db.Integer(10), primary_key=True, nullable=False, autoincrement=True)
    uid = db.Column(db.Integer(11), nullable=False)
    tid = db.Column(db.Integer(11), nullable=False)
    rate = db.Column(db.Integer(11), nullable=False)
    addtime = db.Column(db.Integer(11), nullable=False)
    ispay = db.Column(db.SmallInteger(2), nullable=False, default=0)
