# version 330

in vec4 v_color;
in vec3 v_normal;
in vec2 v_texcoord;
in vec3 frag_pos;
in vec3 world_pos;
in vec3 light_pos;

out vec4 frag_color;

/* You can enable or disable shading by setting mesh.shading_enabled = True or False. */
uniform bool shading_enabled;

/* Shading functions - not related with today's exercise. */
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

    vec3 light_color = vec3(0.5, 0.5, 0.5);
    vec3 specular_color = vec3(1.0, 1.0, 1.0);
    float shininess = 0.0;

    vec3 luminance = diffuse_color * 0.5;

    float l_dot_n = dot(light_dir, n);

    if (l_dot_n > 0.0) {
        vec3 brdf = blinnPhongBRDF(light_dir, view_dir, n, diffuse_color.rgb, specular_color.rgb, shininess);

        luminance += brdf * l_dot_n * light_color.rgb * 0.5;
    }

    return vec4(luminance, 1.0);
}

void main() {
    vec4 color = v_color;

    if (shading_enabled) {
        frag_color = shading(color.xyz);
    } else {
        frag_color = color;
    }
}
