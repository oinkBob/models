"""
Molanex Building Template — Proven Working Patterns
====================================================
Kopiere relevante Abschnitte in jedes neue Blender-Script.
Diese Funktionen haben die erfolgreichen Gebäude gebaut (harvester, storage,
research, distributor, cleaner, maintenance). Nicht neu erfinden.

Load-bearing Invariants:
  APOTHEM = 0.866 (Tier 1), 1.732 (Tier 2)
  PIPE_Z = 0.30 (all flanges, pipes, anchors live at this height)
  HEX_R = 0.98 (Tier 1 stone footprint, slightly inside 1.0)
  Flange: disc r=0.13 d=0.04, bore r=0.055, 8 bolts r=0.013 d=0.025 on ring r=0.095
  Anchor empties: PLAIN_AXES at flange pos, rotation Z = outward normal angle
  Edge index: 0=E (0°), 1=NE (60°), 2=NW (120°), 3=W (180°), 4=SW (240°), 5=SE (300°)
  Pointy-top hex: vertex at 30°+60°·i, edge-midpoint (anchor dir) at 60°·i
"""

import bpy, math, mathutils, bmesh

# ============================================================
# 1. CLEAN SCENE + PALETTE + LIGHTS
# ============================================================

def fresh_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    for coll in [bpy.data.meshes, bpy.data.materials, bpy.data.objects, bpy.data.lights, bpy.data.cameras]:
        for b in list(coll):
            try: coll.remove(b)
            except: pass

def hx(h):
    h = h.lstrip('#')
    return (int(h[0:2],16)/255, int(h[2:4],16)/255, int(h[4:6],16)/255, 1.0)

def mat(name, hexv, rough=0.85):
    m = bpy.data.materials.new(name); m.use_nodes = True
    b = m.node_tree.nodes.get("Principled BSDF")
    b.inputs["Base Color"].default_value = hx(hexv)
    b.inputs["Roughness"].default_value = rough
    m.diffuse_color = hx(hexv)
    return m

PALETTE = {
    "stone_dk":  "#5a5c5e",
    "stone_lt":  "#808286",
    "metal_dk":  "#3a3b3d",
    "metal_mid": "#5a5e62",
    "wood":      "#8B6914",
    "wood_dk":   "#5c4710",
    "harvester": "#f59e0b",
    "heat":      "#f97316",
    "flow_green":"#4ade80",
    "shield_blue":"#38bdf8",
    "warning":   "#dc2626",
    "window":    "#F5CD6B",
    "copper":    "#b86a1c",
}

def setup_palette():
    for k,h in PALETTE.items():
        if f"mx_{k}" not in bpy.data.materials:
            mat(f"mx_{k}", h)

def setup_lights():
    bpy.ops.object.light_add(type='SUN', location=(3,-3,6))
    bpy.context.object.data.energy = 3.0
    bpy.ops.object.light_add(type='SUN', location=(-4,2,3))
    bpy.context.object.data.energy = 1.1

# Shortcut material lookup after setup_palette()
def M(key):
    return bpy.data.materials[f"mx_{key}"]

# ============================================================
# 2. HEX GEOMETRY CONSTANTS + PRIMITIVES
# ============================================================

# Vertex angles: pointy-top with corners at N/S = 30° + 60°·i
VERT_ANGLES = [math.radians(30 + 60*i) for i in range(6)]
# Edge-midpoint angles = anchor directions (0=E, 1=NE, 2=NW, 3=W, 4=SW, 5=SE)
EDGE_ANGLES = [math.radians(60*i) for i in range(6)]

def build_hex_prism(name, radius, height, z_bottom, material):
    """Solid hex prism, pointy-top (vertex at 90°/North)."""
    mesh = bpy.data.meshes.new(name); bm = bmesh.new()
    bot, top = [], []
    for ang in VERT_ANGLES:
        x, y = radius*math.cos(ang), radius*math.sin(ang)
        bot.append(bm.verts.new((x, y, z_bottom)))
        top.append(bm.verts.new((x, y, z_bottom + height)))
    bm.verts.ensure_lookup_table()
    for i in range(6):
        j = (i+1) % 6
        bm.faces.new([bot[i], bot[j], top[j], top[i]])
    bm.faces.new(top); bm.faces.new(list(reversed(bot)))
    bm.to_mesh(mesh); bm.free()
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    obj.data.materials.append(material)
    return obj

