# version 330

in vec4 v_color;
in vec3 v_normal;
in vec2 v_texcoord;
in vec3 frag_pos;
in vec3 light_pos;
in vec3 world_pos;

out vec4 frag_color;

uniform bool shading_enabled;
uniform sampler2D in_texture;

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

const float intensity_threshold = 0.5;

/// Function to calculate the intensity of a color.
///
/// Note: You can access to color elements by indexing:
///     color.x or color.r
///     color.y or color.g
///     color.z or color.b
///
/// There are two ways to calculate the intensity of a color:
///   1. Average method
///
///      The intensity will be the average value of its three channels.
///
///   2. Luminosity method
///
///      Human eys have different sensitivity over red, green and blue lights.
///      Thus we use weighted value to compute intensity. Weights are given:
///      R -- 0.299
///      G -- 0.587
///      B -- 0.114
float intensity(vec3 color) {
    return 1.0;
}

void main() {
    /// Here we want to draw the texture, thus instead of using
    ///     vec4 color = v_color;
    /// we now get color directly from the loaded texture.

    vec4 tex_color = texture(in_texture, v_texcoord);

    /// Task:
    ///     1. Write a function to calculate the intensity of the color.
    ///     2. Use this intensity to decide whether use the texture color (tex_color)
    ///        or vertex color (v_color) for the final output.
    ///        If the intensity of the texture color is less (or greater) than
    ///        intensity_threshold, we use vertex color, otherwise texture color
    vec4 color = tex_color;

    /// Write the code here to test intensity

    if (shading_enabled) {
        frag_color = shading(color.xyz);
    } else {
        frag_color = color;
    }
}
