#/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

from app import create_app

app = Flask(__name__)
bootstrap = Bootstrap(app)
manage = Manager(create_app())

if __name__ == '__main__':
    manage.run()
