# 1、作用：
# 1.1、关系运算
friends1 = ['zero', 'kevin', 'jason', 'adam']
friends2 = ['jy', 'ricky', 'jason', 'adam']

l = []
for x in friends1:
    if x in friends2:
        l.append(x)
print(l)

# 1.2、去重
# ==============去重=================
# 1、只能针对不可变类型去重
print(set[1, 1, 1, 1, 2])

# 2、无法保证原来的顺序
print(set[1, 1, 'a', 1, 1, 2, 'b', 'd', 'w', 'e'])

i = [
    {'name': 'adam', 'age': 18, 'sex': 'male'},
    {'name': 'alex', 'age': 19, 'sex': 'female'},
    {'name': 'academic', 'age': 28, 'sex': 'male'},
    {'name': 'manifest', 'age': 20, 'sex': 'male'},
]
new_l = []
for dic in i:
    if dic not in new_l:
        new_l.append(dic)
print(new_l)

# 2、定义：在{}内用逗号分隔开多个元素，多个元素满足以下三个条件
#   2.1集合内元素必须为不可变类型
#   2.2集合内元素无序
#   2.3集合内元素没有重复

# s = {1,2}  # s = set({1,2})

# s = {1,[1,2]}  # 集合内元素必须为不可变类型
# s = {1,'a','z','b',4,7}  # 集合内元素无序
# s = {1,1,1,1,'a','z','b',4,7}  # 集合内元素没有重复
# print(s)

# 了解
# s = {}  # 默认是空字典
# print(type())
# 定义空集合
# s = set()
# print(s,type())

# 3、类型转换：
# set({1,2,3})
res = set('stationary')
print(res)
# print(set([1,1,1,1,1,1,[11,22]]))  # 报错
# print(set({'k1':'to','k2':'legal'}))

# 4、内置方法：

legal = {'investment', 'mission', 'proud', 'normally'}
legal1 = {'investing', 'miss', 'proud', 'normally'}

# 4.1 取交集：两者共同的好友
res = legal & legal1
print(res)
print(legal.intersection(legal1))
# 4.2 取并集：两者所有的好友
print(legal1 | legal)
print(legal.union(legal1))
# 4.3 取差集：取legal独有的好友
print(legal - legal1)
print(legal.difference(legal1))
# 取legal独有的好友
print(legal1 - legal)
print(legal1.difference(legal))
# 4.4:对称差集：求两个用户独有的好友们
print(legal ^ legal1)
print(legal.symmetric_difference(legal1))
# 4.5父子集：包含的关系
s1 = {1, 2, 3}
s2 = {1, 2, 4}
# 不存在包含关系，下面比较均为False
print(s1 > s2)
print(s1 < s2)

s3 = {1, 2, 3}
s4 = {1, 2, }
print(s3 > s4)  # 当s1大于或等于s2时，才能说s1是s2他爹
print(s3 == s1)  # 互为父子

# 其他操作
'''
# 1、长度
>>>long = {'a','b','s'}
>>>len(long)
3

# 2、成员运算
>>> 'c' in long
False

# 3、循环
>>> for item in long:
	print(item)

	
a
b
s
'''

# 其他内置方法
s = {1, 2, 3}
s.discard(4)  # 删除元素不存在什么也不做
print(s)
# s.remove(4)  # 删除元素不存在则报错

s.update({1, 3, 5})
print(s)
# 了解
s.difference({3, 4, 5})  # s.difference_update({3, 4, 5})
print(s)



