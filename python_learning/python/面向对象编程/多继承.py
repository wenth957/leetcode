'''
Author: your name
Date: 2021-08-20 18:47:04
LastEditTime: 2021-08-20 18:58:57
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \10_days\笔记\多继承.py
'''
# 多个父类，可以调用多个父类的属性和方法


class Dog:
    def bark(self):
        print("汪汪汪……")

    def eat(self):
        print("啃骨头……")


class God:
    def play(self):
        print("在天上飘一会……")

    def eat(self):
        print("吃仙丹妙药……")


class XTQ(Dog, God):
    def eat(self):
        print("子类重写了eat方法……")
        # 调用指定父类中的方法
        # 方法一 类名.方法名(self) 推荐使用
        Dog.eat(self)
        God.eat(self)
        # 方法二 super(类A，self).方法() 调用类A继承顺序链的下一个类中方法
        super(XTQ, self).eat()
        super(Dog, self).eat()

    pass


xtq = XTQ()
xtq.bark()
xtq.play()
xtq.eat()  # 啃骨头……,调用是第一个父类中的方法
# 类名.__mro__
# 可以查看当前类的继承顺序链，也叫做方法的调用顺序
print(XTQ.__mro__)  # 魔法属性
