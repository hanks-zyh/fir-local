#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
from flask import send_from_directory
from flask import render_template
from models import FileInfo, FileUtil, TableItem

app = Flask(__name__)

@app.route('/')
def index():
    apklist = FileUtil.get_files()
    print apklist
    return render_template('index.html', apklist=apklist)

@app.route('/edit/tableitem/<int:id>')
def update_tableitem(id):
    pass

@app.route('/apk/<path:filename>')
def download(filename):
    return send_from_directory(FileUtil.get_upload_path() ,filename,as_attachment=True)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
