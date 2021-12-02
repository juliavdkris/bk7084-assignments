// Welcome to your first GLSL program! This is going to be a bit different from Python.
// the first thing you might notice: comments start with two dashes // and multiline comments start with a
/* and 
end
with
a */

/*
The second thing you need to know: every line in your program should end with a semicolon ;
Anytime your program fails to run, first check your code to see if you forgot about a semicolon anywhere!
VS Code might not understand GLSL yet. You can install the extension 'GLSL Syntax for VS Code'
which can help you find bugs before you make them.

First, we tell the compiler which version it should use to translate your GLSL code.
This line does not need a semicolon, as it's not part of the program itself.
*/
#version 330

/*
Then we tell the shader which inputs it can expect.
These are the position of each vertex, the color of each vertex and the normals on each vertex.
*/
layout (location = 0) in vec3 a_position;
layout (location = 1) in vec4 a_color;
layout (location = 2) in vec3 a_texcoord;
layout (location = 3) in vec3 a_normal;

/*
Next, we tell the shader which outputs to return. We use these outputs in the fragment shader.
*/
out vec4 v_color;
out vec3 v_normal;
out vec3 v_texcoord;
out vec3 frag_pos;
out vec3 light_pos;
out vec3 world_pos;

/*
Some variables are the same for each shader, independent of the vertex you apply it to.
These variables are called uniform variables. In this case, they are the matrices used to
transform models, move the camera and project models to the screen.
*/
uniform mat4 model_mat;
uniform mat4 view_mat;
uniform mat4 proj_mat;

/*
Each shader program needs a main function. This is the program that is run by your GPU.
*/
void main() {
    /*
    Now, here are your tasks. Modify the line right after this comment to:
    [a] Scale the input models by multiplying each position with a scaling factor.
    [b] Move the vertex positions in the direction of the vertex normals `a_normal`. Do you understand what is happening?
    [c] Move the vertex positions in the inverse direction of the vertex normals. What is happening?

    Note that you also need to tell GLSL what the type is of each *new* variable.
    You can do this by first writing the type and then the name of the variable:
    */
    vec3 new_position = a_position;

    /*
    You don't need to change the code after this comment.
    
    Here, we apply the model, view, and project matrix to the input positions
    and output them to a special variable which is reserved by GLSL: gl_Position
    */
    gl_Position = proj_mat * view_mat * model_mat * vec4(new_position, 1.0);
    // The color is piped forward unchanged.
    v_color = a_color;
    
    // Finally, we output a couple of variables used by the fragment shader to determine colours.
    frag_pos = vec3(view_mat * model_mat * vec4(a_position, 1.0));
    world_pos = (model_mat * vec4(a_position, 1.0)).xyz;
    light_pos = vec3(view_mat * vec4(600.0, 600.0, 600.0, 1.0));
    v_texcoord = a_texcoord;
    v_normal = mat3(transpose(inverse(view_mat * model_mat))) * a_normal;
}
