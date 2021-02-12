# -*- coding:utf-8 -*-
'''
1、读写都以str(Unicode)为单位
2、文本文件
3、必须指定encoding = 'utf-8'
'''
# 没有指定encoding参数操作系统会使用自己默认的编码
# Linux系统默认utf-8
# Windows系统默认GBK
with open('b.txt', mode='rt', encoding='utf-8') as f:
    res = f.read()  # t模式会将f.read()独处的结果解码成Unicode
    print(res, type(res))
    f.write('我日')
# 内存：utf-8格式二进制----解码-----》Unicode
# 硬盘：d.txt内容：utf-8格式二进制
