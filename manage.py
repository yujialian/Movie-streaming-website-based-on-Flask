# _*_ coding: utf-8 _*_
__author__ = 'Yujia Lian'
__date__ = '7/28/17 6:44 PM'

from app import app
from flask_script import Manager
manager = Manager(app)
if __name__ == "__main__":
    #manager.run()
    app.run()
