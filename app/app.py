#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
from flask import send_from_directory
from flask import render_template
import os, time, stat
from datetime import datetime

app = Flask(__name__)

dirpath = os.path.join(app.root_path,'upload')

class FileInfo(object):
    """include file name, path, size, ctime"""
    def __init__(self, name, path, size, ctime):
        self.name = name
        self.path = path
        self.size = size
        self.ctime = ctime

def compare(file1, file2):
    stat1 = os.stat(os.path.join(dirpath,file1))
    stat2 = os.stat(os.path.join(dirpath,file2))
    if stat1.st_ctime > stat2.st_ctime:
        return -1
    elif stat1.st_ctime < stat2.st_ctime:
        return 1
    else:
        return 0

def get_files():
    apklist = []
    filelist = os.listdir(dirpath)
    filelist.sort(compare)
    for f in filelist:
        if  os.path.splitext(f)[1] =='.apk':
            path = os.path.join(dirpath,f)
            file_stat = os.stat(path)
            size = '%.2f MB' % (float(file_stat.st_size)/1024/1024)
            ctime = datetime.fromtimestamp(file_stat.st_ctime).strftime('%Y-%m-%d %H:%M:%S')
            fileinfo = FileInfo(f, path, size, ctime)
            apklist.append(fileinfo)
    return apklist

@app.route('/')
def index():
    apklist = get_files()
    print apklist
    return render_template('index.html', apklist=apklist)

@app.route('/apk/<path:filename>')
def download(filename):
    return send_from_directory(dirpath,filename,as_attachment=True)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
