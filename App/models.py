# -*- coding: utf-8 -*-
# @File    : models.py
# @Theme   ：
# @Time    : 2020/1/7 18:37
# @Author  :
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from App.extensions import db, login_manager


# class BbsUser(db.Model):
#     __tablename__= "bbs_user"
#     uid = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
#     # account number
#     username = db.Column(db.CHAR(16), nullable=False)
#     # password sha256 encryption
#     password = db.Column(db.CHAR(32), nullable=False)
#     # email address
#     email = db.Column(db.CHAR(30), nullable=False)
#     # type of the account
#     udertype = db.Column(db.SmallInteger, nullable=False)
#     # registration date
#     regtime = db.Column(db.Integer, nullable=False)
#     # last login time
#     lasttime = db.Column(db.Integer, nullable=False)
#     # registration ip address
#     regip = db.Column(db.Integer, nullable=False)
#     # user portrait
#     picture = db.Column(db.VARCHAR(255), nullable=False, default="static/img/portrait.jpg")
#     # points
#     grade = db.Column(db.Integer, nullable=True, default=0)
#     # Forgot Password Question
#     problem = db.Column(db.VARCHAR(200), nullable=True, default="NULL")
#     # answer of Forgot Password Question
#     result = db.Column(db.VARCHAR(200), nullable=True, default="NULL")
#     # real name
#     realname = db.Column(db.CHAR(50), nullable=True, default="NULL")
#     # gender
#     sex = db.Column(db.SmallInteger, nullable=True, default=2)
#     # birthday
#     birthday = db.Column(db.VARCHAR(20), nullable=True, default="NULL")
#     # location
#     place = db.Column(db.VARCHAR(50), nullable=True, default="NULL")
#     # qq number
#     qq = db.Column(db.CHAR(13), nullable=True, default="NULL")
#     # personal signature
#     autograph = db.Column(db.VARCHAR(500), nullable=True, default="NULL")
#     # login allowed or not
#     allowlogin = db.Column(db.SmallInteger, nullable=False, default=0)
#
#
# class BbsCloseip(db.Model):
#     id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
#     # ip address
#     ip = db.Column(db.Integer, nullable=False)
#     # record time
#     addtime = db.Column(db.Integer, nullable=False)
#     # IP restriction end time
#     overtime = db.Column(db.Integer, nullable=True, default="NULL")
#
#
# class BbsLink(db.Model):
#     lid = db.Column(db.SmallInteger, primary_key=True, nullable=False, autoincrement=True)
#     # order of display, desc
#     displayorder = db.Column(db.SmallInteger, nullable=False, default=0)
#     # name
#     name = db.Column(db.VARCHAR(30), nullable=False)
#     # link address
#     url = db.Column(db.VARCHAR(255), nullable=False)
#     # description
#     description = db.Column(db.TEXT(0), nullable=True, default="NULL")
#     # link address of the logo image
#     logo = db.Column(db.VARCHAR(255), nullable=True, default="NULL")
#     # time
#     addtime = db.Column(db.Integer, nullable=False)
#
#
# class BbsCategory(db.Model):
#     cid = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
#     # section name
#     classname = db.Column(db.VARCHAR(60), nullable=False)
#     # parent id
#     parentid = db.Column(db.Integer, nullable=False)
#     # relations
#     classpath = db.Column(db.CHAR(20), nullable=True, default="NULL")
#     # count of replies
#     relycount = db.Column(db.Integer, nullable=False, default=0)
#     # count of postings
#     motifcount = db.Column(db.Integer, nullable=False, default=0)
#     # section administrator
#     compere = db.Column(db.CHAR(10), nullable=True, default="NULL")
#     # icon of the section
#     classpic = db.Column(db.VARCHAR(255), nullable=False, default="static/img/portrait.jpg")
#     # description of the section
#     description = db.Column(db.TEXT(0), nullable=True, default="NULL")
#     # sorting
#     orderby = db.Column(db.SmallInteger, nullable=False, default=0)
#     # last posting
#     lastpost = db.Column(db.VARCHAR(255), nullable=True, default="NULL")
#     namestyle = db.Column(db.CHAR(10), nullable=True, default="NULL")
#     # audit state
#     ispass = db.Column(db.SmallInteger, nullable=False, default=1)
#
#
# class BbsDetails(db.Model):
#     id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
#     # posting id
#     tid = db.Column(db.Integer, nullable=False)
#     # posting author id
#     authorid = db.Column(db.INTEGER, nullable=False)
#     # title of the posting
#     title = db.Column(db.VARCHAR(600), nullable=False)
#     # content of the posting
#     content = db.Column(db.TEXT(0), nullable=False)
#     # post time
#     addtime = db.Column(db.INTEGER, nullable=False)
#     # post ip
#     addip = db.Column(db.INTEGER, nullable=False)
#     # section of the forum
#     classid = db.Column(db.INTEGER, nullable=False)
#     # count of replies
#     replycount = db.Column(db.INTEGER, nullable=False, default=0)
#     # count of views
#     hits = db.Column(db.INTEGER, nullable=False, default=0)
#     # sticky post or not
#     istop = db.Column(db.SmallInteger, nullable=False, default=0)
#     # recommended or not
#     elite = db.Column(db.SmallInteger, nullable=False, default=0)
#     # hot post or not
#     ishot = db.Column(db.SmallInteger, nullable=False, default=0)
#     # price of post
#     rate = db.Column(db.SmallInteger, nullable=False, default=0)
#     # attachment of post
#     attachment = db.Column(db.SmallInteger, nullable=True, default="NULL")
#     # deleted or not
#     isdel = db.Column(db.Integer, nullable=False, default=0)
#     # color of the title
#     style = db.Column(db.CHAR(10), nullable=True, default="NULL")
#     # block comment or not
#     isdisplay = db.Column(db.Integer, nullable=False, default=0)
#
#
# class BbsComments(db.Model):
#     cmtid = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
#     # posting id
#     ctid = db.Column(db.Integer, nullable=False)
#     # comment user id
#     cmtuid = db.Column(db.INTEGER, nullable=False)
#     # comment content
#     cmtcontent = db.Column(db.TEXT(0), nullable=False)
#     # comment time
#     cmttime = db.Column(db.INTEGER, nullable=False)
#     # comment ip address
#     cmtip = db.Column(db.INTEGER, nullable=False)
#
#
#
# class BbsOrder(db.Model):
#     oid = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
#     # user id
#     uid = db.Column(db.Integer, nullable=False)
#     # posting id
#     tid = db.Column(db.Integer, nullable=False)
#     # price
#     rate = db.Column(db.Integer, nullable=False)
#     # creation time
#     addtime = db.Column(db.Integer, nullable=False)
#     # paid or not, 0 means not paid, 1 means paid
#     ispay = db.Column(db.SmallInteger, nullable=False, default=0)


