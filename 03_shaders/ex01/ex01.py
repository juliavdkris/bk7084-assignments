import os.path as osp
from bk7084 import Window, app
from bk7084.app.input import KeyCode
from bk7084.math import Vec3, Mat4
from bk7084.misc import PaletteDefault
from bk7084.graphics import draw, ShaderProgram, VertexShader, PixelShader
from bk7084.scene import Mesh


window = Window("BK7084: 03-Shaders [ex01]", width=1024, height=1024)
window.create_camera(Vec3(-2.0, 1.0, -2.0), Vec3(0, 0, 0), Vec3.unit_y(), 60.0)

"""
Exercise 1: Vertex Shader
-------------------------

First update your bk7084 package with pip:
$ conda activate compsim
$ pip install --upgrade bk7084

Make sure that you have also activated the compsim environment in Visual Studio Code (bottom left, Python 3...)

This week, you're introduced to the modern graphics pipeline.
An important component of the graphics pipeline is a *shader*
and you will program a shader yourself in this exercise.
A shader is a small program with only a few in- and outputs that can be applied to data *in parallel*.
In other words, a shader can be applied to a lot of data at the same time, speeding up computations drastically.
This concept is important for graphics programming, but also for simulation and machine learning.
Anytime you can split up a large tasks into small chunks that can be run in parallel, shader-like programs can be used.

There are different kinds of shaders for different kinds of data.
Some examples are vertex shaders (applied to each vertex) and fragment (or pixel) shaders (applied to each pixel).
In the graphics pipeline, the vertex shader is followed by the fragment shader,
so you can use output from the vertex shader as input to the fragment shader.
In this exercise, you will get introduced to a vertex shader and try a few simple operations.
In the next exercise, you can explore what is possible with a fragment shader.

Shaders often run on a GPU (graphics programming unit), which has a lot of cores to run shaders in parallel.
To run a shader on the GPU, we do need to write our shaders in a special language, called GLSL (OpenGL Shading Language).
The program is 'compiled' separately and then sent to your GPU.
Compilation is the process of translating code from human-readable language to machine language.

For this exercise, we load these programs from two files: ex01.vert (vertex shader) and ex01.frag (fragment shader).
The 'VertexShader' and 'PixelShader' classes take care of compiling your code and making it ready for your GPU.
"""
shader = ShaderProgram(
    VertexShader.from_file(osp.join('ex01.vert')),
    PixelShader.from_file(osp.join('ex01.frag'))
)

"""
We will use these shaders to draw the cow object seen in this exercise.
Actually, you don't need to do anything in this file, all tasks should be completed in ex01.vert.
First run this program and then open up `ex01.vert` and continue from there.

You can press `A` when the program is running to animate the model.
"""
# Spot the cow model courtesy of Keenan Crane (CC0) https://www.cs.cmu.edu/~kmcrane/Projects/ModelRepository/#spot
spot = Mesh('spot-cow', osp.join('../assets/spot.obj'), colors=[PaletteDefault.BlueB.as_color()])
spot.shading_enabled = True  # Disable or enable shading in shader.
shader_params = {
    'shading_enabled': False
}

animate = False

@window.event
def on_draw(dt):
    draw(spot, shader=shader, shader_params=shader_params)

@window.event
def on_key_press(key, mods):
    global animate
    if key == KeyCode.A:
        animate = not animate

@window.event
def on_update(dt):
    if animate:
        spot.apply_transform(Mat4.from_axis_angle(Vec3.unit_y(), 45.0 * dt, True))

app.init(window)
app.run()
