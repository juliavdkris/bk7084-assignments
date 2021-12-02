# version 330

in vec4 v_color;
in vec3 v_normal;
in vec2 v_texcoord;
in vec3 frag_pos;
in vec3 world_pos;
in vec3 light_pos;

out vec4 frag_color;

uniform sampler2D in_texture;

vec3 compute_rim_light(vec3 color) {
    /// View direction
    vec3 v = -frag_pos;

    /// The rim contribution.
    float vdn = 1.0 - max(dot(v, v_normal), 0.0);

    return vec3(smoothstep(0.6, 1.0, vdn)) * color.xyz;
}

vec3 compute_toon_color(vec3 color) {
    vec3 light_dir = normalize(light_pos - frag_pos);
    float intensity = dot(light_dir, v_normal);

    if (intensity > 0.95)
        return color * 0.95;
    else if (intensity > 0.8)
        return color * 0.8;
    else if (intensity > 0.6)
        return color * 0.6;
    else if (intensity > 0.25)
        return color * 0.3;
    else
        return color * 0.2;
}


void main() {
    /* vec4 color = texture(in_texture, v_texcoord); */
    vec4 color = v_color;

    vec3 rim_color = compute_rim_light(color.xyz);
    vec3 toon_color = compute_toon_color(color.xyz);

    frag_color = vec4(rim_color + toon_color, 1.0);
}
