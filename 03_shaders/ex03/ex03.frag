# version 330

in vec4 v_color;
in vec3 v_normal;
in vec2 v_texcoord;
in vec3 frag_pos;
in vec3 light_pos;
in vec3 world_pos;

flat in int id;
in float t;

out vec4 frag_color;

uniform sampler2D in_texture;
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

void main() {
    vec4 color;

    /// Task:
    ///   Use the time and vertex index passed from vertex shader to
    ///   implement the following effect:
    ///
    ///     every 3 seconds triangles with odd index will be colored using texture color
    ///     and triangles with even index will be colored using vertex color.

    int odd_or_even = int(mod(t, 3.0));

    if (mod((id / 3), 2) == odd_or_even) {
        color = texture(in_texture, v_texcoord);
    } else {
        color = v_color;
    }

    if (shading_enabled) {
        frag_color = shading(color.xyz);
    } else {
        frag_color = color;
    }
}
