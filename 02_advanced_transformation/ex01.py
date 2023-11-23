import os.path
import sys

import bk7084 as bk
from bk7084.math import *


def load_meshes(app, filepath):
    if not os.path.exists(filepath):
        print("File not found: %s" % filepath)
        return
    if os.path.isdir(filepath):
        for root, dirs, files in os.walk(filepath):
            for filename in files:
                if filename.endswith(".obj"):
                    model = app.add_mesh(bk.Mesh.load_from(os.path.join(root, filename)))
                    model.set_visible(True)
    else:
        model = app.add_mesh(bk.Mesh.load_from(filepath))
        model.set_visible(True)


win = bk.Window()
win.set_title('BK7084 - Lab 2 - Advanced Transformation [ex01]')
win.set_size(1024, 1024)
win.set_resizable(True)

app = bk.App()
camera = app.create_camera(pos=Vec3(4, 64, 4), look_at=Vec3(0, 0, 0), fov_v=60.0, near=0.1, far=500.0)
camera.set_as_main_camera()

load_meshes(app, bk.res_path("./assets/village/"))
car = app.add_mesh(bk.Mesh.load_from(bk.res_path("./assets/car.obj")))
car.set_visible(True)

car_transform = Mat4.from_rotation_y(180.0, True)

car_speed = 10.0
car_turn_speed = 90.0

current_segment = 0

#            straight turn_point0, straight, turn_point1, straight, turn_point2, straight, turn_point3, straight
road = [7.0, 90.0, 20.5, 90.0, 8.0, 90.0, 36.0, 90.0, 10.0]

marched_distance = 0.0
turned_angle = 0.0

start = False


@app.event
def on_update(input, dt, t):
    global car_transform
    global current_segment
    global marched_distance
    global turned_angle
    global start

    if input.is_key_pressed(bk.KeyCode.Space):
        start = True

    if start and current_segment < len(road):
        if current_segment % 2 == 0:
            marched_distance += car_speed * dt
            if marched_distance > road[current_segment]:
                marched_distance = 0.0
                current_segment += 1
        else:
            turned_angle += car_turn_speed * dt
            if turned_angle > road[current_segment]:
                turned_angle = 0.0
                current_segment += 1

        # move the car
        if current_segment == 0:
            car_transform = car_transform * Mat4.from_translation(Vec3(car_speed * dt, 0.0, 0.0))

        # turn point 0
        if current_segment == 1:
            car_transform = car_transform * Mat4.from_rotation_y(-car_turn_speed * dt, True)

        if current_segment == 2:
            car_transform = Mat4.from_translation(Vec3(0.0, 0.0, -car_speed * dt)) * car_transform

        # turn point 1
        if current_segment == 3:
            car_transform = car_transform * Mat4.from_rotation_y(-car_turn_speed * dt, True)

        if current_segment == 4:
            car_transform = Mat4.from_translation(Vec3(car_speed * dt, 0.0, 0.0)) * car_transform

        # turn point 2
        if current_segment == 5:
            car_transform = car_transform * Mat4.from_rotation_y(car_turn_speed * dt, True)

        if current_segment == 6:
            car_transform = Mat4.from_translation(Vec3(0.0, 0.0, -car_speed * dt)) * car_transform

        # turn point 3
        if current_segment == 7:
            car_transform = car_transform * Mat4.from_rotation_y(-car_turn_speed * dt, True)

        if current_segment == 8:
            car_transform = Mat4.from_translation(Vec3(car_speed * dt, 0.0, 0.0)) * car_transform

    car.set_transform(car_transform)


app.run(win)