def build_hex_frustum(name, r_bot, r_top, z_bottom, height, material):
    """Tapered hex (smaller at top), pointy-top."""
    mesh = bpy.data.meshes.new(name); bm = bmesh.new()
    bot, top = [], []
    for ang in VERT_ANGLES:
        bot.append(bm.verts.new((r_bot*math.cos(ang), r_bot*math.sin(ang), z_bottom)))
        top.append(bm.verts.new((r_top*math.cos(ang), r_top*math.sin(ang), z_bottom+height)))
    bm.verts.ensure_lookup_table()
    for i in range(6):
        j = (i+1) % 6
        bm.faces.new([bot[i], bot[j], top[j], top[i]])
    bm.faces.new(top); bm.faces.new(list(reversed(bot)))
    bm.to_mesh(mesh); bm.free()
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    obj.data.materials.append(material)
    return obj

def add_cube(name, size_xyz, location, rotation=(0,0,0), material=None):
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=location)
    o = bpy.context.active_object
    o.name = name; o.scale = size_xyz; o.rotation_euler = rotation
    if material: o.data.materials.append(material)
    return o

def add_cyl(name, radius, depth, location, axis='Z', rot_z=0.0, material=None, segs=16):
    bpy.ops.mesh.primitive_cylinder_add(vertices=segs, radius=radius, depth=depth, location=location)
    o = bpy.context.active_object
    o.name = name
    if axis == 'X':
        o.rotation_euler = (0, math.radians(90), rot_z)
    elif axis == 'Y':
        o.rotation_euler = (math.radians(90), 0, rot_z)
    else:
        o.rotation_euler = (0, 0, rot_z)
    if material: o.data.materials.append(material)
    return o

def add_diag(name, p1, p2, material, thickness=0.02):
    """Diagonal strut between two 3D points (cross-X braces etc.)."""
    mid = [(p1[i]+p2[i])/2 for i in range(3)]
    diff = [p2[i]-p1[i] for i in range(3)]
    length = math.sqrt(sum(d*d for d in diff))
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=mid)
    o = bpy.context.active_object
    o.name = name; o.scale = (thickness, thickness, length)
    dvec = mathutils.Vector(diff).normalized()
    q = mathutils.Vector((0,0,1)).rotation_difference(dvec)
    o.rotation_euler = q.to_euler()
    o.data.materials.append(material)
    return o

# ============================================================
# 3. STANDARD PIPE + FLANGE + PIER ASSEMBLY
# ============================================================
#
# Convention: all pipes at z=PIPE_Z (0.30). Flanges at apothem (hex edge midpoint).
# Pipe goes FROM inside building wall OUT to flange at hex edge.
# Pier supports pipe on the foundation level.
#
PIPE_Z       = 0.30
PIPE_R_OUT   = 0.11
FLANGE_R     = 0.13
FLANGE_D     = 0.04
BORE_R       = 0.055
BOLT_R       = 0.013
BOLT_D       = 0.025
BOLT_ORBIT_R = 0.095   # radius of 8-bolt ring on flange face
PIER_Z_BOT   = 0.055   # top of foundation
PIER_CAP_D   = 0.04

def add_pipe_stub(name, from_xy, to_xy, radius=PIPE_R_OUT, material=None):
    """Horizontal cylinder between two XY points at z=PIPE_Z. Rotation makes axis horizontal."""
    x1, y1 = from_xy; x2, y2 = to_xy
    dx, dy = x2-x1, y2-y1
    length = math.sqrt(dx*dx + dy*dy)
    cx, cy = (x1+x2)/2, (y1+y2)/2
    ang = math.atan2(dy, dx)
    bpy.ops.mesh.primitive_cylinder_add(vertices=14, radius=radius, depth=length,
                                         location=(cx, cy, PIPE_Z))
    o = bpy.context.active_object; o.name = name
    # Cylinder default axis = +Z. Y-rotate 90° → axis along +X, then Z-rotate to direction.
    o.rotation_euler = (0, math.radians(90), ang)
    o.data.materials.append(material or M("wood"))
    return o

