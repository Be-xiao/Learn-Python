# 方式一:文本编辑器就是采用这种方式
with open('informal.txt', mode='rt', encoding='utf-8') as f:
    res = f.read()  # 如果文件数据过大，会过分的占用内存
    data = res.replace('狗', "傻")
    print(data)

with open('informal.txt', mode='wt', encoding='utf-8') as f1:
    f1.write(data)

# 方式二：
import os

with open('informal.txt', mode='rt', encoding='utf-8') as f2, \
        open('.informal.txt.swap', mode='wt', encoding='utf -8') as f3:
    for line in f2:
        f3.write(line.replace('傻', "狗"))

os.remove('informal.txt')
os.rename('.informal.txt.swap', 'informal.txt')