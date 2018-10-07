#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader  #required when the user try to login
def load_user(id):
    return User.query.get(int(id))


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    # __bind_key__ = 'user'
    userId = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    # lasttime = db.Column(db.DateTime, default=datetime.now, nullable=False)
    # is_login = db.Column(db.Boolean, default=False, nullable=False)
    # user_authority = db.Column(db.Integer, db.ForeignKey('roles.authority'), nullable=False)

    @property    #work in with load_user
    def id(self):
        return self.userId

    def __repr__(self):
        return self.username