def add_end_flange(prefix, angle_rad, outer_r):
    """Disc + bore + 8 bolts at the hex edge.  angle_rad = outward normal direction.
    outer_r = apothem of the hex edge (0.866 for Tier 1, 1.732 for Tier 2)."""
    nx, ny = math.cos(angle_rad), math.sin(angle_rad)
    # Main disc (slightly inset)
    cx, cy = nx * (outer_r - 0.02), ny * (outer_r - 0.02)
    bpy.ops.mesh.primitive_cylinder_add(vertices=14, radius=FLANGE_R, depth=FLANGE_D,
                                         location=(cx, cy, PIPE_Z))
    d = bpy.context.active_object; d.name = f"{prefix}_disc"
    d.rotation_euler = (0, math.radians(90), angle_rad)
    d.data.materials.append(M("metal_mid"))
    # Dark bore (goes through the disc)
    bpy.ops.mesh.primitive_cylinder_add(vertices=12, radius=BORE_R, depth=0.06,
                                         location=(nx*(outer_r-0.005), ny*(outer_r-0.005), PIPE_Z))
    b = bpy.context.active_object; b.name = f"{prefix}_bore"
    b.rotation_euler = (0, math.radians(90), angle_rad)
    b.data.materials.append(M("metal_dk"))
    # 8 bolts on ring radius BOLT_ORBIT_R on the flange face
    # Tangent plane at face: horizontal axis = (-ny, nx, 0), vertical axis = (0, 0, 1)
    tx, ty = -ny, nx
    for k in range(8):
        t = 2*math.pi*k/8
        offx = math.cos(t)*BOLT_ORBIT_R*tx
        offy = math.cos(t)*BOLT_ORBIT_R*ty
        offz = math.sin(t)*BOLT_ORBIT_R
        bpy.ops.mesh.primitive_cylinder_add(vertices=6, radius=BOLT_R, depth=BOLT_D,
                                             location=(nx*(outer_r-0.015)+offx,
                                                       ny*(outer_r-0.015)+offy,
                                                       PIPE_Z+offz))
        bo = bpy.context.active_object; bo.name = f"{prefix}_bolt_{k}"
        bo.rotation_euler = (0, math.radians(90), angle_rad)
        bo.data.materials.append(M("metal_dk"))

def add_collar(name, at_xy, angle_rad):
    """Dark metal ring where a pipe penetrates a building wall. Looks like the pipe enters the wall."""
    x, y = at_xy
    bpy.ops.mesh.primitive_cylinder_add(vertices=12, radius=0.13, depth=0.03,
                                         location=(x, y, PIPE_Z))
    c = bpy.context.active_object; c.name = name
    c.rotation_euler = (0, math.radians(90), angle_rad)
    c.data.materials.append(M("metal_dk"))

def add_pier_at(name, cx, cy, segment_angle):
    """Stone pier + dark cap under a horizontal pipe (the visible foot).
    segment_angle = rotation around Z so the pier's long side is tangential to the pipe."""
    pier_h = PIPE_Z - 0.02 - PIPE_R_OUT - PIER_Z_BOT
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(cx, cy, PIER_Z_BOT + pier_h/2))
    p = bpy.context.active_object; p.name = f"P_Pier_{name}"
    p.scale = (0.12, 0.22, pier_h); p.rotation_euler = (0, 0, segment_angle)
    p.data.materials.append(M("stone_lt"))
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(cx, cy, PIER_Z_BOT + pier_h + 0.02))
    c = bpy.context.active_object; c.name = f"P_PierCap_{name}"
    c.scale = (0.16, 0.26, PIER_CAP_D); c.rotation_euler = (0, 0, segment_angle)
    c.data.materials.append(M("stone_dk"))

def add_anchor_empty(name, angle_rad, apothem):
    """PLAIN_AXES empty at the flange position (hex edge midpoint, z=PIPE_Z)."""
    nx, ny = math.cos(angle_rad), math.sin(angle_rad)
    bpy.ops.object.empty_add(type='PLAIN_AXES', location=(nx*apothem, ny*apothem, PIPE_Z))
    a = bpy.context.active_object
    a.name = name; a.empty_display_size = 0.15
    a.rotation_euler = (0, 0, angle_rad)
    return a

def build_anchor_set(anchor_indices, apothem, wall_radius, name_prefix="B", pipe_material=None):
    """Build flange + pipe_stub + collar + anchor_empty for each edge index in anchor_indices.
    anchor_indices: list of 0..5 (stage 1 = [0,3], stage 2 = [0,1,3,4], stage 3 = all 6).
    apothem: outer hex-edge apothem (pipe end).
    wall_radius: inner building-wall radius (pipe start).
    Pipe+Collar created; no Pier (add separately with add_pier_at if needed)."""
    mat_wood = pipe_material or M("wood")
    for i in anchor_indices:
        ang = EDGE_ANGLES[i]
        nx, ny = math.cos(ang), math.sin(ang)
        # pipe stub from wall to flange
        add_pipe_stub(
            f"{name_prefix}_PipeStub_{i}",
            (nx*wall_radius, ny*wall_radius),
            (nx*apothem,     ny*apothem),
            material=mat_wood,
        )
        # collar where pipe enters wall
        add_collar(f"{name_prefix}_Collar_{i}",
                   (nx*(wall_radius+0.015), ny*(wall_radius+0.015)), ang)
        # flange at outer end (apothem)
        add_end_flange(f"{name_prefix}_Flange_{i}", ang, apothem)
        # anchor empty
        add_anchor_empty(f"anchor_{i}", ang, apothem)

