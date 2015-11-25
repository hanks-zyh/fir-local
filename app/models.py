#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from flask import Flask, url_for
import os, time, stat
from datetime import datetime
from apkparse.apk import APK
import qrcode

app = Flask(__name__)

class FileUtil(object):
    """
    util class for file operator
    """
    @staticmethod
    def get_upload_path():
        return os.path.join(app.root_path,'upload')

    @staticmethod
    def get_qrcode_path():
        return os.path.join(app.root_path,'static')

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

    @staticmethod
    def md5(str):
        if isinstance(str, basestring):
            import hashlib
            m = hashlib.md5()
            m.update(str)
            return m.hexdigest()
        else:
            return ''

class FileInfo(object):
    """
    include file name, path, size, ctime, verison_name, version_code, package_name, description
    """
    def __init__(self, path):
        self.path = path
        self.name = os.path.split(path)[1].decode('utf-8')
        file_stat = os.stat(path)
        self.size = '%.2f MB' % (float(file_stat.st_size)/1024/1024)
        self.ctime = datetime.fromtimestamp(file_stat.st_ctime).strftime('%Y-%m-%d %H:%M:%S')
        apk = APK(path)
        self.version_name = apk.get_androidversion_name()
        self.version_code = apk.get_androidversion_code()
        self.package_name = apk.package
        self.min_sdk_version = apk.get_min_sdk_version()
        self.description = ''

    def qrcode(self, url):
        qrcode_path = FileUtil.get_qrcode_path()
        img_name = FileUtil.md5(url) + ".png"
        img_path = os.path.join(qrcode_path, img_name)
        if not os.path.isfile(img_path):
            img = qrcode.make(url)
            img.save(img_path)
        return url_for('static', filename=img_name)

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
