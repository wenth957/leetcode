'''
把一组数据结构和处理它们的方法组成(对象)
把相同行为的对象封装为(类)
对象是类的实例
类是对象的蓝图和模板
通过类的(封装)隐藏内部细节
通过(继承)实现类的特化和泛化
通过(多态)实现基于对象类型的动态分派
对象具有属性（静态特征）和行为方法（动态特征）
抽取出来就是一个类
'''
from time import sleep
from math import sqrt


class student(object):

    # 定义类
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s 正在学习 %s.' % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s 只能看熊出没。' % self.name)
        else:
            print('%s 正在看暴力血腥。' % self.name)


def main():
    # 创建对象并指定姓名和年龄
    stu1 = student('wang peiwen', 25)
    # 给对象发study信息
    stu1.study('python100天从入门到大师')
    stu1.watch_movie()
    stu2 = student('liu xing', 12)
    stu2.study('思想品德')
    stu2.watch_movie()


if __name__ == '__main__':
    main()
'''
'''访问可见性问题
在很多面向对象编程中，通常会将对象的属性设为私有的，但方法是公开的
如果希望属性是私有的，那么命名时可以用两个下划线开头
无下划线公有，下面时测试代码
'''

'''


class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    test.__bar()
    print(test.__foo)


if __name__ == '__main__':
    main()
'''
# 只是更换名字来妨碍对他们的访问，如果知道更换名字的规则仍然可以访问到

'''


class Test():

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)
    # 类前加_属性方法前加__即可访问


if __name__ == '__main__':
    main()
'''
# 通常将属性设置为公有在前面加_外界仍可访问，只是一种提示
# 封装 隐藏一切可以隐藏的实现细节，只向外界暴露简单的编程接口
# 如对方法的定义。即使把对数据的操作封装起来
# 我们只需要给对象发送一个消息就可以执行方法中的代码
# 即只需要知道方法名字和参数（外部视图）
# 不需要知道方法的内部实现细节（内部试图）
'''


class Clock(object):
    # 数字时钟

    def __init__(self, hour=0, minute=0, second=0):
        # 初始化
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        # 走字
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        # 显示时间
        return '%2d:%2d:%2d' % \
            (self._hour, self._minute, self._second)


def main():
    clock = Clock(23, 59, 58)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()


class Point(object):
    # 描述平面上的点并提供计算移动点和另一个点的距离方法

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def move_to(self, x, y):
        # 移动到指定位置
        self._x = x
        self._y = y

    def move_by(self, dx, dy):
        # 移动了增量之后的位置
        self._x += dx
        self._y += dy

    def distance_to(self, other):
        dx = self._x - other._x
        dy = self._y - other._y
        distance = sqrt(dx ** 2 + dy ** 2)
        return distance

    def __str__(self):
        return '(%s, %s)' % (str(self._x), str(self._y))


def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))


if __name__ == '__main__':
    main()
