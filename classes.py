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
        self.generated = generated
        self.cube = cube
        destroy(b)
        if left:
<<<<<<< Updated upstream
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
        for i in range(3, 6, 2):
            for j in range(3, -4, -2):
                sudoku_out_parent = Entity(model=None, position=(i - 0.5, j, 0), rotation=Vec3(-45, -45, 0))
                b1 = Voxel(sudoku_out_parent, position=(2.5, 0.1, 0.5), rotation=(0, 90, 0), colour=color.lime)
                sudoku_buttons.append(b1)
                b2 = Voxel(sudoku_out_parent, position=(3, 0.1, 0), rotation=(0, 0, 0), colour=color.red)
                sudoku_buttons.append(b2)
                b3 = Voxel(sudoku_out_parent, position=(3, 0.55, 0.55), rotation=(90, 0, 0), colour=color.orange)
                sudoku_buttons.append(b3)
=======
            self.side("(- 1.3, i - 1.3, 2 - j + 0.5 - 1.3)", (0, 90, 0), 0)
        if right:
            self.side("(j + 0.5 - 1.3, i - 1.3, 0 - 1.3)", (0, 0, 0), 1)
        if up:
            self.side("(j + 0.5 - 1.3, 2.45 - 1.3, i + 0.55 - 1.3)", (90, 0, 0), 2)
        if left2:
            self.side("(3 - 1.3, i - 1.3, j + 0.5 - 1.3)", (0, -90, 0), 3)
        if right2:
            self.side("(2 - j + 0.5 - 1.3, i - 1.3, 3 - 1.3)", (0, 180, 0), 4)
        if back:
            self.side("(j + 0.5 - 1.3, -0.55 - 1.3, i + 0.45 - 1.3)", (-90, 0, 0), 5)
        for i in range(8):
            parent = Entity(model=None, position=(4+(i//4)*2, 3-(i%4)*2, 0.5))
            self.button(parent,i)

    def side(self,position, rotation, n):
        generated = self.generated
        cube = self.cube
        for i in range(3):
            for j in range(3):
                button = Voxel(cube, icon=str(generated[n][i][j]), position=eval(position),
                               rotation=rotation, colour=color.lime)
                if generated[n][i][j] == 0:
                    button.icon = None
                sudoku_buttons.append(button)
    def button(self,parent,n):
        Voxel( position=(-0.5, 0, 0.5), rotation=(0, 90, 0), colour=color.lime , icon='1',parent=parent)
        Voxel( position=(0, 0, 0), rotation=(0, 0, 0), colour=color.red, icon='2',parent=parent)
        Voxel( position=(0, 0.45, 0.55), rotation=(90, 0, 0), colour=color.orange, icon='3',parent=parent)
        parent.rotation = (-34.0429, 685.938, 0)
>>>>>>> Stashed changes
