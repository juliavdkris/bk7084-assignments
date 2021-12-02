/*
Welcome to your first fragment shader.
You're already familiar with some basics of shaders,
so feel free to scroll down to the next comment to get started.
*/
# version 330

/*
Remember the `out` variables in the vertex shader?
You can use these variables as `in` variables in the fragment shader.
You 'plug in' the variables by setting these `in` and `out` variables.
*/
in vec4 v_color;
in vec3 v_normal;
in vec2 v_texcoord;
in vec3 frag_pos;
in vec3 light_pos;
in vec3 world_pos;

out vec4 frag_color;

uniform bool shading_enabled;
uniform sampler2D in_texture;

/*
This function computes what the object looks like under a given light condition.
This is called *shading*, not to be confused with a *shader*.
You don't have to change this function, but if you're interested in what it takes to get
lighting on an object, you're free to read through it.
*/
vec3 blinnPhongBRDF(vec3 light_dir, vec3 view_dir, vec3 normal, vec3 diffuse_color, vec3 specular_color, float shininess) {
    vec3 color = diffuse_color;
    vec3 half_dir = normalize(view_dir + light_dir);
    float spec_dot = max(dot(half_dir, normal), 0.0);
    color += pow(spec_dot, shininess) * specular_color;
    return color;
}

vec4 shading(vec3 diffuse_color) {
    vec3 light_dir = normalize(light_pos - frag_pos);
    vec3 view_dir = normalize(-frag_pos);
    vec3 n = normalize(v_normal);

    vec3 ambient_color = vec3(0.1, 0.1, 0.1);
    vec3 light_color = vec3(0.5, 0.5, 0.5);
    vec3 specular_color = vec3(1.0, 1.0, 1.0);
    float shininess = 0.0;

    vec3 luminance = ambient_color.rgb + diffuse_color * 0.3;

    float illuminance = dot(light_dir, n);
    if (illuminance > 0.0) {
        vec3 brdf = blinnPhongBRDF(light_dir, view_dir, n, diffuse_color.rgb, specular_color.rgb, shininess);

        luminance += brdf * illuminance * light_color.rgb * 0.6;
    }

    return vec4(luminance, 1.0);
}

/*
As mentioned before, in this exercise, you will threshold the texture based on its intensity.
Your first task is to write a function to calculate the intensity of a color.

There are two ways to calculate the intensity of a color:
  1. Average method
     The intensity will be the average value of its three channels.

  2. Luminosity method
     Human eyes have different sensitivity over red, green and blue lights.
     Thus we use weighted value to compute intensity. Weights are given:
     R -- 0.299
     G -- 0.587
     B -- 0.114

[a] Complete the intensity function below.
Note: You can access color elements by indexing:
    color.x or color.r
    color.y or color.g
    color.z or color.b
*/
float intensity(vec3 color) {

    // TODO complete function
    return 1.0;
}

const float intensity_threshold = 0.5;

void main() {
    /*
    Each 'fragment' will be colored using the color from a texture.
    Instead of using v_color, we're going to look up the color in a texture.
    The texture is given by in_texture and the coordinate in the texture that belongs to this fragment
    is given by v_texcoord. Then, the `texture` function looks up the color.
    */
    vec4 tex_color = texture(in_texture, v_texcoord);

    /*
    You just wrote a function to calculate the intensity of a color.
    [b] Now use this intensity to decide whether use the texture color (tex_color)
    or vertex color (v_color) for the final output.
    If the intensity of the texture color is less (or greater) than
    intensity_threshold, we use vertex color, otherwise texture color.
    
    Hint 1:
    if and else statements are written in a different way than in Python.
    Check the lines below for an example of how to use if and else.

    Hint 2:
    You can get a vec3 from a vec4 object by calling color.xyz or color.rgb
    */
    vec4 color = tex_color;

    // TODO use intensity function to threshold color

    /*
    Now that you know how to adjust colors, try a couple of other things:
    [c] Multiply the color with a scaling factor. What's happening?
    [d] Divide the color with a number.
    [e] Multiply the color with a vec4 that you define yourself. Can you explain what is happening?
    */

    if (shading_enabled) {
        frag_color = shading(color.xyz);
    } else {
        frag_color = color;
    }
}
