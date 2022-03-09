def countdown(i):
    '''递归思想：倒计时'''
    print(i)
    if i <= 1:
        return
    else:
        countdown(i - 1)


countdown(10)
