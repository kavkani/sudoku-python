from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

punch_sound = Audio('punch_sound', loop=False, autoplay=False)

window.fps_counter.enabled = False
window.exit_button.visible = False


class Voxel(Button):
    def __init__(self, position=(0, 0, 0), rotation=(0, 0, 0), colour=color.white, size=1):
        super().__init__(
            parent=scene,
            position=position,
            model="Cube",
            origin_y=0.05,
            color=colour,
            scale=Vec3(size * 0.1, size, size),
            rotation=rotation,
            text="1",
            text_rotation=rotation)

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                punch_sound.play()


class Cube:
    def __init__(self, left=True, right=True, up=True):
        if left:
            for y in range(3):
                for x in range(3):
                    Voxel(position=(0, y, x + 0.5), colour=color.lime)
                    # Text(text=str(x + y * 3), position=(-(x / 7) - 0.04 - (y / 50), (y / 8 + x / 9) - 0.37))
        if right:
            for y in range(3):
                for x in range(3):
                    Voxel(position=(x + 0.5, y, 0), rotation=(0, 90, 0), colour=color.orange)
                    Text(text=str(x + y * 3), position=(x + 0.5, y, 0), parent=scene)
        if up:
            for y in range(3):
                for x in range(3):
                    Voxel(position=(x + 0.5, 2.5, y + 0.5), rotation=(0, 0, 90), colour=color.red)


cube = Cube()
ground = Entity(model='plane',
                color=color.gold,
                texture='white_cube',
                collider='mesh',
                scale=(20, 1, 20))
player = FirstPersonController(scale=2)
# camera.position = (-5, 10, -5)
# camera.rotation = Vec3(45, 45, 0)
app.run()
