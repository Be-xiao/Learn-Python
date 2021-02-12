# -*- coding:utf-8 -*-
name = input('Your name>>:')
password = input('Your password>>:')
with open('user.txt', mode='at', encoding='utf-8') as f:
    f.write('{}:{}\n'.format(name, password))