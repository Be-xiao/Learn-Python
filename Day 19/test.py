def add():
    count = 0
    while True:
        count += 1
        yield count


g = add()

list(g)
# 这是一段可以让电脑卡死的代码，请在他人的电脑上随意运行