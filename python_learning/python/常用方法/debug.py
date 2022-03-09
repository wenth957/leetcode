# debug可以查看代码的执行过程，排查错误
# 1 打断点：想要查看代码开始的地方
# 2 debug运行
# 3 点击下一步查看代码执行过程:高亮表示下一步将要运行的代码
# 有些地方debug是不会停下的 一定不执行语句和一定会执行的语句
age = int(input('please enter your age: '))

if age >= 18:
    print('you can do it!')

else:
    print('you have to finish your homework!')
