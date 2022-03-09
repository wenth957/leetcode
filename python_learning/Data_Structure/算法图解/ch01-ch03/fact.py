def fact(x):
    '''函数的调用堆栈'''
    if x == 1:
        return x
    else:
        return x * fact(x - 1)


result = fact(3)
print(result)
