import random

from bk7084.math import *
from components import *


"""
This file contains the Skyscraper, Highrise, and Office classes.
These classes are used to generate buildings with different shapes and sizes.
The Skyscraper class is already implemented for you as an example.
You will need to implement the Highrise and Office classes yourself.

A building is made up of multiple components. Each component is a mesh. For
example, a skyscraper is made up of multiple floors, walls, and windows. Each
floor, wall, and window is a component. To generate a building, we need to
generate each component and place them in the correct position.

But how do we place each component in the correct position? Of course, we can
place each component manually. But what if we want to translate the whole
building? We will need to translate each component individually. This is
tedious and error-prone.

Recall what we have learned in the hierarchy lecture, how do we construct the
solar system? We parent each planet to the sun, and moon to each planet by
multiplying the transformation of the parent right before the transformation
of the child. This way, all the children will be transformed correctly when
the parent is transformed.

We can do the same thing here. We can parent each component to a base
component and only transform the base component. This way, all the children
will be transformed correctly when the base component is transformed. This
time, we will use the app.spawn_building() function to spawn a base component
for us. The app.spawn_building() function will spawn a base component with
nothing in it. You can then parent other components to this base component.

Check out the `self.building` variable in the Skyscraper class. It is the base
component that we will use to parent other components. Go back to the main.py
file and you will see that we apply a transformation to the self.building
component. This transformation will be applied to all the children of the
self.building component. This is how we can translate the whole building.
"""


class Skyscraper:
	"""A basic skyscraper class that procedurally generates
	a skyscraper given a number of floors and width.

	Args:
		app (bk.App):
			The app instance.
		num_floors (int):
			Number of floors to generate.
		max_width (float):
			The maximum width for each component.
	"""
	def __init__(self, app, max_floors):
		self.max_floors = max_floors
		self.building = app.spawn_building()
		self.building.set_visible(True)

		RADIUS = 1
		FLOOR_HEIGHT = 2
		side_length = RADIUS * np.sin(np.pi/8)
		spacing = (1 + 1/sqrt(2)) * side_length

		octagons = []
		octagon_positions = [
			[0, 2],
			[2, 0],
			[0, -2],
			[-2, 0],
			[2, 4],
			[4, 2],
			[4, -2],
			[2, -4],
			[-2, -4],
			[-4, -2],
			[-4, 2],
			[-2, 4],
		]


		octagon_floors = [random.randint(4, max_floors) for _ in range(len(octagon_positions))]

		for [oct_x, oct_z], oct_floors in zip(octagon_positions, octagon_floors):
			floor_base = app.add_mesh(PolygonalFloor(RADIUS, 8), parent=self.building)
			floor_base.set_transform((
				Mat4.from_translation(Vec3(oct_x * spacing, 0, oct_z * spacing)) *
				Mat4.from_rotation_y(360/16, True)
			))
			floor_base.set_visible(True)
			floors = [floor_base]
			octagons.append(floor_base)

			for _ in range(oct_floors):
				last_floor = floors[-1]
				floor = app.add_mesh(PolygonalFloor(RADIUS, 8), parent=last_floor)
				floor.set_transform(Mat4.from_translation(Vec3(0, FLOOR_HEIGHT, 0)))
				floor.set_visible(True)
				floors.append(floor)

				for side in range(8):
					wall = app.add_mesh(BasicWallObsidian(1, 1), parent=last_floor)
					wall.set_transform((
						Mat4.from_rotation_y(360/8 * side, True)						# Rotate to corner of octagon
						* Mat4.from_translation(Vec3(RADIUS, 0, 0))						# Move to corner of octagon
						* Mat4.from_rotation_y(180/8, True)								# Rotate to middle of vertex
						* Mat4.from_translation(Vec3(0, FLOOR_HEIGHT/2, -side_length))	# Move to middle of vertex
						* Mat4.from_rotation_y(90, True)								# Rotate to be perpendicular to center
						* Mat4.from_scale(Vec3(2 * side_length, FLOOR_HEIGHT, 2))		# Scale to fit
					))
					wall.set_visible(True)


class Office:
	"""A Office class that procedurally generates
	a Office building given a number of floors and width.

	Args:
		app (bk.App):
			The app instance.
		num_floors (int):
			Number of floors to generate.
		max_width (float):
			The maximum width for each component.
	"""
	def __init__(self, app, max_floors):
		self.max_floors = max_floors
		self.building = app.spawn_building()
		self.building.set_visible(True)

		WIDTH = 1.75
		FLOOR_HEIGHT = 1


		Squared = []
		Squared_positions =[
			[0,0],
			[0,WIDTH],
			[0,-WIDTH],
			[WIDTH,WIDTH],
			[-WIDTH,-WIDTH],
			[0,-2*WIDTH],
			[0,2*WIDTH],
		]

		Squared_positions_random = [
			[WIDTH,-2*WIDTH],
			[-WIDTH,-2*WIDTH],
			[WIDTH,2*WIDTH],
			[-WIDTH,2*WIDTH],
	]

		for pos in Squared_positions_random:
			if random.choice([True, False]):  # 50% chance to add
				Squared_positions.append(pos)

		Squared_floors = [random.randint(2, max_floors) for _ in range(len(Squared_positions))]


		for [square_x, square_z], square_floors in zip(Squared_positions, Squared_floors):
			floor_base = app.add_mesh(Roof2(WIDTH, WIDTH), parent=self.building)
			floor_base.set_transform((
				Mat4.from_translation(Vec3(square_x, 0, square_z))
			))
			floor_base.set_visible(True)
			floors = [floor_base]
			Squared.append(floor_base)

			for i in range(square_floors):
				last_floor = floors[-1]
				floor = app.add_mesh(Roof2(WIDTH, WIDTH), parent=last_floor)
				floor.set_transform(Mat4.from_translation(Vec3(0, FLOOR_HEIGHT, 0)))
				floor.set_visible(True)
				floors.append(floor)

				for side in range(4):
					if i == 0:
						wall0 = app.add_mesh(Office_Door_Texture(1, 1), parent=last_floor)
						wall0.set_transform((
							Mat4.from_rotation_y(360/4 * side, True)
							* Mat4.from_translation(Vec3(0, FLOOR_HEIGHT/2, WIDTH/2))
							* Mat4.from_scale(Vec3(WIDTH , FLOOR_HEIGHT, 2))

						))
						wall0.set_visible(True)

					else:
						wall = app.add_mesh(Office_Texture(1, 1), parent=last_floor)
						wall.set_transform((
							Mat4.from_rotation_y(360/4 * side, True)
							* Mat4.from_translation(Vec3(0, FLOOR_HEIGHT/2, WIDTH/2))
							* Mat4.from_scale(Vec3(WIDTH , FLOOR_HEIGHT, 2))

						))
						wall.set_visible(True)



