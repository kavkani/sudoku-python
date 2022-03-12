import time


def is_clicked(sudoku_buttons, code1, little_cubes, code2, indexes):
    for item in indexes:
        if code1[0] * 9 + code1[1] * 3 + code1[2] in item:
            number = item.index(code1[0] * 9 + code1[1] * 3 + code1[2])
            c1 = number
            c2 = code2[1]
            for i in range(3):
                if c1 > 2:
                    c1 = 0
                if c2 > 2:
                    c2 = 0
                sudoku_buttons[item[c1]].icon = str(little_cubes[code2[0]][c2].icon)[-1]
                sudoku_buttons[item[c1]].little_cube = little_cubes[code2[0]][i]
                c1 += 1
                c2 += 1
    for i in range(3):
        little_cubes[code2[0]][i].disabled = True
        little_cubes[code2[0]][i].hide()


def cancel(sudoku_buttons, code1, little_cubes, indexes):
    for little_cube in indexes:
        if code1[0] * 9 + code1[1] * 3 + code1[2] in little_cube:
            corner = little_cube
    for i in corner:
        sudoku_buttons[i].icon = '0'
    for cube in little_cubes:
        if sudoku_buttons[corner[0]].little_cube in cube:
            print("lefbede")
            for i in range(3):
                cube[i].disabled = False
                cube[i].show()
    print(2)
    return corner
