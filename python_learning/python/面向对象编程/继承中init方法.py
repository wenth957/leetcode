'''
Author: ML
Date: 2021-08-20 18:35:30
LastEditTime: 2021-08-20 18:44:17
LastEditors: Please set LastEditors
Description: 继承中init方法
FilePath: \10_days\笔记\继承中init方法.py
'''
# 子类重写了__init__方法 默认不再调用父类的init方法
# 需要手动调用


class Dog:
    def __init__(self, name):
        self.name = name
        self.age = 0

    def __str__(self):
        return f"姓名为{self.name},年龄为{self.age}"


class XTQ(Dog):
    def __init__(self, name, color):
        # 子类重写了__init__方法 默认不再调用父类的init方法，需要手动调用
        super().__init__(name)  # 手动调用父类，传入父类所需的参数
        self.color = color

    def __str__(self):
        return f"名字为{self.name},年龄为{self.age},颜色为{self.color}"


xtq = XTQ('小黑', 'black')
print(xtq)
