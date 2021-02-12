import time

with open('access.log', mode='rb', ) as f:
    f.seek(0, 2)  # 将指针移动到文件末尾

    while True:
        line = f.readline()
        if len(line) == 0:
            time.sleep(0.5)
        else:
            print(line.decode('utf-8'), end='')
