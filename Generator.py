import random


def solver():
    def generate_face(b):
        numbers_list = list(range(1, b + 1))
        list1 = []
        for i in range(1, b + 1):
            random_num = random.choice(numbers_list)
            numbers_list.remove(random_num)
            list1.append(random_num)

        return list1

    pmd2 = []
    x = 9
    for j in range(6):
        pmd2.append(generate_face(x))
    return pmd2


pmd = solver()
"""p = pmd[0]
m = pmd[1]
d = pmd[2]
p2 = pmd[3]
m2 = pmd[4]
d2 = pmd[5]
p[random.randrange(0, 9)] = 0
p[random.randrange(0, 9)] = 0
m[random.randrange(0, 9)] = 0
m[random.randrange(0, 9)] = 0
d[random.randrange(0, 9)] = 0
d[random.randrange(0, 9)] = 0
p2[random.randrange(0, 9)] = 0
p2[random.randrange(0, 9)] = 0
m2[random.randrange(0, 9)] = 0
m2[random.randrange(0, 9)] = 0
d2[random.randrange(0, 9)] = 0
d2[random.randrange(0, 9)] = 0
pm = []
pm.append(p)
pm.append(m)
pm.append(d)
pm.append(p2)
pm.append(m2)
pm.append(d2)"""
