# 一、int类型
# 作用：记录年龄、身份证号、个数等等
# 定义：

age = 18  # age = int(10)
print(type(age))

# 名字(参数)
print('你好，帝企鹅')

# 类型转换
res = int('100086')  # 纯数字的字符串转成int
print(res,type(res))
# 了解
# 10进制->二进制
'''
11 -> 1011
1011 -> 8+2+1
'''
print(bin(11))  # 0b1011,十进制转二进制
print(oct(11))  # 十进制转八进制，1*8^1+3*8^0
print(hex(11))  # 0xb,十进制转成其他进制
# 二进制->10进制
print(int(0b1011),2)
# 二进制->8进制
print(int(0o13),8)
# 二进制->16进制
print(int(0xb),16)

# 二、float类型
# 作用：记录薪资、身高、体重
# 定义：
salary = 3.3
height = 1.75
weight = 59.5
print(type(salary))
res = float("3.1")
print(res,type(res))

# 4、使用
# int与float没有需要掌握的内置方法
# 他们的使用就是数学运算+比较运算




