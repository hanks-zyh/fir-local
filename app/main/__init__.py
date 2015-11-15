#!/usr/bin/python
# -*-coding:utf-8 -*-

__author__ = 'hanks'

from flask import Blueprint

main = Blueprint('main',__name__)

from . import views, errors
