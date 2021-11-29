# version 330

in vec4 v_color;
in vec3 v_normal;
in vec3 light_pos;
in vec3 frag_pos;
in vec3 world_pos;

out vec4 frag_color;

uniform bool do_shading;

vec4 simple_shading() {
    vec3 light_color = vec3(1.0, 1.0, 1.0);
    
    // face normal approximation
    vec3 x = dFdx(world_pos);
    vec3 y = dFdy(world_pos);
    vec3 face_normal = cross(x, y);
    
    // diffuse
    vec3 light_dir = normalize(light_pos - frag_pos);
    float diff = max(dot(normalize(face_normal), light_dir), 0.0);
    vec3 diffuse = 0.4 * (diff * light_color * v_color.xyz) + v_color.xyz * 0.5;
     
    return vec4(diffuse, 1.0); 
}

void main() {
    if (do_shading) {
        frag_color = simple_shading();
    } else {
        frag_color = v_color;
    }
}