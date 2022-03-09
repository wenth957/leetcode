'''
Author: your name
Date: 2021-08-20 20:07:05
LastEditTime: 2021-08-20 20:15:12
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \10_days\笔记\多态.py
'''
# 需要使用父类对象的地方，也可以传入子类对象，得到不同的结果
# 不同子类重写父类后，得到不同的结果
# 实现步骤：1、子类继承父类 2、子类重写同名方法 3、定义一个共同的方法：参数为父类对象，并调用同名方法
# 好处：只需要传入不同实例对象即可返回不同结果


class Dog:
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f"小狗{self.name}在玩耍……")


class Xtq(Dog):
    def play(self):
        print(f"小狗{self.name}在天上追云海！")


def play_with_dog(obj_dog):
    obj_dog.play()


dog1 = Dog('大黄')
dog2 = Xtq("大黄")
play_with_dog(dog1)
play_with_dog(dog2)