# class Category(db.Model):
#     cid = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     # section name
#     classname = db.Column(db.String(60), nullable=False)
#     # parent id
#     parentid = db.Column(db.Integer, default=0)
#     # count of replies
#     replycount = db.Column(db.Integer, nullable=False, default=0)
#     # count of postings
#     postcount = db.Column(db.Integer, nullable=False, default=0)
#     # section administrator
#     compere = db.Column(db.VARCHAR(20), nullable=True, default="NULL")
#     # icon of the section
#     classpic = db.Column(db.VARCHAR(255), nullable=False)
#     # description of the section
#     description = db.Column(db.VARCHAR(200), nullable=True, default="NULL")
#     # sorting
#     orderby = db.Column(db.SmallInteger, nullable=False, default=0)
#     # last posting
#     lastpost = db.Column(db.VARCHAR(255), nullable=True, default="NULL")
#     style = db.Column(db.CHAR(10), nullable=True, default="NULL")
#     # audit state
#     ispass = db.Column(db.SmallInteger, nullable=False, default=1)
#
#     __tablename__ = "bbs_category"
#
#     def __str__(self):
#         return f"{self.classname}"
#
#
# class User(db.Model):
#     __tablename__= "bbs_user"
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True, name="uid")
#     # account number
#     username = db.Column(db.CHAR(16), nullable=False)
#     # password sha256 encryption
#     password = db.Column(db.CHAR(32), nullable=False)
#     # email address
#     email = db.Column(db.CHAR(30), nullable=False)
#     # type of the account
#     udertype = db.Column(db.SmallInteger, nullable=False)
#     # registration date
#     regtime = db.Column(db.Integer, nullable=False)
#     # last login time
#     lasttime = db.Column(db.Integer, nullable=False)
#     # registration ip address
#     regip = db.Column(db.Integer, nullable=False)
#     # user portrait
#     picture = db.Column(db.VARCHAR(255), nullable=False, default="static/img/portrait.jpg")
#     # points
#     grade = db.Column(db.Integer, nullable=True, default=0)
#     # Forgot Password Question
#     problem = db.Column(db.VARCHAR(200), nullable=True, default="NULL")
#     # answer of Forgot Password Question
#     result = db.Column(db.VARCHAR(200), nullable=True, default="NULL")
#     # real name
#     realname = db.Column(db.CHAR(50), nullable=True, default="NULL")
#     # gender
#     sex = db.Column(db.SmallInteger, nullable=True, default=2)
#     # birthday
#     birthday = db.Column(db.VARCHAR(20), nullable=True, default="NULL")
#     # location
#     place = db.Column(db.VARCHAR(50), nullable=True, default="NULL")
#     # qq number
#     qq = db.Column(db.CHAR(13), nullable=True, default="NULL")
#     # personal signature
#     autograph = db.Column(db.VARCHAR(500), nullable=True, default="NULL")
#     # login allowed or not
#     allowlogin = db.Column(db.SmallInteger, nullable=False, default=0)
#
#
# class Link(db.Model):
#     id = db.Column(db.SmallInteger, primary_key=True, autoincrement=True, name="lid")
#     # order of display, desc
#     displayorder = db.Column(db.SmallInteger, nullable=False, default=0)
#     # name
#     name = db.Column(db.VARCHAR(30), nullable=False)
#     # link address
#     url = db.Column(db.VARCHAR(255), nullable=False)
#     # description
#     description = db.Column(db.TEXT(0), nullable=True)
#     # link address of the logo image
#     logo = db.Column(db.VARCHAR(255), nullable=True)
#     # time
#     addtime = db.Column(db.Integer, nullable=False)
#     __tablename__ = "bbs_link"
#
#
# class Sponsor(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True, name="sid")
#     # sponsor name
#     sname = db.Column(db.VARCHAR(30), nullable=False)
#     # inc name
#     inc = db.Column(db.VARCHAR(50), nullable=False)
#     # icp name
#     icp = db.Column(db.VARCHAR(50), nullable=True)
#     # btm name
#     btm = db.Column(db.VARCHAR(50), nullable=False)
#     __tablename__ = "bbs_sponsor"
#
#
# class Details(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     # posting id
#     tid = db.Column(db.Integer, nullable=False)
#     # posting author id
#     authorid = db.Column(db.INTEGER, nullable=False)
#     # title of the posting
#     title = db.Column(db.VARCHAR(600), nullable=False)
#     # content of the posting
#     content = db.Column(db.TEXT(0), nullable=False)
#     # post time
#     addtime = db.Column(db.INTEGER, nullable=False)
#     # post ip
#     addip = db.Column(db.INTEGER, nullable=False)
#     # section of the forum
#     classid = db.Column(db.INTEGER, nullable=False)
#     # count of replies
#     replycount = db.Column(db.INTEGER, nullable=False, default=0)
#     # count of views
#     hits = db.Column(db.INTEGER, nullable=False, default=0)
#     # sticky post or not
#     istop = db.Column(db.SmallInteger, nullable=False, default=0)
#     # recommended or not
#     elite = db.Column(db.SmallInteger, nullable=False, default=0)
#     # hot post or not
#     ishot = db.Column(db.SmallInteger, nullable=False, default=0)
#     # price of post
#     rate = db.Column(db.SmallInteger, nullable=False, default=0)
#     # attachment of post
#     attachment = db.Column(db.SmallInteger, nullable=True, default="NULL")
#     # deleted or not
#     isdel = db.Column(db.Integer, nullable=False, default=0)
#     # color of the title
#     style = db.Column(db.CHAR(10), nullable=True, default="NULL")
#     # block comment or not
#     isdisplay = db.Column(db.Integer, nullable=False, default=0)
#     __tablename__ = "bbs_details"


