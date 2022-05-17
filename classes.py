from ursina import *
import generator

delete = -1
sudoku_buttons = []
little_cubes = []
clicked = [None, None]


def close_changeable():
    global sudoku_buttons, exit_button
    for button in sudoku_buttons[0:54]:
        button.color = rgb(188, 134, 90)
    destroy(exit_button)


def show_changeable(sudoku_list, changeable):
    global sudoku_buttons, exit_button
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if sudoku_list[i][j][k] == 0:
                    sudoku_buttons[i * 9 + j * 3 + k].color = rgb(255, 164, 80)
    exit_button = Button(parent=changeable, scale=(0.2, 1), position=(0.62, 0), color=rgb(54, 158, 255),
                         icon="images/close")
    exit_button.on_click = Func(close_changeable)


def output_nums():
    return generator.check(sudoku_buttons[0:54])


class Voxel(Button):
    def __init__(self, parent, list_code, generated, colour, icon=None, position=(0, 0, 0), rotation=(0, 0, 0), size=1):
        super().__init__(
            parent=parent,
            position=position,
            model="Quad",
            origin_y=0.05,
            texture="images/wood-islam",
            scale=Vec2(size, size),
            rotation=rotation,
            double_sided=True,
            color=colour,
            icon=icon)
        self.list_code = list_code
        self.little_cube = None
        self.generated = generated

    def input(self, key):
        global delete
        if self.hovered:
            if key == 'left mouse down':
                if str(self.icon_entity.texture)[0] == '0':
                    clicked[0] = self.list_code
            if key == 'backspace':
                if self.generated[self.list_code[0]][self.list_code[1]][self.list_code[2]] == 0:
                    delete = self.list_code


class Voxel2(Button):
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
            icon=icon,
            texture="images/wood-islam",
            dragable=True)
        self.list_code = list_code

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                clicked[1] = self.list_code


class Cube:
    def __init__(self, cube, little_g, generated, left=True, right=True, up=True, left2=True, right2=True, back=True):
        b = Voxel(cube, -1, generated, colour=color.lime, position=(0, 0, 0 + 0.5), rotation=(0, 90, 0))
        destroy(b)

        def side(position, rotation, n):
            for ii in range(3):
                for jj in range(3):
                    button = Voxel(cube, list([n, ii, jj]), generated, colour=rgb(188, 134, 90),
                                   icon=f'images/{str(generated[n][ii][jj])}', position=eval(position),
                                   rotation=rotation)
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
        """for i in range(3, 6, 2):
            for j in range(3, -4, -2):"""
        for idx in range(len(little_g)):
            little_cubes.append([])
            i = (idx // 4) * 2 + 3
            j = (4 - (idx % 4)) * 2 - 5
            sudoku_out_parent = Entity(model=None, position=(i - 2.2, j, 0), rotation=Vec3(-40, -35, 0))
            b1 = Voxel2(sudoku_out_parent, list([(i - 3) * 2 + (3 - ((j + 3) // 2)), 0]), position=(2.5, 0.1, 0.5),
                        rotation=(0, 90, 0), colour=rgb(188, 134, 90),
                        icon=f'images/{str(little_g[(i - 3) * 2 + (3 - ((j + 3) // 2))][0])}')
            if str(little_g[(i - 3) * 2 + (3 - ((j + 3) // 2))][0]) == "0":
                b1.hide()
                b1.disabled = True
            sudoku_buttons.append(b1)
            little_cubes[(i - 3) * 2 + (3 - ((j + 3) // 2))].append(b1)
            b2 = Voxel2(sudoku_out_parent, list([(i - 3) * 2 + (3 - ((j + 3) // 2)), 1]), position=(3, 0.1, 0),
                        rotation=(0, 0, 0), colour=rgb(188, 134, 90),
                        icon=f'images/{str(little_g[(i - 3) * 2 + (3 - ((j + 3) // 2))][1])}')
            sudoku_buttons.append(b2)
            little_cubes[(i - 3) * 2 + (3 - ((j + 3) // 2))].append(b2)
            if str(little_g[(i - 3) * 2 + (3 - ((j + 3) // 2))][1]) == '0':
                b2.hide()
                b2.disabled = True
            b3 = Voxel2(sudoku_out_parent, list([(i - 3) * 2 + (3 - ((j + 3) // 2)), 2]), position=(3, 0.55, 0.55),
                        rotation=(90, 0, 0), colour=rgb(188, 134, 90),
                        icon=f'images/{str(little_g[(i - 3) * 2 + (3 - ((j + 3) // 2))][2])}')
            sudoku_buttons.append(b3)
            if str(little_g[(i - 3) * 2 + (3 - ((j + 3) // 2))][2]) == "0":
                b3.hide()
                b3.disabled = True
            little_cubes[(i - 3) * 2 + (3 - ((j + 3) // 2))].append(b3)


class Image(Entity):
    def __init__(self, photo):
        super().__init__(
            parent=camera.ui,
            model='quad',
            position=(0.47, -0.25),
            scale=(0.842, 0.5),
            texture=photo)


exit_button = None
