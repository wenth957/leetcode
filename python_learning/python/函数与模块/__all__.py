'''
Author: your name
Date: 2021-08-21 17:56:46
LastEditTime: 2021-08-21 18:46:36
LastEditors: Please set LastEditors
Description： __all__
FilePath: \10_days\笔记\__all__.py
'''
# __all__只影响 from module import * 方式导入
# *方式只能导入__all__变量定义的内容可以是元组、列表
# 对于包python默认的__init__文件中可以通常定义__all__变量 规定哪些模块是 *方式导入


import __name
# 导入时直接运行py文件
__name.add(100, 200)
