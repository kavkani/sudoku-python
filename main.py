from ursina import *
import generator

app = Ursina()
punch_sound = Audio('punch_sound', loop=False, autoplay=False)
sudoku_parent = Entity(model=None, position=(-0.5, 0, 0))
home_buttons = []
sudoku_buttons = []
window.fullscreen = True


class Voxel(Button):
    def __init__(self, parent, icon, position=(0, 0, 0), rotation=(0, 0, 0), colour=color.white, size=1):
        super().__init__(
            parent=parent,
            position=position,
            model="Quad",
            origin_y=0.05,
            color=colour,
            scale=Vec2(size, size),
            rotation=rotation,
            double_sided=True,
            icon=icon)

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                punch_sound.play()


class Cube:
    def __init__(self, cube, generated, left=True, right=True, up=True, left2=True, right2=True, back=True):
        if left:
            for y in range(3):
                for x in range(3):
                    button = Voxel(cube, icon=str(generated[0][y * 3 + x]), position=(0, y, x + 0.5),
                                   rotation=(0, 90, 0), colour=color.lime)
                    sudoku_buttons.append(button)
        if right:
            for y in range(3):
                for x in range(3):
                    button = Voxel(cube, icon=str(generated[1][y * 3 + x]), position=(x + 0.5, y, 0),
                                   rotation=(0, 0, 0), colour=color.lime)
                    sudoku_buttons.append(button)
        if up:
            for y in range(3):
                for x in range(3):
                    button = Voxel(cube, icon=str(generated[2][y * 3 + x]), position=(x + 0.5, 2.45, y + 0.55),
                                   rotation=(90, 0, 0), colour=color.lime)
                    sudoku_buttons.append(button)
        if left2:
            for y in range(3):
                for x in range(3):
                    button = Voxel(parent=sudoku_parent, icon=str(generated[3][y * 3 + x]), position=(3, y, x + 0.5),
                                   rotation=(0, -90, 0), colour=color.lime)
                    sudoku_buttons.append(button)
        if right2:
            for y in range(3):
                for x in range(3):
                    button = Voxel(parent=sudoku_parent, icon=str(generated[4][y * 3 + x]), position=(x + 0.5, y, 3),
                                   rotation=(0, 180, 0), colour=color.lime)
                    sudoku_buttons.append(button)
        if back:
            for y in range(3):
                for x in range(3):
                    button = Voxel(parent=sudoku_parent, icon=str(generated[5][y * 3 + x]),
                                   position=(x + 0.5, -0.55, y + 0.45), rotation=(-90, 0, 0), colour=color.lime)
                    sudoku_buttons.append(button)


def home(scene_code=0):
    Sky(texture="bg")
    if scene_code == 1:
        for button in sudoku_buttons:
            destroy(button)
    tutorial = Button(icon='video', scale=0.13, position=(-0.7, 0.35), color=rgb(83, 221, 108))
    home_buttons.append(tutorial)
    tutorial.tooltip = Tooltip("Tutorial")
    account = Button(icon="account", scale=0.13, position=(0.7, 0.35), color=rgb(83, 221, 108))
    home_buttons.append(account)
    account.tooltip = Tooltip("Account")
    new_game = Button(icon="s4", text="Start a New 3D Sudoku", text_origin=(0, -0.45), scale=(0.54, 0.63),
                      color=rgb(64, 71, 109))
    home_buttons.append(new_game)
    new_game.on_click = Func(game)


def game():
    for button in home_buttons:
        destroy(button)
    sudoku_parent.rotation = (45, 0, -45)
    generated_sudoku = generator.generate_and_remove()
    Cube(sudoku_parent, generated_sudoku)
    back_to_home_button = Button(color=color.red, text="Back to Home", position=(0.7, 0.4))
    back_to_home_button.fit_to_text()
    sudoku_buttons.append(back_to_home_button)
    back_to_home_button.on_click = Func(home, 1)


def update():
    if mouse.right:
        sudoku_parent.rotation_x += mouse.velocity[0] * 630
        sudoku_parent.rotation_y += mouse.velocity[1] * 630


home()
app.run()
