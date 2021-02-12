# -*- coding:utf-8 -*-

# 固定模板
"""
def out(func):
    def wrapper(*args, **kwargs):
        # 1、调用原函数
        # 2、为其增加新功能
        res = func(*args, **kwargs)
        return res

    return wrapper
"""


def author(func):
    def wrapper(*args, **kwargs):
        name = input('请输入您的用户名:>>>').strip()
        pwd = input('请输入密码:>>>').strip()
        if name == 'egon' and pwd == '123':
            res = func(*args, **kwargs)
            return res
        else:
            print('账号密码错误')

    return wrapper


@author
def index():
    print('from index')


index()
