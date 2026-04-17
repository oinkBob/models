# Resonance Harvester

## Funktion & Rolle
Sammelt Kristalle aus kontrollierten War-Hexes. Die War-Seite-
Wirtschaftsquelle — ohne ihn kein Kristallfluss. Handbuch §9.2.

## Vision / Stimmung
Schwer-industrielles Bergwerk. Förderturm über einem Grubenschacht,
Kristallsplitter werden aus dem Boden gefördert und verarbeitet.
Dunkel, rau, staubig. Kontrastiert mit dem edlen Shield Emitter —
der Harvester ist der "schmutzige Arbeiter" der War-Seite.

## Silhouette
**7-Hex-Fläche** (R=2). **Grubenschacht** in der Mitte mit einem
**Förderturm** darüber (offenes Metallgerüst, ca. 2 Units hoch). Am
Fuß des Turms **Kristall-Verarbeitungs-Container**. Ein Förderband
führt Kristalle vom Schacht zu einem Sammelbereich.

## Materialien & Farben
- **Sockel:** Stein-dunkel (`#5a5c5e`) mit gebrochenen Kanten
- **Förderturm:** Metall-dunkel, rostig, sichtbare Verstrebungen
- **Kristall-Container:** Metall mit sichtbaren violett-War-Rot
  Kristall-Fragmenten
- **Förderband:** Holz-dunkel Rahmen, Gummi-schwarz Band
- **Kristalle:** violett-War-Rot Mischton
- **Akzente:** Harvester-Gelb Warn-Aufkleber an gefährlichen Stellen

## Ausbaustufen

### Stage 1 — Einfacher Förderturm (2 Anchors)
Kleiner Schacht, kurzer Förderturm, ein einzelner Kristall-Container
am Fuß. Wirkt wie ein Pioneer-Bergwerk.

### Stage 2 — Bergwerks-Anlage (4 Anchors)
Größerer Schacht, höherer Förderturm mit zwei Seilwinden, **Förderband**
zu einem Verarbeitungshaus an der Seite, zwei Container.

### Stage 3 — Große Bergwerks-Station (6 Anchors)
Breiter Schacht, massiver dreigliedriger Förderturm, vollautomatisches
Förderband-System zu einem großen Verarbeitungs-Komplex, mehrere
Kristall-Container, kleine Loren auf Schienen um den Schacht.

## Pipe-Anchors
Anchors sind **Kristall-Auslass-Schächte** — sichtbar als **Metall-
Tore mit rotierenden Kristall-Siegeln** (die Kristalle werden in Pipes
gepumpt).

- Stage 1: `anchor_0`, `anchor_3` am Sockel (y≈0.35)
- Stage 2: +`anchor_1`, `anchor_4`
- Stage 3: alle 6

## Schornsteine & Emissionen
- **1 Schornstein** (Stage 2+3) am Verarbeitungshaus. `emitter_smoke`
  **staubig-grau** (nicht dunkel wie Battery-Factory-Rauch — eher
  **Steinstaub**).
- **Kontaminations-Beitrag: ja, leicht** (Bergbau-Staub).
- **Emission-Glow:**
  - Kristalle in den Containern leuchten War-Rot/violett
  - Förderband leuchtet flüchtig wenn Kristalle darüber wandern
  - Gruben-Schacht hat von unten einen dunkelroten Glow (tiefer, Shader)

## Animationen

### Ambient (läuft immer)
- **Förderseil** `anim_bob_y` auf und ab (langsam, Shader oder
  procedural)
- **Förderband** bewegt sich (Shader-UV-Scroll)
- Seilrollen am Turm `anim_spin_y` langsam
- Staubpartikel aus dem Schacht (`emitter_haze` staubig-grau minimal)

### State-gekoppelt
- **Bei aktivem Abbau:** Förderseil-Bewegung schneller, Förderband
  läuft, **Kristalle erscheinen sichtbar auf dem Band** (Shader-Tricks
  oder Partikel), Schornstein raucht stärker
- **Bei Kristallmangel (nicht genug War-Hexes kontrolliert):** Anlage
  läuft idle, keine Kristalle auf dem Band, Emitter-Glow matter

## Condition-Varianten

### Condition 100
Metall ölig geputzt, Holz frisch, Kristalle in Containern voll.

### Condition 50
Metall rostig, Förderband mit Rissen, ein Container beschädigt mit
Kristall-Lecks (violett-Partikel am Boden), Holz splittert.

### Condition ruin
Förderturm kollabiert (schief oder am Boden), Schacht eingestürzt,
Container umgekippt mit verstreuten Kristallen, Förderband
gerissen. Dystopisch.

## Condition × Stage Matrix
Schacht-Position konstant, Förderturm und Verarbeitungs-Komplex wachsen
mit Stufen. Ruin-Variante immer mit verstreuten Kristallen am Boden —
charakteristisch.

## Umgebungsinteraktion
- **Grubenschacht** ist sichtbar ins Terrain eingelassen (0.5 Units tief).
- Leichte Staubwolken im Umkreis.
- Kleine Kristall-Splitter um das Gebäude herum (Deko).
- Muss auf War-Seite-Terrain stehen.
- Kontaminations-Beitrag → kleiner Giftgrün-Dunst-Anteil möglich bei
  Kontaminations-Level.

## Gameplay-Hinweise
- **Tier:** 2 (War-Seite)
- **Radius:** 2 Hex (7-Hex-Footprint)
- **Rolle:** Sammelt Kristalle aus kontrollierten War-Hexes
- Handbuch-Referenz: §9.2 Resonance Harvester
