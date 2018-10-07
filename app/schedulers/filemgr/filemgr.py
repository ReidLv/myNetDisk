#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request, render_template, jsonify, send_from_directory
from flask_login import login_user, logout_user, current_user, login_required
from app.schedulers.filemgr import filemgr_blueprint as filemgr
import os


@filemgr.route('/')
# @login_required
def filemgr_():
    return render_template('filemgr.html')

@filemgr.route('/getinfo')
# @login_required
def getinfo():
    files = os.listdir('/home/atguigu/flaskspace/myNetDisk/files')
    return jsonify(files=files)

@filemgr.route('/download')
# @login_required
def download():
    file = request.args.get('file')
    return send_from_directory(os.getcwd(), 'files/'+file, as_attachment=True)


@filemgr.route('/upload', methods=['POST'])
# @login_required
def upload():
    file = request.files['file']
    file.save(os.getcwd()+'/files/'+file.filename)
    return render_template('filemgr.html')