#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
from base64 import b64encode, b64decode
from flask import request, render_template, jsonify, send_from_directory
from flask_login import login_user, logout_user, current_user, login_required
from app.schedulers.filemgr import filemgr_blueprint as filemgr


@filemgr.route('/')
@login_required
def filemgr_():
    try:
        print current_user.username
    except Exception as e:
        print e
    return render_template('filemgr.html')

@filemgr.route('/getinfo')
@login_required
def getinfo():
    files = os.listdir(os.getcwd() + '/files')
    return jsonify(files=files)

@filemgr.route('/download')
@login_required
def download():
    print current_user.username
    file = request.args.get('file')
    return send_from_directory(os.getcwd(), 'files/'+file, as_attachment=True)


@filemgr.route('/upload', methods=['POST'])
@login_required
def upload():
    file = request.files['file']
    file.save(os.getcwd()+'/files/'+file.filename)
    return render_template('filemgr.html')

@filemgr.route('/imgupload', methods=['POST'])
@login_required
def image_upload():
    data = json.loads(request.get_data())
    imgStrB64 = data.get('imgStrB64')
    imgName = data.get('fileName')
    if not all([imgStrB64, imgName]):
        return jsonify(status=0)
    with open(os.getcwd()+'/files/'+imgName, 'wb') as f:
        f.write(b64decode(imgStrB64))
    return jsonify(status=1)
