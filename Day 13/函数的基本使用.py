"""
1、什么是函数
    函数相当于具备某一功能的工具
    函数的使用必须遵循一个原则
        先定义
        后调用
2、为何要用函数
    1、组织结构不清晰，可读性差
    2、代码冗余
    3、可维护性、扩展性差

3、如何用函数
    先定义
        三种定义方式
    都调用
        三种调用方式
    返回值
        三种返回值的形式
"""
# 1、先定义
# 定义语法
'''
def 函数名(参数1,参数2,...):
    """文件描述"""
    函数体
    return 值
'''


# 形式一：无参函数
def func():
    print("I'm you father")


# 定义函数发生的事情
# 1、申请内存空间将函数体代码
# 2、将上述内存地址绑定函数名
# 3、定义函数不会只想函数体代码，但是会检测函数体语法

# 调用函数发生的事情
# 1、通过函数名找到函数内存地址
# 2、然后加括号就是在触发函数体代码执行
print(func)

# 举个栗子
"""
def bar():  # bar=函数的内存地址
    print('form bar')

def foo():
    print(bar)
    print('form foo')

foo()
"""


# 栗子2：
def foo():
    print(bar)
    bar()
    print('form foo')


def bar():  # bar=函数的内存地址
    print('form bar')


foo()


# 形式二：有参函数
def func(x, y):
    print(x, y)


func('theological', 'murder')


# 形式三：空函数，函数体代码为pass
def innovation(x, u):
    pass


# 三种定义方式各用在何处
# 1、无参函数的应用场景
def interactive():
    name = input('username>>:')
    psw = input('password>>:')
    msg = 'name：{}密码：{}'.format('name', psw)
    print(msg)


# 2、有参函数的应用场景
def approach(x, y):  # 参数相当于工厂的原材料
    res = x + y
    print(res)
    return res  # 返回值相当于产品


res = approach(20, 30)
print(res)


# 3、空函数的应用场景
def soulful():  # 构思代码使用
    pass


# 调用函数
# 1、语句的形式：只加括号调用函数
# interactive()
# add(1,2)

# 2、表达式形式：
"""
def add (x,y):
    res = x + y
    return res
# 赋值表达式
res = add(1,2)
print(res)
# 数学表达式   
add(1,2)*10
"""

# 3、函数调用可以当做参数
'''
res = add(add(1,2),3)
print(res)
'''

# 三、函数的返回值
# 1、 return是函数结束的标志，即函数体代码一旦运行到return会立刻终止函数的运行
# 并且会将return后的值当做本次运行的结果返回
# 2、返回一个值： return 值
# 返回None，函数体内没有return后的值当做本次运行的结果返回
#               return
#               return None

# 3、返回多个值：用逗号分隔开多个值，会被return返回成元组
'''
def func():
    return 10,'aaa',[1,2]
    
res = func()
print(res,type(res))
'''
