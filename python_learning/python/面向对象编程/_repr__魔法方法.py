# -*- Coding: UTF-8 -*-
# _repr__魔法方法.py
# @作者 ML
# @创建日期 2021-08-20T15:58:32.544Z+08:00
# @最后修改日期 2021-08-20T16:22:19.018Z+08:00

# 类似__str__
# 将对象放在容器中时打印会打印目标的引用地址
# __repr__可以打印出返回的字符串列表

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name},{self.age}"

    def __repr__(self):
        # 将对象放在容器中，需要打印
        return f"{self.name}"


my_list = [Dog("大黄", 1), Dog("大白", 1), Dog("Dog", 1)]
print(my_list)


class Furniture:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f"家具的类型是<{self.name}>,家具的面积为<{self.area}>"

    def __repr__(self):
        return f"家具的类型是<{self.name}>"


class House:
    def __init__(self, address, area):
        self.address = address
        self.area = area
        self.furniture_list = []
        self.free_area = area

    def add(self, obj_furniture):
        '''
        : msg:  添加家具
        : param: obj_furniture 家具对象
        : return:
        '''
        if self.free_area > obj_furniture.area:
            self.furniture_list.append(obj_furniture)
            # self.furniture_list.append(obj_furniture.name)
            self.free_area -= obj_furniture.area
            print(f"家具<{obj_furniture.name}>添加成功！")
        else:
            print(f"添加失败，换个大房子吧！")
        print(f"现有的家具<{self.furniture_list}>")

    def __str__(self):
        # 可用__repr__方法替代
        buf_list = [obj.name for obj in self.furniture_list]
        if buf_list:
            return f"房子的地址为 <{self.address}> , 占地面积为 <{self.area}>," \
                f"剩余面积为 <{self.free_area}>,房子中的家具为<{','.join(buf_list)}>"
        else:
            return f"房子的地址为 <{self.address}> , 占地面积为 <{self.area}>," \
                f"剩余面积为 <{self.free_area}>,还没有添加家具！"


furniture = Furniture('豪华双人床', 15)
furniture1 = Furniture('沙发', 5)
house = House("北京", 300)
house.add(furniture)
house.add(furniture1)
print(house)
