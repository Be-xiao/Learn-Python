# 1、作用
# 2、定义
# 3、类型转换
# str可以把任意其他类型都转换成字符串
res = str({'a': 1})
print(res, type(res))
# 4、使用：内置方法


# 4.1、优先掌握
# 1、按照索引取值（正向取+反向取）：只能取
msg = 'hello world'
# 正向取
print(msg[0])
print(msg[5])
# 反向取
print(msg[-1])
# 只能取

# 2、切片:索引的拓展应用，从一个大字符串中拷贝一个子字符（顾头不顾尾，步长）
msg = 'would you like some shift'
res = msg[0:5]  # 顾头不顾尾
print(res)
print(msg)
# 步长
res = msg[0:5:2]  # 0 2 4
print(res)
# 反向步长  # 了解
res = msg[0:5:-2]
print(res)

q = 'hello world'
lsp = q[:]  # lsp = q[0:11]
print(lsp)
# 3、长对len
msg = 'hello world'
print(len(msg))

# 4、成员运算in和not in
# 判断一个字符串是否存在于一个大字符串中
print('alex' in 'alex is sb')
print('alex' not in 'alex is sb')

# 5、移除空白strip
msg = '     egon     '
res = msg.strip()  # 默认去掉的空格
print(msg)  # 不会改变原值
print(res)  # 是产生了新值

# 默认去掉的空格
msg = '*****egon******'
res = msg.strip('*')  # 默认去掉的空格
print(msg)  # 不会改变原值
print(res)  # 是产生了新值

msg = '**/-+(egon)/-+=***'
res = msg.strip('*/-+=()')
print(res)
# 应用
inp_user = input('your name>>:').strip()
inp_pwd = input('your password>>:').strip()
if inp_user == '123' and inp_pwd == '123':
    print('登录成功')
else:
    print('账号密码错误')

# 6、切分split：把一个字符串按照某种分隔符进行切分，得到一个列表
# 指定分隔符
info = 'egon:18:male'
res = info.split(':')
print(res)

# 指定分次数(了解)
info = 'egon:18:male'
ss = info.split(':', 1)
print(ss)
# 7、循环
info = 'egon:18:male'
for x in info:
    print(x)

# 需要掌握
# strip\lstrip\rstrip
mag = '*****egon*****'
print(mag.strip('*'))
print(mag.lstrip('*'))
print(mag.rstrip('*'))

# lower\upper
msg = 'AnbbCCeE'
print(mag.lower())  # 全部转换成小写
print(mag.upper())  # 全部转换成大写

# startswith,endswith
print('alex is sb'.startswith('alex'))
print('alex is sb'.endswith('sb'))

# format
# split, rsplit  # 将字符串切成列表
info = "adam: you: dad"
print(info.split(':', 1))  # ['adam', ' you: dad']
print(info.rsplit(':', 1))  # ['adam: you', ' dad']

# jion：把列表切成字符串
l = ['adam', 'you', ' dad']
res = ':'.join(l)  # res = l[0] + ':' + l[1] + ':' + l[2]
print(res)  # 按照某个分隔符，把元素全为字符的列表拼接成一个大的列表

# replace
pp = 'would you like some milk,no,but i want to some drink'
pp.replace('you', 'YOU', 1)

# isdigit
# 判断字符串是否由纯数字组成
age = input('请输入您的年龄').strip()
if age.isdigit():
    age = int(age)
    if age > 18:
        print('猜大了')
    elif age < 18:
        print('猜小了')
    else:
        print('猜对了')
else:
    print('必须输入数字，傻子')

# 了解
