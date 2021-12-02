#version 330

layout (location = 0) in vec3 a_position;
layout (location = 1) in vec4 a_color;
layout (location = 2) in vec2 a_texcoord;
layout (location = 3) in vec3 a_normal;

out vec4 v_color;
out vec3 v_normal;
out vec2 v_texcoord;
out vec3 frag_pos;
out vec3 light_pos;
out vec3 world_pos;

/*
In this exercise, we want to create some effects that use the index of each vertex.
Therefore, we need to pass the current vertex index and the time to fragment (pixel) shader.
The vertex id value can be retrieved directly from gl_VertexID.
The time is given to the vertex shader through a uniform variable.

[a] pass gl_VertexID and the time to the fragment shader.
Hint 1: there are a couple of TODO's in this file to show you where to add code.
Hint 2: if you don't want the value passed to fragment shader be
      interpolated, you need to use `flat` specifier:
          flat in vec3 vector;
          flat out vec3 vector;
*/

// TODO create an output for the vertex id `int id`
// TODO create an output for time `float t`

uniform mat4 model_mat;
uniform mat4 view_mat;
uniform mat4 proj_mat;
uniform float time;

void main() {
    // TODO set id to gl_VertexID
    // TODO set t to the time

    /*
    You have now created a link between the vertex shader and the fragment shader.
    Before we use these values in the fragment shader, let's have some fun with
    the time variable to animate the vertices.

    [b] Add an offset to the vertex positions that is scaled by the time variable.
        Hint 1: Use a sin(t) function to create a periodic effect.
        Hint 2: Try to be creative with this effect. Can you make the cow 'wave'?

    Continue to ex03.frag when you're done.
    */
    // TODO adjust the position with a time variable here
    vec3 new_position = a_position;

    // These lines project the input position to the world space.
    frag_pos = vec3(view_mat * model_mat * vec4(new_position, 1.0));
    light_pos = vec3(view_mat * vec4(600.0, 600.0, 600.0, 1.0));
    world_pos = vec3(view_mat * vec4(a_position, 1.0));

    v_color = a_color;
    v_texcoord = a_texcoord;
    v_normal = mat3(transpose(inverse(view_mat * model_mat))) * a_normal;

    gl_Position = proj_mat * view_mat * model_mat * vec4(new_position, 1.0);
}
