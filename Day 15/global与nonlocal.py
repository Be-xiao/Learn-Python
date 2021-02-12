# -*- coding:utf-8 -*-
# 示例1:
y = 'hello world'


def func():
    y = 'Hello world,Nice to meet you'


func()
print(y)

# 示例2:如果在局部想要修改全局的名字对应的值(不可变类型)，需要使用global
x = 'hello world'


def func():
    global x  # 申明X这个名字是全局的名字，不用再造新值
    x = 'Hello world,Nice to meet you'


func()
print(x)

# 示例3:
l = ['guide', 999, 'choice']


def bridge():
    l.append('gate')


# nonlocal(了解):修改函数外层函数包含的名字对应的值（不可变类型）
"""
z = 'golden'


def f1():
    z = 777

    def f2():
        global z
        z = 'invasion'

    f2()
    print('f1内的z:', z)


f1()
"""
z = 'golden'


def f1():
    z = 777

    def f2():
        nonlocal z
        z = 'invasion'

    f2()
    print('f1内的z:', z)


f1()