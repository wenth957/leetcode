# 组包：将多个数组组成元组，给到一个变量
a = 1, 2, 3
print(a)

# 拆包：将容器中的数据给到多个变量，数据个数和变量个数必须相等
# 元组、列表、字典、字符串均可
b, c, d = a
print(b)
print(c)
print(d)
e = [10, 20]
f, g = e
print(f, g, sep='\n')
# 字典得到key值
dict_1 = {0: 'a', 1: 'b'}
key_1, key_2 = dict_1
print(key_1, key_2)

# sum(*list) 将列表拆包后传递参数
# *dict 将key作为位置实参传递
# **dict 将value作为位置实参传递
