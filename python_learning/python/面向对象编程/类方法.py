'''
Author: your name
Date: 2021-08-20 19:52:17
LastEditTime: 2021-08-20 20:02:28
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \10_days\笔记\类方法.py
'''
# @classmethod装饰的方法 第一个参数cls,类似self
# 1、方法中要使用实例属性，则使用实例方法
# 2、不需要使用实例属性，则可以定义为类方法


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


dog = Dog("大黄", 2)
print(dog.get_class_name())
print(Dog.get_class_name())
