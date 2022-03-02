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
pmd[0][0] = 0
pmd[0][2] = 0
pmd[0][6] = 0
pmd[0][8] = 0
pmd[1][0] = 0
pmd[1][2] = 0
pmd[1][6] = 0
pmd[1][8] = 0
pmd[2][0] = 0
pmd[2][2] = 0
pmd[2][6] = 0
pmd[3][0] = 0
pmd[3][2] = 0
pmd[3][6] = 0
pmd[4][0] = 0
pmd[4][2] = 0
pmd[4][6] = 0
pmd[5][0] = 0
pmd[5][2] = 0
pmd[5][8] = 0
pmd[2][8] = 0
pmd[4][8] = 0
pmd[3][8] = 0
pmd[5][6] = 0