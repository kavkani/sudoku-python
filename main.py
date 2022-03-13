from ursina import *
import click
import generator
import classes

app = Ursina(borderless=False)
window.title = "Sudoku 3D"
punch_sound = Audio('punch_sound', loop=False, autoplay=False)
sudoku_parent = Entity(model=None, position=(-1.8, 0, 0))
home_buttons = []
window.cog_button.enabled = False
window.fps_counter.enabled = False
window.exit_button.enabled = False


def about():
    rect = Entity(model="quad", scale=(3, 1))
    # photo = Button(icon=)


def solver(solved):
    for i in range(6):
        for j in range(9):
            classes.sudoku_buttons[i * 9 + j].icon = str(solved[i][j])
            classes.sudoku_buttons[i * 9 + j].disabled = True
    for item in classes.sudoku_buttons[54: 80]:
        classes.sudoku_buttons.pop(classes.sudoku_buttons.index(item))
        destroy(item)


def after_check(t=None, ok_b=None):
    if t is None:
        for button in classes.sudoku_buttons[:-1]:
            destroy(button)
            classes.sudoku_buttons = []
        t = Text(text="Congratulations!", color=color.red, size=2, position=(-0.3, -0.4))
        home_buttons.append(t)
    else:
        destroy(t)
        destroy(ok_b)


def output(solved):
    if not classes.output_nums(solved):
        print("You didn't solve the 3D Sudoku correctly")
        t = Text(text="You didn't solve the 3D Sudoku correctly", color=color.red, scale=1.25, position=(-0.5, -0.4))
        ok_button = Button(text="OK", color=color.red, position=(0.15, -0.42))
        ok_button.fit_to_text()
        ok_button.on_click = Func(after_check, t, ok_button)
    else:
        after_check()


def home(scene_code=0):
    """if login_code == 1:
        t = Text(text="Please login first.", scale=2, position=(-0.2, 0))
        import login
        while quit_code == 0:
            pass
        destroy(t)"""
    if scene_code == 1:
        for button in classes.sudoku_buttons:
            destroy(button)
            classes.sudoku_buttons = []
    tutorial = Button(icon='video', scale=0.13, position=(-0.7, 0.35), color=rgb(255, 151, 54))
    home_buttons.append(tutorial)
    tutorial.tooltip = Tooltip("Tutorial")
    account = Button(icon="account", scale=0.13, position=(0.7, 0.35), color=rgb(255, 151, 54))
    home_buttons.append(account)
    account.tooltip = Tooltip("Account")
    new_game = Button(icon="s4", text_origin=(0, -0.45), scale=(0.45, 0.55),
                      color=rgb(54, 158, 255), position=(0, -0.1))
    t = Text(text="Start a 3D Sudoku", parent=new_game, position=(-0.3, -0.35), scale=3)
    about_us = Button(text="About us", position=(0, 0.25), color=rgb(255, 151, 54))
    about_us.fit_to_text()
    # about_us.on_click = Func(about)
    home_buttons.append(new_game)
    home_buttons.append(t)
    home_buttons.append(about_us)
    new_game.on_click = Func(game)


def game():
    for button in home_buttons:
        destroy(button)
    sudoku_parent.rotation = (45, 0, -45)
    global indexes
    numbers, indexes, generated_sudoku, correct_answers = generator.generate_and_remove()
    check_button = Button(text="Check", color=rgb(54, 158, 255), position=(-0.6, -0.45))
    check_button.fit_to_text()
    classes.Cube(sudoku_parent, numbers, generated_sudoku)
    check_button.on_click = Func(output, correct_answers)
    classes.sudoku_buttons.append(check_button)
    solve = Button(text="Solve", color=rgb(54, 158, 255), position=(-0.75, -0.45))
    solve.fit_to_text()
    solve.on_click = Func(solver, correct_answers)
    classes.sudoku_buttons.append(solve)
    back_to_home_button = Button(color=rgb(255, 151, 54), text="Back to Home", position=(-0.7, 0.4))
    back_to_home_button.fit_to_text()
    classes.sudoku_buttons.append(back_to_home_button)
    back_to_home_button.on_click = Func(home, 1)


def update():
    if mouse.right:
        sudoku_parent.rotation_x = mouse.velocity[1] * 630
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
