'''
Author: your name
Date: 2021-08-21 18:11:56
LastEditTime: 2021-08-21 18:32:07
LastEditors: Please set LastEditors
Description: __name__
FilePath: \10_days\笔记\__name__.py
'''
# __name__
# 1、 直接运行代码文件,值为"__main__"
# 2、 作为代码文件名导入运行: 在__all__中调用,值为文件名
# 3、 可作为判断语句使用：作为模块被导入时，不会被执行if __name__ == "__main__"条件下的代码
# 每个模块中都有__name__变量，系统定义
# 自己定义的不要和系统定义的模块名


def add(a, b):
    print(a + b)


if __name__ == '__name':
    print(__name__)
# 在当前文件中输出__main__
# 作为模块导入其他文件时，输入此文件名__name

if __name__ == "__main__":
    # 在当前文件中执行
    add(10, 20)
    print(__name__)
