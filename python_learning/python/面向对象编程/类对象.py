'''
Author: your name
Date: 2021-08-20 19:33:27
LastEditTime: 2021-08-20 19:48:52
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \10_days\笔记\类对象.py
'''
# 对象(实例对象)：通过class定义的类创建的
# 类（类对象）：通过class定义的类 类对象：1、通过实例化定义实例对象 2、保存一些属性信息，称为类属性
# 类属性：在类内部，方法外部内定的变量就是类属性，方法内部的是局部变量
# 实例属性：每个实例都存在一份，不同实例值可能是不一样的
# 类属性：在内存中只有一份
# 如何分辨？：对于不同实例中是否值相同，并且同时变化？ 如果是，则定义为类属性；否则为实例属性


class Dog:
    class_name = "狗类"

    def __init__(self, name, age):
        self.name = name
        self.age = age


dog = Dog("大黄", 1)
print(dog.__dict__)  # 查看实例的属性
print(Dog.__dict__)  # 查看类的属性
print(Dog.class_name)
print(dog.class_name)
# 如果不存在和实例属性重名的类属性 则可以通过实例访问类属性
# 如果存在重名，则访问的一定是实例属性
# 修改则只能通过类
