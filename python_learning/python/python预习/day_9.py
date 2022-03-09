# _self. _order  是私有属性和方法，是否正确?不建议外界直接访问
# 如果想要访问但又不改变原有对象
# 可以使用property装饰器的getter和setter方法
# getter 访问属性 setter 设置属性
from math import sqrt
from time import time, localtime, sleep
from abc import ABCMeta, abstractmethod
from random import randint, randrange
import random
# from typing import MutableSequence


class Person(object):
    # slots 限定绑定的属性只有name，age，gender

    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # getter方法：@property
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print("%s 正在玩飞行棋。" % self._name)
        else:
            print("%s 正在玩斗地主" % self._name)


def main():
    person = Person('王大锤', 12)
    person.play()
    person.age = 22
    person.play()
    person._gender = '男'
    # person.name = '白元芳' can't set attribute
    # 如果不设置属性，就变为只读状态
    # person._is_gay = True 动态绑定属性，限制后不能绑定
    # 'Person' object has no attribute '_is_gay'


if __name__ == '__main__':
    main()
# python：动态语言，上述方法允许在程序运行时给对象绑定新的属性
# 也可以解除绑定和限定绑定属性，限制绑定用__slots__

# 类中不必全是对象的方法：如三角形类可以包括求面积方法：也可以是对非对象（边长）的方法：判断是否能构成三角形
# 类中定义静态方法


class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(
            half * (half - self._a) * (half - self._b) *
            (half - self._c))


def main1():
    a, b, c = 3, 4, 5
    # 静态方法和类方法都是通过给类发消息调用
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        # 除了直接给对象发消息调用对象方法
        # 也可以直接给类发消息调用对象方法，但要传入接受信息的对象作为参数
        print(t.perimeter())
        print(t.area())
        print(Triangle.perimeter(t))
        print(Triangle.area(t))
    else:
        print('无法构成三角形')


if __name__ == '__main__':
    main1()
# 类中定义类方法


class Clock(object):
    '''数字时钟'''

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        # time返回当前时间的时间戳1970到现在的秒数
        # localtime转化为现在时刻类
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
    # 类方法的第一个参数约定名为cls 代表当前类相关的信息的对象
    # 可以获取和类相关的信息并且创造出类的对象，可以用类中的其他方法

    def run(self):
        '''走字'''
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
        '''显示时间'''
        return '%02d:%02d:%02d' % \
            (self._hour, self._minute, self._second)


def main2():
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


# if __name__ == '__main__':
#     main2()

# 类之间的关系：继承或泛化：is-a 关联： has-a 依赖：use-a
# 继承：学生和人 手机和电子产品
# 关联：整体和部分：聚合 整体和部分同时存在同时消亡：合成
# 依赖：司机类 驾驶方法用到了汽车类 司机和汽车：依赖
# 继承：子类除了继承父类的属性和方法还可以定义自己特有的属性方法


class Student(Person):

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        # 子类
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        # 重写
        print('%s的%s正在学习%s' % (self.grade, self._name, course))


class Teacher(Person):
    '''老师'''

    def __init__(self, name, age, title):
        super().__init__(name, age)
        # 子类
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        # 重写
        print('%s%s正在讲%s' % (self._title, self._name, course))


def main3():
    student = Student('王大锤', 12, '初三')
    teacher = Teacher('刘晓符', 30, '专家')
    student.study('高数')
    teacher.teach('高数')
    student.play()
    teacher.play()


if __name__ == '__main__':
    main3()
# 子类继承父类的方法后，可以对父类已有的方法给出新的实现方法，这个动作称为重写（override），不同子类对象重写后有不同的实现，这个就是多态


class Pet(object, metaclass=ABCMeta):
    '''宠物：类元类方法'''

    def __init__(self, nickname):
        self._nickname = nickname

    # 抽象类，不能创建对象，专门用来继承
    # 包装器
    @abstractmethod
    def make_voice(self):
        '''发出声音'''
        pass


class Dog(Pet):
    '''狗'''

    def make_voice(self):
        print('%s: 汪汪汪…' % self._nickname)


class Cat(Pet):
    '''猫'''

    def make_voice(self):
        print('%s: 喵喵喵...' % self._nickname)


def main4():
    Pets = [Dog('旺财'), Cat('凯蒂')]
    for pet in Pets:
        pet.make_voice()


if __name__ == '__main__':
    main4()
# 案例1：奥特曼打小怪兽


class Fighter():
    '''战斗者'''

    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        pass


class ULtraman(Fighter):

    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        # 父类只有name和hp属性
        self._mp = mp

    def attack(self, other):
        # other 是类用修饰器访问
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        '''究极必杀技'''

        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        '''魔法攻击'''
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        '''恢复魔法值'''
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '%s奥特曼\n' % self._name + \
            '生命值：%d\n' % self._hp + \
            '魔法值：%d\n' % self._mp


class Monster(Fighter):
    '''小怪兽'''

    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '%s小怪兽\n' % self._name + \
            '生命值：%d\n' % self._hp


def is_any_alive(monsters):
    '''判断有没有小怪兽活着'''
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False


def select_alive_one(monsters):
    '''选中一个活着的小怪兽'''
    # 传入类的列表
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster


