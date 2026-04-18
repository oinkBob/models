# Building Reference — Measured Standards

Diese Datei dokumentiert die **tatsächlichen Maße, Konventionen und Strukturen**,
extrahiert aus den bereits fertig gebauten Modellen (harvester, storage,
battery_factory, distributor, cleaner, maintenance_building, research_building).

**Ziel:** Jedes neue Gebäude muss zu diesen Werten passen, damit Rohre, Flansche
und Gesamt-Look konsistent bleiben. Werte hier sind **Messungen aus der Praxis**,
nicht aus Dokumenten abgeleitet.

Komplementär zu `STYLE_GUIDE.md` (kanonisch) und den Gebäude-`DESCRIPTION.md`.

---

## 1. Koordinaten-System

**Blender-Modellierung:** Z-up (Blender-Default)
**glTF Export:** Y-up (Konvention: `export_yup=True`)

| Blender | glTF/Game | Meaning |
|---|---|---|
| +X | +X | East (rechts auf dem Screen) |
| +Y | −Z | North (oben auf dem Screen, "hinten") |
| +Z | +Y | Up (Höhe über Boden) |

**Origin:** Boden-Mitte des Hex, (0,0,0) in Blender. Gebäude stehen auf z=0.

---

## 2. Hex-Geometrie

**Pointy-top-Orientierung** (Vertex an Norden/Süden, Edges-Mitten an Osten/Westen).
Vertices sind die "Spitzen" (Ecken) des Hex; Kanten-Mitten sind die "flachen Seiten".

Apothem (Zentrum → Kanten-Mitte) = R · cos(30°) ≈ R · 0.866.

### Blender-Hex-Primitive (CRITICAL)

`bpy.ops.mesh.primitive_cylinder_add(radius=R, vertices=6)` + `rotation_euler=(0,0,30°)`
erzeugt einen **pointy-top Hex** mit:
- Vertices (Spitzen) an: **90° (Nord), 30° (NO-Ecke), 330° (SO-Ecke), 270° (Süd), 210° (SW-Ecke), 150° (NW-Ecke)**
- Kanten-Mitten (wo Rohre hin sollen) an: **0° (Ost), 60° (NE), 120° (NW), 180° (West), 240° (SW), 300° (SE)**
- X-Extent (vertex-to-vertex horizontal) = 2·R·cos(30°) = **1.732·R**
- Y-Extent (vertex-to-vertex vertical) = **2·R**
- Apothem (Kanten-Mitten-Radius) = **0.866·R**

**Beachten:** Y-Extent > X-Extent für pointy-top! Die Spitzen zeigen nach oben/unten.

### Tatsächliche Tier-Werte (gemessen aus completed .glb)

| Tier | Blender R (für prim.) | Apothem | X-Extent | Y-Extent | Fläche-HxH | Vertex-Lage |
|---|---|---|---|---|---|---|
| 1 | **1.00** | 0.866 | 1.732 | 2.000 | ~1.79 × 1.96 (gemessen) | z.B. Foundation |
| 2 | **1.96** | 1.697 | 3.395 | 3.920 | ~3.514 × 3.92 (gemessen) | z.B. Foundation |
| 3 | ~2.94 | ~2.547 | ~5.08 | ~5.88 | ~5.27 × ~5.88 (est.) | — |

**Wichtig:** STYLE_GUIDE §15 spricht von "Modell-Kreis ~2.7" für Tier 2. Das ist
ein *grober* Wert. Tatsächlich verwendet: **Hex-Radius 1.96** (nicht 2.0).
Anchor-Position `(±1.732, 0)` für Tier-2 Ost/West liegt knapp **außerhalb** der
Foundation (Apothem 1.697) — der Flansch ragt 0.015 über die Hex-Kante hinaus.

### Pointy-Top-Hex Visualisierung (oben betrachtet)

```
              Spitze (90°)
                   ●
                 /   \
      Spitze   /     \  Spitze
      (150°) ●       ● (30°)
             │  HEX  │
    Kante   │  Zent- │   Kante
     180°───│  rum   │───  0°
      W    │        │    E
    Kante   │        │   Kante
      Spitze ●       ● Spitze
      (210°)  \     /  (330°)
                \   /
                 ●
              Spitze (270°)
```

