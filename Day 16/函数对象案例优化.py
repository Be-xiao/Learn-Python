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
    '0': ['退出', None],
    '1': ['登录', login],
    "2": ['转账', transfer],
    '3': ['查询余额', query_balance],
    '4': ['提现', withdraw],
    '5': ['注册', register]
}

while True:
    for k in domain_dic:
        print(k, domain_dic[k][0])
    choice = input('请输入命令编号:').strip()
    if not choice.isdigit():
        print('为了更好的服务顾客本机友情提示“必须输入编号……你个憨批，Are you understand？”')
        continue

    if choice == '0':
        break

    if choice in domain_dic:
        domain_dic[choice][1]()
    else:
        print('输入指令不存在')
