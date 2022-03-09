from random import randint

# 函数和模块 x1+x2+x3+x4=8 有多少正整数解 C7_3
# 将苹果分为4组，每组至少有一个苹果，3个隔板插7个空位
# 输入m,n计算Cm_n  m!//n!(m-n)！
'''
for i in range(1, m+1):
    f_m *= i
f_n = 1
for j in range(1, n+1):
    f_n *= j
fm_n = 1
for x in range(1, m - n + 1):
    fm_n *= x
answer = f_m//f_n//fm_n
除法运算返回的是float类型
print('answer is %d' % answer)
'''
# 利用函数对上述程序重构


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def roll_dice(n):
    result = 0
    for _ in range(n):
        result += randint(1, 6)
    return result


# print(roll_dice(3))


def add(*args):
    '''当不知道参数个数时用可变参数'''
    sum = 0
    for value in args:
        sum += value
    return sum


#   普通参数+ 缺省参数 定义函数时缺省参数要卸载普通参数后面
#   位置参数 +关键字参数 关键字参数必须在位置参数后面
#   *形参变为不定长的元组形参，可以接受所有的位置实参
#  **形参变为不定长的字典形参，可以接受所有的关键字实参
#   顺序：普通参数 不定长元组形参 缺省参数 不定长字典形参（字典放在最后即可）
# 如果缺省参数在前面，当不输入时，不定长元组形参会修改原来的参数。


def func(*args, **kwargs):
    print(*args)
    print(**kwargs)


# print(add(1, 2, 3, 4, 5, 6, 7))
# python 没有函数重载的概念，所以定义同一个名字的函数，新的会覆盖旧的
# 如何解决：放入两个模块
# 如果在模块中有可执行的代码，调用时就会执行见test.py
# 如何解决： if __name__ == '__main__'
# 只有直接执行的模块名字才是main

# def foo():
# print('hello world!')


def foo():
    print('goodbye world!')


# foo()


def calc_approxi_common(m, n):
    '''最大公约数和最小公倍数的函数'''
    x = min(m, n)
    for i in range(x, 0, -1):
        if m % i == 0 and n % i == 0:
            approxi = i
            multiple = m * n // i
            break
    return approxi, multiple


def reverse_number(num):
    total = 0
    # 要保留最初的num值 ,将值赋给另一个变量
    n = num
    while n > 0:
        total = total * 10 + n % 10
        n //= 10
    # 最后返回比较运算即是否正确
    return total == num


def prime(x):
    is_prime = True
    for i in range(2, x):
        # range(2,2)返回一个空迭代器，并不会执行
        # range(2,1)返回2 1%2是1
        if x % i == 0:
            is_prime = False
            print('%d is not prime!' % x)
            break
    if is_prime and x != 1:
        print('%d is prime!' % x)


# 另一种方法
# for  else结构  else 当循环不是被break终止的时候才会执行


def prime_reverse(num):
    n = num
    total = 0
    while n > 0:
        total = total * 10 + n % 10
        n //= 10
    if total == num:
        is_prime = True
        # 设置关键字
        for i in range(2, num):
            if num % i == 0:
                print('not prime')
                is_prime = False
                break
        if is_prime and num != 1:
            print('%d is reverse_prime' % num)
    else:
        print('%d is not reverse' % num)


# 变量作用域


def zoo():
    b = 'hello'

    def bar():
        '''可以在函数中定义函数'''
        c = True
        # print(a)
        print(b)
        print(c)

    bar()
    # print(c) /name 'c' is not defined 局部变量不能函数外使用


def yoo():
    a = 200
    print(a)


def xoo():
    global a  # 可以改变全局变量的值
    a = 200
    print(a)


if __name__ == '__main__':
    m = int(input('please enter the value of m: '))
    n = int(input('please enter the value of n: '))
    f_m = factorial(m)
    f_n = factorial(n)
    fm_n = factorial(m - n)
    answer = f_m // f_n // fm_n
    print('answer is %d' % answer)
    r1, r2 = calc_approxi_common(12, 24)
    print('最大公约数和最小公倍数分别为:%d,%d' % (r1, r2))
    print(reverse_number(12321))
    prime(111)
    prime_reverse(787)
    zoo()
    yoo()
    # print(a)
    xoo()
    print(a)
'''
原函数中没有a的值但是函数外给出是可以在函数中使用的（全局变量）
 print(b)/name 'b' is not defined
函数外即使调用了函数也不能使用函数内的变量（局部变量）
b属于嵌套作用域
python 查找一个变量按照 局部、嵌套、全局、内置顺序搜索
内置作用域如input、print、int
例如yoo()函数输出结果仍然是函数内的a，因为函数首先查找局部变量
同理print(a)输出结果是100函数并没有对全局a=100做修改
如果想用函数改变全局变量a的值则如函数xoo()
如果全局作用域中没有a那么就会出现一行代码与a有关
同理对于嵌套作用域可以用 nonlocal来实现
在实际开发中要减少对全局变量的使用
标准python代码形式：
def main():
    pass


if __name__ == '__main__':
    main()
'''
