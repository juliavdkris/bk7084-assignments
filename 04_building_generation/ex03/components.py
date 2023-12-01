import bk7084 as bk

stone_brick_material = bk.Material()
stone_brick_material.textures = {
    "diffuse_texture": bk.res_path("../../03_textures/assets/stone_bricks_col.jpg"),
    "normal_texture": bk.res_path("../../03_textures/assets/stone_bricks_nrm.png"),
    "specular_texture": bk.res_path("../../03_textures/assets/stone_bricks_refl.jpg"),
    "shininess_texture": bk.res_path("../../03_textures/assets/stone_bricks_gloss.jpg"),
}


class BasicWallMesh(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1):#, materials=None):
        super().__init__()
        self.w = w
        self.h = h
        #self.materials = materials
        self.vertices = [[-w / 2, -h / 2, 0], [w / 2, -h / 2, 0], [w / 2, h / 2, 0], [-w / 2, h / 2, 0]]
        self.uvs = [[0, 0], [1, 0], [1, 1], [0, 1]]
        self.triangles = [[0, 1, 2], [0, 2, 3]]
        self.set_material(stone_brick_material)