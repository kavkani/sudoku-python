from ursina import *
import generator
import classes
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina(borderless=False)
window.title = "Sudoku 3D"
punch_sound = Audio('punch_sound', loop=False, autoplay=False)
sudoku_parent = Entity(model=None, position=(-0.5, 0, 0))
home_buttons = []
window.cog_button.enabled = False
window.fps_counter.enabled = False
window.exit_button.enabled = False


def home(scene_code=0):
    Sky(texture="bg")
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
    generated_sudoku = generator.generate_and_remove()
    classes.Cube(sudoku_parent, generated_sudoku)
    back_to_home_button = Button(color=color.red, text="Back to Home", position=(0.7, -0.4))
    back_to_home_button.fit_to_text()
    classes.sudoku_buttons.append(back_to_home_button)
    back_to_home_button.on_click = Func(home, 1)


def update():
    if mouse.right:
        sudoku_parent.rotation_x += mouse.velocity[0] * 630
        sudoku_parent.rotation_y += mouse.velocity[1] * 630


exit_button = Button(color=color.red, text="Quit", position=(0.81, 0.46))
exit_button.fit_to_text(0.15)
exit_button.on_click = application.quit
player = FirstPersonController()
ground = Entity(model="plane", scale=20, collider="mesh_collider")
home()
app.run()
