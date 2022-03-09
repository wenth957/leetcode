# 递归：函数自己嵌套调用自己
# 序列有规律
# 递：从前到后 找规律
# 归：从后到前 某个值已知
# 递归函数形成条件：（1）自己调用自己 （2）终止条件


def get_age(n):
    """
    求第i个人的年龄相邻两个人差两岁
    :param n
    :return:
    """
    if n == 1:  # 4-3-2-1
        return 18
    # 求第n个人的年龄，只需前一个人的年龄+2
    age = get_age(n - 1) + 2  # get(get(get(18))) ->get(get(20))->24
    return age


print(get_age(4))
