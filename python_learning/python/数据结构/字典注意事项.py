# 字典的键 可以是 字符串和数值 不可变类型
# 1 和 1.0 是同一个键
# get(key) 有该键则返回值，没有则返回1
dict_1 = {'name': 'python', 'gender': 'nan'}
print(dict_1.get('nam', 1))
# del dict[key] 根据key删除
# dict.pop(key) 根据key删除，返回删除的值
# dict.clear() 删除所有的键值对
# del dict 删除这个变量

# 1、直接遍历字典得到的是key值
for key in dict_1:
    print(key, dict_1[key])

# 2、dict_1.keys
result = dict_1.keys()
print(result, type(result))
# 可迭代类型 可转化为列表

# 3、dict_1.values()
result = dict_1.values()
print(result, type(result))
# 可迭代类型 可转化为列表

# 4、dict_1.items()
result = dict_1.items()
print(result, type(result))  # 结果为元组构成的列表
# 可迭代类型 可转化为列表

# 拆包，将元组中的元素赋值给不同的遍历
for key, value in dict_1.items():
    print(key, value)
