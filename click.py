def is_clicked(sudoku_buttons, code1, little_cubes, code2, indexes):
    for item in indexes:
        if code1[0] * 9 + code1[1] * 3 + code1[2] in item:
            number = item.index(code1[0] * 9 + code1[1] * 3 + code1[2])
            c1 = number
            c2 = code2[1]
            zeros = 0
            non_zeros = []
            for i in range(3):
                if str(little_cubes[code2[0]][i].icon)[-1] == "0":
                    zeros += 1
                else:
                    non_zeros.append(str(little_cubes[code2[0]][i].icon))
            """if (zeros == 0 and item[0] == item[1]) or (zeros == 2 and item[0] != item[1]):
                return None"""
            if zeros == 0:
                if item[0] % 9 not in [0, 2, 6, 8]:
                    return None
                for i in range(3):
                    if c1 > 2:
                        c1 = 0
                    if c2 > 2:
                        c2 = 0
                    print(str(little_cubes[code2[0]][c2].icon))
                    sudoku_buttons[item[c1]].icon = f'images/{str(little_cubes[code2[0]][c2].icon)[-1]}'
                    sudoku_buttons[item[c1]].little_cube = little_cubes[code2[0]][i]
                    c1 += 1
                    c2 += 1
            if zeros == 1:
                if item[0] % 9 not in [1, 3, 5, 7]:
                    return None
                sudoku_buttons[item[c1]].icon = f'images/{str(little_cubes[code2[0]][c2].icon)[-1]}'
                sudoku_buttons[item[c1]].little_cube = little_cubes[code2[0]][c2]
                c1 = abs(c1 - 2)
                if c2 == 2:
                    c2 = 1
                else:
                    c2 = 2
                sudoku_buttons[item[c1]].icon = f'images/{str(little_cubes[code2[0]][c2].icon)[-1]}'
                sudoku_buttons[item[c1]].little_cube = little_cubes[code2[0]][c2]
            if zeros == 2:
                if item[0] % 9 != 4:
                    return None
                sudoku_buttons[item[0]].icon = f'images/{str(non_zeros[0])[-1]}'
                for i in range(3):
                    sudoku_buttons[item[0]].little_cube = little_cubes[code2[0]][i]
    for i in range(3):
        little_cubes[code2[0]][i].disabled = True
        little_cubes[code2[0]][i].hide()


def cancel(sudoku_buttons, code1, little_cubes, indexes):
    for little_cube in indexes:
        if code1[0] * 9 + code1[1] * 3 + code1[2] in little_cube:
            corner = little_cube
    for i in corner:
        sudoku_buttons[i].icon = 'images/0'
    for cube in little_cubes:
        if sudoku_buttons[corner[0]].little_cube in cube:
            for i in range(3):
                if str(cube[i].icon)[-1] != "0":
                    cube[i].disabled = False
                    cube[i].show()
    return corner
