# 1、循环的语法与基本使用
'''
while 条件：
    代码1
    代码2
    代码3
'''
print('{x:*^10}'.format(x='开始执行'))
count = 0
while count <= 5:
    print(count)
    count += 1
print('{x:*^10}'.format(x='执行完毕'))
# 2、死循环与效率问题
'''
print('{x:*^10}'.format(x='开始执行死循环，CPU开始崩坏'))
count = 0
while count < 5:
    print(count)

while True:
    name = input('username：')
    print(name)
while 1:
    print(1 + 1)
    print(2 + 2)
纯运算无io的死循环会导致致命的效率问题

'''

# 3、循环的应用
# 3.1、重复代码：
# 3.2、输对了应该不用重复
print('{x:*^10}'.format(x='开始执行'))
consumer = ['lesson@gmail.com', 'www.@qq.com']
cada = ['lesson123', 'www123']
tag = 1
while tag:
    username = input('请输入您的账号：')
    username = str(username)
    username = username in consumer
    password = input('请输入您的密码：')
    password = str(password)
    password = password in cada
    if username == 1 and password == 1:
        print('登录成功')
        tag = 0
    else:
        print('账号名或密码错误')
    print('{x:*^10}'.format(x='执行完毕'))
# 4、退出循环的两种方式
# 方式一：将条件改为False，等到下次判断条件时才会生效
# 方式二：break,只要运行到break就会立刻终止本层
while 1:
    username = input('请输入您的账号：')
    username = str(username)
    username = username in consumer
    password = input('请输入您的密码：')
    password = str(password)
    password = password in cada
    if username == 1 and password == 1:
        print('登录成功')
        break  # 立刻终止本层循环
    else:
        print('账号名或密码错误')
    print('{x:*^10}'.format(x='执行完毕'))

# 5、while循环的嵌套
'''
# 每一层都必须配一个break
while True:
    while True:
        while True:
            break
        break
    break

'''
# break的方式
while 1:
    inp_name = input('请输入您的账号：')
    inp_paw = input('请输入您的密码：')

    if inp_name == '123' and inp_paw == 'qwe':
        print('登录成功')
        while 1:
            cmd = input('输入命令>:')
            if cmd == '退出':
                break
            print('命令{x}正在运行'.format(x=cmd))
        break
    else:
        print('账号密码错误')
# 改变条件的方式
q = 1
while q:
    inp_name = input('请输入您的账号：')
    inp_paw = input('请输入您的密码：')

    if inp_name == '123' and inp_paw == 'qwe':
        print('登录成功')
        while q:
            cmd = input('输入命令>:')
            if cmd == '退出':
                q = 0
            else:
                print('命令{x}正在运行'.format(x=cmd))
    else:
        print('账号密码错误')

# 8、while+continue：结束本次循环，直接进入下一次
# 强调：在continue之后添加同级代码毫无意义，因为永远无法执行
count = 0
while count < 6:
    if count == 4:
        count += 1
        continue
    print(count)
    count += 1
# 9、while+else
'''
while True:
    ...
else:
    print(else包含的代码会在while循环结束后，并且while循环是在没有被break打断的情况下才会运行)
'''
count = 1
while count < 6:
    print(count)
    count += 1
else:
    print('执行结束')

# 应用案例
count = 0
q = 1
while q:
    if count ==3:
        print('输错次数过多')
        break
    inp_name = input('请输入您的账号：')
    inp_paw = input('请输入您的密码：')

    if inp_name == '123' and inp_paw == 'qwe':
        print('登录成功')
        while q:
            cmd = input('输入命令>:')
            if cmd == '退出':
                q = 0
            else:
                print('命令{x}正在运行'.format(x=cmd))
    else:
        print('账号密码错误')
        count += 1

 # 版本2：
count = 0
while count < 3:

    inp_name = input('请输入您的账号：')
    inp_paw = input('请输入您的密码：')

    if inp_name == '123' and inp_paw == 'qwe':
        print('登录成功')
        while 1:
            cmd = input('输入命令>:')
            if cmd == '退出':
                break
            else:
                print('命令{x}正在运行'.format(x=cmd))
        break
    else:
        print('账号密码错误')
        count += 1