**Rohre gehen in die MITTE einer Kante** (zwischen zwei Spitzen, nie AN einer Spitze):
- `anchor_0` (E): in der Mitte zwischen Spitzen 30° und 330° → Winkel 0°
- `anchor_1` (NE): in der Mitte zwischen Spitzen 30° und 90° → Winkel 60°
- `anchor_2` (NW): in der Mitte zwischen Spitzen 90° und 150° → Winkel 120°
- `anchor_3` (W): in der Mitte zwischen Spitzen 150° und 210° → Winkel 180°
- `anchor_4` (SW): in der Mitte zwischen Spitzen 210° und 270° → Winkel 240°
- `anchor_5` (SE): in der Mitte zwischen Spitzen 270° und 330° → Winkel 300°

Höhen typischer Tier-2-Gebäude (s1 → s2 → s3):
- research_building: 1.605 → 2.020 → 2.725
- distributor:      1.275 → 1.625 → 2.500
- maintenance:      1.085 → 1.080 → 1.680
- cleaner:          1.403 → 1.308 → 1.398 (weitestgehend flach)

---

## 3. Anchor-Positionen (Edge-Mitten)

Anchor-Höhe (z): **0.30** bei allen gemessenen Buildings.

### Tier 1 (apothem = 0.866)
| Anchor | Blender-x | Blender-y | z |
|---|---|---|---|
| anchor_0 (E)  | +0.866 | 0.000  | +0.30 |
| anchor_1 (NE) | +0.433 | +0.750 | +0.30 |
| anchor_2 (NW) | −0.433 | +0.750 | +0.30 |
| anchor_3 (W)  | −0.866 | 0.000  | +0.30 |
| anchor_4 (SW) | −0.433 | −0.750 | +0.30 |
| anchor_5 (SE) | +0.433 | −0.750 | +0.30 |

### Tier 2 (apothem = 1.732)
| Anchor | Blender-x | Blender-y | z |
|---|---|---|---|
| anchor_0 (E)  | +1.732 | 0.000  | +0.30 |
| anchor_1 (NE) | +0.866 | +1.500 | +0.30 |
| anchor_2 (NW) | −0.866 | +1.500 | +0.30 |
| anchor_3 (W)  | −1.732 | 0.000  | +0.30 |
| anchor_4 (SW) | −0.866 | −1.500 | +0.30 |
| anchor_5 (SE) | +0.866 | −1.500 | +0.30 |

### Stage → Anchor-Set
| Stage | Anchors vorhanden |
|---|---|
| s1 | 0, 3              (E + W) |
| s2 | 0, 1, 3, 4        (+ NE + SW) |
| s3 | 0, 1, 2, 3, 4, 5  (alle 6) |

Ausnahmen beobachtet:
- `cleaner`: **immer nur `anchor_0`** (Batterie-Input, 1 Rohr für alle Stages)
- `distributor`: **immer alle 6 Anchors** (Verteiler-Natur)
- `storage`, `battery_factory`, `research_building`: bleiben bei **2 Anchors (E+W)** in allen Stages
- `harvester`: folgt Standard-Pattern 2→4→6

---

## 4. Pipe + Flansch — Standardmaße

**Konstant über alle Gebäude.** Kopiere diese Werte **exakt**.

### Flansch-Scheibe (disc)
- Radius: **0.13** (Dimension 0.253 × 0.26 × 0.04)
- Tiefe (axial): **0.04**
- Material: `mx_stone_dk`
- Position: Scheibenmitte liegt auf Höhe **z = 0.300** und radial **genau auf apothem** (Tier 1: x=±0.861; Tier 2: x=±1.712)
  - Hinweis: minimale +/- Innenschrumpfung (0.005–0.020 inwärts) so dass die Scheibe sichtbar **an der Hex-Kante** sitzt, nicht davor

### Bore (Loch in Scheibenmitte)
- Radius: **0.055** (Dimension 0.11 × 0.11 × 0.06)
- Tiefe: **0.06** (ragt leicht durch die Scheibe)
- Material: `mx_stone_dk` (dunkler als Scheibe → liest als Loch)

### LED-Ring (optional, research hat's)
- Radius: **0.115** (Dimension 0.224 × 0.23 × 0.012)
- Tiefe: **0.012** (sehr dünn, sitzt vor der Scheibe)
- Material: `mx_flow_green`

