from ursina import *
import very_easy_table
import Solver

app = Ursina()


def answer():
    result = []
    for a in range(9):
        r2 = []
        for b in range(9):
            if b_list[a * 9 + b].text == None:
                r2.append(0)
            else:
                r2.append(int(b_list[a * 9 + b].text))
        result.append(r2)
    print(result)
    solved = Solver.solver(result)
    print(solved)
    for num in nums:
        destroy(num)
    destroy(mic)
    destroy(deselect)
    destroy(check)
    destroy(solve)
    for a in range(9):
        for b in range(9):
            b_list[a * 9 + b].text = str(solved[a][b])
            b_list[a * 9 + b].text_color = color.lime
            b_list[a * 9 + b].disabled = True
    menu = Button(text="Back to Main Menu", position=(0.6, -0.36), color=color.orange)
    menu.fit_to_text(radius=0.005)


def enable(bx, t=0):
    b_list[bx].color = color.black
    if t != 0:
        b_list[bx].text = t
    for item in b_list:
        if item.text == None or item.text_color == color.white:
            item.disabled = False
    for num in nums:
        num.disabled = True
    deselect.disabled = True


def click(b, bx):
    global nums, b_list, deselect
    if b.text == None or b.text_color == color.white:
        for item in b_list:
            if item != b_list[bx]:
                item.disabled = True
        b_list[bx].color = color.yellow
        for num in nums:
            num.disabled = False
            num.on_click = Func(enable, bx, num.text)
        deselect.disabled = False
        deselect.on_click = Func(enable, bx)
    return 0


b_list = []
mic = Button(icon="mic", scale=0.06, position=(0.6, -0.215), color=color.blue, disabled=True)
deselect = Button(icon="deselect1", scale=0.06, position=(0.6, -0.29), color=color.blue, disabled=True)
check = Button(text="Check", position=(0.6, -0.37), scale=(0.16, 0.08), color=color.orange)
solve = Button(text="Show Answer", position=(0.6, -0.46))
solve.fit_to_text(radius=0.005)
solve.on_click = Func(answer)
y = 0.46
nums = []
for i in range(9):
    number = Button(text=str(i + 1), scale=0.06, position=(0.6, y), color=color.blue, disabled=True)
    number.pressed_color = color.blue
    nums.append(number)
    y -= 0.075
y = 0.441
final = very_easy_table.generate_table()
for i in range(9):
    x = -0.575
    for j in range(9):
        button = Button(scale=0.105, position=(x, y), highlight_color=color.lime, color=color.black,
                        text_color=color.white)
        if final[i][j] != 0:
            button.text = str(final[i][j])
            button.text_color = color.lime
            button.disabled = True
        b_list.append(button)
        button.on_click = Func(click, button, i * 9 + j)
        if (j + 1) % 3 == 0:
            x += 0.114
        else:
            x += 0.105
    if (i + 1) % 3 == 0:
        y -= 0.114
    else:
        y -= 0.105
window.fullscreen = True
Sky(texture="bg5")
app.run()
