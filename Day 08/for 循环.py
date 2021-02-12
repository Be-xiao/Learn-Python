'''
1、什么是for循环：
    循环就是重复的做某事，for循环是Python提供的第二种循环机制
2、为何要有for循环：
    理论上for循环能做的事情，while都可以做
    之所以要有for循环，是因为for循环在循环环境取值（遍历取值）比while循环更简洁
3、如何用for循环：
语法：
for 变量名 in 可迭代对象：  # 可迭代对象可以是：列表、字典、字符串、元组、集合
    代码1
    代码2
    代码3
    ...
'''
# 案例1： 循环取值
# 简单版
for xw in ['xw_dsb', 'dd_dsb', 'xw_nb']:
    print(xw)
# 复杂版
l = ['摩羯座', '水平座', '巨蟹座', '天蝎座', '白羊座', '天马座', ]
i = 0
while i < 3:
    print(l[i])
    i += 1

# 总结：for与while循环的异同
# 1、相同之外：都是循环 for循环干的事，while循环也可以干
# 2、不同之处：
#    while称之为条件循环，循环次数取决于条件何时变为假
#    for循环取值称之为'取值'，循环次数取决于in后包含的值的个数
for x in [1, 2, 3]:
    print('===*****===')

# for 循环控制循环次数：range
# 有局限性：
for c in 'a w':
    inp_name = input('please input your name:')
    inp_pwd = input('please input your password:')
# range功能介绍：
'''
>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(1,8)
[1, 2, 3, 4, 5, 6, 7]
>>> range(1,8,1)
[1, 2, 3, 4, 5, 6, 7]
>>> range(1,8,2)
[1, 3, 5, 7]
'''
# for+break：同while循环一样
# for+else:同while循环一样
username = '3080213790'
password = '123'
for x in range(3):
    inp_username = input('请输入您的账号：')
    inp_password = input('请输入您的密码：')

    if inp_username == username and inp_password == password:
        print('登录成功')
        break
else:
    print('输入错误次数过多')

# 四：range补充知识（了解）
# 1、for 搭配range，可以按照索引取值，但是麻烦，所以不推荐
l = ['aaa', 'bbb', 'ccc']  # len（l）
for i in l:
    print(i, l[i])
for y in l:
    print(l)
# 2、range()在Python3中会得到一只”会下蛋的母鸡“

# 五、for+continue
for i in range(6):  # 0 1 2 3 4 5
    if i == 4:
        continue
    print(i)
# 六、for循环嵌套
for i in range(3):
    print('外层循环-->,i')
    for j in range(5):
        print('内层===》,j')
# 补充：终止for循环只有break一种方案



