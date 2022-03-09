# -*- Coding: UTF-8 -*-
# day_5.py
# @作者
# @创建日期 2021-01-30T17:12:42.006Z+08:00
# @最后修改日期 2021-04-11T17:58:20.477Z+08:00
#

from random import randint


'''
总结前面所学，exercise
寻找水仙花数即 153 = 1^3 + 5^3 + 3^3 所以要得到三位数每一位数
个位数 对10取余 十位数对10取整然后对10取余 百位数对100取整
利用这种方法拆分组合任意整数 每个数对10取余即可得到当前个位数
'''
for i in range(100, 1000):
    low = i % 10
    mid = i // 10 % 10
    high = i // 100
    if i == low**3 + mid**3 + high**3:
        print('%d is correct!' % i)
# 正整数的反转（难）
num = int(input('please enter a positive integer:'))
reverse_num = 0
while num > 0:
    reverse_num = reverse_num * 10 + num % 10
    # 第一次得到个位数，num变成n-1位数
    # 第二次得到十位数，变成个位数，个位数变成10位数，num为n-2位数
    # 第三次得到百位数，变成个位数，个位数变成百位数，十位数从个位数变为十位数……
    num //= 10
print(reverse_num)
# 百钱百鸡问题用100元买100只鸡 公鸡5元 母鸡3元 小鸡1元三只
# x y z 最多买20只公鸡 33只母鸡
for x in range(0, 21):
    for y in range(0, 34):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡：%d\n母鸡:%d\n小鸡：%d' % (x, y, z))

# CRAPS赌博游戏：两个骰子
# 游戏规则放在循环主体部分：分为第一次摇骰子和继续摇骰子两个过程
# 游戏规则第一次点数之和为7或11 玩家胜 点数之和为2 3 12 庄家胜 其他点数继续
money = 1000
while money > 0:
    print('remaining money: %d' % money)
    needs_go_on = False
    # 标记
    while True:
        debt = int(input('please give your debt: '))
        if 0 < debt <= money:
            # 赌注小于赌本，否则需要重新下注
            break
    first = randint(1, 6) + randint(1, 6)
    print('your scores is: %d' % first)
    if first == 7 or first == 11:
        print('玩家胜')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜')
        money -= debt
    else:
        needs_go_on = True
    while needs_go_on:
        needs_go_on = False
        current = randint(1, 6) + randint(1, 6)
        print('your scores is: %d' % current)
        if current == first:
            print('玩家胜！')
            money += debt
        elif current == 7:
            print('庄家胜')
            money -= debt
        else:
            needs_go_on = True
print('你破产了，游戏结束！')

# 斐波那契数列
max = 20
a, b = 0, 1
number = 1
while number <= 20:
    a, b = b, a+b
    print('第%d的斐波那契数列为%d' % (number, a))
    number += 1

# 10000以内的完美数 真因子之和等于本身 1+2+3=6
for x in range(1, 10001):
    sum = 0
    for j in range(1, x):
        if x % j == 0:
            # i自身外的因子和
            sum += j
    if sum == x:
        print('%d是完美数!' % x)
# 素数
for x in range(2, 100):
    is_prime = True
    # 从2开始，从1开始无意义且必定能整除判断为非素数
    # 重点是写出循环终止条件
    for i in range(2, x):
        if x % i == 0:
            # range区间取值，不能大于一定值
            # 如果都是大于该数的一半就不能整除
            # 用小于根号x+1更快
            is_prime = False
            break
    if is_prime:
        print('%d is  prime' % x)
