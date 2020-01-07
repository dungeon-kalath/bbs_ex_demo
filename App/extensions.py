# -*- coding: utf-8 -*-
# @File    : extensions.py
# 描述     ： application extensions, including Class instances, database objects, mail objects, bootstrap
# @Time    : 2020/1/7 17:48
# @Author  : Kalath
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()


# initialization
def app_init(app):
    db.init_app(app)
    migrate.init_app(app)
