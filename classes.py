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
                    button = Voxel(cube, icon=str(generated[3][y * 3 + x]), position=(3, y, x + 0.5),
                                   rotation=(0, -90, 0), colour=color.lime)
                    sudoku_buttons.append(button)
        if right2:
            for y in range(3):
                for x in range(3):
                    button = Voxel(cube, icon=str(generated[4][y * 3 + x]), position=(x + 0.5, y, 3),
                                   rotation=(0, 180, 0), colour=color.lime)
                    sudoku_buttons.append(button)
        if back:
            for y in range(3):
                for x in range(3):
                    button = Voxel(cube, icon=str(generated[5][y * 3 + x]),
                                   position=(x + 0.5, -0.55, y + 0.45), rotation=(-90, 0, 0), colour=color.lime)
                    sudoku_buttons.append(button)
