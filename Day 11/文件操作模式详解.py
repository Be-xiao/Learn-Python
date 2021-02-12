# -*- coding:utf-8 -*-
# 以t模式为基础进行操作

# 1、r(默认的操作模式)：只读模式,当文件不存在时报错，当文件存在时文件指针跳到开始位置
with open('d.txt', encoding='utf-8') as f:
    res = f.read()  # 把所有内容从硬盘读入
    print('读入'.center(50, '-'))
    print(res)
# 案列
'''
inp_username = input('Your name>>:').strip()
inp_password = input('Your password>>:').strip()
# 验证：
with open('user.txt', mode='rt', encoding='utf-8') as f:
    for line in f:
        username, password = line.strip().split(':')
        if inp_username == username and inp_password == password:
            print('Login in successful')
            break
    else:
        print('账号密码错误')
'''

# 应用程序===》文件
# 应用程序===》数据管理软件===》文件
# 2、w：只写模式，当文件不存在时
with open('d.txt', mode='wt', encoding='utf-8') as f:
    # f.read()  # 不可读
    f.write('擦你个出资')

# 强调1：
# 在以w模式打开文件，没有关闭的情况下，连续的写，新写的内容总是跟在旧内容之后
# 强调1：
# 如果重新以w模式打开，则会清空文件内存

# 案列:w模式用来创建全新的文件
# 文件的copy工具
src_file = input('源文件路径:')
dst_file = input('源文件路径：')
with open(r'{}'.format(src_file), mode='rt', encoding='utf-8') as f1, \
        open(r'{}'.format(dst_file), mode='wt', encoding='utf-8') as f2:
    res = f1.read()
    f2.write(res)

# 3、a：只追加写，在文件不存时会创建空文档，当文件存在时文件指针会直接调到末尾
with open('e.txt', mode='at', encoding='utf -8') as f:
    f.write('日你仙人板板')
    f.write('日你大爷')
    f.write('艹尼玛')

# 注册功能:a模式用来在原有的文件内存的基础之上写入新的内容，比如记录日志、注册
name = input('Your name>>:')
password = input('Your password>>:')
with open('user.txt', mode='at', encoding='utf-8') as f:
    f.write('{}:{}\n'.format(name, password))

# 了解：+不能单独使用，必须配合r、w、a
