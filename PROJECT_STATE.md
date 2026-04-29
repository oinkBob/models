# Asset-Pipeline Übergabe

> **Stand:** 2026-04-25 abends. Geschrieben damit eine neue Claude-Session ohne Kontext-Verlust weiterarbeiten kann.

---

## Was ist das Projekt?

Modelle, erstellt mit Claude — für ein Hex-Grid-Strategiespiel im Browser (Three.js). Das Spiel nutzt **nur eine Hex-Größe** (HEX_R=1.0). Auf jedem Hex liegt entweder Terrain oder eine "Plate", auf die Spieler ein Gebäude oder ein Rohr-Segment setzen können.

Alle Assets liegen in `/home/diwidan/Schreibtisch/Assets/`. Memory-Files in `~/.claude/projects/-home-diwidan-Schreibtisch/memory/` dokumentieren Projekt-Konventionen.

---

## Aktueller Asset-Stand

```
/home/diwidan/Schreibtisch/Assets/
├── PROJECT_STATE.md                       ← du liest gerade
│
├── base_plate/                            ✓ FERTIG
│   ├── plate/
│   │   ├── base_plate.glb        376 KB · 1084 Tris · Building-Foundation
│   │   ├── base_plate.blend
│   │   └── base_plate_preview.png
│   ├── deko/
│   │   ├── planks.glb             76 KB · 2 verwitterte Holzbretter
│   │   ├── lamp.glb              332 KB · PolyHaven wooden_lantern_01
│   │   └── deko.blend
│   ├── base_plate_with_deko_preview.png
│   └── meta.json
│
├── pipe_plate/                            ✓ FERTIG
│   ├── pipe_plate.glb            126 KB · 168 Tris · niedrige Plate für Rohre
│   ├── pipe_plate.blend
│   ├── pipe_plate_preview.png
│   └── meta.json
│
└── pipes/                                 ⚙ IN PROGRESS
    ├── pipe_straight.glb         162 KB · 1750 Tris · ✓ DONE — Holz-Brackets, 5 Lampen, Connection-getestet
    ├── pipe_curve_gentle.glb     174 KB · 1614 Tris · ✓ DONE — 60°-Bogen Radius 1.5 (E↔NW)
    ├── pipe_curve_sharp.glb      ⏳ TODO — 120°-Bogen (benachbarte Kanten, Radius 0.5)
    ├── connection_test.png             Composite: base_plate + pipe_plate + pipe_straight
    ├── connection_closeup.png          Close-up am Joint
    ├── pipe_curve_gentle_*.png         3 renders: preview, topdown, connection_test
    ├── pipe_*.blend                    Blender-Quellen
    └── meta.json
```

**Gesamt aktuell:** ~1.1 MB für drei Hex-Asset-Familien. Web-tauglich ✓.

---

## Geometrie-Konventionen (zwingend einhalten)

| Maß | Wert | Bedeutung |
|---|---|---|
| Hex-Radius (HEX_R) | 1.0 | Apothem = 0.866. Pointy-top (Vertex bei 30°+60°·i, Edge-Mitte bei 60°·i) |
| Pipe-Centerline-Z | 0.30 | Alle Flansche und Pipe-Mittelachsen liegen hier |
| Pipe-Außenradius | 0.11 | → Pipe-Bottom z=0.19, Pipe-Top z=0.41 |
| pipe_plate-Top | 0.19 | Damit liegt Pipe-Bottom nahtlos auf dem Wood-Deck |
| base_plate-Höhe | 0.72 | Building-Plate (mit Pipe-Recess auf z=0.30) |
| Flansch-Disc | r=0.135, d=0.04 | Im Recess der base_plate (apothem−0.04 inset) |
| Flansch-Bolts | r=0.020, d=0.040, Orbit r=0.10, 8 Stück | **Dieselben Maße auf Pipe und base_plate — Bolts greifen ineinander wenn 2 Hexes sich treffen** |

**Anchor-Konvention:** Edge-Index 0=E (0°), 1=NE (60°), 2=NW (120°), 3=W (180°), 4=SW (240°), 5=SE (300°). Anchor-Empties (`PLAIN_AXES`) heißen `anchor_0..5`, sitzen auf z=0.30 am Apothem.

---

## Material-Pipeline (KRITISCH — Blender 5.1.1 spezifisch)

