'''
Author: your name
Date: 2021-08-20 19:05:08
LastEditTime: 2021-08-20 19:28:11
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \10_days\笔记\私有权限.py
'''
# 私有权限： 在属性和方法前面加上两个下划线__name __play()
# 1、不能在类外部访问和使用，只能在类内部使用
# 2、不能通过继承使用
# 3、如果知道更换名字的规则仍然可以访问到:_类__属性方法


class People():
    def __init__(self, name):
        self.name = name
        self.__ICBC_money = 0

    def get_money(self):
        # 通过公有方法调用
        return self.__ICBC_money

    def set_money(self, money):
        # 通过公有方法存取钱
        self.__ICBC_money += money


xw = People("小王")  # 魔法属性__dict__查看属性星系
print("赋值之前", xw.__dict__)  # '_People__ICBC_money': 0 本质是通过更改属性名来更改属性类型
# xw.__ICBC_money = 1000  # 相当于添加了一个公有属性
# print(xw.ICBC_money)  # 可直接修改银行存的钱，显然不合理，定义为私有
print("赋值之后", xw.__dict__)  # '_People__ICBC_money': 0, '__ICBC_money': 1000
# print(xw.__ICBC_money)  # 'People' object has no attribute '__ICBC_money'
print(xw.get_money())
xw.set_money(1000)
print(xw.get_money())
xw.set_money(-500)
print(xw.get_money())


class Dog:
    def born(self):
        print("生了一只小狗……", end=',')
        self.__sleep()

    def __sleep(self):
        print("休息30天……")


dog = Dog()
# dog.sleep() # 改变了业务规则，直接休息，使用私有方法
dog.born()
