from ursina import *
import click
import generator
import classes
import time

app = Ursina(borderless=False)
window.title = "Sudoku 3D"
punch_sound = Audio('punch_sound', loop=False, autoplay=False)
sudoku_parent = Entity(model=None, position=(-1.8, 0, 0))
home_buttons = []
window.cog_button.enabled = False
window.fps_counter.enabled = False
window.exit_button.enabled = False


def output(generated):
    if not classes.output_nums(generated):
        t = Text(text="You didn't solve the 3D Sudoku correctly")
        time.sleep(2)
        destroy(t)
    else:
        home(1)


def home(scene_code=0):
    if scene_code == 1:
        for button in classes.sudoku_buttons:
            destroy(button)
    tutorial = Button(icon='video', scale=0.13, position=(-0.7, 0.35), color=rgb(83, 221, 108))
    home_buttons.append(tutorial)
    tutorial.tooltip = Tooltip("Tutorial")
    account = Button(icon="account", scale=0.13, position=(0.7, 0.35), color=rgb(83, 221, 108))
    home_buttons.append(account)
    account.tooltip = Tooltip("Account")
    new_game = Button(icon="s4", text="Start a New 3D Sudoku", text_origin=(0, -0.45), scale=(0.49, 0.6),
                      color=rgb(64, 71, 109))
    home_buttons.append(new_game)
    new_game.on_click = Func(game)


def game():
    for button in home_buttons:
        destroy(button)
    sudoku_parent.rotation = (45, 0, -45)
    global indexes
    numbers, indexes, generated_sudoku = generator.generate_and_remove()
    check_button = Button(text="Check", color=color.red, position=(0.7, -0.4))
    check_button.fit_to_text()
    check_button.on_click = Func(output, generated_sudoku)
    classes.Cube(sudoku_parent, numbers, generated_sudoku)
    classes.sudoku_buttons.append(check_button)
    back_to_home_button = Button(color=color.red, text="Back to Home", position=(-0.7, 0.4))
    back_to_home_button.fit_to_text()
    classes.sudoku_buttons.append(back_to_home_button)
    back_to_home_button.on_click = Func(home, 1)


def update():
    if mouse.right:
        sudoku_parent.rotation_x += mouse.velocity[0] * 630
        sudoku_parent.rotation_y += mouse.velocity[1] * 630
    if classes.clicked[0] is not None and classes.clicked[1] is not None:
        click.is_clicked(classes.sudoku_buttons, classes.clicked[0], classes.little_cubes, classes.clicked[1], indexes)
        classes.clicked = [None, None]
    if classes.delete != -1:
        click.cancel(classes.sudoku_buttons, classes.delete, classes.little_cubes, indexes)


home()
app.run()
