# -*- Coding: UTF-8 -*-
# 07 数据类型.py
# @作者
# @创建日期 2021-01-30T17:13:10.756Z+08:00
# @最后修改日期 2021-08-07T12:12:03.631Z+08:00

import sys
import os
import time
import random
from random import randint, sample


# 字符串
# 0个或多个字符组成的有限序列
s1 = 'hello world'
s2 = "hello world"
s3 = '''
hello
world!
'''
print(s1, s2, s3, end='')
# 输出在一行中间空格，end中字符只加在输入末尾
# \表示转义即后面加字符不是本意\n换行\t制表\'表示字符串中的'\\表示字符串
# 中的\
s1 = '\'hello,world!\''
s2 = '\n\\hello,world!\\\n'
print(s1, s2, end='')
# \后面跟一个八进制或者十六进制来表示字符如\141和\x61表示小写字母a
# \后面加unicode编码 \u94c0
s1 = '\141\142\143\x61\x62\x63'
s2 = '\u94c0'
print(s1, s2, end='')
# 如果不希望字符串中的\表示转义，前面加r
s1 = r'\'hello world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')
# +实现字符串的拼接 *重复字符串的内容 in，not in判断是否包含
# []取出某个字符 [:]切片
s1 = 'hello' * 3
print(s1)
s2 = 'world!'
s1 += s2
print(s1)
print('ll' in s1)
print('good' in s1)
str2 = 'abc123456'
print(str2[2])
print(str2[2:5])
print(str2[2:])
print(str2[2::2])
# 第二个：后面是间隔长度
print(str2[::2])
print(str2[::-1])
print(str2[-3:-1])
# 开区间
str1 = 'hello world!'
print(len(str1))
print(str1.capitalize())
# 获得字符串首字母大写的拷贝
print(str1.title())
# 获得字符串每个单词首字母大写
print(str1.upper())
# 所有字符串都大写
print(str1.lower)
print(str1.find('or'))
# 寻找字符串的位置（中间有个空格返回7）
print(str1.find('shit'))
# 没有对应字符会返回-1
print(str1.index('or'))
# print(str1.index('shit')) 会引发错误
print(str1.startswith('He'))
print(str1.startswith('hel'))
# starts with检验是否以某个字符开头
print(str1.endswith('Ld'))
print(str1.endswith('orld!'))
print(str1.center(50, '*'))
# 将字符串指定宽度居中，两边用*填充
print(str1.rjust(50, ' '))
# 将字符串指定宽度右侧停靠，左边用空格填充
str2 = 'abc123456'
print(str2.isdigit())
# 是否由数字构成
print(str2.isalpha())
# 是否由字母构成
print(str2.isalnum())
# 是否以字母和数字构成
str3 = ' wangpeiwen@126.com '
print(str3)
print(str3.strip())
# 获得字符串修剪两侧空格之后的拷贝
# 格式化字符串
a, b = 5, 10
print('%d * %d = %d' % (a, b, a * b))
print('{0} * {1}= {2}'.format(a, b, a * b))
print(f'{a} * {b} = {a * b}')
# 一般使用第一种和第三种注意format简写放字符串前面然后用大括号


# 列表：可变类型
# 有序序列
# 查找
# 有index操作 count操作 最小单元是字符串 数字等
# in/not in 判断存不存在

# 索引、遍历、修改
list1 = [1, 3, 5, 7, 100]
list2 = ['hello!'] * 3
print(list2)
print(len(list1))
print(list1[0])
print(list1[4])
print(list1[-1])
print(list1[-3])
list1[2] = 3
# 列表遍历
print(list1)
for index in range(len(list1)):
    print(list1[index])
for value in list1:
    print(value)
for index, value in enumerate(list1):
    print(index, value)
# 通过enumerate（枚举）函数处理列表后再遍历可以同时获得列表索引和值

# 向列表添加元素
result = list1.append(200)
# print(result)  返回结果为None，直接在原列表上修改
list1.insert(1, 400)
# insert(index, object)  # 在索引index处插入
list1.extend([2020, 2021])  # 可迭代对象元素逐个添加到末尾
# 延长列表，合并
# list1 += [2020, 2021]
print(list1)

