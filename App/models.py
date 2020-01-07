# -*- coding: utf-8 -*-
# @File    : models.py
# 描述     ：
# @Time    : 2020/1/7 18:37
# @Author  :
from App.extensions import db


class BbsUser(db.Model):
    __tablename__= "bbs_user"
    uid = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    # account number
    username = db.Column(db.CHAR(16), nullable=False)
    # password sha256 encryption
    password = db.Column(db.CHAR(32), nullable=False)
    # email address
    email = db.Column(db.CHAR(30), nullable=False)
    # type of the account
    udertype = db.Column(db.SmallInteger, nullable=False)
    # registration date
    regtime = db.Column(db.Integer, nullable=False)
    # last login time
    lasttime = db.Column(db.Integer, nullable=False)
    # registration ip address
    regip = db.Column(db.Integer, nullable=False)
    # user portrait
    picture = db.Column(db.VARCHAR(255), nullable=False, default="static/img/portrait.jpg")
    # points
    grade = db.Column(db.Integer, nullable=True, default=0)
    # Forgot Password Question
    problem = db.Column(db.VARCHAR(200), nullable=True, default="NULL")
    # answer of Forgot Password Question
    result = db.Column(db.VARCHAR(200), nullable=True, default="NULL")
    # real name
    realname = db.Column(db.CHAR(50), nullable=True, default="NULL")
    # gender
    sex = db.Column(db.SmallInteger, nullable=True, default=2)
    # birthday
    birthday = db.Column(db.VARCHAR(20), nullable=True, default="NULL")
    # location
    place = db.Column(db.VARCHAR(50), nullable=True, default="NULL")
    # qq number
    qq = db.Column(db.CHAR(13), nullable=True, default="NULL")
    # personal signature
    autograph = db.Column(db.VARCHAR(500), nullable=True, default="NULL")
    # login allowed or not
    allowlogin = db.Column(db.SmallInteger, nullable=False, default=0)


class BbsCloseip(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    # ip address
    ip = db.Column(db.Integer, nullable=False)
    # record time
    addtime = db.Column(db.Integer, nullable=False)
    # IP restriction end time
    overtime = db.Column(db.Integer, nullable=True, default="NULL")


class BbsLink():
    lid = db.Column(db.SmallInteger, primary_key=True, nullable=False, autoincrement=True)
    # order of display, desc
    displayorder = db.Column(db.SmallInteger, nullable=False, default=0)
    # name
    name = db.Column(db.VARCHAR(30), nullable=False)
    # link address
    url = db.Column(db.VARCHAR(255), nullable=False)
    # description
    description = db.Column(db.TEXT(0), nullable=True, default="NULL")
    # link address of the logo image
    logo = db.Column(db.VARCHAR(255), nullable=True, default="NULL")
    # time
    addtime = db.Column(db.Integer, nullable=False)


class BbsCategory(db.Model):
    cid = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    # section name
    classname = db.Column(db.VARCHAR(60), nullable=False)
    # parent id
    parentid = db.Column(db.Integer, nullable=False)
    # relations
    classpath = db.Column(db.CHAR(20), nullable=True, default="NULL")
    # count of replies
    relycount = db.Column(db.Integer, nullable=False, default=0)
    # count of postings
    motifcount = db.Column(db.Integer, nullable=False, default=0)
    # section administrator
    compere = db.Column(db.CHAR(10), nullable=True, default="NULL")
    # icon of the section
    classpic = db.Column(db.VARCHAR(255), nullable=False, default="static/img/portrait.jpg")
    # description of the section
    description = db.Column(db.TEXT(0), nullable=True, default="NULL")
    # sorting
    orderby = db.Column(db.SmallInteger, nullable=False, default=0)
    # last posting
    lastpost = db.Column(db.VARCHAR(255), nullable=True, default="NULL")
    namestyle = db.Column(db.CHAR(10), nullable=True, default="NULL")
    # audit state
    ispass = db.Column(db.SmallInteger, nullable=False, default=1)


class BbsDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    # posting id
    tid = db.Column(db.Integer, nullable=False)
    # posting author id
    authorid = db.Column(db.INTEGER, nullable=False)
    # title of the posting
    title = db.Column(db.VARCHAR(600), nullable=False)
    # content of the posting
    content = db.Column(db.TEXT(0), nullable=False)
    # post time
    addtime = db.Column(db.INTEGER, nullable=False)
    # post ip
    addip = db.Column(db.INTEGER, nullable=False)
    # section of the forum
    classid = db.Column(db.INTEGER, nullable=False)
    # count of replies
    replycount = db.Column(db.INTEGER, nullable=False, default=0)
    # count of views
    hits = db.Column(db.INTEGER, nullable=False, default=0)
    # sticky post or not
    istop = db.Column(db.SmallInteger, nullable=False, default=0)
    # recommended or not
    elite = db.Column(db.SmallInteger, nullable=False, default=0)
    # hot post or not
    ishot = db.Column(db.SmallInteger, nullable=False, default=0)
    # price of post
    rate = db.Column(db.SmallInteger, nullable=False, default=0)
    # attachment of post
    attachment = db.Column(db.SmallInteger, nullable=True, default="NULL")
    # deleted or not
    isdel = db.Column(db.Integer, nullable=False, default=0)
    # color of the title
    style = db.Column(db.CHAR(10), nullable=True, default="NULL")
    # block comment or not
    isdisplay = db.Column(db.Integer, nullable=False, default=0)


class BbsComments(db.Model):
    cmtid = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    # posting id
    ctid = db.Column(db.Integer, nullable=False)
    # comment user id
    cmtuid = db.Column(db.INTEGER, nullable=False)
    # comment content
    cmtcontent = db.Column(db.TEXT(0), nullable=False)
    # comment time
    cmttime = db.Column(db.INTEGER, nullable=False)
    # comment ip address
    cmtip = db.Column(db.INTEGER, nullable=False)



class BbsOrder(db.Model):
    oid = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    # user id
    uid = db.Column(db.Integer, nullable=False)
    # posting id
    tid = db.Column(db.Integer, nullable=False)
    # price
    rate = db.Column(db.Integer, nullable=False)
    # creation time
    addtime = db.Column(db.Integer, nullable=False)
    # paid or not, 0 means not paid, 1 means paid
    ispay = db.Column(db.SmallInteger, nullable=False, default=0)


    # def __init__(self, uid, tid, rate, addtime):
    #     self.uid = uid
    #     self.tid = tid
    #     self.rate = rate
    #     self.addtime = addtime
