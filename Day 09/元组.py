# 元组就是“一个不可变的列表”
# 1、作用：按照索引\存放多个值，只用于读，不用于改

# 2、定义：（）内用逗号分隔开多个任意类型的元素
t = ('completely', 'complete', 'completed', 'incomplete', 'completeness')
# t = tuple()
print(t, type(t))
x = (10)  # 单独一个括号代表包含的意思
print(x, type(x))
x = (10,)  # 如果元组中只有一个元素，必须加逗号
print(x, type(x))
# 元组不可改，指的是内存地址无法改
# 3、类型的转换
# 3.1、按照索引取值（正向取+反向取）：只能取
m = ['heartbroken', 'investment', 'shack']
# 正向取
print(m[0])
# 反向取
print(m[-1])
# 3.2、切片（顾头不顾尾，步长）
u = ['corner', 'cornerstone', 'cornered', 'academic', 'academical']
print(u[0:3])
print(u[0:5:2])  # 0 2 4
print(u[2:len(u)])
print(u[:])
new_u = u[:]  # 切片等同于拷贝行为，相当于浅拷贝
print(u[::-1])
# 3.3、长度
print(len([1, 'proud', 2, 'proudly']))
# 3.4、成员运算 in 和 not in
# 3.5、循环
for x in u:
    print(u)
# 3.6
t = (2, 11, 333, 555, 999)
print(t.index(111))
