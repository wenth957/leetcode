import sys

# 生成式和生成器
f = [x for x in range(1, 10)]
# 每循环一次生成一次数据 可对该数据进行运算
print(f)
# 可用if函数判断是否生成数据
f = [x for x in range(10) if x % 2 == 0]
print(f)
f = [x + y for x in 'ABCDE' for y in '1234567']
# print(f) 可以直接获取数据

# 列表生成式
# 这就是列表的生成表达式创建列表容器
f = [x**2 for x in range(1, 1000)]
print(sys.getsizeof(f))
# 查看对象占用的内存 9024
# print(f)

# 字典生成式、推导式
f = {f"name{i}": i for i in range(10)}
print(f)
# 生成器对象：节约内存，但是需要时间获得数据
# 通过生成器可以获取数据但不占用额外的内存
# 每次需要数据通过内部运算获得
f = (x**2 for x in range(1, 1000))
print(sys.getsizeof(f))

# 88
# print(f)

# for val in f:
#     print(val)
# 9024bytes与88bytes


# yield关键字可以将一个普通函数改造成生成器
def fib(n):
    # 斐波那契数列
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


# def main():
#     for val in fib(20):
#         print(val)

# if __name__ == '__main__':
#     main()