class Highrise:

	def __init__(self, app, max_floors):
		self.max_floors = max_floors
		self.building = app.spawn_building()
		self.building.set_visible(True)

		RADIUS = 1
		FLOOR_HEIGHT = 1
		side_length = RADIUS * np.sin(np.pi/8)

		octagons = []
		octagon_positions = [
			[0, 0],
			[RADIUS*2 -side_length, 0],
			[0, -RADIUS*2 + side_length],
			[-RADIUS*2 +side_length, 0],
			[0, RADIUS*2 -side_length],

		]


		octagon_floors = [random.randint(max_floors, max_floors) for _ in range(len(octagon_positions))]

		for [oct_x, oct_z], oct_floors in zip(octagon_positions, octagon_floors):
			floor_base = app.add_mesh(Roof(RADIUS, 8), parent=self.building)
			floor_base.set_transform((
				Mat4.from_translation(Vec3(oct_x, 0, oct_z )) *
				Mat4.from_rotation_y(360/16, True)
			))
			floor_base.set_visible(True)
			floors = [floor_base]
			octagons.append(floor_base)

			for i in range(oct_floors):
				last_floor = floors[-1]
				floor = app.add_mesh(Roof(RADIUS, 8), parent=last_floor)
				# Add a rotation for each floor (incremental rotation for each level)
				rotation_angle = 20 * i # Rotate 10 degrees per floor, change as needed
				floor.set_transform((
				Mat4.from_translation(Vec3(0, FLOOR_HEIGHT, 0)) *
				Mat4.from_rotation_y(rotation_angle, True)  # Apply cumulative rotation
				))
				floor.set_visible(True)
				floors.append(floor)

				for side in range(8):
					if i == 0:
						wall0 = app.add_mesh(Highrise_Door_Texture(1, 1), parent=last_floor)
						wall0.set_transform((
							Mat4.from_rotation_y(360/8 * side, True)						# Rotate to corner of octagon
							* Mat4.from_translation(Vec3(RADIUS, 0, 0))						# Move to corner of octagon
							* Mat4.from_rotation_y(180/8, True)								# Rotate to middle of vertex
							* Mat4.from_translation(Vec3(0, FLOOR_HEIGHT/2, -side_length))	# Move to middle of vertex
							* Mat4.from_rotation_y(90, True)								# Rotate to be perpendicular to center
							* Mat4.from_scale(Vec3(2 * side_length, FLOOR_HEIGHT, 2))		# Scale to fit
						))
						wall0.set_visible(True)

					else:
						wall = app.add_mesh(Highrise_Texture(1, 1), parent=last_floor)
						wall.set_transform((
							Mat4.from_rotation_y(360/8 * side, True)						# Rotate to corner of octagon
							* Mat4.from_translation(Vec3(RADIUS, 0, 0))						# Move to corner of octagon
							* Mat4.from_rotation_y(180/8, True)								# Rotate to middle of vertex
							* Mat4.from_translation(Vec3(0, FLOOR_HEIGHT/2, -side_length))	# Move to middle of vertex
							* Mat4.from_rotation_y(90, True)								# Rotate to be perpendicular to center
							* Mat4.from_scale(Vec3(2 * side_length, FLOOR_HEIGHT, 2))		# Scale to fit
						))
						wall.set_visible(True)


# pre-loaded park model
park_model = bk.Mesh.load_from(bk.res_path("./assets/park.obj"))


class Park:
	def __init__(self, app):
		self.building = app.add_mesh(park_model)
		self.building.set_visible(True)
		angle = random.randint(0, 3) * 90
		self.pre_transform = (
			Mat4.from_translation(Vec3(0, 1.4, 0))
			* Mat4.from_scale(Vec3(0.5))
			* Mat4.from_rotation_y(angle, True)
		)


# pre-loaded house model
house_model = bk.Mesh.load_from(bk.res_path("./assets/house.obj"))


class House:
	def __init__(self, app):
		self.building = app.add_mesh(house_model)
		self.building.set_visible(True)
		angle = random.randint(0, 3) * 90
		self.pre_transform = (
			Mat4.from_scale(Vec3(0.5))
			* Mat4.from_translation(Vec3(0, 6.8, 0))
			* Mat4.from_rotation_y(angle, True)
		)