### Bolzen (8 Stück, gleichmäßig rund um die Scheibe)
- Radius: **0.012**, Höhe: **0.025** (Dimension 0.023 × 0.026 × 0.025)
- Orbit-Radius um Scheibenmitte: **0.095**
- Winkel-Abstand: 45° (360°/8)
- Material: `mx_stone_lt`
- Achse: parallel zur Rohrachse (zeigt nach außen aus der Scheibe raus)

### Pipe-Stub (das Rohr selbst)
- Außenradius: **0.11** (Dimension 0.214 × 0.22 entspricht Durchmesser ~0.22)
- Material: `mx_metal_mid`
- Zentrum der Rohrachse: **z = 0.300**
- Achse: zeigt radial **vom Gebäude zum Flansch** (Normalenrichtung der Hex-Kante)
- **Länge variiert** je nach Abstand Gebäude ↔ Hex-Kante. Beispiele:
  - `harvester` (GF geht bis fast an Hex-Kante) → Stub sehr kurz (~0.10)
  - `storage` (Tier 1, GF schmaler): Stub-Länge 0.506
  - `research_building s2`: Stub-Länge 0.967, Center bei x=±1.248
  - `distributor` (mehrere Rohre pro Seite): 1.442 lang mit **2 Piers drunter**

### Pier (Stein-Stütze unterm Rohr)
- Dimension: **0.12 × 0.22 × 0.11** (WxDxH)
- z-Zentrum: **0.115** (zwischen Foundation oben und Plinth-Top)
- Material: `mx_stone_mid` bzw. `mx_stone_lt`
- **Orientierung:** die kurze Seite (0.12) entlang der Rohrachse; die lange Seite (0.22) quer dazu
- Bei langen Rohren **mehrere Piers** (Distributor hat Piers bei Rohr-Position 0.40 und 0.80)

### Pier-Cap (Abdeckung oben auf Pier)
- Dimension: **0.16 × 0.26 × 0.04**
- z-Zentrum: **0.190**
- Material: `mx_stone_dk`

---

## 5. Schicht-Aufbau (Layer-Stack) — Tier-2-Gebäude

Aus `research_building_s2` / `_s3` gemessen. Dies ist der **Standard-Aufbau**
für vertikal gegliederte Tier-2-Gebäude. Andere Tier-2 (z.B. flacher Cleaner,
breiter Distributor) weichen ab, aber das Schema hier ist die Referenz.

| Layer | z-Range | Footprint (X × Y) | Form | Material |
|---|---|---|---|---|
| **Foundation**    | 0.00 – 0.08 | Hex r≈1.76 | 6-Vertex-Plate (pointy-top) | `mx_stone_dk` |
| **FoundRim**      | 0.00 – 0.02 | Hex r≈1.86 | Rand-Hex, knapp unter Foundation | `mx_stone_lt` |
| **Plinth**        | 0.04 – 0.14 | ~1.65 × 1.05 (Gebäude-shape) | Rechteck unter GF | `mx_stone_lt` |
| **PlinthCap**     | 0.11 – 0.14 | ~1.65 × 1.05 | Abdeck-Trim | `mx_stone_dk` |
| **GF_Walls**      | 0.10 – 0.52 | 1.55 × 0.95 (s2) / 1.90 × 1.21 (s3) | Stein-Rechteck | `mx_stone_lt` |
| **GFBand_Low**    | ~0.12 – ~0.15 | GF +0.03 | Horizontales Akzentband | `mx_wood_dk` |
| **GFBand_High**   | ~0.48 – ~0.52 | GF +0.03 | Horizontales Akzentband | `mx_wood_dk` |
| **GFBeam** (4×)   | 0.09 – 0.53 | Ecken | 0.07 × 0.07 Holzbalken (s2: mx_wood_dk) | `mx_wood_dk` |
| **GFWinFrame/Window** | Mitte GF | N/S-Wände | Fenster-Rahmen + Glas | `mx_wood_dk` / `mx_heat` |
| **Balcony1**      | 0.55 – 0.58 | GF + ~0.05 | breite Stein-Plattform | `mx_stone_lt` |
| **Balcony1Trim**  | 0.56 – 0.58 | Balcony1 + 0.04 | Trim-Rand | `mx_wood_dk` |
| **Balc1Rail_Post** (8×) | 0.58 – 0.72 | rund um Balcony1 | Holz-Pfosten | `mx_wood_dk` |
| **Balc1Rail_Rail** (4×mid + 4×top) | 0.65 / 0.72 | Balcony1 Kanten | Horizontale Stäbe | `mx_wood` |
| **MF_Walls**      | 0.75 – 1.10 | 1.66 × 0.97 | schmaler als GF | `mx_wood` |
| **MFBand_Low/High** | variabel | MF + 0.03 | Akzentbänder | `mx_wood_dk` |
| **MFBeam** (4×)   | Ecken MF | | Holzbalken | `mx_wood_dk` |
| **Balcony2**      | ~0.95 – 1.00 | MF + 0.05 | zweite Balcony | `mx_stone_lt` |
| **Balc2Rail** | analog Balc1 | | Railing um Balcony2 | `mx_wood`/`mx_wood_dk` |
| **UF_Walls**      | 1.10 – 1.42 | 1.38 × 0.86 (s3) | noch schmaler | `mx_wood` |
| **UFBand**, **UFBeam**, **UFWinFrame/Window** | analog MF | | | |
| **UFRoof**        | 1.34 – 1.38 | UF +0.06 | Stein-Dach-Platte | `mx_stone_lt` |
| **Dome / Tower / Chimney / Flag** | 1.38 – var | zentral | gebäude-spezifisch | — |

