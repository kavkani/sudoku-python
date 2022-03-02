from ursina import *
import Generator

app = Ursina()
punch_sound = Audio('punch_sound', loop=False, autoplay=False)


class Voxel(Button):
    def __init__(self, cube, icon="sword", position=(0, 0, 0), rotation=(0, 0, 0), colour=color.white, size=1):
        super().__init__(
            parent=cube,
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
    def __init__(self, cube, left=True, right=True, up=True, left2=True, right2=True, back=True):
        if left:
            for y in range(3):
                for x in range(3):
                    Voxel(cube, position=(0, y, x + 0.5), icon=str(Generator.pmd[0][y * 3 + x]), colour=color.lime,
                          rotation=(0, 90, 0))
        if right:
            for y in range(3):
                for x in range(3):
                    Voxel(cube, position=(x + 0.5, y, 0), icon=str(Generator.pmd[1][y * 3 + x]), rotation=(0, 0, 0),
                          colour=color.orange)
        if up:
            for y in range(3):
                for x in range(3):
                    Voxel(cube, position=(x + 0.5, 2.45, y + 0.55), icon=str(Generator.pmd[2][y * 3 + x]),
                          rotation=(90, 0, 0), colour=color.red)
        if left2:
            for y in range(3):
                for x in range(3):
                    Voxel(cube, position=(3, y, x + 0.5), icon=str(Generator.pmd[3][y * 3 + x]), colour=color.lime,
                          rotation=(0, -90, 0))
        if right2:
            for y in range(3):
                for x in range(3):
                    Voxel(cube, position=(x + 0.5, y, 3), icon=str(Generator.pmd[4][y * 3 + x]),
                          rotation=(0, 180, 0),
                          colour=color.orange)
        if back:
            for y in range(3):
                for x in range(3):
                    Voxel(cube, position=(x + 0.5, -0.55, y + 0.45), icon=str(Generator.pmd[5][y * 3 + x]),
                          rotation=(-90, 0, 0), colour=color.red)


def home(code=0):
    window.fullscreen = True
    Sky(texture="bg")
    if code == 1:
        scene.clear()
    tutorial = Button(icon='video', scale=0.13, position=(-0.7, 0.35), color=rgb(83, 221, 108))
    tutorial.tooltip = Tooltip("Tutorial")
    account = Button(icon="account", scale=0.13, position=(0.7, 0.35), color=rgb(83, 221, 108))
    account.tooltip = Tooltip("Account")
    new_game = Button(icon="s4", text="Start a New 3D Sudoku", text_origin=(0, -0.45), scale=(0.54, 0.63),
                      color=rgb(64, 71, 109))
    new_game.on_click = Func(game)


def game():
    def exit_code():
        global exit_c
        exit_c = 1
        home(1)
    exit_c = 0
    scene.clear()
    Sky(texture="bg")
    window.fps_counter.enabled = False
    window.exit_button.visible = False
    c = Entity(model=None)

    def update():
        if mouse.right:
            c.rotation_x += mouse.velocity[0] * 630
            c.rotation_y += mouse.velocity[1] * 630
        Cube(c)
    exit_b = Button(position=(2, 2), scale=0.3, text="Back to Home")
    exit_b.on_click = Func(exit_code)
    while exit_c == 0:
        update()

    print(Generator.pmd)


home()
app.run()
