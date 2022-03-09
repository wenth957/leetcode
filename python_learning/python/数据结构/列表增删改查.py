# 列表：可变类型
# 有序序列
# 查找
# 有index操作 count操作 最小单元是字符串 数字等
# in/not in 判断存不存在

# 索引、遍历、修改
list1 = [1, 3, 5, 7, 100]
list2 = ['hello!'] * 3
print(list2)
print(len(list1))
print(list1[0])
print(list1[4])
print(list1[-1])
print(list1[-3])
list1[2] = 3
# 列表遍历
print(list1)
for index in range(len(list1)):
    print(list1[index])
for value in list1:
    print(value)
for index, value in enumerate(list1):
    print(index, value)
# 通过enumerate（枚举）函数处理列表后再遍历可以同时获得列表索引和值

# 向列表添加元素
result = list1.append(200)
# print(result)  返回结果为None，直接在原列表上修改
list1.insert(1, 400)
# insert(index, object)  # 在索引index处插入
list1.extend([2020, 2021])  # 可迭代对象元素逐个添加到末尾
# 延长列表，合并
# list1 += [2020, 2021]
print(list1)

# 列表删除
# remove 根据值删除
if 3 in list1:
    list1.remove(3)
    print(list1)
# 只能移除一个3
if 1234 in list1:
    list1.remove(1234)
print(list1)

# pop 根据索引删除 默认删除最后一个
list1.pop(0)  # 返回删除的值
print(list1)
# 删除第1个元素
list1.pop(len(list1) - 1)
# 删除最后一个元素
print(list1)

# del list[] 根据索引删除
del list1[0]
print(list1)

# remove移除特定元素 pop移除指定位置函数 del删除指定位置
# append放在末尾 insert 插入指定位置 []修改指定位置 extend延长

# 列表切片复制
fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
fruits2 = fruits[1:4]
print(fruits2)
fruits3 = fruits[:]
fruits4 = fruits[-3:-1]
fruits5 = fruits[::-1]  # 逆序
fruits.reverse()  # 原列表上操作
print(fruits3)
print(fruits4)
print(fruits5)

# 列表排序 数据类型一致

list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
# sort对原列表进行操作
list1.sort(reverse=True)  # 对原列表进行操作

# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 按首字母正向排序
list2 = sorted(list1)
# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 按首字母正向排序
list3 = sorted(list1, reverse=True)
# 字符串按首字母反向排序
list4 = sorted(list1, key=len)
# 按长度排序
print(list1)
print(list2)
print(list3)
print(list4)
