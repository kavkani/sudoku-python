def is_clicked(sudoku_buttons, code1, little_cubes, code2):
    sudoku_buttons[code1[0] * 9 + code1[1] * 3 + code1[2]].icon = str(little_cubes[code2[0]][code1[1]].icon)[-1]
