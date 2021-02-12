list1 = ['adam', 'l//', [1, '88']]
# 二者分割不开，list1改list2也跟着改，因为指向的是同一个内存地址
list2 = list1  # 这不叫拷贝

# 需求：
# 1、拷贝一下原列表，产生一个新列表
# 2、想让两个列表完全独立开，针对的是改操作的独立而不是读操作

# 3、如何copy列表
# 3.1 浅copy:是把原列表第一层内存地址完全copy一份
# 试验1：
list3 = list1.copy()
print(list3)
print(id(list3))
print(id(list2))
print(id(list1))
print(id(list1[0]), id(list1[1]), id(list1[2]))
print(id(list3[0]), id(list3[1]), id(list3[2]))
# 试验2：对于可变类型，我们可以改变类型中包含的值，但内存地址不变，
# 即原列表的索引指向仍然指向原来的内存地址，于是列表也就跟着一起受影响
# 如下：
list1[0] = 'egon'
list1[1] = '/*-'
list1[2][0] = 222
list1[2][1] = 999
print(list1)
print(list3)

# 综合试验1和试验2可以得出，想要copy得到新列表与原列表的改操作完全独立开
# 必须有一种可以区分开不可变类型与不可变类型的copy机制，这就是深copy
# 3.2、深copy：
import copy

list4 = copy.deepcopy(list1)
print(id(list1[0]), id(list1[1]), id(list1[2]))
print(id(list4[0]), id(list4[1]), id(list4[2]))
'''
2769214459184 2769214458864 2769216619584
2769214459184 2769214458864 2769216620544
'''
print(list4)

list1[0] = 'alex'
list1[1] = '(^-^)'
list1[2][0] = '(*_*)'
list1[2][1] = '(>_<)'
print(list1)
print(list4)
print(id(list1[0]), id(list1[1]), id(list1[2]), id(list1[2][0]), id(list1[2][1]))
print(id(list4[0]), id(list4[1]), id(list4[2]), id(list4[2][0]), id(list4[2][1]))

# 总结：
# 浅copy：只copy第一层，
# 深copy：会对每一层加以区分，所以内存地址会不一样