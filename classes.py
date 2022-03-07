from ursina import *

sudoku_buttons = []
punch_sound = Audio('punch_sound', loop=False, autoplay=False)


class Voxel(Button):
    def __init__(self, parent, icon=None, position=(0, 0, 0), rotation=(0, 0, 0), colour=color.white, size=1):
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
        b = Voxel(cube, position=(0, 0, 0 + 0.5), colour=color.lime, rotation=(0, 90, 0))
        destroy(b)

        def side(position, rotation, n):
            for i in range(3):
                for j in range(3):
                    button = Voxel(cube, icon=str(generated[n][i][j]), position=eval(position),
                                   rotation=rotation, colour=color.lime)
                    if generated[n][i][j] == 0:
                        button.icon = None
                    sudoku_buttons.append(button)
        if left:
            side("(0, i, 2 - j + 0.5)", (0, 90, 0), 0)
        if right:
            side("(j + 0.5, i, 0)", (0, 0, 0), 1)
        if up:
            side("(j + 0.5, 2.45, i + 0.55)", (90, 0, 0), 2)
        if left2:
            side("(3, i, j + 0.5)", (0, -90, 0), 3)
        if right2:
            side("(2 - j + 0.5, i, 3)", (0, 180, 0), 4)
        if back:
            side("(j + 0.5, -0.55, i + 0.45)", (-90, 0, 0), 5)
        sudoku_out_parent = Entity(model=None, position=(-0.5, 0, 0), rotation=Vec3(-45, -45, 0))
        b1 = Voxel(sudoku_out_parent, position=(2.5, 0.1, 0.5), rotation=(0, 90, 0), colour=color.lime)
        sudoku_buttons.append(b1)
        b2 = Voxel(sudoku_out_parent, position=(3, 0.1, 0), rotation=(0, 0, 0), colour=color.red)
        sudoku_buttons.append(b2)
        b3 = Voxel(sudoku_out_parent, position=(3, 0.55, 0.55), rotation=(90, 0, 0), colour=color.orange)
        sudoku_buttons.append(b3)
