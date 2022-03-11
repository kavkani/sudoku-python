from ursina import *

app = Ursina()
little_cubes = [[Entity(name=''voxel2'', position=Vec3(2.5, 0.1, 0.5), rotation=Vec3(0, 90, 0), model='Quad', origin=Vec3(0, 0.05, 0), color=Color(0.5, 1.0, 0.0, 1.0), collider='box', ), Entity(name=''voxel2'', position=Vec3(3, 0.1, 0), model='Quad', origin=Vec3(0, 0.05, 0), color=Color(1.0, 0.0, 0.0, 1.0), collider='box', ), Entity(name=''voxel2'', position=Vec3(3, 0.55, 0.55), rotation=Vec3(90, 0, 0), model='Quad', origin=Vec3(0, 0.05, 0), color=Color(1.0, 0.5, 0.0, 1.0), collider='box', )], [Entity(name=''voxel2'', position=Vec3(2.5, 0.1, 0.5), rotation=Vec3(0, 90, 0), model='Quad', origin=Vec3(0, 0.05, 0), color=Color(0.5, 1.0, 0.0, 1.0), collider='box', ), Entity(name=''voxel2'', position=Vec3(3, 0.1, 0), model='Quad', origin=Vec3(0, 0.05, 0), color=Color(1.0, 0.0, 0.0, 1.0), collider='box', ), Entity(name=''voxel2'', position=Vec3(3, 0.55, 0.55), rotation=Vec3(90, 0, 0), model='Quad', origin=Vec3(0, 0.05, 0), color=Color(1.0, 0.5, 0.0, 1.0), collider='box', )], [Entity(name=''voxel2'', position=Vec3(2.5, 0.1, 0.5), rotation=Vec3(0, 90, 0), model='Quad', origin=Vec3(0, 0.05, 0), color=Color(0.5, 1.0, 0.0, 1.0), collider='box', ), Entity(name=''voxel2'', position=Vec3(3, 0.1, 0), model='Quad', origin=Vec3(0, 0.05, 0), color=Color(1.0, 0.0, 0.0, 1.0), collider='box', ), Entity(name=''voxel2'', position=Vec3(3, 0.55, 0.55), rotation=Vec3(90, 0, 0), model='Quad', origin=Vec3(0, 0.05, 0), color=Color(1.0, 0.5, 0.0, 1.0), collider='box', )], [Entity(name=''voxel2'', position=Vec3(2.5, 0.1, 0.5), rotation=Vec3(0, 90, 0), model='Quad', origin=Vec3(0, 0.05, 0), color=Color(0.5, 1.0, 0.0, 1.0), collider='box', ), Entity(name=''voxel2'', position=Vec3(3, 0.1, 0), model='Quad', origin=Vec3(0, 0.05, 0), color=Color(1.0, 0.0, 0.0, 1.0), collider='box', ), Entity(name=''voxel2'', position=Vec3(3, 0.55, 0.55), rotation=Vec3(90, 0, 0), model='Quad', origin=Vec3(0, 0.05, 0), color=Color(1.0, 0.5, 0.0, 1.0), collider='box', )], [Entity(name=''voxel2'', position=Vec3(2.5, 0.1, 0.5), rotation=Vec3(0, 90, 0), model='Quad', origin=Vec3(0, 0.05, 0), color=Color(0.5, 1.0, 0.0, 1.0), collider='box', ), Entity(name=''voxel2'', position=Vec3(3, 0.1, 0), model='Quad', origin=Vec3(0, 0.05, 0), color=Color(1.0, 0.0, 0.0, 1.0), collider='box', ), Entity(name=''voxel2'', position=Vec3(3, 0.55, 0.55), rotation=Vec3(90, 0, 0), model='Quad', origin=Vec3(0, 0.05, 0), color=Color(1.0, 0.5, 0.0, 1.0), collider='box', )], [Entity(name=''voxel2'', position=Vec3(2.5, 0.1, 0.5), rotation=Vec3(0, 90, 0), model='Quad', origin=Vec3(0, 0.05, 0), color=Color(0.5, 1.0, 0.0, 1.0), collider='box', ), Entity(name=''voxel2'', position=Vec3(3, 0.1, 0), model='Quad', origin=Vec3(0, 0.05, 0), color=Color(1.0, 0.0, 0.0, 1.0), collider='box', ), Entity(name=''voxel2'', position=Vec3(3, 0.55, 0.55), rotation=Vec3(90, 0, 0), model='Quad', origin=Vec3(0, 0.05, 0), color=Color(1.0, 0.5, 0.0, 1.0), collider='box', )], [Entity(name=''voxel2'', position=Vec3(2.5, 0.1, 0.5), rotation=Vec3(0, 90, 0), model='Quad', origin=Vec3(0, 0.05, 0), color=Color(0.5, 1.0, 0.0, 1.0), collider='box', ), Entity(name=''voxel2'', position=Vec3(3, 0.1, 0), model='Quad', origin=Vec3(0, 0.05, 0), color=Color(1.0, 0.0, 0.0, 1.0), collider='box', ), Entity(name=''voxel2'', position=Vec3(3, 0.55, 0.55), rotation=Vec3(90, 0, 0), model='Quad', origin=Vec3(0, 0.05, 0), color=Color(1.0, 0.5, 0.0, 1.0), collider='box', )], [Entity(name=''voxel2'', position=Vec3(2.5, 0.1, 0.5), rotation=Vec3(0, 90, 0), model='Quad', origin=Vec3(0, 0.05, 0), color=Color(0.5, 1.0, 0.0, 1.0), collider='box', ), Entity(name=''voxel2'', position=Vec3(3, 0.1, 0), model='Quad', origin=Vec3(0, 0.05, 0), color=Color(1.0, 0.0, 0.0, 1.0), collider='box', ), Entity(name=''voxel2'', position=Vec3(3, 0.55, 0.55), rotation=Vec3(90, 0, 0), model='Quad', origin=Vec3(0, 0.05, 0), color=Color(1.0, 0.5, 0.0, 1.0), collider='box', )]]
for item in little_cubes:
    icons = []
    for i in range(3):
        icons.append(int(str(item[i].icon)[-1]))
    print(icons)
app.run()
