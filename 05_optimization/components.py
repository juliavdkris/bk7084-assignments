import bk7084 as bk
import numpy as np

from numpy.random import randint, rand
from math import sqrt

"""
Materials are used to define the appearance of a mesh.
"""
material_stone_bricks = bk.Material()
material_stone_bricks.textures = {
	"diffuse_texture": bk.res_path("../03_textures/assets/stone_bricks_col.jpg"),
	"normal_texture": bk.res_path("../03_textures/assets/stone_bricks_nrm.png"),
	"specular_texture": bk.res_path("../03_textures/assets/stone_bricks_refl.jpg"),
	"shininess_texture": bk.res_path("../03_textures/assets/stone_bricks_gloss.jpg"),
}

material_basic_bricks = bk.Material()
material_basic_bricks.specular = bk.Color(0.1, 0.1, 0.1)
material_basic_bricks.textures = {
	"diffuse_texture": bk.res_path("assets/brick.jpg"),
}

material_basic_floor = bk.Material()
material_basic_floor.diffuse = bk.Color(0.8, 0.5, 0.5)

material_basic_window = bk.Material()
material_basic_window.textures = {
	"diffuse_texture": bk.res_path("assets/window.jpg"),
}

material_basic_ground = bk.Material()
material_basic_ground.textures = {
	"diffuse_texture": bk.res_path("assets/grass.jpg"),
}

material_obsidian = bk.Material()
material_obsidian.textures = {
	"diffuse_texture": bk.res_path("assets/obsidian.png"),
}

material_roof = bk.Material()
material_roof.textures = {
	"diffuse_texture": bk.res_path("assets/grass.jpg"),
}

material_roof2 = bk.Material()
material_roof2.textures = {
	"diffuse_texture": bk.res_path("assets/Roof2.png"),
}

material_grass = bk.Material()
material_grass.textures = {
	"diffuse_texture": bk.res_path("assets/obsidian.png"),
}
material_Highrise_Texture = bk.Material()
material_Highrise_Texture.textures = {
	"diffuse_texture": bk.res_path("assets/Highrise_Texture.png"),
}

material_Highrise_Door_Texture = bk.Material()
material_Highrise_Door_Texture.textures = {
	"diffuse_texture": bk.res_path("assets/Highrise_Door_Texture.png"),
}

material_Office_Texture = bk.Material()
material_Office_Texture.textures = {
	"diffuse_texture": bk.res_path("assets/Office_Texture.png"),

}

material_Office_Door_Texture = bk.Material()
material_Office_Door_Texture.textures = {
	"diffuse_texture": bk.res_path("assets/Office_Door_Texture.png"),

}
class Dummy(bk.Mesh):
	'''Dummy mesh used as a container for other meshes'''
	def __new__(cls, *args, **kwargs):
		return super().__new__(cls)

	def __init__(self):
		super().__init__()
		self.name = "Dummy"
		self.positions = [[0, 0, 0]]
		self.texcoords = [[0, 0]]
		self.triangles = [[0, 0, 0]]


class BasicWall(bk.Mesh):
	"""
	Create a basic wall mesh with the given size and material.
	This class is a subclass of bk.Mesh, so it can be used as a mesh. For example,
	you can create a mesh instance by `mesh = BasicWallMesh(...)`, and then add it to
	a scene by `app.add_mesh(mesh)`. It's the same as using `mesh = create_basic_wall(...)`.
	"""

	def __new__(cls, *args, **kwargs):
		return super().__new__(cls)

	def __init__(self, w=1, h=1, m=material_basic_bricks):
		super().__init__()
		self.w = w
		self.h = h
		self.name = "BasicWallMesh"
		self.positions = [
			[-w / 2, -h / 2, 0],
			[w / 2, -h / 2, 0],
			[w / 2, h / 2, 0],
			[-w / 2, h / 2, 0],
		]
		self.texcoords = [[0, 0], [1, 0], [1, 1], [0, 1]]
		self.triangles = [[0, 1, 2], [0, 2, 3]]
		self.materials = [m]


