'''
使用input()自己输入来进行运算，碰到回车结束
input结果是字符串用int()转变为整数
用print()输出带占位符的字符串
'''
a = input('a = ')
b = input('b = ')
a = int(a)
b = int(b)
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