**Faustregel:** Jede höhere Etage ist schmaler als die darunter. Jeder
Übergang hat einen Balcony mit sichtbarem Trim + Holz-Geländer.

### Tier-1-Aufbau (einfacher)

Harvester_s2:
- `Base`: 1.70 × 1.96 × 0.46 (wuchtige Basis direkt auf Hex)
- `Capstone`: 1.60 × 1.85 × 0.10
- `T` (Trim): 1.53 × 1.77 × 0.03
- Rotor/Turm/Schornstein darüber (gebäude-spezifisch)
- Piers sind meist nicht nötig — Base reicht bis nah an die Hex-Kante

---

## 6. Material-Palette (aus STYLE_GUIDE §5 + benutzte Material-Namen)

Verwende im Blender die **Material-Namen** aus der Spalte "Material".

### Stein / Metall
| Farbe | Hex | Material-Name | Verwendung |
|---|---|---|---|
| Stein hell    | `#808286` | `mx_stone_lt`   | Mauern, Plinth, Balcony |
| Stein dunkel  | `#5a5c5e` | `mx_stone_dk`   | Foundation, Trim, Pier-Cap |
| Metall mittel | *mid-grey*| `mx_metal_mid`  | Pipes |
| Metall dunkel | *charcoal*| `mx_metal_dk`   | Maschinen-Teile, Schornstein-Ringe |

### Holz
| Farbe | Hex | Material-Name |
|---|---|---|
| Holz       | `#8B6914` | `mx_wood` |
| Holz dunkel| `#5c4710` | `mx_wood_dk` |

### Akzent / Emissive
| Farbe | Hex | Material-Name |
|---|---|---|
| Flow-Grün    | `#4ade80` | `mx_flow_green` |
| Heat-Orange  | `#f97316` | `mx_heat` |
| Shield-Blau  | `#38bdf8` | `mx_shield_blue` |
| War-Rot      | `#dc2626` | `mx_warning` |
| Kontamination| `#84cc16` | `mx_contam` (selten benutzt) |
| Harvester-Gelb| `#f59e0b` | `mx_harvester` (nur Harvester) |
| Kupfer       | `#b86a1c` | `mx_copper` |

**Palette-Einhaltung:** Abweichungen werden vom Validator als Warning markiert.
Jedes `meta.json` listet die erlaubten Paletten-Farben des Gebäudes.

---

## 7. Naming-Konvention (Objekt-Präfixe)

Jedes Gebäude verwendet ein **ein-Buchstabe Präfix** vor allen Mesh-Namen,
damit Objekte eindeutig zuordenbar bleiben.

| Gebäude | Präfix |
|---|---|
| harvester | `H_` |
| storage | `S_` |
| battery_factory | `B_` |
| distributor | `D_` |
| cleaner | `C_` |
| maintenance_building | `T_` (nicht "M_", da Main reserviert) |
| research_building | `R_` |
| **main_building** | `M_` |
| trading_post | `TP_` oder `TR_` |
| beacon | `BC_` |
| black_market | `BM_` |
| analysis_center | `AC_` |
| guild_beam | `GB_` |
| harbor | `HB_` |
| exchange | `EX_` |
| — War-Side — | |
| control_projector | `CP_` |
| watch_tower | `WT_` |
| energy_node | `EN_` |
| jammer | `JM_` |
| phalanx | `PH_` |
| shield_emitter | `SE_` |
| resonance_harvester | `RH_` |
| resonance_trap | `RT_` |
| bastion | `BT_` |
| howitzer | `HW_` |
| overload_matrix | `OM_` |