# Stage → anchor indices (STYLE_GUIDE §7.4)
STAGE_ANCHORS = {
    1: [0, 3],
    2: [0, 1, 3, 4],
    3: [0, 1, 2, 3, 4, 5],
}

# ============================================================
# 4. STANDARD TIER-1 HEX STONE BASE (Harvester-pattern)
# ============================================================

def build_tier1_base(prefix="B", hex_r=0.98):
    """Foundation stack for Tier-1 buildings: dark stone 0→0.46, capstone 0.46→0.56,
    wood trim 0.56→0.59. Building body starts at z=0.59."""
    build_hex_prism(f"{prefix}_Base",     hex_r,      0.46, 0.00, M("stone_dk"))
    build_hex_prism(f"{prefix}_Capstone", hex_r*0.94, 0.10, 0.46, M("stone_lt"))
    build_hex_prism(f"{prefix}_Trim",     hex_r*0.90, 0.03, 0.56, M("wood_dk"))
    return 0.59  # returns top-of-base z where body can start

# ============================================================
# 5. ANIMATION PIVOTS + EMITTERS (Empties)
# ============================================================

def add_anim_pivot(name, location):
    """Empty that the runtime rotates. Parent rotating parts to it."""
    bpy.ops.object.empty_add(type='PLAIN_AXES', location=location)
    p = bpy.context.active_object
    p.name = name; p.empty_display_size = 0.15
    return p

def parent_to(pivot, children, keep_transform=True):
    bpy.ops.object.select_all(action='DESELECT')
    for o in children: o.select_set(True)
    pivot.select_set(True)
    bpy.context.view_layer.objects.active = pivot
    bpy.ops.object.parent_set(type='OBJECT', keep_transform=keep_transform)

def add_emitter(name, location):
    bpy.ops.object.empty_add(type='PLAIN_AXES', location=location)
    e = bpy.context.active_object
    e.name = name; e.empty_display_size = 0.08
    return e

# ============================================================
# 6. FINALIZE: FLAT-SHADE + AO BAKE + VCOL WIRE-UP (MANDATORY before export)
# ============================================================

def finalize_shading_and_bake():
    # Flat shading on all meshes
    for o in bpy.data.objects:
        if o.type == 'MESH':
            for p in o.data.polygons:
                p.use_smooth = False

    # Ensure each mesh has "Col" BYTE_COLOR attribute (POINT domain)
    meshes = [o for o in bpy.data.objects if o.type == 'MESH']
    for o in meshes:
        if not o.data.color_attributes.get("Col"):
            o.data.color_attributes.new(name="Col", type='BYTE_COLOR', domain='POINT')
        idx = list(o.data.color_attributes).index(o.data.color_attributes["Col"])
        o.data.color_attributes.active_color_index = idx

    # Select all, bake AO into vertex colors
    bpy.ops.object.select_all(action='DESELECT')
    for o in meshes: o.select_set(True)
    bpy.context.view_layer.objects.active = meshes[0]

    scene = bpy.context.scene
    scene.render.engine = 'CYCLES'
    scene.cycles.bake_type = 'AO'
    scene.cycles.samples = 128
    scene.cycles.use_denoising = False
    bpy.ops.object.bake(type='AO', target='VERTEX_COLORS', use_clear=True)

    # Rewire each mx_* material: Base Color = RGB(base) * VertexColor("Col"), MULTIPLY
    for m in bpy.data.materials:
        if not m.name.startswith("mx_") or not m.use_nodes: continue
        nt = m.node_tree
        bsdf = nt.nodes.get("Principled BSDF")
        if not bsdf: continue
        base_color = tuple(bsdf.inputs["Base Color"].default_value)
        for link in list(nt.links):
            if link.to_socket == bsdf.inputs["Base Color"]:
                nt.links.remove(link)
        for n in list(nt.nodes):
            if n.name in ("mx_VColor", "mx_RGB", "mx_Mix"):
                nt.nodes.remove(n)
        attr = nt.nodes.new("ShaderNodeAttribute"); attr.name="mx_VColor"
        attr.attribute_name="Col"; attr.location=(-600,100)
        rgb = nt.nodes.new("ShaderNodeRGB"); rgb.name="mx_RGB"
        rgb.outputs[0].default_value = base_color; rgb.location=(-600,-100)
        mix = nt.nodes.new("ShaderNodeMixRGB"); mix.name="mx_Mix"
        mix.blend_type='MULTIPLY'; mix.inputs["Fac"].default_value=1.0; mix.location=(-300,0)
        nt.links.new(rgb.outputs[0], mix.inputs["Color1"])
        nt.links.new(attr.outputs["Color"], mix.inputs["Color2"])
        nt.links.new(mix.outputs["Color"], bsdf.inputs["Base Color"])

