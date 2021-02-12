# 1、作用：按照位置存多个值，
# 2、定义：
i = ['coda', 'weight', 1, 1.2]  # l=list(['coda','weight',1,1.2])
print(type(i))

# 3、类型转换：但凡被for循环的类型都可以当做参数传给list（）转成列表
res = list('stat sign')
print(res)
monkey_paw = list({'k1': 'standard', 'k2': 'consumer', 'k3': 111})
print(monkey_paw)

# 4、内置方法
# 4.1按索引存取值（正向存取+反向存取）：即可以取也可以改
m = ['heartbroken', 'investment', 'shack']
# 正向取
print(m[0])
# 反向取
print(m[-1])
# 可以取也可以改：索引存在修改对应的值
m[0] = 'mission'  # 修改行为
print(m)
# 无论是取还是赋值，索引不存在则报错
# m[3] = 'review'

# 4.2、切片（顾头不顾尾，步长）
u = ['corner', 'cornerstone', 'cornered', 'academic', 'academical']
print(u[0:3])
print(u[0:5:2])  # 0 2 4
print(u[2:len(u)])
print(u[:])
new_u = u[:]  # 切片等同于拷贝行为，相当于浅拷贝
print(u[::-1])
# 4.3、长度
print(len([1, 'proud', 2, 'proudly']))
# 4.4、成员运算 in 和 not in
# 4.5、追加
n = ['normally', 'norm', 'normal']
n.append('abnormal')
print(n)

# 4.6、插入值
k = ['embarrassing', 'embarrass', 'unembarrassed']
k.insert(1, 'embarrassment')
print(k)

# 4.7、
new_d = ['figure', 'figurative', 'disfigure']
d = ['prefigure', 'transfigure']
d.append(new_d)
print(d)
# 代码实现
for figure in new_d:
    d.append(

    )
print(d)
# extend实现上述代码
d.extend('abd')
print(d)

# 4.8、删除
# 方式一：通用的删除方法，只是单纯的删除，没有返回值
q = ['argument', 'argue', 'argumentative', 'argumentation']
del q[1]
# x =del q[1]  # 抛出异常，不支持赋值语法
print(q)

# 方式二：l.pop（）根据索引删除,会返回值
y = ['monarchist', 'academic', 'academy', 'academia', 'academically']
y.pop()  # 不指定索引默认删除最后一个
print(y)
y.pop(0)
print(y)

# 方式三：l.remove根据元素删除,返回None
e = ['move', 'moved', 'moving', 'movement', 'movable', 'mover']
e.remove('move')
print(res)

# 需要掌握的操作
w = ['fair', 'fairly', 'unfair', 'unfairness', 'unfairly', 'fairness']
# 1、w.count()
print(w.count('fair'))

# 2、w.index()
print(w.index('fair'))  # 找不到报错

# 3、w.clear()
e.clear()  # 清空
print(e)
# 4、w.reverse():不是排序，就是将列表倒过来
w.reverse()
print(w)

# 5、w.sort()：默认从小到大排，称之为升序
j = [11, 2, 8, -9, -5]
j.sort(reverse=True)  # 从大到小排，设置为降序
print(j)

j = ['a', 'y', 'w', 'b']  # 了解：字符串可以比大小，按照对于的位置的字符依次pk，按照ASCI码表的先后顺序区别字符的大小,表中排在后面的大于前面的
j.sort()
print(j)
print('asdad' > 'sdfsafe')

# 了解：列表之间也可以比大小，原理同字符串一样

# 补充：
# 队列:FIFO,先进先出
# 入栈操作
l = []
l.append('whilst')
l.append('whiles')
l.append('proud')
print(l)

# 出栈操作
print(l.pop(0))
print(l.pop(0))
print(l.pop(0))



# 堆栈：
