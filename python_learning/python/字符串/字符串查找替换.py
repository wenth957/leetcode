'''
Author: your name
Date: 2021-08-09 02:22:36
LastEditTime: 2021-08-23 00:09:20
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \10_days\python\字符串\字符串查找替换.py
'''
# find(sub_str,start,end) rfind
# 返回sub_str在str中的位置 只返回第一次找到词的第一个字母的下表
# index rindex 函数基本一致，区别是index找不到会报错
# count 统计字符串中出现特定字符的次数
# my_str.replace(old_str,new_str,count) 字符串替换

# find
my_str = 'hello world! you are foolish! you!'
index = my_str.find('hello')
print(index)  # 返回0 第一次找到的字母
print(my_str[index:index + 5])  # 返回某个词开始的固定长度的内容
index = my_str.find('hello', 2, 4)  # 未找到
print(index)  # 没有找到返回-1
index = my_str.find('you')
print(index)  # 13 空格也算
index = my_str.rfind('you')
print(index)  # 30 从右边开始查找

# index
index = my_str.index('hello')
print(index)  # 返回0 第一次找到的字母
# index = my_str.index('hello', 2, 4)
# print(index)  # 代码错误substring not found
index = my_str.index('you')
print(index)  # 13 空格也算
index = my_str.rindex('you')
print(index)  # 30 从右边开始查找

# count：统计字符串中出现特定字符的次数
print(my_str.count('aaaa'))
print(my_str.count('hello'))
print(my_str.count('you'))
print(my_str.count('you', 20))

# my_str.replace(old_str,new_str,count)
# count替换次数，默认全部替换
my_str = 'hello world hello python'
my_str1 = my_str.replace('hello', 'we are')
print(my_str1)
my_str2 = my_str.replace('hello', 'we are', 1)
print(my_str2)
