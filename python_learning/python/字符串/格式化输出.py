# 占位符%s%d%f
print('my name is %s' % 'ml')
# 50%的输出 多加一个%
print('my name is %d%%' % (50))
# .format{}
print('my name is {}'.format('ml'))  # 位置传参
print('my name is {0},my age is {1}'.format('ml', 100))  # 索引传参
print('my name is {name},my age is {age}'.format(name='ml', age=100))  # 关键字传参
# f-string # 推荐使用
name = 'ml'
age = 100
print(f'my name is {name},my age is {age:.2f}')
