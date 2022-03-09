# enumerate 将可迭代序列中的  元素的下标和值 组合在一块编程元组
# 用于列表元组和字符串
list_1 = ['a', 'b', 'c', 'd', 'e']
# 遍历的同时想要获得索引
for i in list_1:
    print(list_1.index(i), i)

print("函数实现+++++++++++")

for i, value in enumerate(list_1):
    print(i, value)
