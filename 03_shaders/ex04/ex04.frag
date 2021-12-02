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
Use a piece of paper and draw the situation.
If you can't figure it out, follow the tutorials provided in ex04.py.
*/
vec3 compute_rim_light(vec3 color) {
    // We give you the viewing direction v
    vec3 v = -frag_pos;

    // TODO compute a rim light value based on the viewing direction and the normal of the fragment
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
