def is_clicked(sudoku_buttons, code1, little_cubes, code2, indexes):
    # sudoku_buttons[code1[0] * 9 + code1[1] * 3 + code1[2]].icon = str(little_cubes[code2[0]][code2[1]].icon)[-1]
    for item in indexes:
        if code1[0] * 9 + code1[1] * 3 + code1[2] in item:
            print(code1[0] * 9 + code1[1] * 3 + code1[2])
            for i in range(3):
                # if item.index(code1[0] * 9 + code1[1] * 3 + code1[2]) != i:
                print(sudoku_buttons[item[i]].icon)
                print(str(little_cubes[code2[0]][i].icon)[-1])
                sudoku_buttons[item[i]].icon = str(little_cubes[code2[0]][i].icon)[-1]
