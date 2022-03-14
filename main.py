from ursina import *
import click
import generator
import classes

app = Ursina(borderless=False)
window.title = "Sudoku 3D"
punch_sound = Audio('punch_sound', loop=False, autoplay=False)
sudoku_parent = Entity(model=None, position=(-1.8, 0, 0))
window.cog_button.enabled = False
window.fps_counter.enabled = False
window.exit_button.enabled = False


def difficulty(num):
    game(num)


def difficulty_show(d_l):
    for item in d_l:
        item.disabled = False
        item.show()


def to_home(a_l):
    for item in a_l:
        destroy(item)
    home()


def about():
    global home_buttons
    for button in home_buttons[:-1]:
        destroy(button)
    for button in home_buttons[-1]:
        destroy(button)
    home_buttons = []
    about_list = []
    photo1 = Button(icon="amirmohammad", scale=0.25, position=(-0.3, 0.3))
    about_list.append(photo1)
    t1 = Text(text="Amirmohammad Kavkani", scale=3, position=(-0.15, 0.4), color=rgb(255, 164, 80),
              font='TheGodfather-v2.ttf')
    about_list.append(t1)
    d1 = Text(text="AI Department", scale=1.75, position=(-0.15, 0.3), color=rgb(255, 151, 54),
              font='SelfDestructButtonBB_reg.ttf')
    about_list.append(d1)
    photo2 = Button(icon="arash", scale=0.25, position=(-0.3, 0))
    about_list.append(photo2)
    t2 = Text(text="Arash Ostadsharif", scale=3, position=(-0.15, 0.1), color=rgb(255, 164, 80),
              font='TheGodfather-v2.ttf')
    about_list.append(t2)
    d2 = Text(text="Database Department", scale=1.75, position=(-0.15, 0), color=rgb(255, 151, 54),
              font='SelfDestructButtonBB_reg.ttf')
    about_list.append(d2)
    photo3 = Button(icon="bardia", scale=0.25, position=(-0.3, -0.3))
    about_list.append(photo3)
    t3 = Text(text="Bardia Sohrabi", scale=3, position=(-0.15, -0.2), color=rgb(255, 164, 80),
              font='TheGodfather-v2.ttf')
    about_list.append(t3)
    d3 = Text(text="Graphics Department", scale=1.75, position=(-0.15, -0.3), color=rgb(255, 151, 54),
              font='SelfDestructButtonBB_reg.ttf')
    about_list.append(d3)
    back = Button(color=rgb(255, 151, 54), text="Back", position=(-0.7, 0.4))
    back.fit_to_text()
    about_list.append(back)
    back.on_click = Func(to_home, about_list)


def solver(solved,little_cubes_count):
    for i in range(6):
        for j in range(9):
            classes.sudoku_buttons[i * 9 + j].icon = str(solved[i][j])
            classes.sudoku_buttons[i * 9 + j].disabled = True
    back_to_home_button = classes.sudoku_buttons[54+little_cubes_count*3+2]
    for item in classes.sudoku_buttons[54: 54+little_cubes_count*3+5]:
        if item != back_to_home_button:
            classes.sudoku_buttons.pop(classes.sudoku_buttons.index(item))
            destroy(item)


def after_check(t=None, ok_b=None):
    if t is None:
        for button in classes.sudoku_buttons[:-1]:
            destroy(button)
        classes.sudoku_buttons = []
        classes.little_cubes = [[], [], [], [], [], [], [], []]
        t = Text(text="Congratulations!", color=color.red, size=2, position=(-0.3, -0.4))
        home_buttons.append(t)
    else:
        destroy(t)
        destroy(ok_b)


def output(solved):
    if not classes.output_nums(solved):
        t = Text(text="You didn't solve the 3D Sudoku correctly", color=color.red, scale=1.25, position=(-0.5, -0.4))
        ok_button = Button(text="OK", color=color.red, position=(0.15, -0.42))
        ok_button.fit_to_text()
        ok_button.on_click = Func(after_check, t, ok_button)
        classes.sudoku_buttons.append(t)
        classes.sudoku_buttons.append(ok_button)
    else:
        after_check()


