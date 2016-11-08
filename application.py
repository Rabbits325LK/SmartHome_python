#E:\python_workspace\WebPython_Demo1\application.py
#coding:utf-8

from url import url

import tornado.web
import os

"""
setting引用了一个字典对象，里面约定了模板和静态文件的路径，
即声明已经建立的文件夹"templates"和"statics"分别为模板目录和静态文件目录。
"""
settings = dict(
	template_path = os.path.join(os.path.dirname(__file__), "templates"),
	static_path = os.path.join(os.path.dirname(__file__), "statics")
	)

application = tornado.web.Application(handlers = url, **settings)