**Render-Konzept:** Three.js nutzt `MeshBasicMaterial` (= flat-shaded, kein PBR). Wir backen daher AO ins Vertex-Color, alles weitere ist die Diffuse-Textur. **Kein Normal/Rough/Metal/Specular** — würde nur Bytes verschwenden.

### Material-Setup (modern Blender 5.1):
```
Image Texture (Diffuse) → ShaderNodeMix(MULTIPLY, RGBA) → BSDF Base Color
                            ↑
                       VertexColor("Col")
```

⚠ **Blender 5.1-spezifische Stolperfallen** (entdeckt durch leidvolle Erfahrung):
1. **`ShaderNodeMixRGB` (Legacy) wird vom 5.1 glTF-Exporter NICHT als VertexColor-Nutzung erkannt.** Immer den **modernen `ShaderNodeMix` mit `data_type='RGBA'`** nutzen, sonst kommt im Export "Active Vertex Color will not be exported"-Warnung und der AO-Bake landet stillschweigend nicht im GLB.
2. **`ShaderNodeAttribute(name='Col')` ebenfalls nicht erkannt** — stattdessen `ShaderNodeVertexColor(layer_name='Col')` verwenden.
3. **Mix-Socket-Indizes für RGBA-Mode:** Factor=`mix.inputs[0]`, A=`mix.inputs[6]`, B=`mix.inputs[7]`, Result=`mix.outputs[2]`. Nicht über `.inputs["A"]` ansprechen — kann scheitern.
4. **`export_colors=True` Parameter gibt es in 5.1 nicht mehr** → einfach weglassen, Vertex-Colors werden default exportiert sobald sie im Material referenziert sind.
5. **AO-Bake braucht `bpy.context.scene.render.engine = 'CYCLES'`** vor dem Aufruf. Sonst: "Current render engine does not support baking" — Eevee kann nicht baken.
6. **Cylinder ohne Längs-Subdivisionen → AO-Bake = 0 wenn Endkappen in andere Geometrie eingebettet sind.** Pipes brauchen `subdivide(number_cuts=4)` damit Mid-Vertices vorhanden sind.
7. **Lampen-Embed in Pipe vermeiden:** wenn Lampe minimal in Pipe eingebettet ist, starten AO-Rays inside der Lampe → AO=0 auf der gesamten Pipe-Oberseite. **Lampe immer GENAU auf Pipe-Top setzen, kein Z-Embed.** Während AO-Bake Lampe per `hide_render=True` ausblenden — sie soll keine AO-Rays auf der Pipe blockieren.

### Texture-Pipeline (Standard für JEDES neue Asset):
1. **PolyHaven-Asset importieren** via `mcp__blender-mcp__download_polyhaven_asset`
2. **PBR-Maps strippen** — nur Diffuse behalten. Normal/Rough/Metal/Displacement/AO entfernen (wir rendern flat-shaded).
3. **Bilder runterskalieren** auf 512×512: `for img in bpy.data.images: if img.size[0]>512: img.scale(512,512)`
4. **Cube-Project UVs**: `bpy.ops.uv.cube_project(cube_size=...)` — Größe abhängig vom Mesh (kleiner Mesh = kleinerer cube_size).
5. **AO-Bake** (Cycles, `bake_type='AO'`, samples=32, `world.light_settings.distance=0.4..0.6`, `target='VERTEX_COLORS'`).
6. **Material verdrahten**: TexImage → MixRGBA(MULT) → MixRGBA(MULT) → BSDF (Texture × Tint × VertexColor).
7. **Glättung erforderlich:** `for p in mesh.polygons: p.use_smooth = False` (flat shading).

### Export-Standard:
```python
bpy.ops.export_scene.gltf(
    filepath=...,
    export_format='GLB',
    use_selection=True,
    export_apply=True,
    export_yup=True,
    export_materials='EXPORT',
    export_extras=True,
    export_animations=False,
    export_lights=False,
    export_image_format='JPEG',
    export_jpeg_quality=80,
    export_draco_mesh_compression_enable=True,
    export_draco_mesh_compression_level=6,
)
```
→ Liefert typische Größen 50-400 KB pro Modell. Alle Browser-tauglich.

---

## Material-Familien (aktueller Stand)

