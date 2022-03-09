# object 是最基本的类 括号中的内容可以不写
# 三种定义


class Dog0(object):
    pass


class Dog1():
    pass


class Dog2:
    pass


# 新式类：直接或间接继承object，所有类默认继承object
# 旧式类：python2 不默认继承
# 每个对象可以在类外添加自己的专属属性
# self代表对象，作为第一个形参，调用方法时不需要手动传递：本质是形参
# self在类的内部作为对象使用

# 魔法方法：两个下划线开头 两个下划线结束
# 满足特定条件会自动调用

# 1.__init__() 构造函数
# 调用：创建对象时会立即调用
# 作用：1、用来给对象添加属性，给对象属性一个初始值
#    2、代码的业务需求：每创建一个对象都需要执行的代码块
# 可以传入参数改变初始值

# 2.__str__()
# 调用：1、print(对象)，会自动调用,打印的是__str__方法的返回值
#    2、str(对象)将自定义对象转换为字符串的时候会自动调用
# 作用：1、打印对象的时候输出一些属性信息
#    2、将对象转换为字符串对象的时候
# 注意点：方法必须返回一个字符串，只有self一个参数

# # 3.__del__() 析构函数
# 调用：对象在内存中被消除（引用计数为0）时会自动调用
#    1：程序代码运行结束，程序运行过程中创建的所有对象和变量都会销毁删除
#    2：使用del 变量 将这个对象的引用计数变为0，会自动调用
# 作用：程序运行或者del时，对象被销毁时需要书写的代码


class Dog(object):
    def __init__(self, name, age):
        print("我是init 我被调用了")
        self.name = name
        self.age = age

    def __str__(self):
        print("我是str,我被调用了")
        return f"小狗的名字是{self.name},年龄是{self.age}"

    def __del__(self):
        print(f"我是del,{self.name}被销毁了")


dog = Dog('wang', 26)
# print(dog)  # 没有__str__默认输出引用地址 # 定义后返回的是__str__的return部分
# str_dog = str(dog)
# print(str_dog)  # 外部转换也是引用地址
# 我是del,wang被销毁了  所有程序运行完才会运行
# dog1 = dog  # ‘wang'引用计数为2
# print("第1次删除前")
# del dog  # 计数为1
# print("第二次删除前")
# del dog1  # 计数为0，立即调用
# print("第二次删除后")


class Potato(object):
    def __init__(self):
        self.status = '生的'
        self.total_time = 0
        self.spices_list = []

    def cook(self, time):
        self.total_time += time
        if self.total_time < 3:
            self.status = "生的"
        elif self.total_time < 6:
            self.status = "半生不熟的"
        elif self.total_time < 8:
            self.status = "熟了"
        else:
            self.status = "烤糊了"

    def add(self, spices):
        self.spices_list.append(spices)

    def __str__(self):
        if self.spices_list:
            spice = ' '.join(self.spices_list)
            return f"地瓜的状态是： {self.status} 烧烤时间为 {self.total_time}\
  调料有: {spice}"

        else:
            return "还没有添加调料"


potato = Potato()
potato.cook(5)
potato.add("辣椒")
potato.add("油")
print(potato)
'''属性：状态：生的 、烧烤时间 方法：烧烤、计算烧烤时间、修改地瓜状态
输出属性信息'''
