# 集合：无重复元素，元素必须是不可变类型，字典中的key也是，但是集合是可变类型
# 不可变类型是可哈希的，可变类型是不可哈希的
# 创建集合的字面语法类似数学
# 集合是无序的，不能使用下标操作
set1 = {1, 2, 3, 3, 3, 2}
print(set1)
print('length = ', len(set1))
# 创建集合的构造器语法
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)
# 创建集合的推导式语法
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
print(set4)
# 集合的交、并、差、对称差
print(set1 & set2)
# print(set1.intersection(set2))
print(set1 | set2)
# print(set1.union(set2))
print(set1 - set2)
# print(set1.difference(set2))
print(set1 ^ set2)  # set2-se1
# print(set1.symmetric_difference(set2))

# 判断子集和超集
print(set2 <= set1)
print(set2.issubset(set1))
print(set3 <= set1)
print(set3.issubset(set1))
print(set1 >= set2)
print(set1.issuperset(set2))
print(set1 >= set3)
print(set1.issuperset(set3))
