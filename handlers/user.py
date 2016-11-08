# E://python_workspace//WebPython_Demo1//handlers//user.py
# coding = utf-8

import tornado.web
import methods.readdb as mrd

class UserHandler(tornado.web.RequestHandler):
	def get(self):
		username = self.get_argument("user")
		print("userName:{}".format(username))
		user_infos = mrd.select_table(table="user",column="*",condition="username",value=username)
		print(user_infos)
		self.render("user.html", users = user_infos)