# 列表删除
# remove 根据值删除
if 3 in list1:
    list1.remove(3)
    print(list1)
# 只能移除一个3
if 1234 in list1:
    list1.remove(1234)
print(list1)

# pop 根据索引删除 默认删除最后一个
list1.pop(0)  # 返回删除的值
print(list1)
# 删除第1个元素
list1.pop(len(list1) - 1)
# 删除最后一个元素
print(list1)

# del list[] 根据索引删除
del list1[0]
print(list1)

# remove移除特定元素 pop移除指定位置函数 del删除指定位置
# append放在末尾 insert 插入指定位置 []修改指定位置 extend延长

# 列表切片复制
fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
fruits2 = fruits[1:4]
print(fruits2)
fruits3 = fruits[:]
fruits4 = fruits[-3:-1]
fruits5 = fruits[::-1]  # 逆序
fruits.reverse()  # 原列表上操作
print(fruits3)
print(fruits4)
print(fruits5)

# 列表排序 数据类型一致

list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
# sort对原列表进行操作
list1.sort(reverse=True)  # 对原列表进行操作

# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 按首字母正向排序
list2 = sorted(list1)
# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 按首字母正向排序
list3 = sorted(list1, reverse=True)
# 字符串按首字母反向排序
list4 = sorted(list1, key=len)
# 按长度排序
print(list1)
print(list2)
print(list3)
print(list4)

# 生成式和生成器
f = [x for x in range(1, 10)]
print(f)
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)
# 这就是列表的生成表达式创建列表容器
f = [x ** 2 for x in range(1, 1000)]
print(sys.getsizeof(f))
# 查看对象占用的内存
# print(f)
# 下面的代码创建一个生成器对象
# 通过生成器可以获取数据但不占用额外的内存
# 每次需要数据通过内部运算获得
f = (x ** 2 for x in range(1, 1000))
print(sys.getsizeof(f))
# 88
# print(f)
# for val in f:
# print(val)
# 需要时间获得数据
# 内存：字节由8个位构成代表数字和字母
# 9024bytes与88bytes
# yield关键字可以将一个普通函数改造成生成器


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()


# 元组
# 定义元组
t = ()  # 没有意义
t = (3)  # 这是一个整型
t = (3,)  # 必须加逗号才是元组
t = ('王培文', 25, True, '四川成都')
print(t)
# 获取元组中的元素
print(t[3])
# 遍历元组
for num in t:
    print(num)
# 修改
# t[0] = '王大锤' 类型错误元组不可修改
# 造一个新的元组,原来元组被垃圾回收
t = ('王大锤', 25, True, '四川成都')
print(t)
# 将元组转化为列表
person = list(t)
print(person)
# 修改列表元素
person[0] = '李小龙'
person[1] = 25
print(person)
# 将列表转化为元组
fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)


# 既然有了列表为什么还要tuple
# 多线程环境，不变对象更加容易维护、安全
# 元组在时间和空间上都优于列表
print(sys.getsizeof(person))  # 120
print(sys.getsizeof(fruits_tuple))  # 72


# 集合：无重复元素
# 创建集合的字面语法类似数学
set1 = {1, 2, 3, 3, 3, 2}
print(set1)
print('length = ', len(set1))
# 创建集合的构造器语法
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)
# 创建集合的推导式语法
set4 = {
    num for num in range(1, 100)
    if num % 3 == 0 or num % 5 == 0
    }
print(set4)
# 集合的交、并、差、对称差
print(set1 & set2)
# print(set1.intersection(set2))
print(set1 | set2)
# print(set1.union(set2))
print(set1 - set2)
# print(set1.difference(set2))
print(set1 ^ set2)
# print(set1.symmetric_difference(set2))
# 判断子集和超集
print(set2 <= set1)
print(set2.issubset(set1))
print(set3 <= set1)
print(set3.issubset(set1))
print(set1 >= set2)
print(set1.issuperset(set2))
print(set1 >= set3)
print(set1.issuperset(set3))


