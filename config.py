#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/6/18 9:52 AM
# @Author  : Reid
# @Site    : 
# @File    : config.py
# @Software: PyCharm
# @license : Copyright(C), ChangYang Technology Co. Ltd.
import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SECRET_KEY = '- secret key -'
    SESSION_TYPE = 'filesystem'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_RECYCLE = 10  # make the pool to recycle connections after 10 seconds
    SEND_FILE_MAX_AGE_DEFAULT = 1  # js/css文件缓存时长为1s
    PERMANENT_SESSION_LIFETIME = 60 * 30  # Session lifetime Default


class DevelopmentConfig(Config):
    account = 'mysql'
    password = '12345678'
    ip = '127.0.0.1'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{account}:{password}@{ip}/netdisk'.format(account=account, password=password, ip=ip)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'databases/user.db')
    # SQLALCHEMY_BINDS = {}


config = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
}

LOGIN_MANAGER_CONFIG = {
    'LOGIN_MANAGER_SESSION_PROTECTION': 'strong',  # or 'basic' or None
    'LOGIN_MANAGER_LOGIN_VIEW': '/',  # Jump to the login page when Failed login_required
    'LOGIN_MANAGER_LOGIN_MESSAGE': 'Please login first!',
    'LOGIN_MANAGER_REFRESH_VIEW': '/',
    'LOGIN_MANAGER_REFRESH_MESSAGE': 'Refresh for login!',
}



