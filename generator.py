import copy
import random


def generate_and_remove(delete_score):
    distraction_cubes = delete_score // 4
    delete_score *= 3

    def generate_face(b):
        numbers_list = list(range(1, b + 1))
        list1 = []
        for k in range(1, b + 1):
            random_number = random.choice(numbers_list)
            numbers_list.remove(random_number)
            list1.append(random_number)

        return list1

    pmd = []
    x = 9
    for j in range(6):
        pmd.append(generate_face(x))
    corners = [0, 1, 2, 3, 4, 5, 6, 7]
    centres = [0, 1, 2, 3, 4, 5]
    between = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    corners_delete = []
    centres_delete = []
    between_delete = []
    if delete_score < 0:
        corners_delete = [0, 1, 2, 3, 4, 5, 6, 7]
        centres_delete = [0, 1, 2, 3, 4, 5]
        between_delete = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    else:
        while delete_score > 0:
            random_num = random.choice([1, 2, 3])
            if random_num == 1 and len(corners) > 0:
                random_num = random.choice(corners)
                corners.remove(random_num)
                corners_delete.append(random_num)
                delete_score -= 3
            elif random_num == 2 and len(centres) > 0:
                random_num = random.choice(centres)
                centres.remove(random_num)
                centres_delete.append(random_num)
                delete_score -= 1
            elif (random_num == 3) and (len(between) > 0):
                random_num = random.choice(between)
                between.remove(random_num)
                between_delete.append(random_num)
                delete_score -= 2

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
    answers = []
    pmd1 = copy.deepcopy(pmd)
    pmd63 = []
    if 0 in corners_delete:
        pmd[0][8] = 0
        pmd[1][6] = 0
        pmd[2][0] = 0
        a0.append(pmd1[0][8])
        a0.append(pmd1[1][6])
        a0.append(pmd1[2][0])
        answers.append(a0)
        p0.append(8)
        p0.append(15)
        p0.append(18)
        pmd63.append(p0)
    if 1 in corners_delete:
        pmd[4][8] = 0
        pmd[0][6] = 0
        pmd[2][6] = 0
        a1.append(pmd1[4][8])
        a1.append(pmd1[0][6])
        a1.append(pmd1[2][6])
        answers.append(a1)
        p1.append(44)
        p1.append(6)
        p1.append(24)
        pmd63.append(p1)
    if 2 in corners_delete:
        pmd[0][0] = 0
        pmd[4][2] = 0
        pmd[5][6] = 0
        a2.append(pmd1[0][0])
        a2.append(pmd1[4][2])
        a2.append(pmd1[5][6])
        answers.append(a2)
        p2.append(0)
        p2.append(38)
        p2.append(51)
        pmd63.append(p2)
    if 3 in corners_delete:
        pmd[0][2] = 0
        pmd[5][0] = 0
        pmd[1][0] = 0
        a3.append(pmd1[0][2])
        a3.append(pmd1[5][0])
        a3.append(pmd1[1][0])
        answers.append(a3)
        p3.append(2)
        p3.append(45)
        p3.append(9)
        pmd63.append(p3)
    if 4 in corners_delete:
        pmd[3][8] = 0
        pmd[4][6] = 0
        pmd[2][8] = 0
        a4.append(pmd1[3][8])
        a4.append(pmd1[4][6])
        a4.append(pmd1[2][8])
        answers.append(a4)
        p4.append(35)
        p4.append(42)
        p4.append(26)
        pmd63.append(p4)
    if 5 in corners_delete:
        pmd[5][2] = 0
        pmd[3][0] = 0
        pmd[1][2] = 0
        a5.append(pmd1[5][2])
        a5.append(pmd1[3][0])
        a5.append(pmd1[1][2])
        answers.append(a5)
        p5.append(47)
        p5.append(27)
        p5.append(11)
        pmd63.append(p5)
    if 6 in corners_delete:
        pmd[1][8] = 0
        pmd[3][6] = 0
        pmd[2][2] = 0
        a6.append(pmd1[1][8])
        a6.append(pmd1[3][6])
        a6.append(pmd1[2][2])
        answers.append(a6)
        p6.append(17)
        p6.append(33)
        p6.append(20)
        pmd63.append(p6)
    if 7 in corners_delete:
        pmd[4][0] = 0
        pmd[3][2] = 0
        pmd[5][8] = 0
        a7.append(pmd1[4][0])
        a7.append(pmd1[3][2])
        a7.append(pmd1[5][8])
        answers.append(a7)
        p7.append(36)
        p7.append(29)
        p7.append(53)
        pmd63.append(p7)

    p0 = []
    p1 = []
    p2 = []
    p3 = []
    p4 = []
    p5 = []
    a0 = []
    a1 = []
    a2 = []
    a3 = []
    a4 = []
    a5 = []
    if 0 in centres_delete:
        pmd[0][4] = 0
        a0.append(0)
        a0.append(0)
        a0.append(pmd1[0][4])
        answers.append(a0)
        p0.append(4)
        p0.append(4)
        p0.append(4)
        pmd63.append(p0)
    if 1 in centres_delete:
        pmd[1][4] = 0

        a1.append(0)
        a1.append(0)
        a1.append(pmd1[1][4])
        answers.append(a1)
        p1.append(4 + (1 * 9))
        p1.append(4 + (1 * 9))
        p1.append(4 + (1 * 9))
        pmd63.append(p1)
    if 2 in centres_delete:
        pmd[2][4] = 0

        a2.append(0)
        a2.append(0)
        a2.append(pmd1[2][4])
        answers.append(a2)
        p2.append(4 + (2 * 9))
        p2.append(4 + (2 * 9))
        p2.append(4 + (2 * 9))
        pmd63.append(p2)
    if 3 in centres_delete:
        pmd[3][4] = 0

        a3.append(0)
        a3.append(0)
        a3.append(pmd1[3][4])
        answers.append(a3)
        p3.append(4 + (3 * 9))
        p3.append(4 + (3 * 9))
        p3.append(4 + (3 * 9))
        pmd63.append(p3)
    if 4 in centres_delete:
        pmd[4][4] = 0

        a4.append(0)
        a4.append(0)
        a4.append(pmd1[4][4])
        answers.append(a4)
        p4.append(4 + (4 * 9))
        p4.append(4 + (4 * 9))
        p4.append(4 + (4 * 9))
        pmd63.append(p4)
    if 5 in centres_delete:
        pmd[5][4] = 0

        a5.append(0)
        a5.append(0)
        a5.append(pmd1[5][4])
        answers.append(a5)
        p5.append(4 + (5 * 9))
        p5.append(4 + (5 * 9))
        p5.append(4 + (5 * 9))
        pmd63.append(p5)
    p0 = []
    p1 = []
    p2 = []
    p3 = []
    p4 = []
    p5 = []
    p6 = []
    p7 = []
    p8 = []
    p9 = []
    p10 = []
    p11 = []
    a0 = []
    a1 = []
    a2 = []
    a3 = []
    a4 = []
    a5 = []
    a6 = []
    a7 = []
    a8 = []
    a9 = []
    a10 = []
    a11 = []
    if 0 in between_delete:
        pmd[5][3] = 0
        pmd[0][1] = 0
        a0.append(0)
        a0.append(pmd1[5][3])
        a0.append(pmd1[0][1])
        answers.append(a0)
        p0.append(5 * 9 + 3)
        p0.append(5 * 9 + 3)
        p0.append(1)
        pmd63.append(p0)
    if 1 in between_delete:
        pmd[5][1] = 0
        pmd[1][1] = 0
        a1.append(0)
        a1.append(pmd1[5][1])
        a1.append(pmd1[1][1])
        answers.append(a1)
        p1.append(5 * 9 + 1)
        p1.append(5 * 9 + 1)
        p1.append(10)
        pmd63.append(p1)
    if 2 in between_delete:
        pmd[5][5] = 0
        pmd[3][1] = 0
        a2.append(0)
        a2.append(pmd1[5][5])
        a2.append(pmd1[3][1])
        answers.append(a2)
        p2.append(5 * 9 + 5)
        p2.append(5 * 9 + 5)
        p2.append(28)
        pmd63.append(p2)
    if 3 in between_delete:
        pmd[5][7] = 0
        pmd[4][1] = 0
        a3.append(0)
        a3.append(pmd1[5][7])
        a3.append(pmd1[4][1])
        answers.append(a3)
        p3.append(5 * 9 + 7)
        p3.append(5 * 9 + 7)
        p3.append(4 * 9 + 1)
        pmd63.append(p3)
    if 4 in between_delete:
        pmd[2][7] = 0
        pmd[4][7] = 0
        a4.append(0)
        a4.append(pmd1[2][7])
        a4.append(pmd1[4][7])
        answers.append(a4)
        p4.append(2 * 9 + 7)
        p4.append(2 * 9 + 7)
        p4.append(4 * 9 + 7)
        pmd63.append(p4)
    if 5 in between_delete:
        pmd[2][3] = 0
        pmd[0][7] = 0
        a5.append(0)
        a5.append(pmd1[2][3])
        a5.append(pmd1[0][7])
        answers.append(a5)
        p5.append(2 * 9 + 3)
        p5.append(2 * 9 + 3)
        p5.append(7)
        pmd63.append(p5)
    if 6 in between_delete:
        pmd[2][1] = 0
        pmd[1][7] = 0
        a6.append(0)
        a6.append(pmd1[2][1])
        a6.append(pmd1[1][7])
        answers.append(a6)
        p6.append(19)
        p6.append(19)
        p6.append(16)
        pmd63.append(p6)
    if 7 in between_delete:
        pmd[2][5] = 0
        pmd[3][7] = 0
        a7.append(0)
        a7.append(pmd1[2][5])
        a7.append(pmd1[3][7])
        answers.append(a7)
        p7.append(2 * 9 + 5)
        p7.append(2 * 9 + 5)
        p7.append(3 * 9 + 7)
        pmd63.append(p7)

    if 8 in between_delete:
        pmd[3][3] = 0
        pmd[1][5] = 0
        a8.append(0)
        a8.append(pmd1[3][3])
        a8.append(pmd1[1][5])
        answers.append(a8)
        p8.append(3 * 9 + 3)
        p8.append(3 * 9 + 3)
        p8.append(14)
        pmd63.append(p8)
    if 9 in between_delete:
        pmd[3][5] = 0
        pmd[4][3] = 0
        a9.append(0)
        a9.append(pmd1[3][5])
        a9.append(pmd1[4][3])
        answers.append(a9)
        p9.append(3 * 9 + 5)
        p9.append(3 * 9 + 5)
        p9.append(4 * 9 + 3)
        pmd63.append(p9)
    if 10 in between_delete:
        pmd[0][3] = 0
        pmd[4][5] = 0
        a10.append(0)
        a10.append(pmd1[0][3])
        a10.append(pmd1[4][5])
        answers.append(a10)
        p10.append(3)
        p10.append(3)
        p10.append(4 * 9 + 5)
        pmd63.append(p10)
    if 11 in between_delete:
        pmd[0][5] = 0
        pmd[1][3] = 0
        a11.append(0)
        a11.append(pmd1[0][5])
        a11.append(pmd1[1][3])
        answers.append(a11)
        p11.append(5)
        p11.append(5)
        p11.append(12)
        pmd63.append(p11)
    for i in range(distraction_cubes):
        if len(answers) >= 30:
            break
        random_num = random.choice([1, 2])
        a0 = []
        if random_num == 1 and len(between_delete) > 1:
            a0.append(0)
            a0.append(random.choice(
                random.choice(answers[len(corners_delete) - 1:len(corners_delete) + len(between_delete)])))
            randint = random.choice(
                random.choice(answers[len(corners_delete) - 1:len(corners_delete) + len(between_delete)]))
            while randint == 0:
                randint = random.choice(
                    random.choice(answers[len(corners_delete) - 1:len(corners_delete) + len(between_delete)]))
            a0.append(randint)
            answers.append(a0)
        elif len(corners_delete) > 1:
            a0.append(random.choice(random.choice(answers[:len(corners_delete)])))
            a0.append(random.choice(random.choice(answers[:len(corners_delete)])))
            a0.append(random.choice(random.choice(answers[:len(corners_delete)])))
            answers.append(a0)

    randomized_answers = []
    for i in range(len(answers)):
        random_num = random.randint(0, len(answers) - 1)
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
    return randomized_answers, pmd63, list_3d_sudoku, pmd1


def check(sudoku_list):
    for p in range(6):
        nums = []
        for m in range(9):
            nums.append(int(str((sudoku_list[p * 9 + m]).icon_entity.texture)[0]))
        if 0 in nums:
            return False
        if len(set(nums)) != 9:
            return False
    return True