class BasicWallObsidian(BasicWall):
	'''
	Copy of BasicWall with a different name, for weird parenting bug reasons
	'''

	def __init__(self, w=1, h=1, m=material_basic_bricks):
		super().__init__(w, h, m)
		self.name = 'BasicWall2Mesh'
		self.materials = [material_obsidian]


class Highrise_Texture(BasicWall):
	'''
	Copy of BasicWall with a different name, for weird parenting bug reasons
	'''

	def __init__(self, w=1, h=1, m=material_basic_bricks):
		super().__init__(w, h, m)
		self.name = 'BasicWall3Mesh'
		self.materials = [material_Highrise_Texture]

class Highrise_Door_Texture(BasicWall):
	'''
	Copy of BasicWall with a different name, for weird parenting bug reasons
	'''

	def __init__(self, w=1, h=1, m=material_basic_bricks):
		super().__init__(w, h, m)
		self.name = 'BasicWall4Mesh'
		self.materials = [material_Highrise_Door_Texture]

class Office_Texture(BasicWall):
	'''
	Copy of BasicWall with a different name, for weird parenting bug reasons
	'''

	def __init__(self, w=1, h=1, m=material_basic_bricks):
		super().__init__(w, h, m)
		self.name = 'BasicWall5Mesh'
		self.materials = [material_Office_Texture]

class Office_Door_Texture(BasicWall):
	'''
	Copy of BasicWall with a different name, for weird parenting bug reasons
	'''

	def __init__(self, w=1, h=1, m=material_basic_bricks):
		super().__init__(w, h, m)
		self.name = 'BasicWall7Mesh'
		self.materials = [material_Office_Door_Texture]


class BasicFloor(bk.Mesh):
	def __new__(cls, *args, **kwargs):
		return super().__new__(cls)

	def __init__(self, w=1, h=1, m=material_basic_floor):
		super().__init__()
		self.w = w
		self.h = h
		self.name = "BasicFloorMesh"
		# self.materials = materials
		self.positions = [
			[-w / 2, 0, -h / 2],
			[w / 2, 0, -h / 2],
			[w / 2, 0, h / 2],
			[-w / 2, 0, h / 2],
		]
		self.texcoords = [[0, 0], [1, 0], [1, 1], [0, 1]]
		self.triangles = [[0, 2, 1], [0, 3, 2]]
		self.materials = [m]

class Roof2(bk.Mesh):
	def __new__(cls, *args, **kwargs):
		return super().__new__(cls)

	def __init__(self, w=1, h=1, m=material_basic_floor):
		super().__init__()
		self.w = w
		self.h = h
		self.name = "Roof2Mesh"
		# self.materials = materials
		self.positions = [
			[-w / 2, 0, -h / 2],
			[w / 2, 0, -h / 2],
			[w / 2, 0, h / 2],
			[-w / 2, 0, h / 2],
		]
		self.texcoords = [[0, 0], [1, 0], [1, 1], [0, 1]]
		self.triangles = [[0, 2, 1], [0, 3, 2]]
		self.materials = [material_roof2]


class BasicWindowWall(bk.Mesh):
	def __new__(cls, *args, **kwargs):
		return super().__new__(cls)

	def __init__(self, w=1, h=1):
		super().__init__()
		self.w = w
		self.h = h
		self.name = "BasicWindowWallMesh"
		# self.materials = materials
		self.positions = [
			[-w/2, -h/2, 0.0], [w/2, -h/2, 0.0], [w/2, h/2, 0.0], [-w/2, h/2, 0.0],
			[-w*0.2, -h*0.2, 0.0], [w*0.2, -h*0.2, 0.0], [w*0.2, h*0.2, 0.0], [-w*0.2, h*0.2, 0.0],
			[-w*0.2, -h*0.2, 0.0], [w*0.2, -h*0.2, 0.0], [w*0.2, h*0.2, 0.0], [-w*0.2, h*0.2, 0.0],
		]
		self.texcoords = [
			[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0, 1.0],
			[0.3, 0.3], [0.7, 0.3], [0.7, 0.7], [0.3, 0.7],
			[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0, 1.0]
		]
		self.triangles = [
			[0, 1, 5], [0, 5, 4], [1, 2, 6], [1, 6, 5], [2, 3, 7], [2, 7, 6], [3, 0, 4], [3, 4, 7],
			[8, 9, 10], [8, 10, 11],
		]
		self.materials = [
			material_basic_bricks,
			material_basic_window,
		]
		self.sub_meshes = [
			bk.SubMesh(0, 8, 0),
			bk.SubMesh(8, 10, 1),
		]


