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

// used for this exercise
flat out int id;
out float t;

uniform mat4 model_mat;
uniform mat4 view_mat;
uniform mat4 proj_mat;
uniform float time;

/// In this exercise, we want to make some effects related with
/// index of vertex, thus we need to pass the current vertex index and
/// the time to fragment (pixel) shader. This value can be retrieved
/// directly from gl_VertexID.

/// Task: pass gl_VertexID to fragment shader.
/// Note: if you don't want the value passed to fragment shader be
///       interpolated, you need to use `flat` specifier:
///           flat in vec3 vector;
///           flat out vec3 vector;

void main() {
    frag_pos = vec3(view_mat * model_mat * vec4(a_position, 1.0));
    light_pos = vec3(view_mat * vec4(600.0, 600.0, 600.0, 1.0));
    world_pos = vec3(view_mat * vec4(a_position, 1.0));

    v_color = a_color;
    v_texcoord = a_texcoord;
    v_normal = mat3(transpose(inverse(view_mat * model_mat))) * a_normal;

    id = gl_VertexID;
    t = time;

    gl_Position = proj_mat * view_mat * model_mat * vec4(a_position, 1.0);
}
