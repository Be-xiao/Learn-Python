# 1、作用：key对应值，其中key通常为字符串类型，所以key对值可以有描述性的功能，用来存多个值，每个值都有唯一一个key与其对应，key对值有描述功能
# 2、定义：在{}内用逗号分开各多个key：value，其中value可以是任意类型，但是key必须是不可变类型,且不能重复
d = {'a': 1, 'b': 3}  # d = dict(...)
print(type(d))
print(d['a'])  # 字典当中默认无序
D = {}  # 默认定义出来的是空字典
q = dict()
print(q, type(q))
e = dict(x=1, y=2, i=5)
print(e, type(D))
# 3、类型转换：
info = [
    ['name', 'adam'],
    ('age', 18),
    ['gender', 'male']
]
p = {}
for item in info:  # item=['name','adam']
    print(item)
    p[item[0]] = item[1]
print(p)

res = dict(info)  # 一行代码搞定上面的for循环工作
print(res)

# 造字典的方式:快速初始化一个字典
keys = ['name', 'age', 'gender']
value = None

d = {}
for k in keys:
    d[k] = None
print(d)

h = {}.fromkeys(keys, None)
print(h)

# 4、内置方法
# 优先掌握的操作：

# 4.1、按照key取值，可存可取
f = {'k1': 'lll'}
# 针对赋值操作：key存在，则修改
f['k1'] = 999
print(f)
# 针对赋值操作：key不存在，则创建新值
f['k2'] = 999
print(f)

# 4.2、长达len（）
d = {'k1': 999, 'k2': 999}
print(len(d))

# 4.3、成员运算 in 和 not for,in根据key
d = {'k1': 999, 'k2': 999}
print('k1' in d)
print(999 in d)

# 4.4、删除
d = {'k1': 999, 'k2': 999}
# 4.4.1 通用删除
del d['k1']
print(d)

# 4.4.2 pop删除:根据key删除,返回key对应的valu值
d = {'k1': 999, 'k2': 999}
d.pop('k1')
print(d)
res = d.pop('k2')
print(res)
# 4.4.3 .popitem删除：随机删除，返回元组(key,value)
d = {'k1': 999, 'k2': 999}
res = d.popitem()
print(d)
print(res)

# 4.5、键keys（），值values,键值对items()...--->在Python3中得到的是老母鸡
d = {'k1': 999, 'k2': 999}
'''
在python2中：
>>> d = {'k1': 999, 'k2': 999}
>>> d.keys()
['k2', 'k1']
>>> d.values()
[999, 999]
>>> d.items()
[('k2', 999), ('k1', 999)]
>>> dict(d.items())
{'k2': 999, 'k1': 999}
'''

# 4.6、循环
for k, v in d.items():
    print(k, v)
# 需要掌握的内置方法：
d = {'k1': 999}
d.clear()

# 2、d.update()  # 以新字典更新老字典，以新字典为准
dic = {'k2': 222, 'k1': 999}
d.update(dic)
print(d)

# 3、d.get():根据key取值容错性更好
# print(d['k4'])  # key不存在则报错
print(d.get('k1'))  # key不存在不报错，返回None

# 4、d.d.setdefault()
info = {'name': 'adam', 'age': 18, 'sex': 'male'}
if 'name' in info:
    ...  # 等同于pass
else:
    info['name'] = 'egon'
print(info)

# 如果k1有则不添加,返回字典中key对应的值
d = {'k2': 222, 'k1': 999}
d.setdefault('k1', 222)
print(d)
res = d.setdefault('k1', 222)
print(res)

# 如果key没有则添加
info = {}
info.setdefault('name', 'egon')
print(info)

