# -*- coding: utf-8 -*-
"""
@author: xiongyongfu
@contact: xyf_0704@sina.com
@file: chitchat.py
@Software: PyCharm
@time: 2019/2/25 19:30
@desc: 接入图灵闲聊机器人
"""
import requests
import json


def get_response(msg):
    key = ''   # 自己的图灵机器人key
    api = 'http://www.tuling123.com/openapi/api?key={}&info={}'.format(
        key, msg)

    return requests.get(api).json()


while True:
    info = input('\n我：')
    if info == 'quit':
        break
    # result = get_response(info)
    print(get_response(info)["code"])
    print('\nTuling: ' + get_response(info)["text"])