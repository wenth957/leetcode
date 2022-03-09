# -*- Coding: UTF-8 -*-
# 排序中的key.py
# @作者 ML
# @创建日期 2021-08-11T17:23:47.447Z+08:00
# @最后修改日期 2021-08-11T18:03:29.821Z+08:00
#

list1 = [1, 2, 3, 4, 5, 6]
list2 = [{
    'name': 'a',
    'age': 21
}, {
    'name': 'b',
    'age': 19
}, {
    'name': 'c',
    'age': 20
}]
list2.sort(key=lambda x: x['age'])  # key后面跟一个函数
list2.sort(key=lambda x: (x['age'], x['age']))  # 先比较第一个key，再按第二个key比较
print(list2)
