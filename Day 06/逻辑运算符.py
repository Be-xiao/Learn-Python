# 什么是条件？什么当做条件？为何要用条件？
# 条件可以是：比较运算符
# 第一大类：显示布尔值
age = input('请输入您的年龄：')
age = int(age)
print(age > 18)  # 条件判断之后会得到一个布尔值

# 2.1 条件可以是：True、False
is_beautiful = input('你漂亮吗：')
is_beautiful = str(is_beautiful)
print(is_beautiful == '漂亮')

# 第二大类：隐式的布尔值，所有的值都可以当成条件去用
# 其中：0、None、空（空字符串、空列表、空字典）=》代表布尔值为false、其余类型都为真

# 逻辑运算符：
# not:就是把紧跟其后那个条件结果取反
print(16 > 13)
print(not 16 > 13)
print(not 10)
print(not 0)

# and:用来连接左右两个条件，两个条件同时为真，最终结果才为真
# 条件一 and 条件二
print(True and 10 > 3)
print(True and 10 > 3 and 0)  # 条件全为真，最终结果才为True

# or:逻辑或，or用来链接左右两个条件，两个条件但凡有一个为True,最终结果就位True
# 两个结果都为False的情况下，最终结果才为False
print(3 > 2 or 0)  # 偷懒原则


# 3、区分优先级：not > and > or
# ps：
# 如果单独就只是一串and链接或者单独一串or链接，就按照从左到右依次运算。（偷懒原则），如果混用，则需要考虑优先级

# 短路原则：偷懒原则，偷懒到哪个位置，就把当前位置的值返回
