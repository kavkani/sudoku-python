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
            for y in range(3):
                for x in range(3):
                    button = Voxel(cube, icon=str(generated[n][y * 3 + x]), position=eval(position),
                                   rotation=rotation, colour=color.lime)
                    if generated[n][y * 3 + x] == 0:
                        button.icon = None
                    sudoku_buttons.append(button)
        if left:
            side("(0, y, x + 0.5)", (0, 90, 0), 0)
        if right:
            side("(x + 0.5, y, 0)", (0, 0, 0), 1)
        if up:
            side("(x + 0.5, 2.45, y + 0.55)", (90, 0, 0), 2)
        if left2:
            side("(3, y, x + 0.5)", (0, -90, 0), 3)
        if right2:
            side("(x + 0.5, y, 3)", (0, 180, 0), 4)
        if back:
            side("(x + 0.5, -0.55, y + 0.45)", (-90, 0, 0), 5)
        Voxel(scene, position=(2.6, 0.1, 0.5), rotation=(0, 90, 0), colour=color.lime)
        Voxel(scene, position=(3, 0.1, 0), rotation=(0, 45, 0), colour=color.red)
        Voxel(scene, position=(3, 0.4, -0), rotation=(90, 0, 0), colour=color.orange)
