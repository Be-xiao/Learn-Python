# -*- coding:utf-8 -*-
src_file = input('源文件路径:')
dst_file = input('源文件路径:')
with open(r'{}'.format(src_file), mode='rb') as f1, \
        open(r'{}'.format(dst_file), mode='wb') as f2:
    # res = f1.read()  # 内存占用过大
    # f2.write(res)
    for line in f1:
        f2.write(line)