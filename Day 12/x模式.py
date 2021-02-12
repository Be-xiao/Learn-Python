# X模式 (控制文件操作的模式)-> 了解
# x,只写模式【不可读：不存在则创建，存在则报错】
with open('a.txt',mode='x',encoding='utf-8') as f:
    ...

