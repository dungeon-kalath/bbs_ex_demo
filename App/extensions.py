# -*- coding: utf-8 -*-
# @File    : extensions.py
# @Theme   ： application extensions, including Class instances, database objects, mail objects, bootstrap
# @Time    : 2020/1/7 17:48
# @Author  : Kalath
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate(db=db)
login_manager = LoginManager()


# initialization
def app_init(app):
    db.init_app(app)
    migrate.init_app(app)
    login_manager.init_app(app)

    # set login position
    login_manager.login_view = "user_info.user_login"
