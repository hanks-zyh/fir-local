#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
from flask.ext.script import Manager

from app import create_app

app = Flask(__name__)
manage = Manager(create_app())

if __name__ == '__main__':
    manage.run()
