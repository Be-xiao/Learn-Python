'''
语法一：
if条件：
    代码1
    代码2
'''
age = 18
is_beautiful = True
stat_sign = '摩羯座'
if age > 16 and age < 20 and is_beautiful and stat_sign == '摩羯座':
    print('I love you')

'''
语法二：
if条件：
    代码1
    代码2
else:
    代码1
    代码2
'''
age = input('请输入您的年龄：')
age = int(age)
is_beautiful = True
stat_sign = '摩羯座'
if age >= 16 and age <= 20 and is_beautiful and stat_sign == '摩羯座':
    print('I love you')
else:  # 条件不成立运行
    print('阿姨好，你是个好人')

'''
语法三：
if条件：
    代码1
    代码2
elif 条件2:
    代码1
    代码2
elif 条件3:
    代码1
    代码2
'''
score = input('请输入您的成绩：')
score = int(score)
if score >= 90:
    print('优秀')
elif score >= 75:
    print('良好')
elif score >= 60:
    print('合格')
elif score < 60:
    print('不合格，你个垃圾')

'''
语法三：
if条件：
    代码1
    代码2
elif 条件2:
    代码1
    代码2
elif 条件3:
    代码1
    代码2
else:
'''
score = input('请输入您的成绩：')
score = int(score)
if score >= 90:
    print('优秀')
elif score >= 75:
    print('良好')
elif score >= 60:
    print('合格')
else:
    print('不合格，你个垃圾')
