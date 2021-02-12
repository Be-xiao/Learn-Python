# -*- coding:utf-8 -*-
def circle(radius, action=0):
    from math import pi

    def perimeter(radius):
        return 2 * pi * radius

    def area(radius):
        return pi * (radius ** 2)

    if action == 0:
        return perimeter(radius)
    elif action == 1:
        return area(radius)


x = input('请输入圆半径:>>>')
y = input('请选择圆面积或圆周长<1/0>:>>>')
res = circle(x, action=y)
print(res)
