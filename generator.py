import random
import copy


def generate_and_remove(delete_count):
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
    corners = [0, 1, 2, 3, 4, 5, 6, 7]
    delete = []
    for i in range(delete_count):
        random_num = random.choice(corners)
        corners.remove(random_num)
        delete.append(random_num)
    pmd1 = copy.deepcopy(pmd)
    if 0 in delete:
        pmd[0][8] = 0
        pmd[1][6] = 0
        pmd[2][0] = 0
    if 1 in delete:
        pmd[4][8] = 0
        pmd[0][6] = 0
        pmd[2][6] = 0
    if 2 in delete:
        pmd[0][0] = 0
        pmd[4][2] = 0
        pmd[5][6] = 0
    if 3 in delete:
        pmd[0][2] = 0
        pmd[5][0] = 0
        pmd[1][0] = 0
    if 4 in delete:
        pmd[3][8] = 0
        pmd[4][6] = 0
        pmd[2][8] = 0
    if 5 in delete:
        pmd[5][2] = 0
        pmd[3][0] = 0
        pmd[1][2] = 0
    if 6 in delete:
        pmd[1][8] = 0
        pmd[3][6] = 0
        pmd[2][2] = 0
    if 7 in delete:
        pmd[4][0] = 0
        pmd[3][2] = 0
        pmd[5][8] = 0
    p0 = []
    p1 = []
    p2 = []
    p3 = []
    p4 = []
    p5 = []
    p6 = []
    p7 = []
    a0 = []
    a1 = []
    a2 = []
    a3 = []
    a4 = []
    a5 = []
    a6 = []
    a7 = []
    if 0 in delete:
        a0.append(pmd1[0][8])
        a0.append(pmd1[1][6])
        a0.append(pmd1[2][0])
    if 1 in delete:
        a1.append(pmd1[4][8])
        a1.append(pmd1[0][6])
        a1.append(pmd1[2][6])
    if 2 in delete:
        a2.append(pmd1[0][0])
        a2.append(pmd1[4][2])
        a2.append(pmd1[5][6])
    if 3 in delete:
        a3.append(pmd1[0][2])
        a3.append(pmd1[5][0])
        a3.append(pmd1[1][0])
    if 4 in delete:
        a4.append(pmd1[3][8])
        a4.append(pmd1[4][6])
        a4.append(pmd1[2][8])
    if 5 in delete:
        a5.append(pmd1[5][2])
        a5.append(pmd1[3][0])
        a5.append(pmd1[1][2])
    if 6 in delete:
        a6.append(pmd1[1][8])
        a6.append(pmd1[3][6])
        a6.append(pmd1[2][2])
    if 7 in delete:
        a7.append(pmd1[4][0])
        a7.append(pmd1[3][2])
        a7.append(pmd1[5][8])
    if 0 in delete:
        p0.append(8)
        p0.append(15)
        p0.append(18)
    if 1 in delete:
        p1.append(44)
        p1.append(6)
        p1.append(24)
    if 2 in delete:
        p2.append(0)
        p2.append(38)
        p2.append(51)
    if 3 in delete:
        p3.append(2)
        p3.append(45)
        p3.append(9)
    if 4 in delete:
        p4.append(35)
        p4.append(42)
        p4.append(26)
    if 5 in delete:
        p5.append(47)
        p5.append(27)
        p5.append(11)
    if 6 in delete:
        p6.append(17)
        p6.append(33)
        p6.append(20)
    if 7 in delete:
        p7.append(36)
        p7.append(29)
        p7.append(53)
    answers = [a0, a1, a2, a3, a4, a5, a6, a7]
    randomized_answers = []
    for i in range(len(answers)):
        random_num = random.randint(0, len(answers)-1)
        randomized_answers.append(answers[random_num])
        answers.pop(random_num)
    list_3d_sudoku = []
    for p in range(6):
        side = []
        for m in range(3):
            row = []
            for d in range(3):
                row.append(pmd[p][m * 3 + d])
            side.append(row)
        list_3d_sudoku.append(side)
    pmd63 = [p0, p1, p2, p3, p4, p5, p6, p7]
    return randomized_answers, pmd63, list_3d_sudoku, pmd1


def check(sudoku_list, answers):
    if 0 in sudoku_list:
        print(0)
        return False
    list_3d_sudoku = []
    for p in range(6):
        side = []
        for m in range(9):
            side.append(sudoku_list[p * 6 + m])
        list_3d_sudoku.append(side)
    if list_3d_sudoku != answers:
        return False
    return True

