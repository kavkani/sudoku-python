import random
import copy


def generate_and_remove(delete_score):
    delete_score *= 3
    delete_score_b = delete_score
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
    midles = [0,1,2,3,4,5]
    between = [0, 1, 2, 3, 4, 5, 6, 7]
    delete = []
    corners_delete = []
    midles_delete = []
    between_delete = []
    c = 0
    while delete_score > 0:
        if c == 1:
            corners = [0, 1, 2, 3, 4, 5, 6, 7]
            midles = [0,1,2,3,4,5]
            between = [0, 1, 2, 3, 4, 5, 6, 7]
            delete = []
            corners_delete = []
            midles_delete = []
            between_delete = []
            c = 0
        if delete_score < 3 :
            c = 1
        random_num = random.choice([1,2])
        if random_num == 1 and len(corners) > 0 and (delete_score-3 > -1):
            random_num = random.choice(corners)
            corners.remove(random_num)
            corners_delete.append(random_num)
            delete_score -= 3
        if random_num == 2 and len(midles) > 0 :
            random_num = random.choice(midles)
            midles.remove(random_num)
            midles_delete.append(random_num)
            delete_score -= 1
        if (random_num == 3) and (len(between) > 0) and delete_score - 2 > -1 :
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
    if 0 in corners_delete:
        pmd[0][4] = 0
        a0.append(0)
        a0.append(0)
        a0.append(pmd1[0][4])
        answers.append(a0)
        p0.append(4)
        p0.append(4)
        p0.append(4)
        pmd63.append(p0)
    if 1 in corners_delete:
        pmd[1][4] = 0
        
        a1.append(0)
        a1.append(0)
        a1.append(pmd1[1][4])
        answers.append(a1)
        p1.append(4+(1*9))
        p1.append(4+(1*9))
        p1.append(4+(1*9))
        pmd63.append(p1)
    if 2 in corners_delete:
        pmd[2][4] = 0
        
        a2.append(0)
        a2.append(0)
        a2.append(pmd1[2][4])
        answers.append(a2)
        p2.append(4+(2*9))
        p2.append(4+(2*9))
        p2.append(4+(2*9))
        pmd63.append(p2)
    if 3 in corners_delete:
        pmd[3][4] = 0
        
        a3.append(0)
        a3.append(0)
        a3.append(pmd1[3][4])
        answers.append(a3)
        p3.append(4+(3*9))
        p3.append(4+(3*9))
        p3.append(4+(3*9))
        pmd63.append(p3)
    if 4 in corners_delete:
        pmd[4][4] = 0
        
        a4.append(0)
        a4.append(0)
        a4.append(pmd1[4][4])
        answers.append(a4)
        p4.append(4+(4*9))
        p4.append(4+(4*9))
        p4.append(4+(4*9))
        pmd63.append(p4)
    if 5 in corners_delete:
        pmd[5][4] = 0
        
        a5.append(0)
        a5.append(0)
        a5.append(pmd1[5][4])
        answers.append(a5)
        p5.append(4+(5*9))
        p5.append(4+(5*9))
        p5.append(4+(5*9))
        pmd63.append(p5)
    



    

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
    print(randomized_answers)
    print(pmd63)
    print(list_3d_sudoku)
    print(pmd1)
    return randomized_answers, pmd63, list_3d_sudoku, pmd1


def extra_cubes():
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
            count = 8
        if difficulty_num == 1:
            count = 6

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


# extra_cubes()
