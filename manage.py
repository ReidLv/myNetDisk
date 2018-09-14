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


app = create_app('development')



@app.route('/')
def test():
    return render_template('login.html')






app.run()