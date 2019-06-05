#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/5/18 6:27 PM
# @Author  : Reid
# @Site    : 
# @File    : __init__.py
# @Software: PyCharm
# @license : Copyright(C), ChangYang Technology Co. Ltd.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config, LOGIN_MANAGER_CONFIG


db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    print __name__, __file__
    app = Flask(__name__, static_folder='../frontend/static', template_folder='../frontend/templates')
    app.config.from_object(config[config_name])

    login_manager.init_app(app)
    login_manager.session_protection = LOGIN_MANAGER_CONFIG['LOGIN_MANAGER_SESSION_PROTECTION']
    login_manager.login_view = LOGIN_MANAGER_CONFIG['LOGIN_MANAGER_LOGIN_VIEW']
    login_manager.login_message = LOGIN_MANAGER_CONFIG['LOGIN_MANAGER_LOGIN_MESSAGE']
    login_manager.refresh_view = LOGIN_MANAGER_CONFIG['LOGIN_MANAGER_REFRESH_VIEW']
    login_manager.needs_refresh_message = LOGIN_MANAGER_CONFIG['LOGIN_MANAGER_REFRESH_MESSAGE']


    db.init_app(app)
    db.app = app    # solved    RuntimeError: No application found


    from app.schedulers.logio import logio_blueprint
    app.register_blueprint(logio_blueprint)

    from app.schedulers.filemgr import filemgr_blueprint
    app.register_blueprint(filemgr_blueprint, url_prefix='/filemgr')




    return app
