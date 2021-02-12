# 1、算数运算符
print(10 + 6)
print(10 + 3.3)
print(10 / 6)  # 结果带小数
print(10 // 6)  # 只保留整数部分
print(10 % 6)  # 取模，取余数
print(10 ** 6)  # 几次方的意思，代表10的6次方

# 2、比较运算:>、<、>=、<=、==、!=
print(10 > 3)
print(10 == 3)
print(10 >= 3)
print(10 <= 10)

name = input('you name:')
print(name == 'egon')

# 3、赋值运算符
# 3.1  '=' :变量的赋值
# 3.2 增量的赋值
age = 19
age += 1  # age = age + 1
age /= 3
age %= 3
age **= 3  # age=age**3
# 3.3 链式赋值
z = y = x = 10  # x=10,z=y,y=z
print(x, y, z)
print(id(x), id(y), id(z))
# 3.4 交叉赋值
m = 10
n = 20
print(m, n)
# 交换值
temp = m  # 临时指定
m = n
n = temp
print(m, n)

m, n = n, m  # 交叉赋值
print(m, n)

# 3.5解压赋值
salaries = [111, 222, 333, 444, 'eee']
# 把五天的工资取出来分别赋予值给不同的变量名
day0 = salaries[0]
day1 = salaries[1]
day2 = salaries[2]
day3 = salaries[3]
day4 = salaries[4]
print(day0)
print(day1)
print(day2)
print(day3)
print(day4)

day0, day1, day2, day3, day4 = salaries  # 对应的变量名少一个不行，多一个不行
print(day0)
print(day1)
print(day2)
print(day3)
print(day4)
# 引入*，可以帮助我们取两头的值，无法取中间的值
x, y, z, *_ = salaries  # 只取前三个值，*会将没有对应关系的值存成列表然后赋值给紧跟其后的那个变量名，此处为_
print(x, y, z)
*_, x, y, z, = salaries  # 取后三个值
print(x, y, z)
x, *_, y, z, = salaries  # 取两头的值
print(x, y, z)
_, *middle, _ = salaries  # 可以取中间的值，但不是人干的事
print(middle)
# 解压字典默认解压出来的是字典key
x,y,z =dic={'a':1,'b':"2",'c':3}
print(x,y,z)