def home(scene_code=0):
    global home_buttons
    home_buttons = []
    if scene_code == 1:
        for button in classes.sudoku_buttons:
            destroy(button)
        classes.sudoku_buttons = []
        classes.little_cubes = [[], [], [], [], [], [], [], []]
    tutorial = Button(icon='video', scale=0.13, position=(-0.7, 0.35), color=rgb(255, 151, 54))
    home_buttons.append(tutorial)
    tutorial.tooltip = Tooltip("Tutorial")
    account = Button(icon="account", scale=0.13, position=(0.7, 0.35), color=rgb(255, 151, 54))
    home_buttons.append(account)
    account.tooltip = Tooltip("Account")
    new_game = Button(icon="s4", scale=(0.45, 0.55), color=rgb(54, 158, 255), position=(0, -0.05))
    t = Text(text="New Game", parent=new_game, position=(-0.2, -0.35), scale=5, font='Soulgood.ttf')
    about_us = Button(text="About us", position=(0, 0.3), color=rgb(255, 151, 54))
    about_us.fit_to_text()
    about_us.on_click = Func(about)
    home_buttons.append(new_game)
    home_buttons.append(t)
    home_buttons.append(about_us)
    sudoku = Text(text="3D Sudoku", position=(-0.23, 0.45), scale=5, color=rgb(54, 158, 255), font='Soulgood.ttf')
    home_buttons.append(sudoku)
    home_buttons.append(['0'])
    del home_buttons[-1][0]
    easy = Button(text="Easy", position=(-0.107, -0.35), color=rgb(255, 151, 54), disabled=True)
    easy.fit_to_text()
    easy.hide()
    easy.on_click = Func(difficulty, 4)
    home_buttons[-1].append(easy)
    medium = Button(text="Medium", position=(0, -0.35), color=rgb(255, 151, 54), disabled=True)
    medium.hide()
    medium.fit_to_text()
    medium.on_click = Func(difficulty, 6)
    home_buttons[-1].append(medium)
    hard = Button(text="Hard", position=(0.11, -0.35), color=rgb(255, 151, 54), disabled=True)
    hard.hide()
    hard.fit_to_text()
    hard.on_click = Func(difficulty, 8)
    home_buttons[-1].append(hard)
    new_game.on_click = Func(difficulty_show, home_buttons[-1])


def game(d):
    global home_buttons
    for button in home_buttons[:-1]:
        destroy(button)
    for button in home_buttons[-1]:
        destroy(button)
    home_buttons = []
    sudoku_parent.rotation = (45, 0, -45)
    global indexes
    numbers, indexes, generated_sudoku, correct_answers = generator.generate_and_remove(d)
    check_button = Button(text="Check", color=rgb(54, 158, 255), position=(-0.6, -0.45))
    check_button.fit_to_text()
    classes.Cube(sudoku_parent, numbers, generated_sudoku)
    check_button.on_click = Func(output, correct_answers)
    classes.sudoku_buttons.append(check_button)
    solve = Button(text="Solve", color=rgb(54, 158, 255), position=(-0.75, -0.45))
    solve.fit_to_text()
    solve.on_click = Func(solver, correct_answers,d)
    classes.sudoku_buttons.append(solve)
    back_to_home_button = Button(color=rgb(255, 151, 54), text="Back to Home", position=(-0.7, 0.4))
    back_to_home_button.fit_to_text()
    classes.sudoku_buttons.append(back_to_home_button)
    back_to_home_button.on_click = Func(home, 1)


def update():
    if mouse.right:
        sudoku_parent.rotation_x += mouse.velocity[1] * 630
        sudoku_parent.rotation_y += mouse.velocity[0] * 630
    if classes.clicked[0] is not None and classes.clicked[1] is not None:
        click.is_clicked(classes.sudoku_buttons, classes.clicked[0], classes.little_cubes, classes.clicked[1], indexes)
        classes.clicked = [None, None]
    if classes.delete != -1:
        c = click.cancel(classes.sudoku_buttons, classes.delete, classes.little_cubes, indexes)
        classes.delete = -1
        classes.clicked = [None, None]
        for i in range(3):
            (classes.sudoku_buttons[c[i]]).little_cube = None


home()
app.run()
