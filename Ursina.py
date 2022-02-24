from ursina import *

app = Ursina()

punch_sound = Audio('assets/punch_sound', loop=False, autoplay=False)
num_pick = 1

window.fps_counter.enabled = False
window.exit_button.visible = False


class Voxel(Button):
    def __init__(self, position=(0, 0, 0), rotation=(0, 0, 0), colour=color.white):
        super().__init__(
            parent=scene,
            position=position,
            model="Cube",
            origin_y=0.05,
            color=colour,
            scale=Vec3(0.1, 1, 1),
            rotation=rotation)

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                punch_sound.play()


for xy in range(3):
    for xx in range(3):
        Voxel(position=(0, xy, xx + 0.5), colour=color.green)
        Text(text=str(xx), position=(-(xx / 7) - 0.04 - xy / 50, (xy / 8 + xx / 9) - 0.37))
for xy in range(3):
    for xx in range(3):
        if xy == 0:
            Voxel(position=(xx + 0.5, xy, 0), rotation=(0, 90, 0), colour=color.white)
        elif xx == 2:
            Voxel(position=(xx + 0.5, xy, 0), rotation=(0, 90, 0), colour=color.black)
        else:
            Voxel(position=(xx + 0.5, xy, 0), rotation=(0, 90, 0), colour=color.blue)
        Text(text=str(xx), position=(xx / 7 + 0.03 + xy / 50, (xy / 8 + xx / 9) - 0.37))
for xy in range(3):
    for xx in range(3):
        Voxel(position=(xx + 0.5, 2.5, xy + 0.5), rotation=(0, 0, 90), colour=color.red)


camera.position = (-5, 10, -5)
camera.rotation = Vec3(45, 45, 0)
app.run()
