# -*- coding: utf-8 -*-
# @File    : settings.py
# 描述     ： Application Configuration
# @Time    : 2020/1/7 17:49
# @Author  : Kalath


class BaseConfig:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "12k3jlakjscdasd10231lkj2jlasjd123098"


class DevelopConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/test"


class ProductConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/forum"


config = {
    "default": BaseConfig,
    "development": DevelopConfig,
    "production": ProductConfig
}


