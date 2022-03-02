import random


def generate_face(x):
    numbers_list = list(range(1, x + 1))
    list1 = []
    for i in range(1, x + 1):
        random_num = random.choice(numbers_list)
        numbers_list.remove(random_num)
        list1.append(random_num)

    return list1


pmd = []
x = 9
for i in range(6):
    pmd.append(generate_face(x))

print(pmd)
