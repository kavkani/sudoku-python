from ursina import *

sudoku_buttons = []
little_cubes = [[], [], [], [], [], [], [], []]
punch_sound = Audio('punch_sound', loop=False, autoplay=False)
clicked = [None, None]


class Voxel(Button):
    def __init__(self, parent, list_code, colour, icon=None, position=(0, 0, 0), rotation=(0, 0, 0), size=1):
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
        self.list_code = list_code

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                if str(self.icon)[-1] == '0':
                    clicked[0] = self.list_code


class Voxel2(Button):
    def __init__(self, parent, list_code, colour, icon="2", position=(0, 0, 0), rotation=(0, 0, 0), size=1):
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
        self.list_code = list_code

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                clicked[1] = self.list_code


class Cube:
    def __init__(self, cube, generated, left=True, right=True, up=True, left2=True, right2=True, back=True):
        b = Voxel(cube, 0, position=(0, 0, 0 + 0.5), colour=color.lime, rotation=(0, 90, 0))
        destroy(b)

        def side(position, rotation, n):
            for ii in range(3):
                for jj in range(3):
                    button = Voxel(cube, list([n, ii, jj]), icon=str(generated[n][ii][jj]), position=eval(position),
                                   rotation=rotation, colour=color.lime)
                    if generated[n][ii][jj] == 0:
                        button.icon = None
                    sudoku_buttons.append(button)

        if left:
            side("(-1.3, ii - 1.3, 2 - jj + 0.5 - 1.3)", (0, 90, 0), 0)
        if right:
            side("(jj + 0.5 - 1.3, ii - 1.3, 0 - 1.3)", (0, 0, 0), 1)
        if up:
            side("(jj + 0.5 - 1.3, 2.45 - 1.3, ii + 0.55 - 1.3)", (90, 0, 0), 2)
        if left2:
            side("(3 - 1.3, ii - 1.3, jj + 0.5 - 1.3)", (0, -90, 0), 3)
        if right2:
            side("(2 - jj + 0.5 - 1.3, ii - 1.3, 3 - 1.3)", (0, 180, 0), 4)
        if back:
            side("(jj + 0.5 - 1.3, -0.55 - 1.3, ii + 0.45 - 1.3)", (-90, 0, 0), 5)
        for i in range(3, 6, 2):
            for j in range(3, -4, -2):
                sudoku_out_parent = Entity(model=None, position=(i - 0.5, j, 0), rotation=Vec3(-45, -45, 0))
                b1 = Voxel2(sudoku_out_parent, list([(i - 3) * 2 + (3 - ((j + 3) // 2)), 0]), position=(2.5, 0.1, 0.5),
                            rotation=(0, 90, 0), colour=color.lime)
                sudoku_buttons.append(b1)
                little_cubes[(i - 3) * 2 + (3 - ((j + 3) // 2))].append(b1)
                b2 = Voxel2(sudoku_out_parent, list([(i - 3) * 2 + (3 - ((j + 3) // 2)), 1]), position=(3, 0.1, 0),
                            rotation=(0, 0, 0), colour=color.red)
                sudoku_buttons.append(b2)
                little_cubes[(i - 3) * 2 + (3 - ((j + 3) // 2))].append(b2)
                b3 = Voxel2(sudoku_out_parent, list([(i - 3) * 2 + (3 - ((j + 3) // 2)), 2]), position=(3, 0.55, 0.55),
                            rotation=(90, 0, 0), colour=color.orange)
                sudoku_buttons.append(b3)
                little_cubes[(i - 3) * 2 + (3 - ((j + 3) // 2))].append(b3)
