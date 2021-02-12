print("hello world")
# 1、变量基本使用
# 原则：先定义，后引用
name = 'egon'  # 定义->存数据到内存
print(name)  # 引用->取

age = 19
print(age)

# 2、内存管理：垃圾回收机制
# 垃圾：当一个变量值绑定的变量名的个数为0时，该变量值无法被访问到
# 引用计数增加：Ctrl+D
X = 10
y = X
Z = X
# 引用计数减少
del X  # 解除变量名X与10的绑定关系，10的引用计数变为2
# print(y)
del y  # 10的引用计数变为1
# print(z)
# Z = 12345  # 10的引用计数变为0

# 3、变量有三大组成部分
# I:变量名-》是指向等号右侧值的内存地址的，用来访问等号右侧的值
# II：赋值符号-》将变量值的内存地址绑定给变量名
# III：变量值-》代表记录的事物的状态

# 4、变量名
# 原则：变量名的命名应该见名知意
# 变量名只能是字母、数字或下划线的任意组合
# 变量名的第一个字符不能是数字
# 关键字不能申明为变量名，常用关键字如下：
# [and、as、assert、break、class、continue、def、del、elif、else、except、exec、finally、for、from、alobal、if、import、in、is、lambda、not、or、pass、print、raise、return、try、while、with]
# ps:不要用拼音，不要用中文，在知名见意的情况下尽可能短

# 5、变量名的命名风格
# 5.1、纯小写加下划线的方式(在Python，关于变量名的命名推荐使用）
age_of_alex = 18
print(age_of_alex)
# 5.2、驼峰体
AgeOfAlex = 18
print(AgeOfAlex)

# 6、变量值三个重要特征
name = 'egon'
# id：反应的是变量值的内存地址，内存地址的不同ID则不同
print(id(name))
# type：不同类型的值用来表示记录不同的状态
print(type(name))
# value：值本身
print(name)

# 6.2、is与==
X = 'info:egon:19'
y = 'info:egon:19'
print(X, y)
print(id(X), id(y))
# is：比较左右两个值的身份id是否相等
# ==：比较左右两个值他们是否相等
'''
ID不同的情况下，值可能相同，即两块不同的内存空间里可以存相同的值
ID不同的情况下，值一定相同，x is y成立，x==y也必然成立
>>> X = 'info:egon:19'
>>> y = 'info:egon:19'
>>> print(X, y)
info:egon:19 info:egon:19
>>> print(id(X), id(y))
2895690054448 2895690054192
>>> X==y
True
>>> X is y
False
'''

# 了解：小整数池[-5,256]
# 从Python解释器启动那一刻开始，就会在内存中事先申请好一系列内存空间存放好常用的整数
"""
>>> m=10
>>> n=10
>>> id(m)
2895650187856
>>> id(n)
2895650187856
>>> m is n
True
"""

'''
>>> m=10
>>> res=4+6
>>> res
10
>>> id(res)
2895650187856
>>> id(m)
2895650187856
'''
# 在小整数区间内他的ID值相同
"""
>>> x=-5
>>> y=-5
>>> x is y
True
>>> x=-6
>>> y=-6
>>> x is y
False
"""
x = -6
y = -6
print(id(x))
print(id(y))
print(id(x), id(y))

# 7、常量：不变的量
# 注意：Python语法中没有常量的概念，但是在程序的开发过程中会涉及到常量的概念
AGE_OF_ALEX = 19  # 小写字母全为大写代表常量，这只是一种约定、规范
