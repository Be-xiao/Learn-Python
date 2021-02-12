# 精髓:可以把函数当变量去用
def func():
    print('romance')


# 1、可以赋值
f = func
print(f, func)  # 内存地址相同
f()


# 2、可以当做函数的参数传入
def foo(x):  # x = func的内存地址
    print(x)


foo(func)  # foo(func的内存地址)


# 3、可以把函数当做另外一个函数的返回值
def even(x):  # x = func的内存地址
    return x  # return func的内存地址


res = even(func)  # even(func的内存地址)
print(res)  # res=func的内存地址
res()

# 4、可以当做容器类型的一个元素
'''
l = [func]
print(l)
l[0]()

dic = {'k1': func}
print(dic)
dic['k1']()
'''


# 案列一
def login():
    print('Login function')


def transfer():
    print('Transfer function')


def query_balance():
    print('Query Balance function')


def withdraw():
    print('Withdraw function')


def register():
    print('注册功能')


domain_dic = {
    '1': login,
    "2": transfer,
    '3': query_balance,
    '4': withdraw,
    '5': register
}

while True:
    print("""
    0 退出
    1 登录
    2 转账
    3 查询余额
    4 提现
    5 注册
    """)
    choice = input('请输入命令编号:').strip()
    if not choice.isdigit():
        print('为了更好的服务顾客本机器友情提示“必须输入编号……你个憨批，Are you understand？”')
        continue

    if choice == '0':
        break

    if choice in domain_dic:
        domain_dic[choice]()
    else:
        print('输入指令不存在')

    """
    if choice == '1':
        login()
    elif choice == '2':
        transfer()
    elif choice == '3':
        query_balance()
    else:
        print('输入指令不存在')
    """
