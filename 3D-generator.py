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
    p0 = []
    p1 = []
    p2 = []
    p3 = []
    p4 = []
    p5 = []
    p6 = []
    p7 = []
    p8 = []
    a0 = []
    a1 = []
    a2 = []
    a3 = []
    a4 = []
    a5 = []
    a6 = []
    a7 = []
    a8 = []
    a0.append(pmd1[0][0])
    a0.append(pmd1[1][0])
    a0.append(pmd1[5][0])
    a1.append(pmd1[0][2])
    a1.append(pmd1[4][0])
    a1.append(pmd1[5][6])
    a2.append(pmd1[0][6])
    a2.append(pmd1[2][0])
    a2.append(pmd1[1][6])
    a3.append(pmd1[0][8])
    a3.append(pmd1[2][6])
    a3.append(pmd1[4][6])
    a4.append(pmd1[1][8])
    a4.append(pmd1[2][2])
    a4.append(pmd1[3][6])
    a5.append(pmd1[1][2])
    a5.append(pmd1[3][0])
    a5.append(pmd1[5][2])
    a6.append(pmd1[3][2])
    a6.append(pmd1[4][2])
    a6.append(pmd1[5][8])
    a7.append(pmd1[2][8])
    a7.append(pmd1[3][8])
    a7.append(pmd1[4][8])
    p0.append(0)
    p0.append(9)
    p0.append(45)
    p1.append(2)
    p1.append(36)
    p1.append(51)
    p2.append(6)
    p2.append(18)
    p2.append(15)
    p3.append(8)
    p3.append(24)
    p3.append(42)
    p4.append(17)
    p4.append(20)
    p4.append(33)
    p5.append(11)
    p5.append(27)
    p5.append(47)
    p6.append(29)
    p6.append(38)
    p6.append(53)
    p7.append(26)
    p7.append(35)
    p7.append(44)
    answers = [a0 ,a1 ,a2 ,a3 ,a4 ,a5 ,a6 ,a7]
    randomized_answers = []
    for i in range(len(answers)):
        random_num = random.randint(0,len(answers)-1)
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
    pmd63 = [list_3d_sudoku,list([p0, p1, p2, p3, p4, p5, p6, p7]),randomized_answers]
    return pmd63


print(generate_and_remove()[2])
