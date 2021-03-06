#E:\python_workspace\WebPython_Demo1\handlers\index.py
# coding=utf-8

import tornado.web
import methods.readdb as mrd
import json

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		usernames = mrd.select_columns(table="user", column="username")
		one_user = usernames[0][0]
		self.render("index.html", user = one_user)

	def post(self):
		username = self.get_argument("username")
		password = self.get_argument("password")
		user_infos = mrd.select_table(table="user",column="*",condition="username",value=username)
		if user_infos:
			db_pwd = user_infos[0][2]
			if db_pwd == password:
				data = {'success':'true','data':username}
				self.write(json.dumps(data))
			else:
				data = {'success':'false','data':'您输入的密码不正确'}
				self.write(json.dumps(data))
		else:
			data = {'success':'false','data':'用户名不存在'}
			self.write(json.dumps(data))