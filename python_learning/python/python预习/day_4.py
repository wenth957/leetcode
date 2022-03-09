import random
from math import sqrt


'''
重复执行某些指令 循环语句for in 和 while
for-in明确知道循环次数或者对一个容器进行迭代
'''
sum = 0
for i in range(101):
    sum += i
print(sum)
'''
range 可理解为(左闭右开区间)三种用法
range(101)
range(1,101)
range(1,2,101)
range(101,-2,1)
'''
# 偶数求和
sum = 0
for i in range(101):
    if i % 2 == 0:
        sum += i
print(sum)
'''
while 不知道具体循环次数的循环结构
通过能够产生或者转化布尔值的表达来控制循环
表达式为True则继续循环表达式False则结束循环
'''

# 猜数字游戏
answer = random.randint(1, 100)
counter = 0
while True:
    number = int(input('please enter yoour guess: '))
    if number > answer:
        print('your number is bigger!')
    elif number < answer:
        print('your number is smaller!')
    else:
        print('Correct answer!')
        break
    counter += 1
    print('your guess numbers are %d' % counter)
if counter > 7:
    print('your IQ is dangerous!')

'''
# 用关键字break来终止循环，只能终止它所在的循环，在嵌套结构要注意，
# 还有一个关键字continue可以直接跳过后面的程序开始下一次循环
# 乘法口诀表
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = %d' % (i, j, i*j))
    print()
'''
# 素数
x = int(input('please enter a positive integer: '))
end = int(sqrt(x))
is_prime = True
for i in range(2, end + 1):
    # 从2开始，从1开始无意义且必定能整除判断为非素数
    # 重点是写出循环终止条件
    if x % i == 0:
        is_prime = False
        break
if is_prime and x != 1:
    print('%d is prime!' % x)
else:
    print('%d is not prime' % x)
# 最大公约数
x = int(input('please enter a positive integer: '))
y = int(input('please enter a positive integer: '))
u = min(x, y)
v = max(x, y)
approximate = 1
for i in range(1, u+1):
    if x % i == 0 and y % i == 0:
        if i > approximate:
            approximate = i
print('%d and %d max approximate number is %d ' % (x, y, approximate))
multiple = x*y
for i in range(v, multiple + 1):
    if i % x == 0 and i % y == 0:
        if i < multiple:
            multiple = i
print('%d and %d min common mutiple is %d ' % (x, y, multiple))
# 下面是教程里的答案
x = int(input('x = '))
y = int(input('y = '))
# 如果x大于y就交换x和y的值
if x > y:
    # 通过下面的操作将y的值赋给x, 将x的值赋给y，交换
    x, y = y, x
# 从两个数中较小的数开始做递减的循环，递减循环，代替了赋值
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        # 第一次碰到的公约数即为最大公约数
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        # 最小公倍数与最大公约数之间的关系
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break
# 打印三角图案(难)
row = int(input('please enter numbers of row'))
for i in range(row):
    for _ in range(i+1):
        print('*', end='')
    print()
# 先确定行数，在确定每一行元素放什么，空白处放空格
for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()
for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
        # 已经打印了空格接着打印*即可奇数表达方式
    for _ in range(2 * i+1):
        print('*', end='')
    print()
