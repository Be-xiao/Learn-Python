# -*- coding:utf-8 -*-
# 1、打开文件
# windows路径分隔符问题
# open('C:\a\nb\c\d.txt')
# 解决方案一 # 推荐
# open(r'C:\a\nb\c\d.txt')
# 解决方案二：
# open('C:/a/nb/c/d.txt')
f = open(r'\a.txt', mode='rt')  # f的值是一种变量，占用的是应用程序的内存空间
# print(f)
# 2、操作文件：读/写文件,应用程序对文件的读写请求都是在向操作系统发送系统调用，
# 然后由操作系统控制硬盘把数据读入内存，或写入内存
res = f.read()
print(res)
# 3、关闭文件
f.close()  # 回收操作系统资源
del f  # 回收应用程序资源


