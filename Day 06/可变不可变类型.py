# 1、可变不可变类型
# 可变类型：值改变， ID不变（内存地址不变），证明改的是原值，证明原值是可以被改变的
# 不可变类型：值改变，ID也变了，证明是产生新的值，压根没有改变原值，证明原值不可以被修改的
# 2、验证
# 2.1、int是不可变类型
x = 10
print(id(x))
x = 15  # 产生新值
print(id(x))

# 2.2 float是不可变类型
x = 5.1
print(id(x))
x = 6.1
print(id(x))

# 2.3 str是不可变类型
x = 'cost a pretty penny'
print(id(x))
x = "microphone"
print(id(x))

# 2.4 list是可变类型
l = ['conclusive', 'conclusion', 'compensation']
print(id(l))
l[2] = 'compensate'
print(l)
print(id(l))

# 2.5 dict是可变类型
dic = {"name": "adam", 'age': 19}
print(id(dic))

dic['age'] = 18
print(dic)
print(id(dic))

# bool不可变类型

# 关于dict的补充：
# 定义：{}内用逗号分开多个key:value,其中value可以是任意数据类型,但是key必须是不可变类型

k = {
    'k1': 19,
    'k2': 19.9,
    'k3': 'debase',
    'k4': [333, [444, ], {'m': 'str'}],
    'k5': {'salary': 888888}
}
print(k)
