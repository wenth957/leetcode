# 有一个字符串’hello python' 是否包含p
# 输出包含p，不包含输出不包含p
my_str = 'hello python'
for i in my_str:
    if i == 'p':
        print("包含p")
        break  # 首次确定则break
    else:
        pass  # 如果是循环结束才输出，不能在这儿输出不包含
else:
    print("不包含p")  # for如果不是被break结束循环 会运行
