# continue break 只能用在循环当中
# break 终止循环
# continue 跳过本次循环、下面语句不执行，进行下次循环
# 有5个吃了3个之后饱了后续不吃了
for i in range(1, 6):
    if i > 3:
        print("吃饱了,不吃了！")
        break
    print(f"正在吃第{i}个苹果！")
# 迟到第4个苹果发现有虫子不吃了
for i in range(1, 6):
    if i == 4:
        print("有虫子，不吃了")
        continue
        print("恶心")
    print(f"正在吃第{i}个苹果")