# 字典
# 创建字典的字面量语法
scores = {'王培文': 91, '李元芳': 78, '狄仁杰': 82}
print(scores)
# 创建字典的构造器语法
items1 = dict(one=1, two=2, three=3, four=4)
# 通过zip函数压缩两个序列成字典
# zip传入多个序列对应元素压缩成元组返回
items2 = dict(zip(['a', 'b', 'c'], '123'))
# 创建字典的推导式语法
items3 = {num: num ** 2 for num in range(1, 10)}
print(items1)
print(items2)
print(items3)
# 字典可以通过键获取对应的值
print(scores['王培文'])
# 对字典中的键值进行遍历
# 遍历得到的是键
for key in scores:
    print(f'{key}:{scores[key]}')
# 第一种方法最简单
for key in scores.keys():
    print(key)
for value in scores.values():
    print(value)
for key, value in scores.items():
    print(f'{key}:{value}')
# 更新字典中的元素
scores['李元芳'] = 65
scores['诸葛元康'] = 71
scores.update(冷漠=67, 王启蒙=85)
print(scores)
if '武则天' in scores:
    print(scores['武则天'])
print(scores.get('武则天', 60))
# get 也是通过键获取对应的值
# 删除字典中的元素
print(scores.popitem())
print(scores.popitem())
print(scores.pop('王培文', 20))
print(scores)
# 清空字典
scores.clear
print(scores)


def main():
    # 在屏幕上显示跑马灯文字
    content = '北京欢迎您为您开天辟地!'
    while True:
        os.system('cls')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]


def get_code(len_code=4):
    code_str = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    len_str = len(code_str)
    code = ''
    for i in range(len_code):
        index = random.randint(0, len_str-1)
        code += code_str[index]
    return code


def get_suffix(filename, has_dot=False):
    '''
    获取文件你的后缀名
    has_dot 返回的后缀名是否带点
    寻找小数点位置
    '''
    pos = filename.rfind('.')
    if 0 <= pos < len(filename)-1:
        # 如果在中间
        if has_dot:
            index = pos
        else:
            index = pos + 1
        return filename[index:]
    else:
        return ''


def max1_2(list):
    #
    if list[0] > list[1]:
        m1, m2 = list[0], list[1]
    else:
        m1, m2 = list[1], list[0]
    for index in range(2, len(list)):
        if list[index] > m1:
            m2 = m1
            m1 = list[index]
        elif list[index] > m2:
            m2 = list[index]
    return m1, m2


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


def which_day(year, month, date):
    '''传入年月日判断是一年中的第几天
    从一个月开始累加计算'''
    days_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        ][is_leap_year(year)]
    # 返回1索引1，返回0变成索引0即第一行
    print(days_month)
    total = 0
    for index in range(month-1):
        total += days_month[index]
    return total + date


def yhthree():
    num = int(input('please enter the number of row: '))
    yht = [[]] * num
    for row in range(num):
        yht[row] = [None] * (row+1)
        for col in range(len(yht[row])):
            if col == 0 or col == row:
                yht[row][col] = 1
            else:
                yht[row][col] = yht[row-1][col] + yht[row-1][col-1]
            print(yht[row][col], end='\t')
        print()


'''
if __name__ == '__main__':
    # main()
    code = get_code()
    print(code)
    print(get_suffix('.txt'))
    print(max1_2([1, 2, 3, 45, 6, 5, 4]))
    print(which_day(2021, 1, 31))
    yhthree()
'''


def display(balls):
    # 单个输出列表中的双色球号码
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')


def random_select():
    # 随机选一组号码
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


def main1():
    n = int(input('机选几注：'))
    for _ in range(n):
        display(random_select())


def main2():
    persons = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
        # 会使索引大于30所以取余
    for person in persons:
        print('基' if person else '非', end='')
# ＃字棋游戏


def main():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        os.system('clear')
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s走棋，请输入位置： ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('cls')
            print_board(curr_board)
        chioce = input('再玩一局？（yes|no）')
        begin = chioce == 'yes'


def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])


if __name__ == '__main__':
    # main1()
    # main2()
    main()