Beispiele aus Realität:
- `R_Foundation`, `R_Plinth`, `R_GF_Walls`, `R_FlangeE_disc`, `R_Pier_E_mid`
- `H_Base`, `H_Capstone`, `H_FlangeE_disc`
- `D_PipeEast`, `D_Pier_E_0.40`, `D_Pier_E_0.80` (Distributor mit mehreren Piers)

**Sub-Naming für Anchors mit Richtung:**
- `{prefix}_Flange{E|W|NE|NW|SE|SW}_{disc|bore|led|bolt_0..7}`
- `{prefix}_PipeStub{E|W|NE|NW|SE|SW}` oder `{prefix}_Pipe{East|West|...}`
- `{prefix}_Pier_{E|W|NE|...}[_mid|_0.40|_0.80]`

---

## 8. Empty-Nodes (Anchors / Emitters / Animation)

**Anchors:** immer genau `anchor_0` … `anchor_5`, `PLAIN_AXES`-Empty.
Lokale +X-Achse zeigt radial nach außen.

**Emitters (optional pro Gebäude):**
- `emitter_smoke` — Kaminrauch (dunkelgrau)
- `emitter_sparks` — Funken (heat-orange)
- `emitter_flow` — Flow-Start (flow-grün)
- `emitter_haze` — Kontaminations-Nebel (giftgrün)

**Animation-Nodes (Parent der rotierenden Teile):**
- `anim_spin_y` / `anim_spin_x` / `anim_spin_z` — Rotation
- `anim_bob_y` — Auf-/Ab-Oszillation
- `anim_pump` — Pump-Scale

---

## 9. Render- & Export-Pipeline (konkret)

### Vor dem Bake
1. **Flat-Shading:** alle Meshes → `bpy.ops.object.shade_flat()`
2. Vertex-Color-Attribute **`Col`** (BYTE_COLOR, CORNER domain) auf allen Meshes

### AO-Bake (Cycles)
```python
scn.render.engine = 'CYCLES'
scn.cycles.samples = 48
scn.cycles.bake_type = 'AO'
scn.render.bake.target = 'VERTEX_COLORS'
# Alle Meshes selektiert, active gesetzt, dann:
bpy.ops.object.bake(type='AO')
```

### Material-Setup (pro Farbe)
Shader-Graph:
```
[RGB = Palette-Farbe] ┐
                       ├─ MixRGB (Multiply, Fac=1.0) ─→ BSDF Base Color
[Attribute 'Col']     ┘
BSDF → Material Output
Roughness 0.85, Specular 0.2
```

### glTF-Export
```python
bpy.ops.export_scene.gltf(
    filepath=path,
    export_format='GLB',
    use_selection=True,
    export_yup=True,
    export_apply=True,
    export_colors=True,
    export_attributes=True,
    export_animations=True,
    export_extras=True,
)
```

Zielgröße: **< 400 KB** für Tier-2 s3 hat bisher gehalten. Limit aus
STYLE_GUIDE: 1 MB (Tier 2), 2 MB (Tier 3), 500 KB (Tier 1).

---

## 10. Wichtige Regeln & Gotchas (aus User-Feedback)

### Rohre versorgen das Gebäude — immer klar sichtbar
- Rohre müssen **ins Gebäude** gehen. Sie starten INNERHALB des Baukörpers
  (durch die Wand hindurch) und enden am Flansch an der Hex-Außenkante.
  Mindest-Einschub: 0.10–0.15 Units hinter die sichtbare Außenwand.
- Rohre müssen **bis zur Hex-Kante reichen** — Flansch bei apothem 1.732
  (Tier 2) / 0.866 (Tier 1). Der Flansch ragt leicht aus der Foundation
  heraus (ca. 0.015 Units außerhalb Foundation-Apothem).
- Rohre dürfen **NICHT an einer Hex-Spitze** sitzen, sondern nur **in der
  MITTE einer Hex-Kante** (zwischen 2 Spitzen). Siehe §2 Visualisierung.
