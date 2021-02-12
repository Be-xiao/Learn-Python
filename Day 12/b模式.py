# 控制文件读写内容的模式:
'''
t:
    1、读写都是以字符串(Unicode)为单位
    2、只能针对文本文件
    3、必须指定字符编码，即一定要指定encoding参数
b：
    1、读写都是以bytes为单位
    2、可以针对所有文件
    3、一定不能指定字符编码，一定不要指定encoding参数
总结：b模式跟通用
'''
# 错误演示：
# with open(r'IMG_20200930_005901_916.jpg', mode='rt') as f:
#     f.read()  # 硬盘的二进制读入内存-》t模式会将读入内存的内容进行decode解码

#

with open(r'IMG_20200930_005901_916.jpg', mode='rb') as f:
    res = f.read()  # 硬盘的二进制读入内存-》b模式下，不做任何转换，直接读入内存
    print(res)  # bytes类型->当成二进制

# 文件拷贝工具

src_file = input('源文件路径:')
dst_file = input('源文件路径:')
with open(r'{}'.format(src_file), mode='rb') as f1, \
        open(r'{}'.format(dst_file), mode='wb') as f2:
    # res = f1.read()  # 内存占用过大
    # f2.write(res)
    for line in f1:
        f2.write(line)

# 循环读取文件
# 方式一：

with open(r'IMG_20200930_005901_916.jpg', mode='rb') as f:
    while True:
        res = f.read(1024)
        if not res:
            break
        print(len(res))

# 方式二：以行为单位，当行内容过长时会导致一次性读入内容的数据量过大
'''
with open(r'g.txt', mode='utf-8', encoding='utf-8')as f:
    for line in f:
        print(line)
'''
with open('g.txt', mode='rb') as f:
    for line in f:
        print(line)
