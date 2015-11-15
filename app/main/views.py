#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'hanks'

from flask import Flask
from flask import send_from_directory
from flask import render_template
from ..models import FileInfo, FileUtil, TableItem
from . import main

@main.route('/')
def index():
    apklist = FileUtil.get_files()
    print apklist
    return render_template('index.html', apklist=apklist)

@main.route('/edit/tableitem/<int:id>')
def update_tableitem(id):
    pass

@main.route('/apk/<path:filename>')
def download(filename):
    return send_from_directory(FileUtil.get_upload_path() ,filename,as_attachment=True)

