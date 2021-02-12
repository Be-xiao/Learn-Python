# 2.5命名关键字参数(了解)
# 在定义函数时，*后定义的参数，如下所示，称之为命名关键字参数
# 特点：
# 1、命名关键字实参必学按照key = value的形式为其传值
# 2、
def func(x, y, *, a, b):  # 其中，a和b称之为命名关键字参数
    print(x, y)
    print(a, b)


func(1, 2, a=4, b=3)


# 示例：
def corner(x, y, *, a, b='world'):
    print(x, y)
    print(a, b)


corner(1, 2, a='hello')


# 2.6组合使用
# 形参混用的顺序:位置形参，默认形参，*args，命名关键字形参，**kwargs
def clarification(x, y=999, *args, z, **kwargs):
    print(x)
    print(y)
    print(*args)
    print(z)
    print(**kwargs)


# 实参混用顺序:
def church(x, y, z, a, b, c):
    print(x)
    print(y)
    print(z)
    print(a)
    print(b)
    print(c)


church(520, *[1314, 666], a=9, **{'b': 'standard', 'c': 777})

# 常用格式
"""
func(1)
func(x=1)
func(1, x=1)
func(*'Hello world')
func(**{})
func(*'Hello', **{})
"""
