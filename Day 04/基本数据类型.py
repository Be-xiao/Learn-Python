# 1、数字类型
# 1.1整型int
# 作用：记录年龄、身份证号、个数等等
# 定义：
age = 18
print(type(age))

# 1.2浮点型float(小数)
# 作用：记录薪资、身高、体重
# 定义：
salary = 3.3
height = 1.75
weight = 59.5
print(type(salary))
# 数字类型的其他应用
level = 1
level = level + 1
print(level)

print(10 * 3)

print(10 + 3.3)  # int与float之间可以相加

age = 19
print(age > 18)  # 比较大小

# 2、字符串类型str
# 作用：记录描述性质的状态，名字，一段话
# 定义：用引号（'',"",'''  ''',"""  """）包含的一串一串字符
info = '''草泥马'''
print(type(info))
name = "you father"
print(type(name))

x = 18
print(type(x))
x = 18  # 由数字组成的字符串，是字符串类型，不是int类型
print(x)

# 'name' = ‘name’  # 语法错误，等号左边是变量名，变量名的命名不能有引号
# name  # 代表访问的变量名
# ”name“  # 代表的是值

# 其他使用：
# 字符串的嵌套，注意：外层用单引号，内层用双引号,反之亦然
print('my name is "you father"')
print('my name is \'you father\'')  # 转译
# 字符串之间可以相加,但仅限于str与str之间进行
# 代表字符串的拼接，了解即可，不推荐使用，因为str之间相加效率极低
print('my name is' + 'egon')
print('A' * 10)

print("=" * 20)
print("hello world")
print("=" * 20)

# 3、列表：索引对于值，索引从0开始，0代表第一个
# 作用：按照位置记录多个值(同一个人的多个爱好、同一个班级的所有学生姓名、同一个人12个月的薪资)，并且可以按照索引取指定位置的值
hobbies = 'read music play'
print(hobbies)
print(hobbies[1])

# 定义：在[]内用逗号分隔开多个任意类型的值，一个值称之为一个元素
#     0  1       2                  3
l = [10, 3, 'conclusive；决定性的，', ['conclusion;结论', 'compensate；补偿，付薪水，弥补'], 'compensation；薪资待遇']
print(l)
print(l[1])
print(l[2])
print(l[3][1])

# 其他用途：
students_info = [
    ['tony', 18, ['jack']],
    ['jason', 18, ['play', 'sleep']]
]
# 取出第一个学生的第一个爱好
print(students_info[0][2][0])

# 4、
# 索引反映的是顺序、位置，对值没有描述性的功能
village = ['base', '58', 'male']
print(village[1])
print(village[0])
print(type(village))

# 字典类型：key对应值，其中key通常为字符串类型，所以key对值可以有描述性的功能
# 作用：用来存多个值，每个值都有唯一一个key与其对应，key对值有描述功能
# 定义：在{}内用逗号分开各多个key：value
d = {'a': 1, 'b': 3}
print(type(d))
print(d['a'])  # 字典当中默认无序

local = {'name': 'adam',
         'age': "19",
         'gender': "male",
         'date': "2.18"
         }
print(local['name'])

# 其他用途：
tours = [
    {'name': 'egon', 'age': '19', 'gender': 'male'},
    {'name': 'father', 'age': '50', 'gender': 'male'},
    {'name': 'Adam', 'age': '23', 'gender': 'male'},
]
print(tours[1]['name'])  # 取第二个的名字

# 5 布尔bool
# 5.1 作用:用来记录真假两种状态
# 5.2 定义：
is_ok = True
is_ok = False
print(type(is_ok))
# 5.3 使用
# 通常用来当做判断条件，我们将在if判断中用到它
