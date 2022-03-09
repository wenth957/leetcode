# lambda 形参1 形参2 :表达式或函数调用
# 不能使用条件循环
# 不需要写return


def calc_num(a, b, func):
    """四则运算
    params: a first num;b seconde num;func
    """
    print("其他的代码pass")
    num = func(a, b)
    print(num)


def add(a, b):
    return a + b


calc_num(3, 4, add)
calc_num(3, 4, lambda a, b: a - b)
calc_num(3, 4, lambda a, b: a * b)
calc_num(3, 4, lambda a, b: a / b)
