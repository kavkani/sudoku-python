import random


def difficulty(x):
    level = 0
    if x == 'Hard':
        level = 3
    if x == 'Medium':
        level = 2
    if x == 'Easy':
        level = 1

    return level


def random_generate(difficulty_num):
    list1 = []
    count = 0
    if difficulty_num == 3:
        count = 10
    if difficulty_num == 2:
        count = 6
    if difficulty_num == 1:
        count = 4

    for i in range(1, count + 1):
        numbers_list = list(range(1, 10))

        for j in range(1, 4):
            random_num = random.choice(numbers_list)
            numbers_list.remove(random_num)
            list1.append(random_num)

    return list1


difficulty_num = difficulty(input())
return_list = (random_generate(difficulty_num))

p1 = []
j = 0
for i in range(len(return_list)):
    j1 = j + 3
    p1.append(list(return_list[j:j1]))
    j = j1

print(p1)