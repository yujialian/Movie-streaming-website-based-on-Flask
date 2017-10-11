# _*_ coding: utf-8 _*_
__author__ = 'Yujia Lian'
__date__ = '7/28/17 4:17 PM'

from flask import Blueprint

admin = Blueprint("admin", __name__)

import app.admin.views