### Aufs `base_plate.glb`:
- `mx_stone_tex` — castle_wall_slates Diffuse (1k→512) — Stein-Wand
- `mx_wood_tex` — dark_planks Diffuse — schmaler Holz-Trim-Band
- `mx_metal_tex` — rust_coarse_01 Diffuse — Flanschen, Recess-Backs, Pipe-Stubs
- `mx_metal_dk`, `mx_metal_lt` — Palette dark/light grey für Bolts und kleine Details

### Auf `pipe_plate.glb`:
- `mx_stone_tex` — castle_wall_slates für Foundation-Body
- `mx_wood_tex` — wood_planks_dirt für Holz-Deck oben
- `mx_metal_mid` — Palette grau für Nägel

### Auf `pipe_straight.glb` (rusty_metal_04 + wood_planks_dirt):
| Material | Tint RGB | Verwendung |
|---|---|---|
| `mx_metal_pipe` | (0.92, 0.92, 0.94) | Pipe-Body |
| `mx_metal_fittings` | (1.15, 1.05, 0.95) | Flansche + Bänder |
| `mx_metal_lamps` | (0.40, 0.42, 0.48) | Lamp-Frames |
| `mx_metal_bolts` | (1.35, 1.20, 1.00) | Alle Bolts |
| `mx_wood_brackets` | (0.85, 0.78, 0.65) | **Holz-Brackets** (NEU) |
| `mx_lamp_bulb` | warm yellow | Emissive Glühbirne (5×) |

Zwei Diffuse-Texturen, 5 Material-Varianten via Tint-Multiplikator.

---

## Workflow-Konventionen

### Three.js Anchor-Snap
- Pipe-/Plate-Modelle haben `anchor_0..5` als Empties an den Hex-Edge-Mitten (z=0.30, am Apothem).
- Threejs liest die Welt-Position dieser Empties NACH Y-Rotation des Pipe-Roots, um zu wissen wo angrenzende Hexes andocken müssen.
- Z=0.30 ist die UNIVERSELLE Pipe-Höhe — alle Flansche und Pipe-Mittelachsen sitzen hier.

### Three.js Lamp Flow-Indikator
- Pipe-Modelle haben pro Lampe eine separate Bulb-Mesh (`PS_Lamp0_bulb`..`PS_Lamp4_bulb`) mit emissive Material.
- Three.js kann pro Bulb `material.emissive` und `material.emissiveIntensity` zur Laufzeit setzen für Flow-Anzeige.
- Wandernde Welle (z.B. für Flow-Richtung):
  ```js
  bulbs.forEach((b, i) => {
    const phase = ((t/300 + i*0.2) % 1);
    const intensity = Math.max(0, 1 - 4*Math.abs(phase - 0.5)) * 2;
    b.traverse(c => { if (c.material?.emissiveIntensity !== undefined) c.material.emissiveIntensity = intensity; });
  });
  ```

### Pipe-Rotation
- `pipe_straight.glb` deckt 3 Verbindungen ab durch Y-Rotation:
  - 0° = E↔W
  - 60° = NE↔SW
  - 120° = NW↔SE
- Analog werden curve-Pipes durch Rotation auf alle 6 Edge-Paare passen.

### Mounting-Architecture (clean-slate)
- **Pipes haben KEINE integrierte Foundation** — die `pipe_plate` ist die separate Foundation. Workflow im Spiel: erst Plate bauen, dann Rohr drauf.
- Spieler-Workflow im Game: erst Plate bauen, dann Rohr drauf.

---

## Was als nächstes ansteht

1. **`pipe_curve_gentle.glb`** — 120°-Bogen (eine Hex-Kante übersprungen). Geometrie: Bogen-Tube von einem Anchor zum anderen, gleicher Radius/Querschnitt wie pipe_straight, gleiche Bauteile (Flansche, Bänder, Brackets, 5 Lampen entlang der Kurve).
2. **`pipe_curve_sharp.glb`** — 60°-Bogen (benachbarte Kanten). Engere Kurve, evtl. weniger Lampen.
3. **Open visuelle Punkte** für Refinement-Pass:
   - Bracket-Texturierung wirkte zuletzt noch nicht ganz richtig — User-Feedback "stimmt noch nicht"
   - Bolts könnten weniger "clean" wirken (aktuell: rusty_metal_04 mit Bright-Tint, evtl. dunkler oder mit anderem Wear-Look testen)
