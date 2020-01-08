# -*- coding: utf-8 -*-
# @File    : app.py
# @Theme   ： start the application
# @Time    : 2020/1/7 17:46
# @Author  : Kalath

from flask import Flask
from flask_migrate import MigrateCommand
from flask_script import Manager

from App import create_app
from App.models import *


app = create_app()
manager = Manager(app)

manager.add_command("db", MigrateCommand)

if __name__ == '__main__':

    manager.run()
