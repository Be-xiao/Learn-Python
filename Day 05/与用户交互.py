# 接收用户的输入
# 在Python3中，input会将用户所有的内容都存成字符串类型
username = input("请输入您的账号：")  # "egon"
print(username, type(username))
age = input("请输入您的年龄:")  # "age=18"
print(age, type(age))
age = int(age)  # int只能将纯数字的字符串转换成整型
print(age > 16)

# 在Python2中，
# raw_input()：用法与Python3中的input相同
# input():要求用户输入一个明确的数据类型，输入的是什么类型，就存成什么类型。
'''
>>> age=input("age:")
age:18
>>> age,type(age)
(18, <type 'int'>)

>>> birthday=input("birthday")
birthday12.28
>>> birthday,type(birthday)
(12.28, <type 'float'>)
'''

# 2、格式化输出
# 2、1字符串的格式化输出
# 值按照位置与%s一一对应，少一行不行，多一个也不行
res = "my name is %s,I'm %s year ago" % ('Adam', "18")
print(res)
# 以字典的形式传值，打破位置的限制
res = "I'm %(name1)s,I'm %(age1)s year ago" % {"name1": 'adam', "age1": "19"}
print(res)
# %s可以接收任意类型
print('This is %s' % "steak")
print('This is %s' % 19)
print('This is %(x)s' % {'x': "soup of the day"})
print('This is %s' % ['phrasal', 'brown'])
print('This is %d' % 19)  # %d只能接收int

# 2、2str.format:兼容性好
# 按照位置传值
res = 'would you like some {},No,I like to have {}'.format('organ', 'apple')
# 按照数列传值
print(res)
res = 'would you like some {0} or {1},No,I like to have {1}'.format('organ', 'apple')
print(res)
# 按照key=value传值
res = "I’m go on a {site},You want a {something} of something?".format(site='convenience store', something="drink")
print(res)
# format()新增：
print('{x}******'.format(x='开始执行'))  # 开始执行*****
print('{x:=<10}'.format(x='开始执行'))  # 开始执行======
print('{x:=^10}'.format(x='开始执行'))  # ====开始执行=====

print('{salary:.3f}'.format(salary = 123313.21254))
# 2、3 f   python3.5以后才支持
x = input("where you want to go:")
y = input("what do you want to there:")
res = f"I'd like go to {x} to {y}"
# f的新用法：{}内的字符串可以被当做表达式运行
print(res)
res = f'{10 + 3}'
print(res)
f'{print("10+3")}'
print(res)
