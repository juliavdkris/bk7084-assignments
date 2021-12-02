# version 330

in vec4 v_color;
in vec3 v_normal;
in vec2 v_texcoord;
in vec3 frag_pos;
in vec3 world_pos;
in vec3 light_pos;

out vec4 frag_color;

uniform sampler2D in_texture;

/*
You can finish the two tasks by completing the two functions:
1. compute_rim_light
2. compute_toon_color

First, try to think about how you would implement each effect.
Look up 'rim light' and 'toon shading' on Google images to understand what each effect looks like.
Then use a piece of paper and draw the situation to think about how you should achieve the effect.
Draw a camera, an object, and a light source.
- Where on the object does the rim light show up?
- How can you determine this location based on the information the shader has?
  There are a couple of hints in the functions.
Don't give up too quickly. Even if you can't completely finish the exercise on your own,
it helps to first think about how to achieve the goals with the tools you know. 

If you can't figure it out, follow the tutorials provided in ex04.py.
*/
vec3 compute_rim_light(vec3 color) {
    // We give you the viewing direction v
    vec3 v = -frag_pos;

    // TODO compute a rim light value based on the viewing direction and the normal
    // Hint 1: you can get the normal with v_normal
    // Hint 2: you can apply a smooth threshold with 
    // >>> smoothstep(start, end, value)

    return color;
}

vec3 compute_toon_color(vec3 color) {
    // Given a light direction
    vec3 light_dir = normalize(light_pos - frag_pos);

    // TODO compute a toon color based on the light direction and the normal of the point.

    return color;
}

void main() {
    vec4 color = texture(in_texture, v_texcoord);

    // Here, we combine the light contributions of each effect.
    vec3 rim_color = compute_rim_light(color.xyz);
    vec3 toon_color = compute_toon_color(color.xyz);

    frag_color = vec4(rim_color + toon_color, 1.0);
}
