#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/6/18 11:02 AM
# @Author  : Reid
# @Site    : 
# @File    : logio.py
# @Software: PyCharm
# @license : Copyright(C), ChangYang Technology Co. Ltd.
from flask import request, render_template, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from app.schedulers.logio import logio_blueprint as logio
from app.models.user import User
from app import db


@logio.route('/')
def index():
    return render_template('login.html')


@logio.route('/login', methods=['POST'])
def login():
    data = request.form
    username = data.get('username')
    password = data.get('password')
    user = User.query.filter_by(username=username, password=password).first()
    if not user:
        return jsonify(status=0, msg='账号或密码错误')
    login_user(user)
    return jsonify(status=1, msg='登陆成功，网页即将跳转')

@logio.route('/logout', methods=['POST'])
@login_required
def logout():
    try:
        logout_user()
    except:
        return jsonify(stauts=0, msg='用户退出失败,请重新登录')
    return jsonify(stauts=1, msg='用户已退出,即将返回登录页')




@logio.route('/signup', methods=['POST'])
def signup():
    data = request.form
    username = data.get('username')
    password = data.get('password')
    if User.query.filter_by(username=username).first():
        return jsonify(status=0, msg='用户已存在')
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    login_user(user)
    return jsonify(status=1, msg='注册成功，网页即将跳转')