class Category(db.Model):
    __tablename__ = 'bbs_category'

    cid = db.Column(db.Integer, primary_key=True)
    classname = db.Column(db.String(60))
    parentid = db.Column(db.Integer, nullable=False)
    replycount = db.Column(db.SmallInteger)
    postcount = db.Column(db.SmallInteger, name="forumcount")
    compere = db.Column(db.String(20))
    classpic = db.Column(db.String(200))
    descrition = db.Column(db.String(200))
    orderby = db.Column(db.SmallInteger)
    lastpost = db.Column(db.String(3000))
    ispass = db.Column(db.Integer)


class Closeip(db.Model):
    __tablename__ = 'bbs_closeip'

    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.Integer, nullable=False)
    addtime = db.Column(db.Integer, nullable=False)
    overtime = db.Column(db.Integer)


class Link(db.Model):
    __tablename__ = 'bbs_link'

    id = db.Column(db.SmallInteger, primary_key=True, name="lid")
    displayorder = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String)
    logo = db.Column(db.String(255))
    addtime = db.Column(db.Integer, nullable=False)


class Order(db.Model):
    __tablename__ = 'bbs_order'

    oid = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, nullable=False)
    tid = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Integer, nullable=False)
    addtime = db.Column(db.Integer, nullable=False)
    ispay = db.Column(db.Integer, nullable=False)


