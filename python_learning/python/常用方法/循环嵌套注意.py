i = 0
while i < 5:
    j = 0  # 初始化值放在当前循环外即可
    print(f"操场跑圈中……{i}")
    while j < 3:
        print(f"做俯卧撑中……{j}")
        j += 1
    i += 1
# 打印正方形
'''
1、打印1个*
2、打印1行*
3、记录1行中*的个数
4、打印5行
'''
i = 0
while i < 5:
    j = 0
    while j < 5:
        print("*", end=' ')
        j += 1
    i += 1
    print()

m = 5
for j in range(m):
    n = 5
    for i in range(n):
        print('*', end=' ')  # 不换行
    print()  # 输出默认换行
