#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/6/18 11:02 AM
# @Author  : Reid
# @Site    : 
# @File    : logio.py
# @Software: PyCharm
# @license : Copyright(C), ChangYang Technology Co. Ltd.
from flask import request, render_template, jsonify
from flask_login import login_user, logout_user, current_user
from app.schedulers.logio import logio_blueprint as logio
from app.models.user import User
from app import db


@logio.route('/')
def index():
    print 'return the index page'
    return render_template('login.html')


@logio.route('/login', methods=['POST'])
def login():
    print 'this is login page'
    data = request.form
    username = data.get('username')
    password = data.get('password')
    print username, password
    if not User.query.filter_by(username=username, password=password).first():
        return jsonify(status=0, msg='账号或密码错误')
    return jsonify(status=1, msg='登陆成功，网页即将跳转')



@logio.route('/signup', methods=['POST'])
def signup():
    data = request.form
    username = data.get('username')
    password = data.get('password')
    print username, password
    if User.query.filter_by(username=username).first():
        return jsonify(status=0, msg='用户已存在')
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify(status=1, msg='新用户注册成功，请重新登录')



