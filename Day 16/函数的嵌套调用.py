# 函数嵌套
# 1、函数的嵌套调用：在调用一个函数的过程中又调用其他函数
def max(x, y):
    if x > y:
        return x
    else:
        return y


def max2(a, b, c, d):
    # 第一步：比较a，b，得到res1
    res1 = max(a, b)
    # 第二步：比较res1，c，得到res2
    res2 = max(res1, c)
    # 第三步：比较res2，d，得到res3
    res3 = max(res2, d)
    return res3


res = max2(9, 5, 8, 4)
print(res)


# 函数的嵌套定义:在函数内定义其他函数
def f1():
    def f2():
        pass


# 圆形
def circle(radius, action=0):
    # 求圆形周长:2*pi*radius
    from math import pi

    def perimeter(radius):
        return 2 * pi * radius

    # 求圆形面积:pi*(radius**2)
    def area(radius):
        return pi * (radius ** 2)

    if action == 0:
        return perimeter(radius)
    elif action == 1:
        return area(radius)


circle(33, action=0)
