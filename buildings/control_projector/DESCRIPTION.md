# Control Projector

## Funktion & Rolle
Projiziert territoriale Kontrolle auf benachbarte Hexes der War-Seite.
Ohne Control Projectors kann ein Spieler keine War-Hexes halten.
Handbuch §9.1.

## Vision / Stimmung
Ein technisches, leicht bedrohliches Projektor-Gerät. Gerichtet,
funktional, kalt. Passt zur War-Seite-Ästhetik: Metall dominant, rote
Akzente, weniger warm als Economy-Seite. Soll "hier wird Territorium
gesichert" ausstrahlen.

## Silhouette
**Dreifuß-Stativ** mit einer **geneigten Projektor-Schüssel** oben —
wie eine Satelliten-Parabol, aber nach unten geneigt (projiziert in die
Umgebung). Die Schüssel kann rotieren. Am Fuß schwere Kabel-Bündel.

## Materialien & Farben
- **Stativ:** Metall-dunkel, Stein-dunkel Fußplatten
- **Schüssel:** Metall mit War-Rot Innenseite
- **Strahler-Kern in der Schüssel:** War-Rot (`#dc2626`) emissive
- **Kabel:** dunkles Gummi-Schwarz mit War-Rot Ummantelungs-Streifen
- **Warn-Markierungen:** gelb-schwarze Schraffur an der Basis (auf
  War-Seite angemessen)

## Ausbaustufen

### Stage 1 — Einfacher Projektor (2 Anchors)
Schlankes Dreifuß-Stativ mit einer Schüssel oben. Ein Kontrollkasten
am Fuß.

### Stage 2 — Doppel-Projektor (4 Anchors)
Stativ breiter, **zwei Schüsseln** in gegenüberliegender Anordnung
(gegenseitig verstärkend). Stabilere Basis mit Ring-Sockel.

### Stage 3 — Projektor-Krone (6 Anchors)
Breiter Sockel, **drei Schüsseln** im 120°-Raster, zentraler Turm
zwischen den Schüsseln mit einem roten Warnlicht auf der Spitze.
Massive Kabel-Bündel.

## Pipe-Anchors
Anchors sind **War-Seite-Energie-Einlässe** — kompakter als Economy-
Anchors, mit **roten LED-Ringen** um die Flansche. Sichtbar "militärisch".

- Stage 1: `anchor_0`, `anchor_3` am Sockel (y≈0.2)
- Stage 2: +`anchor_1`, `anchor_4`
- Stage 3: alle 6

## Schornsteine & Emissionen
- **Kein Schornstein.**
- **Keine Kontaminations-Emission.**
- **Emission-Glow:**
  - Strahler-Kerne in den Schüsseln pulsieren War-Rot (Ambient)
  - Kabel-Ummantelungs-Streifen pulsieren synchron
  - Warnlicht auf der Spitze (Stage 3) blinkt alle 1.5s
  - Projektor wirft einen **War-Roten Lichtkegel auf das Ziel-Hex**
    (Projektion-Beam, Shader-Vertex auf einem Kegel-Mesh zum Boden)

## Animationen

### Ambient (läuft immer)
- `anim_spin_y` auf der Hauptschüssel (Stage 1), 0.6 rad/s
- Zwei Schüsseln `anim_spin_y` synchron (Stage 2)
- Drei Schüsseln `anim_spin_y` mit leichtem Versatz (Stage 3)
- Warnlicht Shader-Blink

### State-gekoppelt
- **Bei aktiver Projektion:** Lichtkegel auf Ziel-Hex intensiv sichtbar,
  `emitter_sparks` War-Rot an der Schüssel-Innenseite, Schüssel-
  Rotation schneller
- **Bei Stromausfall:** Warn-Rot-Blinken schneller, alle Emissionen aus
- **Bei Beschuss (eingehender Schaden):** kurzer Warn-Flash

## Condition-Varianten

### Condition 100
Metall geputzt, Schüssel-Innenseite glatt War-Rot, Kabel ordentlich.

### Condition 50
Schüsseln zerkratzt, ein Kabel hängt lose, Rost an der Basis, ein
Warnlicht erloschen.

### Condition ruin
Stativ umgekippt, Schüsseln auf dem Boden, Kabel gebrochen mit
Funken-Partikeln, War-Rot-Kern erloschen.

## Condition × Stage Matrix
Sockel-Form bleibt konstant, Schüssel-Anzahl wächst mit Stufen.
Ruin-Variante immer "umgekippt" — dramatisch gescheitert.

## Umgebungsinteraktion
- Kleine War-Rot-Bodenplatten markieren den Wirkungsradius.
- Muss auf War-Seite-Terrain stehen (Gameplay).
- Bei Nacht sehr auffällig durch Projektions-Beam.

## Gameplay-Hinweise
- **Tier:** 1 (War-Seite)
- **Radius:** 1 Hex
- **Rolle:** Projiziert Kontrolle auf bis zu 7 benachbarte Hexes
- Handbuch-Referenz: §9.1 Control Projector
