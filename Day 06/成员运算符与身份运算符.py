# 1、成员运算符
print('egon' in "hello egon")  # 判断一个字符串是否存在与一个大字符串之中
print('e' in "hello egon")
print(222 in [111, 222, 333, ])  # 判断元素是否存在于列表
print('k1' in {'k1': '222', 'k2': 222})  # 判断key是否存在于字典

# not in
print('adam' not in "adam is you father")
print(not 'adam' in "adam is you father")  # 逻辑同上，但语义不明确，不推荐使用

# 2、身份运算
# is  # 判断的是ID是否相等