def display_info(ultraman, monsters):
    '''显示奥特曼和小怪兽的信息'''
    print(ultraman)
    for monster in monsters:
        print(monster, end='')


def main5():
    u = ULtraman('王培文', 1000, 120)
    m1 = Monster('狄仁杰', 250)
    m2 = Monster('白元芳', 500)
    m3 = Monster('王大锤', 750)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('=====第%2d回合====' % fight_round)
        m = select_alive_one(ms)
        skill = randint(1, 10)
        if skill <= 6:
            # 60%的概率使用普通攻击
            print('%s使用普通攻击打了%s.' % (u.name, m.name))
            u.attack(m)
            print('%s的魔法值恢复了%d点' % (u.name, u.resume()))
        elif skill <= 9:
            # 只有7，8，9才会运行
            # 30%的概率使用魔法攻击
            # 可能魔法值不足
            if u.magic_attack(ms):
                print('%s使用了魔法攻击.' % u.name)
            else:
                print('%s使用魔法失败' % u.name)
        else:
            # 10%使用究极必杀技
            if u.huge_attack(m):
                print('%s对%s使用必杀技了' % (u.name, m.name))
            else:
                print('%s对%s使用普通攻击' % (u.name, m.name))
                print('%s魔法值恢复了%d点' % (u.name, u.resume()))
        if m.alive > 0:
            print('%s回击了%s' % (m.name, u.name))
            m.attack(u)
        display_info(u, ms)
        fight_round += 1
    print('\n====战斗结束！=====\n')
    if u.alive > 0:
        print('%s奥特曼胜利！' % u.name)
    else:
        print('小怪兽胜利！')


if __name__ == '__main__':
    main5()

# 案例二：扑克游戏


class Card(object):
    '''一张牌'''

    def __init__(self, suite, face):
        self._suite = suite
        self._face = face

    @property
    def face(self):
        return self._face

    @property
    def suite(self):
        return self._suite

    def __str__(self):
        # 除了AJQK其他都是数字
        if self._face == 1:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return '%s%s' % (self._suite, face_str)

    def __repr__(self):
        return self.__str__()


class Poker(object):
    '''一副牌'''

    def __init__(self):
        self._cards = [
            Card(suite, face)
            for suite in '♠♥♣♦'
            for face in range(1, 14)]
        self._current = 0

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        '''洗牌'''
        self._current = 0
        random.shuffle(self._cards)
        # 从对象集合中随机抽取

    @property
    def next(self):
        '''发1张牌'''
        card = self._cards[self._current]
        # 类的列表
        self._current += 1
        return card

    @property
    def has_next(self):
        '''还有没有牌'''
        return self._current < len(self._cards)


class Player(object):
    '''玩家'''

    def __init__(self, name):
        self._name = name
        self._cards_on_hand = []

    @property
    def name(self):
        return self._name

    @property
    def cards_on_hand(self):
        return self._cards_on_hand

    def get(self, card):
        '''上述牌对象添加进去：摸牌'''
        self._cards_on_hand.append(card)

    def arrange(self, card_key):
        '''整理手上的牌'''
        self._cards_on_hand.sort(key=card_key)
# 排序规则：先根据花色再根据点数排序


def get_key(card):
    return (card.suite, card.face)


def main6():
    p = Poker()
    # 创建一副牌列表
    p.shuffle()
    # 洗牌
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    # 创建玩家列表
    for _ in range(13):
        for player in players:
            # 每个玩家抽取13次
            player.get(p.next)
    for player in players:
        # 打印每个玩家持有的牌
        print(player.name + ':', end=' ')
        player.arrange(get_key)
        print(player.cards_on_hand)


if __name__ == '__main__':
    main6()


# 案例三：工资结算系统 某公司有三种类型员工：经理、程序员、销售
# 经理 15000/月 程序员 150/小时 销售 1200/每月+5%提成（销售额）


class Employee(object):
    '''员工'''

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        pass


class Manager(Employee):

    def __init__(self, name):
        super().__init__(name)

    def get_salary(self):
        return 15000.0


class Programmer(Employee):

    def __init__(self, name, work_hours=0):
        super().__init__(name)
        self._work_hours = work_hours

    @property
    def work_hours(self):
        return self._work_hours

    @work_hours.setter
    def work_hours(self, work_hours):
        self._work_hours = work_hours if work_hours > 0 else 0

    def get_salary(self):
        return 150.0 * self._work_hours


class Salesman(Employee):

    def __init__(self, name, sales=0):
        super().__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def get_salary(self):
        return 1200.0 + self._sales * 0.05


def main7():
    emps = [
        Manager('刘备'), Programmer('诸葛亮'), Manager('曹操'),
        Salesman('荀彧'), Salesman('吕布'), Programmer('张辽'), Programmer('赵云')]
    for emp in emps:
        if isinstance(emp, Programmer):
            emp.work_hours = int(input('请输入%s本月工作时间：' % emp.name))
        elif isinstance(emp, Salesman):
            emp.sales = float(input('请输入%s本月销售额' % emp.name))
        print('%s本月工资为：￥%s' % (emp.name, emp.get_salary()))


if __name__ == '__main__':
    main7()
    