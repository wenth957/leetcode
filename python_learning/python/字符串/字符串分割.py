my_str = 'hello word hello python'

# my_str.split(sub_str,count)  # 按照sub_str进行切割
# sub_str 切割字符 默认切割方式 空格 \t
# count 切割次数，遇到sub_str进行一次切割 默认全部切割
# 返回值列表
my_list = my_str.split()
print(my_list)
print(my_str.split('hello'))
print(my_str.split('hello', 1))  # 从左边开始切割
print(my_str.rsplit('hello', 1))  # 从右边开始切割