class Post(db.Model):
    __tablename__ = 'bbs_post'

    id = db.Column(db.Integer, primary_key=True)
    tid = db.Column(db.Integer)
    authorid = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(600), nullable=False)
    content = db.Column(db.String, nullable=False)
    addtime = db.Column(db.Integer, nullable=False)
    addip = db.Column(db.Integer, nullable=False)
    classid = db.Column(db.Integer, nullable=False)
    replycount = db.Column(db.Integer, nullable=False)
    hits = db.Column(db.Integer, nullable=False)
    istop = db.Column(db.Integer, nullable=False)
    elite = db.Column(db.Integer, nullable=False)
    ishot = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.SmallInteger, nullable=False)
    attachment = db.Column(db.SmallInteger)
    isdel = db.Column(db.Integer, nullable=False)
    style = db.Column(db.String(10))
    isdisplay = db.Column(db.Integer, nullable=False)


class Reply(db.Model):
    __tablename__ = 'bbs_reply'

    id = db.Column(db.Integer, primary_key=True)
    tid = db.Column(db.Integer)
    authorid = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String, nullable=False)
    addtime = db.Column(db.Integer, nullable=False)
    addip = db.Column(db.Integer, nullable=False)
    classid = db.Column(db.Integer, nullable=False)
    isdel = db.Column(db.Integer, nullable=False)
    isdisplay = db.Column(db.Integer, nullable=False)


class User(db.Model, UserMixin):
    __tablename__ = 'bbs_user'

    id = db.Column(db.Integer, primary_key=True, name="uid")
    username = db.Column(db.String(60), unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    usertype = db.Column(db.Integer)
    sex = db.Column(db.Integer)
    birthday = db.Column(db.Date)
    realname = db.Column(db.String(60))
    portrait = db.Column(db.String(200))
    regtime = db.Column(db.DateTime)
    qq = db.Column(db.String(15))
    signature = db.Column(db.String(300))
    answer = db.Column(db.String(300))
    isactive = db.Column(db.Integer)
    email = db.Column(db.String(300))
    lasttime = db.Column(db.DateTime)
    allowlogin = db.Column(db.Integer)
    grade = db.Column(db.Integer)

class Sponsor(db.Model):
    __tablename__ = 'bbs_sponsor'

    id = db.Column(db.Integer, primary_key=True, name="sid")
    sname = db.Column(db.String, nullable=False)
    inc = db.Column(db.String, nullable=False)
    icp = db.Column(db.String, nullable=False)
    btm = db.Column(db.String, nullable=False)


    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, value):
        # password signature
        self.password_hash = generate_password_hash(value)

    def check_password(self, password):
        # compare whether the original password is identified to signature or not
        return check_password_hash(self.password_hash, password)

# login callback
@login_manager.user_loader
def load_user(uid):
    return User.query.get(uid)
