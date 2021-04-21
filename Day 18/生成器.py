# 如何得到自定义的迭代器：
# 在函数内一旦存在yield关键字，调用函数并不会执行函数体代码，会返回一个生成器对象
# 生成器即自定义的迭代器


def func():
    print('first')
    yield 1
    print('second')
    yield 2
    print('third')
    yield 3
    print('fourth')


g = func()
print(g)
# 生成器就是迭代器
g.__iter__()

# 会触发函数体代码的运行，然后遇到yield停下来，将yield后的值当做本次调用的返回结果
g.__next__()
g.__next__()
next(g)

print('aaa'.__len__())
print(len('aaa'))  # 'aaa'.__len__()


# 应用案例
def my_range(start, stop, step=1):
    print('start...')
    while start < stop:
        yield start
        start += step
        yield start

    print('end...')


'''
g = my_range(1, 5, 2)  # 1 3
print(next(g))
print(next(g))
print(next(g))
print(next(g))
'''
for n in my_range(1, 7, 2):
    print(n)