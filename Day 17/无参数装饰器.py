# *args,**kwargs

"""
def index(x, y):
    print(x, y)


def wrapper(*args, **kwargs):  # args = (1,2,3,4) kwargs = {'a':1,'b':2}
    index(*args, **kwargs)  # index(*(1, 2, 3, 4),**{a=1, b=2})
    # index(1, 2, 3, 4, a=1, b=2)


wrapper(1, 2, 3, 4, a=1, b=2)
wrapper(1, 2)
"""


# 名称空间与作用域:名称空间的“嵌套”关系是在函数定义阶段，即检测语法的时候确定的


# 函数对象:
#   可以把函数当做参数传入
#   可以把函数当做返回值返回
def disinvest():
    return 666


def foo(func):
    return func


foo(disinvest)


# 函数的嵌套定义
def outer():
    def wrapper():
        pass

    return wrapper


# 闭包函数:传参的一种方式
def first():
    x = 777

    def wrapper():
        print(x)

    return wrapper  # wrapper内的wrapper函数的内存地址


wrapper = first()
wrapper()  # 变量名的

# 装饰器
'''
1、什么是装饰器
    器值的是工具，可以定义成函数
    装饰指的是为其他事物添加额外的东西点缀
    即，装饰器定义一个函数，该函数用来为其他函数增加额外的功能
2、为何要有装饰器
    开放封闭原则:
        开放:指的是对拓展功能是开放的
        封闭:指的是对修改源代码是封闭的
        
    装饰器就是在修改被装饰器对象源代码以及调用方式的前提下为被装饰对象添加新功能
3、如何用
    
'''

"""
需求:在不修改index函数源代码以及调用方式的前提下为其添加统计运行时间的功能
import time


def index(name):
    time.sleep(3)
    print('welcome %s to index page' % name)


index('egon')
"""
# 解决方案一：失败
# 问题:没有修改装饰对象的调用方式，但修改了其源代码
'''
import time


def index(name):
    start = time.time()
    time.sleep(3)
    print('welcome %s to index page' % name)
    stop = time.time()
    print(stop - start)


index('egon')
'''

# 解决方案二：
# 问题：没有修改装饰对象的调用方式，也没有修改了其源代码，但代码冗余
"""
import time


def index(name):
    time.sleep(3)
    print('welcome %s to index page' % name)


start = time.time()  
index('egon')
stop = time.time()
print(stop - start)
"""

# 解决方案三:
# 问题:解决了方案二的代码冗余问题，但函数的调用方式改变了
"""
import time


def index(name):
    time.sleep(3)
    print('welcome %s to index page' % name)

def index_wrapper():
    start = time.time()
    index('egon')
    stop = time.time()
    print(stop - start)


index_wrapper()
"""

# 方案三的优化:
"""
import time


def index(name):
    time.sleep(3)
    print('welcome %s to index page' % name)


print(index)


def out(func):
    # func = index的内存地址
    def index_wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        stop = time.time()
        print(stop - start)

    return index_wrapper


# index = wrapper函数的内存地址
index = out(index) # index = out(index的内存地址)  ps：此index非彼index
print(index)
index('Adam')
"""

# 方案三优化二:
'''
import time


def index(name):
    time.sleep(3)
    print('welcome %s to index page' % name)


def home(x, y):
    time.sleep(2)
    print('home to %s %s' % (x, y))
    return 123


def out(func):
    # func = index的内存地址
    def index_wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        stop = time.time()
        print(stop - start)
        return res

    return index_wrapper


home = out(home)
index = out(index)
res = home(9,8)
index('Adam')
print('返回值--->', res)
'''
# 语法糖:
import time


def timer(func):
    # func = index的内存地址
    def index_wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        stop = time.time()
        print(stop - start)
        return res

    return index_wrapper


@timer
def index(name):
    time.sleep(3)
    print('welcome %s to index page' % name)


@timer
def home(x, y):
    time.sleep(2)
    print('home to %s %s' % (x, y))
    return 123


index('egon')
home('9,', 7)

# 叠加多个装饰器，运行顺序
'''
@deco1  # index = deco1(deco2,wrapper的内存地址)
@deco2  # deco2.wrapper的内存地址=deco2(deco3,wrapper的内存地址)
@deco3  # deco3.wrapper的内存地址=deco3(index)
def index()
    pass
'''