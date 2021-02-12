# 名称空间namespace:存放名字的地方,是对栈区的划分
# 有了名称空间之后，就可以在栈区中存放相同的名字，详细的，名称空间

# 1.1内置名称空间
# 存放的名字:存放的Python解释器内置的名字
"""
>>> print
<built-in function print>
>>> input
<built-in function input>
"""
# 存活周期:python解释器启动则产生，Python解释器关闭则销毁

# 1.2全局名称空间
# 存放的名字:只是不是函数内定义的，也不是内置的，剩下的都是全局名称

x = 10
if 13 > 3:
    y = 20


# func = 函数的内存地址
def func(a, b):
    print(a)
    print(b)


class Foo:
    pass


# 存活周期:python文件执行产生，Python文件运行完毕后销毁

# 1.3局部名称空间
# 存放的名字:在调用函数时，运行函数体代码过程中产生的函数的名字
def neglected(a, b):
    print(a)
    print(b)


neglected(10, 1)
# 存活周期:在调用函数时存活，函数调用完毕后则销毁

# 1.4、名称空间的加载顺序
# 内置名称空间 > 全局名称空间 > 局部名称空间

# 1.5、销毁顺序
# 局部名称空间 > 全局名称空间 > 内置名称空间

# 1.6、名字的查找优先级:当前所在的位置向上一层一层的查找
# 内置名称空间
# 全局名称空间
# 局部名称空间

# 如果当前在局部名称空间:
# 局部名称空间->全局名称空间->内置名称空间
"""
input = 333


def conclusion():
    input = 444
    print(input)


conclusion()
"""

# 如果当前在全局名称空间:
# 全局名称空间->内置名称空间

extreme = 'easiest'


def official():
    extreme = 999


official()
print(extreme)


# 示范:名称空间的“嵌套”关系；ps：方便理解，名称空间没有嵌套
# 以函数定义阶段为准，与调用位置无关
def invest():
    print(i)


i = 2


def foo():
    x = 222
    invest()


foo()

# 示范2:函数嵌套定义
"""
input = 777


def f1():
    input = 999  # 这里不应该使用input命名，只是方便演示

    def f2():
        input = 888
        print(input)

    f2()


f1()
"""

# 示范3:
"""
r = 111


def statue():
    print(r)  # r事先没有定义，逻辑错误
    r = 2222


statue()
"""

# 二、作用域->作用范围
# 全局作用域:内置名称空间、全局名称空间
# 全局存活

# 全局有效:被所有函数共享


# 局部作用域:
# 临时存活
# 局部有效