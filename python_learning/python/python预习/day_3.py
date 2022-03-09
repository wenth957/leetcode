# 分支结构if-elif-else语句
# 用户身份验证
username = input('please enter your username: ')
password = input('please enter your password: ')
if username == 'admin' and password == '1234':
    print('Correct!')
else:
    print('Failed')
'''
分段函数求值
    3x-5 x>1
f(x)=  x+2 -1=<x<=1
    5x+3 x<-1
'''
x = float(input('please enter value of x: '))
if x > 1.0:
    print('f(x): ', 3 * x - 5)
elif x >= -1.0 and x < 1.0:  # 判断条件1已经不成立
    print('f(x): ', x + 2)
else:  # 判断条件1、2 均不成立
    print('f(x): ', 5 * x + 3)
# 可以计算f(x)的值，最后输出一条print语句
# 分支结构的嵌套: 类似二叉树
x = float(input('please enter value of x: '))
if x > 1.0:  # 第一个规则
    y = 3 * x - 5
else:
    if x < -1.0:  # 第二个规则
        y = 5 * x + 3
    else:
        y = x + 2
print('f(%.2f) = %.2f ' % (x, y))
# 扁平化比嵌套结构更可读
# 英寸和厘米的互相转化
value = float(input('please enter length: '))
unit = input('please enter your unit: ')
if unit == 'in' or unit == '英寸':
    unit = 'cm'
    print('%.2fin = %.2fcm:' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    unit = 'in'
    print('%.2fcm = %.2fin' % (value, value / 2.54))
else:
    print('error unit!\nplease enter new unit: ')
# 百分制转化为等级制成绩
scores = int(input('please speak your grade: '))
if scores >= 90:
    grade = 'A'
elif scores >= 80 and scores < 90:
    grade = 'B'
elif scores >= 70 and scores < 80:
    grade = 'C'
elif scores >= 60 and scores < 70:
    grade = 'D'
else:
    grade = 'E'
print('your scores:%d = grade:%s' % (scores, grade))
# 输入三条边长，如果能构成三角形，计算周长和面积
a = float(input("please enter the first line's length:"))
b = float(input("please enter the second line's length:"))
c = float(input("please enter the third line's length:"))
if a + b > c and a + c > b and b + c > a:
    perimeter = a + b + c
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c))**0.5
    # 海伦公式
    print('perimeter is %.2f\n area is %.2f' % (perimeter, area))
else:
    print('a, b ,c is error value!')
