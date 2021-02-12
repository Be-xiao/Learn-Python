def my_sum(*args):
    res = 0
    for item in args:
        res += item
    return res


numbers = input('请输入您要相加的数：')
res = my_sum(numbers)
print(res)
