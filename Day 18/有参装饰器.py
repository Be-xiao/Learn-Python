
# 由于语法糖的限制，out函数只有一个参数，并且该参数只用来接收被装饰对象的内存地址
"""
def out(func):
    # func = 函数的内存地址
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res

    return wrapper


@out  # index = out(index)  # index=>wrapper
def index(x, y):
    print(x, y)
"""

# 偷梁换柱之后
# index的参数什么样子，wrapper的参数就应该什么样子
# index的返回值什么样子，wrapper的返回值就应该什么样子
# index的属性什么样子，wrapper的属性就应该什么样子

# 非常Low的一种用法
'''
def login(func, db_type):
    def wrapper(*args, **kwargs):
        inp_username = input('Your name>>:').strip()
        inp_password = input('Your password>>:').strip()

        if db_type == 'file':  # 判断文件是否来源于文件
            with open('user.txt', mode='rt', encoding='utf-8') as f:
                for line in f:
                    username, password = line.strip().split(':')
                    if inp_username == username and inp_password == password:
                        print('Login in successful')
                        res = func(*args, **kwargs)
                        return res
                else:
                    print('账号密码错误')
        elif db_type == 'MySQL':
            print('基于MySQL的验证')
        elif db_type == 'ldap':
            print('基于ldap的验证')
        else:
            print('不支持dp_type')

    return wrapper


# @login  # 假设账号密码的来源是文件
def index(x, y):
    print("index->%s%s" % (x, y))


# @login  # 假设账号密码的来源是数据库
def home(name):
    print('home->%s' % name)


# @login  # 假设账号密码的来源是ldap
def transfer():
    print('登录成功')


index = login(index, 'file')
home = login(home, 'MySQL')
transfer = login(transfer, 'ldap')

index(1, 2)
home('egon')
transfer()
'''

# 山炮玩法
"""
def login(db_type):
    def deco(func):
        def wrapper(*args, **kwargs):
            inp_username = input('Your name>>:').strip()
            inp_password = input('Your password>>:').strip()

            if db_type == 'file':  # 判断文件是否来源于文件
                with open('user.txt', mode='rt', encoding='utf-8') as f:
                    for line in f:
                        username, password = line.strip().split(':')
                        if inp_username == username and inp_password == password:
                            print('Login in successful')
                            res = func(*args, **kwargs)
                            return res
                    else:
                        print('账号密码错误')
            elif db_type == 'MySQL':
                print('基于MySQL的验证')
            elif db_type == 'ldap':
                print('基于ldap的验证')
            else:
                print('不支持dp_type')

        return wrapper

    return deco


deco = login(db_type='file')


@login  # 假设账号密码的来源是文件
def index(x, y):
    print("index->%s%s" % (x, y))


deco = login(db_type='MySQL')


@login  # 假设账号密码的来源是数据库
def home(name):
    print('home->%s' % name)


deco = login(db_type='ldap')


@login  # 假设账号密码的来源是ldap
def transfer():
    print('登录成功')


index(1, 2)
home('egon')
transfer()
"""


# 语法糖


import imp


def login(db_type):
    def deco(func):
        def wrapper(*args, **kwargs):
            inp_username = input('Your name>>:').strip()
            inp_password = input('Your password>>:').strip()

            if db_type == 'file':  # 判断文件是否来源于文件
                with open('/home/noah/Documents/code/venv/python/Day 18/user.txt', mode='rt', encoding='utf-8') as f:
                    for line in f:
                        username, password = line.strip().split(':')
                        if inp_username == username and inp_password == password:
                            print('Login in successful')
                            res = func(*args, **kwargs)  # index(1,2)
                            return res
                    else:
                        print('账号密码错误')
            elif db_type == 'MySQL':
                print('基于MySQL的验证')
            elif db_type == 'ldap':
                print('基于ldap的验证')
            else:
                print('不支持dp_type')

        return wrapper

    return deco


@login(db_type='file')  # @deco  # index = deco(index)  # index = wrapper
def index(x, y):
    print("index->%s%s" % (x, y))


@login(db_type='MySQL')  # 假设账号密码的来源是数据库
def home(name):
    print('home->%s' % name)


@login(db_type='ldap')  # 假设账号密码的来源是ldap
def transfer():
    print('登录成功')


index(1, 2)
home('egon')
transfer()