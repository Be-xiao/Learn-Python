# 固定模板
def 有参装饰器(x,y):
    def out(func):
        def wrapper(*args, **kwargs):
            # 1、调用原函数
            # 2、为其增加新功能
            res = func(*args, **kwargs)
            return res

        return wrapper
    return out


@有参装饰器(1,y=2)
def 被装饰对象():
    pass