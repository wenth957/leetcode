# 只能被1和自身整除
# 从2开始整除 直到该数字-1
# 如果有一个能整除该数，则输出

num = int(input("please enter your number:"))
if num == 1 or num == 0:
    print("既不是素数也不是合数")
else:
    for i in range(2, num):
        if num % 2 != 0:
            print('it is a 素数！')
            break
        else:
            pass
    else:
        print("it is not a 素数！")
