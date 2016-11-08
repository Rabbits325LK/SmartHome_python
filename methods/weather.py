# E:\python_workspace\WebPython_Demo1\methods\raddb.py
# -*- coding : utf-8 -*-

import json,urllib
from urllib.parse import urlencode

def weather_future():
    url = 'http://api.k780.com:88'
    params = {
        'app' : 'weather.future',
        'weaid' : '1',
        'appkey' : '12228',
        'sign' : 'f0e60420623628110a9aab511715644f',
        'format' : 'json'
    }
    params = urlencode(params)
    f = urllib.urlopen('%s?%s' % (url, params))
    nowapi_call = f.read()
    a_result = json.loads(nowapi_call)
    if a_result:
        if a_result['success'] != '0':
            return a_result['result']
        else:
            return a_result['msgid'] + ' ' + a_result['msg']
    else:
        return 'Request mowapi fail.'