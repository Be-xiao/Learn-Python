print('{x:*^10}'.format(x='开始执行'))

print('尊敬的用户,您好\n')
print('欢迎使用相亲系统')
criteria = [
    '漂亮', '美', '好看', '可爱', '卡哇伊', '美美哒',
    '是', 'yes', 'of course', '这还用说', '当然',
    '还行吧', '一般', '不算丑', '长得还行', '还行',
    '一般般啦', '还凑合吧', '还凑合', '凑合', "天生丽质"
]
constellation = [
    '摩羯座', '水平座', '巨蟹座', '天蝎座', '白羊座', '天马座',
]
genders = [
    '女', '妹子', 'woman', 'girl', 'nv'
]
consumer = [
    'lesson@gmail.com', 'www.@qq.com', '123'
]
coda = [
    'lesson123', 'www123', '123'
]
fondness = [
    '看书', '打游戏', '画画', '看番', '追剧', '玩王者荣耀', '吃鸡', '睡觉', '美食', '爱旅游',
    '看漫画', '听音乐', '看小说', '旅游', '睡觉', '刷抖音', '搞研究', '玩手机', '爱装电脑',
    '天文', '马克思主义', '爱干净', '做饭', '追星', '爱逛街', '爱家人', '美容', '运动', '奥特曼',
]
for i in range(5):
    username = input('请输入您的账号：').strip()
    username = str(username)
    username = username in consumer
    password = input('请输入您的密码：').strip()
    password = str(password)
    password = password in coda
    if username == 1 and password == 1:
        print('登录成功')
        while 1:
            gender = input('请输入您的性别：').strip()
            gender = str(gender)
            gender = gender in genders
            if gender == 0:
                print('你是基佬吗？(●￣(ｴ)￣●)')
                break
            print('美女，我很期待哦！')
            age = input('请输入您的年龄：').strip()
            if age.isdigit():
                age = int(age)
                if age > 25:
                    print('对不起，阿姨，你是个好人，但是老牛吃嫩草是不道德的')
                    break
                elif age >= 16:
                    print('我们年龄很合适哦！')
                else:
                    print('小姑凉，好好读书，不要谈恋爱')
                    break
            else:
                print('请输入数字，傻子，难道您不是正常人类(？_ ?)')
            is_beautiful = input('您漂亮吗：').strip()
            is_beautiful = str(is_beautiful)
            is_beautiful = is_beautiful in criteria
            if is_beautiful:
                print('美女，您的长相一定是我喜欢的类型')
            else:
                print('我对长相虽然不挑，但不是什么都要，丑拒')
                break
            stat_sign = input('请输入您的星座：').strip()
            stat_sign = str(stat_sign)
            stat_sign = stat_sign in constellation
            if stat_sign:
                print('美女我们星座很匹配哦！')
            else:
                print('虽然星座不匹配，但我是坚定的马克思主义信徒')
            weight = input('请输入您的体重：')
            if weight.isdigit():
                weight = int(weight)
                if weight <= 60:
                    print('我打赌你的身材一定很棒')
                elif weight > 60 and weight <= 70:
                    print('微胖才是极品，赞')
                else:
                    print('我建议您减肥')
                    break
            else:
                print('请输入纯数字，默认单位kg，不用输入的，二哈')
            height = input('请输入您的身高：')
            if height.isdigit():
                height = int(height)
                print('美女，我对身高没有要求，你一定很nice')
            else:
                print('请输入纯数字，默认单位CM，不用输入的，智障女神')
            hobbies = input("请输入您的爱好：")
            hobbies = str(hobbies)
            hobbies = hobbies in fondness
            if hobbies == 1:
                print('我们的三观应该很合的来')
            else:
                print('其实我对于这个无所谓的（*_*）')
            print('我们去吃饭吧，这是我QQ:12345678')
            print('输入“退出”退出本系统')
            cmd = input('输入命令>:')
            if cmd == '退出':
                break
            break
        break  # 立刻终止本层循环
    else:
        print('账号名或密码错误')
else:
    print('输错次数过多，自动终止')

print('{x:*^10}'.format(x='程序执行结束'))
