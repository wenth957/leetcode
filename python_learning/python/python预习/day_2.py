'''
计算机硬件系统：运算器、控制器、存储器、输入、输出
程序送到前两个即CPU执行指令，存储要和CPU分开、二进制
程序运行需要将其放入到内存中
变量是存储数据的载体，存储器中的一块内存空间，代表内存地址
变量类型：整型、浮点型、字符串、布尔、复数
变量命名（标识符）：PEP 8 小写字母下划线连接 实例用下划线开头
关键字：python已经命名的标识符，不能重复命名
type 函数检查变量类型
'''
a = 100
b = 100.0001
c = 'helloworld'
d = True
e = 1 + 2j
print(type(a))  # 两个空格再加注释
print(type(b))  # 先对括号里面的进行函数运算
print(type(c))
print(type(d))
print(type(e))
'''
可以使用python内置函数进行转换变量类型
chr 将整数转化成该编码对应的字符
ord返回一个字符的编码：整数
'''
print(int(b))

print(chr(a))

print(ord('i'))
'''
使用input()自己输入来进行运算，碰到回车结束
input结果是字符串用int()转变为整数
用print()输出带占位符的字符串
'''
'''
a = input('a = ')
b = input('b = ')
a = int(a)
b = int(b)
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
# 占位符后面的变量值会替换掉占位符，这些变量要括起来，元组
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
# // 取整 % 取余
'''
''' 一些常见运算符
[] [:] 下标、切片
** 指数 ~ 按位取反
>>右移 <<左移 & ^ | 按位与、异或、或
== 等于 !=不等于
比较运算符> < 会产生布尔值 与逻辑运算符连用
身份运算符 is is not
成员运算符 in not in
逻辑运算符 not or and
and 两边都对才是1 or任意一个对就是1
赋值运算符 =
复合赋值运算符 += -= *= /= %= //= **=
'''
# 复合赋值
a = 10
b = 3
a += b
print(a)
a *= b
print(a)
# 比较与逻辑
flag_0 = 1 == 1
flag_1 = 3 > 2
flag_2 = 2 < 1
flag_3 = flag_1 and flag_2
flag_4 = flag_1 or flag_2
flag_5 = not (1 != 2)
print('flag_0=', flag_0)
print('flag_1=', flag_1)
print('flag_2', flag_2)
print('flag_3', flag_3)
print('flag_4', flag_4)
print('flag_5', flag_5)
# 比较运算符优先于赋值运算符，所以先做右边==><运算然后赋值给左边
# print可任意输出多个值
print('flag_0 flag_1 flag_2 flag_3 flag_4 flag_5\n', flag_0, flag_1, flag_2,
      flag_3, flag_4, flag_5)
# 华氏温度和摄氏温度的转化
F = input('please enter F temperature:')
F = float(F)
C = (F - 32) / 1.8
print('C temperature is %.1f' % C)
# 也可以用下面这种占位符
print(F'{F:.1f}华氏度 = {C:.1f}摄氏度')
# 计算圆的周长和面积
radius = float(input('please enter radius:'))
perimeter = 2 * 3.1415926 * radius
area = 3.1415926 * radius**2
print('perimeter:%.2f' % perimeter)
print('area:%.2f' % area)
# 判断年份是不是闰年
year = int(input('please input year:'))
flag_0 = year/4 == 0 and year/100 != 0 or \
    year/400 == 0
print(flag_0)
