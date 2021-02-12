# -*- coding:utf-8 -*-
inp_username = input('Your name>>:').strip()
inp_password = input('Your password>>:').strip()
# 验证：
with open('user.txt', mode='rt', encoding='utf-8') as f:
    for line in f:
        username, password = line.strip().split(':')
        if inp_username == username and inp_password == password:
            print('Login in successful')
            break
    else:
        print('账号密码错误')
print('{x:*^10}'.format(x='程序执行结束'))
