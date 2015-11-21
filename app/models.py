#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from flask import Flask
import os, time, stat
from datetime import datetime

app = Flask(__name__)

class FileUtil(object):
    """
    util class for file operator
    """
    @staticmethod
    def get_upload_path():
        return os.path.join(app.root_path,'upload')

    @staticmethod
    def get_files():
        apklist = []
        dirpath = FileUtil.get_upload_path()
        filelist = os.listdir(dirpath)
        filelist.sort(FileInfo.compare)
        for f in filelist:
            if  os.path.splitext(f)[1] =='.apk':
                path = os.path.join(dirpath,f)
                fileinfo = FileInfo(path)
                apklist.append(fileinfo)
        return apklist


class FileInfo(object):
    """
    include file name, path, size, ctime, verisonname, versioncode, packagename, description
    """
    def __init__(self, path):
        self.path = path
        self.name = os.path.split(path)[1]
        file_stat = os.stat(path)
        self.size = '%.2f MB' % (float(file_stat.st_size)/1024/1024)
        self.ctime = datetime.fromtimestamp(file_stat.st_ctime).strftime('%Y-%m-%d %H:%M:%S')
        self.versionname = '1.0'
        self.versioncode = 1
        self.packagename = ''
        self.description = ''


    @staticmethod
    def compare(file1, file2):
        dirpath = FileUtil.get_upload_path()
        stat1 = os.stat(os.path.join(dirpath,file1))
        stat2 = os.stat(os.path.join(dirpath,file2))
        if stat1.st_ctime > stat2.st_ctime:
            return -1
        elif stat1.st_ctime < stat2.st_ctime:
            return 1
        else:
            return 0
