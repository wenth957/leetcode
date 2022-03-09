'''
Author: your name
Date: 2021-08-20 19:59:07
LastEditTime: 2021-08-20 20:03:22
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \10_days\笔记\静态方法.py
'''
# 使用@staticmethod装饰
# 使用情况：不需要使用实例属性也不需要使用类属性


class Dog(object):
    class_name = "狗类"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def play(self):
        print(f"{self.name}正在玩耍！")

    @classmethod
    def get_class_name(cls):
        return cls.class_name

    @staticmethod
    def show_info():  # 无默认参数
        print("这是一个狗类！")


dog = Dog("大黄", 2)
Dog.show_info()  # 直接通过类调用
dog.show_info()  # 通过实例调用