class PolygonalFloor(bk.Mesh):
	def __new__(cls, *args, **kwargs):
		return super().__new__(cls)

	def __init__(self, w=1, n=6):
		super().__init__()
		self.w = w
		self.name = "PolygonalFloorMesh"

		# Note: position and texcoords are reversed so that the normals are facing up
		self.positions = [[0, 0, 0]] + [[
			w * np.cos(i/n * 2*np.pi),
			0,
			w * np.sin(i/n * 2*np.pi)
		] for i in range(n)][::-1]

		self.texcoords = [[0, 0]] + [[
			w * np.cos(i/n * 2*np.pi),
			w * np.sin(i/n * 2*np.pi)
		] for i in range(n)][::-1]

		self.triangles = [[i, i + 1, 0] for i in range(1, n)] + [[0, n, 1]]
		self.materials = [material_obsidian]


class Roof(bk.Mesh):
	def __new__(cls, *args, **kwargs):
		return super().__new__(cls)

	def __init__(self, w=1, n=6):
		super().__init__()
		self.w = w
		self.name = "Roof Mesh"

		# Note: position and texcoords are reversed so that the normals are facing up
		self.positions = [[0, 0, 0]] + [[
			w * np.cos(i/n * 2*np.pi),
			0,
			w * np.sin(i/n * 2*np.pi)
		] for i in range(n)][::-1]

		self.texcoords = [[0, 0]] + [[
			w * np.cos(i/n * 2*np.pi),
			w * np.sin(i/n * 2*np.pi)
		] for i in range(n)][::-1]

		self.triangles = [[i, i + 1, 0] for i in range(1, n)] + [[0, n, 1]]
		self.materials = [material_roof]

class RoundedSquareFloor(bk.Mesh):
	def __new__(cls, *args, **kwargs):
		return super().__new__(cls)

	def __init__(self, w=1, h=1):
		super().__init__()
		self.w = w
		self.h = h
		self.name = "RoundedSquareFloorMesh"

		self.positions = [
			[0,0,0], #0
			[w/2, 0, -h/4], #1
			[w/4, 0, -h/2], #2
			[0, 0, -h/2], #3
			[-w/4, 0, -h/2], #4
			[-w/2, 0, -h/4], #5
			[-w/2, 0, 0], #6
			[-w/2, 0, h/4], #7
			[-w/4, 0, h/2], #8
			[0, 0, h/2], #9
			[w/4, 0, h/2], #10
			[w/2, 0, h/4], #11
			[w/2, 0, 0] #12
		]
		self.texcoords = [
			[0.0, 0.0],   # 0 (Center)
			[1.0, -0.5],  # 1
			[0.5, -1.0],  # 2
			[0.0, -1.0],  # 3
			[-0.5, -1.0], # 4
			[-1.0, -0.5], # 5
			[-1.0, 0.0],  # 6
			[-1.0, 0.5],  # 7
			[-0.5, 1.0],  # 8
			[0.0, 1.0],   # 9
			[0.5, 1.0],   # 10
			[1.0, 0.5],   # 11
			[1.0, 0.0]  # 12
		]
		self.triangles = [
			[0,1,2],
			[0,2,3],
			[0,3,4],
			[0,4,5],
			[0,5,6],
			[0,6,7],
			[0,7,8],
			[0,8,9],
			[0,9,10],
			[0,10,11],
			[0,11,12],
			[0,12,1]
		]
		self.materials = [material_obsidian]

