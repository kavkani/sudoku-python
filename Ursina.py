from ursina import *

app = Ursina()

punch_sound = Audio('punch_sound', loop=False, autoplay=False)

window.fps_counter.enabled = False
window.exit_button.visible = False


class Voxel(Button):
    def __init__(self, position=(0, 0, 0), rotation=(0, 0, 0), colour=color.white, size = 1):
        super().__init__(
            parent=scene,
            position=position,
            model="Cube",
            origin_y=0.05,
            color=colour,
            scale=Vec3(size * 0.1, size, size),
            rotation=rotation)

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                punch_sound.play()
class Cube():
    def __init__(self,pos,size,left = True , right = True , up = True):
        pos_x = pos[0]
        pos_y = pos[1]
        if left:
            for y in range(3):
                for x in range(3):
                    Voxel(position=(0, y, x + 0.5), colour=color.lime,size = size)
                    Text(text=str(x + y * 3), position=(-(x / 7) - 0.04 - y / 50, (y / 8 + x / 9) - 0.37), scale=size)
        if right:
            for y in range(3):
                for x in range(3):
                    Voxel(position=(x + 0.5, y, 0), rotation=(0, 90, 0), colour=color.orange,size = size)
                    Text(text=str(x + y * 3), position=(x / 7 + 0.03 + (2 - y) / 50, (y / 8 + x / 9) - 0.37),scale = size)
        if up:
            for y in range(3):
                for x in range(3):
                    Voxel(position=(x + 0.5, 2.5, y + 0.5), rotation=(0, 0, 90), colour=color.red,size = size)
cube = Cube([0,0],2,True,True,True)
camera.position = (-5, 10, -5)
camera.rotation = Vec3(45, 45, 0)
app.run()