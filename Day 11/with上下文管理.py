# 文件对象又称文件句柄
with open(r'b.txt', mode='rt') as f1,\
        open(r'd.txt') as f2:
    res1 = f1.read()
    res2 = f2.read()
    print(res1)
    print(res2)