# ============================================================
# 7. HERO CAMERA + RENDER PREVIEW + EXPORT
# ============================================================

def setup_hero_cam_and_world(target_z=0.5, bg_color=(0.659, 0.831, 0.941, 1.0)):
    bpy.ops.object.camera_add(location=(2.5, -2.5, 1.6))
    cam = bpy.context.object; cam.name = "HeroCam"
    target = mathutils.Vector((0, 0, target_z))
    direction = target - cam.location
    cam.rotation_euler = direction.to_track_quat('-Z', 'Y').to_euler()
    bpy.context.scene.camera = cam
    world = bpy.context.scene.world
    if world is None:
        world = bpy.data.worlds.new("World"); bpy.context.scene.world = world
    world.use_nodes = True
    bg = world.node_tree.nodes.get("Background")
    bg.inputs[0].default_value = bg_color
    bg.inputs[1].default_value = 1.0
    return cam

def render_preview(filepath, resolution=(1200, 900)):
    scene = bpy.context.scene
    scene.render.resolution_x, scene.render.resolution_y = resolution
    scene.render.resolution_percentage = 100
    scene.render.filepath = filepath
    bpy.ops.render.render(write_still=True)

def export_glb(export_path, save_blend=True, blend_path=None):
    import os
    if save_blend and blend_path:
        bpy.ops.wm.save_as_mainfile(filepath=blend_path)
    bpy.ops.object.select_all(action='DESELECT')
    for o in bpy.data.objects:
        if o.type in ('MESH', 'EMPTY'):
            o.select_set(True)
    bpy.ops.export_scene.gltf(
        filepath=export_path,
        export_format='GLB',
        use_selection=True,
        export_apply=True,
        export_yup=True,
        export_materials='EXPORT',
        export_extras=True,
    )
    meshes = [o for o in bpy.data.objects if o.type == 'MESH']
    polys = sum(len(o.data.polygons) for o in meshes)
    sz_kb = os.path.getsize(export_path) / 1024.0
    print(f"Exported {export_path}  {sz_kb:.1f}KB  polys={polys}")
    return export_path, sz_kb, polys

# ============================================================
# 8. USAGE SKELETON (copy this into a new building script)
# ============================================================
#
# fresh_scene()
# setup_palette()
# setup_lights()
#
# # Base
# body_z = build_tier1_base(prefix="X")
#
# # Body (building-specific)
# build_hex_prism("X_Body", 0.75, 0.80, body_z, M("stone_lt"))
# # ... more geometry ...
#
# # Pipes/Anchors — Stage 2 = [0,1,3,4], Tier 1 apothem=0.866, wall_radius=0.75
# build_anchor_set(STAGE_ANCHORS[2], apothem=0.866, wall_radius=0.75, name_prefix="X")
#
# # Optional: piers under long pipes
# # ang = EDGE_ANGLES[0]; mid = 0.5*(0.75+0.866); add_pier_at("E_mid", mid*math.cos(ang), mid*math.sin(ang), ang)
#
# # Optional animation: anim_spin_y pivot at top for rotating parts
# # pivot = add_anim_pivot("anim_spin_y", (0,0,top_z)); parent_to(pivot, [r1,r2,r3])
#
# # Finalize
# finalize_shading_and_bake()
# setup_hero_cam_and_world(target_z=0.5)
# render_preview("/home/diwidan/Schreibtisch/molanex/assets/buildings/XXX/XXX_s2_preview.png")
# export_glb(
#     export_path="/home/diwidan/Schreibtisch/molanex/assets/buildings/XXX/XXX_s2_100.glb",
#     save_blend=True,
#     blend_path="/home/diwidan/Schreibtisch/molanex/assets/buildings/XXX/XXX.blend",
# )
