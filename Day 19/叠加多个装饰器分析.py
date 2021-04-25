# 叠加多个装饰器的加载、运行分析(了解)
'''
@deco1  # index = deco1(deco2.wrapper的内存地址)
@deco2  # deco2.wrapper的内存地址 = deco2(deco3.wrapper的内存地址)
@deco3  # deco3.wrapper的内存地址 = deco3(index)
def index():
    pass
'''


def index(x, y):
    print('from index %s：%s' % (x, y))


index(1, 2)
