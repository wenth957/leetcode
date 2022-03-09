import random

# while 条件成立，无线循环代码
# if  条件成立，执行一次代码
num = 0
while num < 5:
    print(f"我已经跑了{num+1}圈了！")
    num += 1

while True:
    user = int(input('choose：1（石头） 2（剪刀） 3（布）'))
    computer = random.randint(1, 3)
    if user == computer:
        print("平局")
    elif (user == computer - 1) or (user == 3 and computer == 1):
        print("我赢了！")
    else:
        print("电脑赢了")
