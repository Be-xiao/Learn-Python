"""
1、什么是迭代器
    迭代器指的是迭代取值的工具，迭代是一个重复的过程，每次重复都是基于上一次的结果而继续的，
    单纯的重复并不是迭代

# >>> count = 1
# >>> while count < 5:
# 	        print(count)
#   	    count += 1


1
2
3
4

2、为何要有迭代器
    迭代器是用来取值的工具，而涉及到把多个值循环取出来的
    类型有：列表、字符串、元组、字典、集合、文件

# >>> l = ['elgon', 'normal', 'alex']
# >>> i = 0
# >>> while i < len(l):
# >>>	    print(l[i])
# >>>	    i += 1


#elgon
#normal
#alex

    上述迭代取值的方式只适用于有索引的数据类型:列表、字符串
    为了解决基于索引取值的局限性
    Python必须提供一种能够不依赖与索引的取值方式，这就是迭代器

3、如何用迭代器

"""
# 可迭代对象:但凡内置有__iter__方法的都称之为可迭代的对象
# 字符串、列表、元组、字典、集合、文件

dictionary = {'a': 1, 'b': 2, 'c': 3}
dictionary_iterator = dictionary.__iter__()
# print(dictionary_iterator)

while True:  # 在一个迭代器取值取完的情况下，在对其取值取不到
    try:
        print(dictionary_iterator.__next__())
    except StopIteration:
        break