4. **Gebäude-Modelle** (kommt später) — auf der base_plate stehende Tier-1-Gebäude (Harvester, Storage, etc.).
5. **Terrain-Tiles** für Hexes ohne Plate (Gras, Wald, Berg, Wasser, Sand, Sumpf).

---

## Tech-Setup (Stand 2026-04-25)

- **Blender 5.1.1** in `/opt/blender-5.1.1/`, `/usr/local/bin/blender` zeigt drauf. Draco-Library liegt in `/opt/blender-5.1.1/5.1/scripts/addons_core/io_scene_gltf2/libextern_draco.so` und wird automatisch beim Export benutzt.
- **blender-mcp** v1.5.5 (GitHub HEAD `7636d13b`) installiert via `uv tool install --force git+https://github.com/ahujasid/blender-mcp.git`. Addon `blender_mcp_addon.py` ist im Blender 5.1.1 installiert und mit Connect to Claude verbunden.
- **Claude MCP**: `claude mcp list` zeigt `blender-mcp: ✓ Connected`. PolyHaven-Integration ist aktiv.
- **GitHub CLI** `gh` ist als `oinkBob` authentifiziert.

---

## Memory-System (Auto-recall in jeder neuen Session)

Diese Files werden automatisch in jeder neuen Claude-Session geladen:

- `~/.claude/projects/-home-diwidan-Schreibtisch/memory/MEMORY.md` (Index)
- Project-Memory — Projektkontext mit HEX_R=1, Renderpipeline, neuer Asset-Ordner
- `feedback_workflow_quality.md` — User bevorzugt langsam+gewissenhaft, mit Rückfragen
- `feedback_asset_optimization.md` — Standard-Optimierungs-Pipeline (PBR strippen, 512px, JPEG Q80, Draco)

**Bei neuer Session:** Diese Datei lesen + die Memory-Files werden eh geladen → in 5 Minuten wieder im Bilde.

---

## Render-Beispiele (im jeweiligen Asset-Ordner)

- `base_plate/base_plate_with_deko_preview.png` — Foundation + Bretter + Laterne
- `pipe_plate/pipe_plate_preview.png` — niedrige Plate
- `pipes/pipe_straight_with_plate_preview.png` — Rohr auf Plate, finaler Look v6

---

## User-Präferenzen (wichtig fürs Verhalten)

- **Sprache:** Deutsch in Kommunikation. Code/JSON-Schlüssel auf Englisch.
- **Tempo:** langsam und sorgfältig, lieber Rückfragen stellen als schnell falsch liefern.
- **Optik:** stylized low-poly+ aber visuell hochwertig. Web-Performance ist KRITISCH (jedes Modell <500 KB Ziel, hartes Limit <2 MB).
- **Konsistenz wichtig:** Bolts/Schrauben sollen zwischen Assets dieselben Maße + Material haben. Texturen sollen über die Welt zusammenpassen, nicht jedes Asset eine neue Familie aufmachen.
- **Vor destruktiven Aktionen IMMER bestätigen** (sudo, Datei-Löschen, etc.). Nicht-destruktive Schritte können einfach ausgeführt werden.

---

## Connection-Test (✓ verifiziert in dieser Session)

`pipes/connection_test.png` und `pipes/connection_closeup.png` zeigen die Welt-Komposition:
- base_plate at (0, 0, 0) + pipe_plate at (1.732, 0, 0) — angrenzende Hexes mit gemeinsamer East-West-Edge bei x=0.866
- pipe_straight auf der pipe_plate
- Pipe-W-Flansch trifft visuell auf base_plate-E-Recess
- Bolts treffen sich am Apothem (x=0.866) — exakte Spiegelung der 8-Bolt-Ringe von beiden Seiten
- 5mm Lücke zwischen den beiden Flansch-Discs ist die natürliche Hex-Edge-Boundary

→ **Geometrie-Konventionen sind VALIDIERT**, das System funktioniert.

## Rückfragen / offene Punkte für nächste Session

- Bolts wirken evtl. immer noch leicht zu clean — Bright-Tint hilft, aber nicht perfekt. Niedrige Prio.
- Lamp-Frame AO-Bake könnte intensiver sein. Niedrige Prio.
- Bracket-Textur ist nun Holz (wood_planks_dirt) — User happy. ✓
