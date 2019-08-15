import json
with open('data.json', 'r', encoding='utf8') as f:
    dict1 = {}  # 存储数据
    while True:
        # 取出每一行数据
        file = f.readline()
        t = file.strip().replace(',', '', 1)  # 将字符串中的\n\t替换为空
        # 为空 跳出
        if not t:
            break
        # 字符串
        m = t.find(":")
        if m == -1:
            continue
        list1 = t.split(':')
        i = 0
        for str1 in list1:
            # 判断是否是数字，
            if str1.isdigit():
                s = eval(list1[i - 1])
                dict1[s] = int(str1)
            i += 1
# print(dict1)
with open('p2.txt', 'a') as f1:
    for index, value in dict1.items():
        f1.write(index + '   ' + str(value) + '\n')