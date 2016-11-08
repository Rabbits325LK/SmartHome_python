#E:\python_workspace\WebPython_Demo1\url.py
# coding=utf-8
"""
python3中已经没有设置默认字符集的函数了
设置方法 在文件的第1或 2行 使用注解的方式 # coding=utf-8 or # -*- coding : utf-8 -*-
the url structure of website
网站的网址结构
"""
#from imp import reload
#import sys #utf-8, 兼容汉字
#sys.setdefaultencoding("utf-8")  #设置默认字符集
#reload(sys)
from handlers.index import IndexHandler
from handlers.user import UserHandler
url = [
	(r'/', IndexHandler),
	(r'/user', UserHandler)
]