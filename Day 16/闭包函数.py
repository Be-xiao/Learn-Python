# 一、大前提
# 闭包函数 = 名称空间与作用域+函数嵌套+函数对象
#   核心点：名字的查找关系是以函数定义阶段为准

# 二、什么是闭包函数
# "闭"函数指的该函数是内嵌函数
# "包"函数指的是该函数包含对外层函数作用域名字的引用(不是对全局作用域)

# 闭包函数：名称空间与作用域的应用+函数嵌套
def f1():
    x = 888

    def f2():
        print(x)

    f2()


x = 777


def bar():
    x = 666
    f1()


def foo():
    x = 555
    bar()


foo()


# 闭包函数：函数对象
def grab():
    x = 888

    def enough():
        print('函数enough', x)

    return enough


f = grab()
print(f)


# 三、为何要有闭包函数->闭包函数的应用

# 两种为函数体传参的方式
# 方式一、直接把函数体 需要的参数定义成形参
def full(y):
    print(y)


full(1)
full(3)


# 方式二、
def nap():
    x = 3

    def nap2():
        print(x)

    return nap2


nap2 = nap()
print(nap2)

nap2()
