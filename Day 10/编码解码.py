# coding：utf-8
x = '上'
res = x.encode('gbk')  # Unicode---->gbk
print(res, type(res))
res.decode('gbk')


