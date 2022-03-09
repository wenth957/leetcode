import random

schools = [[], [], []]
teachers = ['A', 'B', 'C', 'D', 'E', 'F']
for teacher in teachers:
    num = random.randint(0, 2)  # [0,2]之间的随机数
    schools[num].append(teacher)

print(schools)

for school in schools:
    print(f"该办公室的老师人数为{len(school)},他们的名字是： ")
    for teacher in school:
        print(teacher, end=' ')
    print()
