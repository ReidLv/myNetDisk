#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/6/18 11:10 AM
# @Author  : Reid
# @Site    : 
# @File    : manage.py
# @Software: PyCharm
# @license : Copyright(C), ChangYang Technology Co. Ltd.
from app import create_app
from flask import render_template
from flask_script import Manager, Shell
from app import db


def make_shell_context():
   return dict(app=app, db=db)

app = create_app('development')
manager = Manager(app)

manager.add_command('shell', Shell(make_context=make_shell_context))









manager.run()