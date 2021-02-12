# -*- coding:utf-8 -*-
# 读相关
# 1、readline：一次读一一行
with open(r'g.txt', mode='rt', encoding='utf-8') as f:
    res1 = f.readline()
    res2 = f.readline()
    print(res2)

    while 1:
        line = f.readline()
        if len(line) == 0:
            break
        print(line)

# 2、readlines:
with open(r'g.txt', mode='rt', encoding='utf-8') as f:
    res = f.readlines()
    print(res)

# 强调：
# f.read() or f.readlines() 都是将内容一次读入内存，如果内容过大，会导致内存溢出，诺还想将内容全部读入内存，则必须分多次读入，有两种方法实现

# 2、写相关的操作
# f.writelines():
with open('h.txt', mode='rt', encoding='utf - 8') as f:
    f.write('111\n222\n666\n')
    # l = [
    #      '111aa\n'.encode('utf-8'),
    #      'sssd'.encode('utf-8'),
    #      'as442w'.encode('utf-8'),
    #      ]
# 如果实纯英文字符，可以直接加前缀b得到bytes类型
    l = [
        b'111aa\n',
        b'sssd',
        b'as442w',
     ]
# 补充2： '上'.encode('utf-8')等同于bytes('上',encoding = 'utf-8')
    '''
    >>> '上'.encode('utf-8')
    b'\xe4\xb8\x8a'
    >>> bytes('上',encoding = 'utf-8')
    b'\xe4\xb8\x8a'
    '''
    f.writelines(l)

# 3、flush:通常出现在测试环节
with open('g.txt',mode='wb') as f:
    f.write('发发发')
    f.flush()

# 4、了解
with open('g.txt',mode='wb',encoding= 'utf-8') as f:
    print(f.readable())  # 判断是否可读
    print(f.writable())  # 判断是否可写
    print(f.name)  # 文件的名字