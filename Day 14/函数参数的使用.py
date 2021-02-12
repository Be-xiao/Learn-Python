# 一、形式参数与实际参数
# 形参:在定义函数阶段定义的参数称之为形式参数，称之为形参，形参相当于变量名
def func(x, y):
    print(x, y)


# 实参:在调用函数阶段传入的值，称之为实际参数，简称实参，相当于变量值
func(1, 2)

# 形参与实参的关系：
# 1、在调用阶段，实参(变量值)会绑定给形参(变量名)
# 2、这种绑定关系只能在函数体内使用
# 3、实参与形参的绑定关系在函数调用时生效，函数调用结束后解除绑定关系

# 实参相当于值，值可以是以下形式?
# 形式一:
# func(1,2)

# 形式二:
a = 3
b = 5
func(a, b)

# 形式三：
func(int('1'), 2)

func(func(1, 1), func(2, 3))


# 形参与实参的具体参数
# 2.1位置参数:按照从左到右的顺序依次定义的参数称之为位置参数
# 位置形参：在函数定义阶段:按照从左到右的顺序直接定义的变量名
#           特点：必须被传值，多一个不行，少一个也不行
def after(x, y):
    print(x, y)


after(y=3, x=1)
# 位置实参:在函数调用阶段:按照从左到右的顺序依次传入的值
#       特点:按照顺序与形参一一对应
after(1, 2)
after(2, 1)


# 2.2关键字参数
# 关键字实参:在函数调用阶段，按照key=value的形式传入的值
#       特点：可以指明道姓给某个形参传值，可以完全不参照顺序
def func(x, y):
    print(x, y)


func(y=2, x=1)
func(1, 2)
# 混合使用，强调：
# 1、位置实参必须放在关键字实参前
# func(y=2,1)  # 错误
func(1, y=2)


# 2、不能为同一个形参重复传值
# func(1,y=2,x=3)  # 错误

# 2.3默认参数
# 默认形参:在定义函数阶段，就已经被形参赋值的形参，称之为默认参数
#       特点：在定义阶段就已经被赋值，意味着在调用阶段可以不用为其赋值
def academic(x, y=3):
    print(x, y)


academic(x=6)
academic(x=8, y=55)


def innovation(name, age, sex='男'):
    print(name, age, sex)


innovation('大炮', '21')
innovation('二炮', '20')
innovation('三炮', '19')
innovation('炮姐', '18', '女')

# 位置形参与默认形参混用，强调:
# 2.3.1、位置参数必须在默认形参的左边
# def func(y=3, x):
#   pass

# 2.3.2、默认参数的值是在函数定义阶段被赋值的，准确的说被赋予的是值的内存地址
# 示范一
m = 2


def innovative(x, y=m):  # y=>2的内存地址
    print(x, y)


m = 3333
innovative(1)

# 示范二
n = [1111, ]


def innovativeness(x, y=n):  # y=>list的内存地址
    print(x, y)


n.append(2222)
innovativeness(1)


# 2.3.3、虽然默认值可以被指定为任意数据类型，但不推荐使用可变类型
# 函数定义最理想的状态:函数的调用值跟函数本身有关系，不收外界代码的干扰
def innovator(x, y, z, l=None):
    if l is None:
        l = []
    l.append(x)
    l.append(y)
    l.append(z)
    print(l)


innovator(1, 2, 3)
new_innovator = [11, 22]
innovator(1, 2, 3, new_innovator)


# 2.4可变长度的参数
# 可变长度指的是在调用函数时，传入的值(实参)的个数不固定
# 实参是用来为形参赋值的，所以对应着，针对溢出的实参必须有对应的形参来接收


# 2.4.1可变长度的位置参数
# I:*形参名：用来接收溢出的位置实参，溢出的位置实参会被*保存成元组的格式，然后赋值紧跟其后的形参名
#           *后跟的可以是任意名字，但是约定俗成为args
def distinct(x, y, *args):
    print(x, y)


distinct(1, 2, 1, 3, 5, 5)


# II:*可以用在实参中,实参中带*，先将*后的值拆分成位置实参
def distinctly(x, y, z):
    print(x, y, z)


l = [11, 22, 33]
distinctly(*l)


# III:形参与实参中都带*
def clarification(x, y, *args):
    print(x, y, args)


clarification(1, 2, *[3, 4, 5, 6])
clarification(1, 2, [3, 4, 5, 6])
clarification(*'Hello world')


# 2.4.2可变长度的关键字参数
# I:**形参名：用来接收溢出的关键字，**会将溢出的关键字实参保存成字典格式，然后赋值给紧跟其后的形参名
#       **后跟的可以是任意名字，但是约定俗成为kwargs
def distinction(x, y, **kwargs):
    print(x, y, kwargs)


distinction(1, y=2, a=1, c=88)


# II:**可以用在实参中（**后跟的只能是字典）,实参中带**，先将**后的值拆分成关键字实参

def clear(x, y, z):
    print(x, y, z)


clear(**{'x': 1, 'y': 2, 'z': 3})


# III:形参与实参中都带**
def unclear(x, y, **kwargs):
    print(x, y, kwargs)


unclear(**{'x': 1, 'b': 2, 'y': 3, "a": 4})


def index(x, y, z):
    print('index==>>>', x, y, z)


def wrapper(a, b, c):  # a=1,b=2,c=3
    index(a, b, c)  # index(1, 2, 3)


wrapper(1, 2, 3)  # 为wrapper传递的参数是给index用的


# 混用*与**
# *args必须在**kwargs之前(语法规定)

def country(*args, **kwargs):
    print(*args)
    print(**kwargs)


country(1, 2, 1, 3, 5, 9, 7, x=1, y=9)

# 2.5命名关键字参数

# 2.6组合使用