- **Keine schwebenden Rohrstummel** ohne Verbindung zum Baukörper.
- Unter jedem Rohr ein **Pier** (Stein-Stütze) zum Foundation-Level — gibt
  dem Rohr visuellen Halt. Pier muss **innerhalb der Foundation** liegen.

### Etagen dürfen nicht schweben
- Jede obere Etage sitzt **DIREKT** auf der Balcony-Oberkante darunter
  (kein z-Gap!). Beispiel: Balcony-Trim z=0.84-0.86, nächste Etage
  z_bot=0.86 (nicht 0.90).
- Wenn ein Balcony zwischen zwei Etagen sitzt: Balcony-Plate liegt auf
  Etage darunter; Railing-Posten ragen von Balcony-Top aus; Etage darüber
  beginnt auf derselben Höhe wie Balcony-Top (Railing ist AUSSERHALB der
  oberen Etagen-Wände).

### Rechteckige vs. hexagonale Sockel
- **Rechteckiger Sockel** funktioniert nur für 2 Rohre (E + W), weil nur
  diese senkrecht in die Wand gehen. Beispiele: research, storage,
  battery_factory.
- **4+ Rohre brauchen einen hex-ähnlichen Sockel** (oder Anschluss-Türme
  die aus der Wand ragen). Distributor macht's mit großer Hexagon-Basis;
  Maintenance hat Anschlusskanten an allen 6 Hex-Seiten.
- **Main Building:** hexagonaler oder sechseckiger War-Sockel mit Anschluss-
  Türmchen an jeder Hex-Kante (laut `main_building/DESCRIPTION.md` §7).

### Keine freihängenden Elemente
- Flaggen, Antennen, Schornsteine müssen auf dem Baukörper **aufsetzen**,
  nicht zur Seite rausstehen. Schornstein mit -0.05 Inset auf die
  UF-Roof, nicht am Rand balancieren.
- Dekoration nur **innerhalb des Gebäude-Umrisses**.

### Proportionen pro Tier einhalten
- Tier-2-Gebäude sollten Höhe **1.0 – 2.7** haben und das Tier-2-Hex
  (3.514 × 3.92) ausfüllen.
- Kein Gebäude auf halb-leerem Hex lassen (Fundament sollte mindestens
  `FoundRim` für die volle Hex-Größe haben).

### Stage-Progression sichtbar
- s1 → s2: +Etage oder +Turm, +2 Anchors, kein neuer Footprint
- s2 → s3: +höchste Etage / Dome / Turm-Spitze, +2 Anchors bei Standard-Pattern
- Condition-Degradation erst nach allen s1-s3-100 bauen (niedrigste Prio)

---

## 11. Pipeline-Standards — Pipes zwischen Gebäuden (nicht am Gebäude selbst)

`/assets/pipes/` hat `pipe_straight.glb`, `pipe_curve_gentle.glb`, `pipe_curve_sharp.glb`.
Diese Modelle müssen sich mit **denselben Flansch-Maßen** aus §4 andocken lassen —
Radius 0.11, Höhe z=0.30. Wenn du neue Pipe-Segmente baust, Bezugsfläche ist:

- **Entry/Exit auf Hex-Kante:** z=0.30, radial nach außen.
- **Entry-/Exit-Radius:** 0.11 außen. Keine verdickten Flansche am Pipe-Segment —
  der Flansch ist Teil des Gebäudes, nicht des Pipe-Segments.

---

## 12. Validierungs-Checkliste vor Export

- [ ] Alle Meshes flat-shaded
- [ ] `Col` Vertex-Color-Attribut baked (AO)
- [ ] Alle Empties heißen korrekt (`anchor_X`, `emitter_X`, `anim_X`)
- [ ] Anchor-Position stimmt mit Tabelle §3
- [ ] Flansch-Maße (§4) eingehalten — Radius 0.13, 8 Bolts
- [ ] Pipe-Radius 0.11, z=0.30
- [ ] Jedes Rohr hat einen Pier drunter (außer Rohr ist sehr kurz innerhalb Hex-Center)
- [ ] Keine schwebenden Elemente
- [ ] Material-Namen `mx_*` aus Palette
- [ ] File-Size < 1 MB (Tier 2)
- [ ] Export: `export_yup=True`, `export_colors=True`
- [ ] Dateiname: `{building}_s{stage}_100.glb`
- [ ] `meta.json` um neues Variant erweitert
- [ ] `manifest.json` aktualisiert (path + totalSize)
