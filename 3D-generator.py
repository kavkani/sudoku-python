import random
import copy
def generate_and_remove():
    def generate_face(b):
        numbers_list = list(range(1, b + 1))
        list1 = []
        for i in range(1, b + 1):
            random_num = random.choice(numbers_list)
            numbers_list.remove(random_num)
            list1.append(random_num)
        return list1
    pmd = []
    x = 9
    for j in range(6):
        pmd.append(generate_face(x))
    pmd1 = copy.deepcopy(pmd)
    pmd[0][0] = 0
    pmd[0][2] = 0
    pmd[0][6] = 0
    pmd[0][8] = 0
    pmd[1][0] = 0
    pmd[1][2] = 0
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
    p0 = []
    p1 = []
    p2 = []
    p3 = []
    p4 = []
    p5 = []
    p6 = []
    p7 = []
    p8 = []
    p0.append(pmd1[0][0])
    p0.append(pmd1[1][0])
    p0.append(pmd1[5][0])
    p1.append(pmd1[0][2])
    p1.append(pmd1[4][0])
    p1.append(pmd1[5][6])
    p2.append(pmd1[0][6])
    p2.append(pmd1[2][0])
    p2.append(pmd1[1][6])
    p3.append(pmd1[0][8])
    p3.append(pmd1[2][6])
    p3.append(pmd1[4][6])
    p4.append(pmd1[1][8])
    p4.append(pmd1[2][2])
    p4.append(pmd1[3][6])
    p5.append(pmd1[1][2])
    p5.append(pmd1[3][0])
    p5.append(pmd1[5][2])
    p6.append(pmd1[3][2])
    p6.append(pmd1[4][2])
    p6.append(pmd1[5][8])
    p7.append(pmd1[2][8])
    p7.append(pmd1[3][8])
    p7.append(pmd1[4][8])
    p8.append(pmd1[4][8])
    p8.append(pmd1[3][8])
    p8.append(pmd1[5][6])
    list_3d_sudoku = []
    for p in range(6):
        side = []
        for m in range(3):
            row = []
            for d in range(3):
                row.append(pmd[p][m * 3 + d])
            side.append(row)
        list_3d_sudoku.append(side)
    pmd63 = [list_3d_sudoku, p1, p2, p3, p4, p5, p6, p7, p8]
    return pmd63

print(generate_and_remove())