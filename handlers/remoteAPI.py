#E:\python_workspace\WebPython_Demo1\handlers\index.py
# coding=utf-8

import tornado.web
import methods.weather as weather


class WeatherFutureRemoteAPIHandler(tornado.web.RequestHandler):

    def post(self):
        self.set_header("Content-Type", "application/json")
        result = weather.weather_future()
        self.write(result)
