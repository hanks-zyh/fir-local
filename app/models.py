#!/usr/bin/env python
# -*- coding:utf-8 -*-

class FileInfo(object):
    """include file name, path, size, ctime"""
    def __init__(self, name, path, size, ctime):
        self.name = name
        self.path = path
        self.size = size
        self.ctime = ctime

class TableItem(object):
    """descripte a tableitem in table"""
    def __init(self,fileinfo,description):
        self.fileinfo = fileinfo
        self.description = description
        
