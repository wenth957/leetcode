'''
Author: ML
Date: 2021-08-21 16:10:28
LastEditTime: 2021-08-21 17:18:03
LastEditors: Please set LastEditors
Description: 异常：程序运行过程中，代码遇到错误，给出错误提示。
FilePath: \10_days\笔记\异常.py
'''
# 1.1 异常的组成:类型+解释
# 1.2 异常的捕获：代码运行中，遇到错误，让其继续运行，同时会给使用者一个提示信息，便于后期改进
# 1.2.1 单个异常
'''
try:
    可能发生异常的代码
  except 异常的类型:
    发生异常时执行的代码
'''
# 1.2.2 多个异常
'''
try:
    可能发生异常的代码
  except (异常1，异常2,……）:
    发生异常时执行的代码
'''
# print("其他的代码……")
# num = input("请输入一个数字： ")
# try:
#     result = 10 / int(num)    # 只要发生异常立马跳转到except
#     print(f"计算得到的结果是{result}")
# except (ZeroDivisionError, ValueError):
#     print("请输入一个不为0的数字")  # ZeroDivisionError: division by zero
#     # ValueError: invalid literal for int() with base 10: 'a'
# print("其他的代码……")

'''
try:
    可能发生异常的代码
except 异常1:
    发生异常时执行的代码1
except 异常2:
    发生异常时执行的代码2
……
'''
# print("其他的代码……")
# num = input("请输入一个数字： ")
# try:
#     result = 10 / int(num)    # 只要发生异常立马跳转到except
#     print(f"计算得到的结果是{result}")
# except ZeroDivisionError:
#     print("请输入一个不为0的数字")  # ZeroDivisionError: division by zero
# except ValueError:
#     print("输入的不是数字，请输入一个非0数字")   # ValueError: invalid literal for int() with base 10: 'a'
# print("其他的代码……")
# 1.3 打印异常信息
'''
try:
    可能发生异常的代码
except 异常1 as a:
    发生异常时执行的代码1
    print(a)
except 异常2 as b:
    发生异常时执行的代码2
    print(b)
……
'''

# print("其他的代码……")
# num = input("请输入一个数字： ")
# try:
#     result = 10 / int(num)    # 只要发生异常立马跳转到except
#     print(f"计算得到的结果是{result}")
# except ZeroDivisionError as a:
#     print("请输入一个不为0的数字", a)  # ZeroDivisionError: division by zero
# except ValueError as b:
#     print("输入的不是数字，请输入一个非0数字", b)   # ValueError: invalid literal for int() with base 10: 'a'
# print("其他的代码……")
# 1.4  捕获所有异常
'''
try:
    可能发生异常的代码
except:
    发生异常时执行的代码
不能打印异常信息
'''
'''
try:
    可能发生异常的代码
except Exception as e:  Exception-->BaseException(object) 继承的错误类
    发生异常时执行的代码
    print(e)
打印异常信息
'''
# print("其他的代码……")
# num = input("请输入一个数字： ")
# try:
#     result = 10 / int(num)    # 只要发生异常立马跳转到except
#     print(f"计算得到的结果是{result}")
# except Exception as a:
#     print("请输入一个非0数字", a)

# print("其他的代码……")

# 1.5 异常的完整结构
'''
try:
    可能发生异常的代码
except Exception as a:
    发生异常时输入的提示信息
    print(a)
else:
    代码没有发生异常时运行
finally:
    不管有没有发生异常都会执行

'''
# print("其他的代码……")
# num = input("请输入一个数字： ")
# try:
#     result = 10 / int(num)    # 只要发生异常立马跳转到except
#     print(f"计算得到的结果是{result}")
# except Exception as a:
#     print("请输入一个非0数字", a)
# else:
#     print("except不满足时，我才会执行")
# finally:
#     print("无论何时，我都会执行")

# print("其他的代码……")


# 1.6 异常的传递：底层原理
'''
当一行代码发生异常时，会向外层传递这个异常，直到被捕获或者程序报错为止
1、try 嵌套
2、函数嵌套
'''
# print("其他的代码")
# num = input("请输入一个数字： ")
# try:
#     try:
#         a = int(num)
#     except ValueError:  # 捕获不了0除错误，传递到外层
#         print("发生异常")
#     finally:
#         print("我都执行了")
#     num = 10 / a
#     print(f"结果是：{num}")
# except Exception as a:
#     print(a)
# print("其他代码")


# def func(num):
#     print("传递异常")
#     result = 10 / num# 报错，没有捕获异常，向外层传递
#     print(result)
#     print("________1_________")


# def func1(num):
#     print("++++++++2++++++++++")
#     func(num)
#     print("++++++++3++++++++++")


# try:
#     print("+++++++++4+++++++++")
#     func1(0)
#     print("+++++++++5+++++++++")
# except Exception as e:
#     print("+++++++++6+++++++++")
#     print(e)


# 1.7 抛出自定义异常
'''
程序不满足语法，python使用if语句抛出异常
raise 异常对象=异常类(参数)
- 自定义异常类：继承Exception
- 选择书写，定义__init__方法，定义__str__方法
- 合适时机抛出异常对象
'''


class PasswordLengthError(Exception):
    pass


def get_password():
    password = input("请输入密码：")
    if len(password) == 6:
        print("密码长度合适！")
    else:
        raise PasswordLengthError("密码长度不是6！")


try:
    get_password()
except Exception as e:
    print(e)  # 密码长度不是6！
