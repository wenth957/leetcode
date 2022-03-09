'''
Author: ML
Date: 2021-08-20 18:08:20
LastEditTime: 2021-08-20 18:29:57
LastEditors: Please set LastEditors
Description: 子类调用父类方法
FilePath: \10_days\笔记\子类调用父类方法.py
'''

# 通过对象调用方法不需要传递self实参值，python解释器会自动将对象传递给self
# 如果通过类名调用方法，python解释器不会自动传递实参，需要手动传递


class Dog:
    def bark(self):
        print("汪汪汪……")


class XTQ(Dog):
    def bark(self):
        print("嗷嗷嗷……")

    def see_host(self):
        print("看见主人了", end=',')
        # self.bark() # 看见主人了,嗷嗷嗷……
        # 调用父类方法
        # 一、父类名.方法名(self,其他参数)或父类名(实参).方法名()
        Dog.bark(self)

        # 二、super(当前类，self).方法名（参数）会调用当前类的父类方法
        super(XTQ, self).bark()

        # 三、方法二的简写
        super().bark()


xtq = XTQ()
xtq.bark()
xtq.see_host()
