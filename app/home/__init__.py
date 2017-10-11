# _*_ coding: utf-8 _*_
__author__ = 'Yujia Lian'
__date__ = '7/28/17 4:17 PM'
from flask import Blueprint

home = Blueprint("home", __name__)

import app.home.views
