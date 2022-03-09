my_str = "hello world"
print(my_str.capitalize())  # 句子首字母
print(my_str.title())  # 全部首字母
print(my_str.upper())  # 全部大写
print(my_str.lower())  # 全部小写
print(my_str.startswith('hello'))  # 是否以hello开头
print(my_str.center(64))  # 以特定字节居中
print(my_str.ljust(64))  # 左对齐
print(my_str.rjust(64))  # 右对齐
space_str = " hello world "
print(space_str.lstrip())  # 去掉字符串左边空格
print(space_str.rstrip())  # 去掉字符串右边空格
print(space_str.strip())  # 去掉两边字符串
num_str = '1234'
str_str = 'hello'
print(str_str.isalpha())  # 只有字母组成 不包含空格
print(num_str.isdigit())
print(space_str.isspace())  # 是否只包含空格
