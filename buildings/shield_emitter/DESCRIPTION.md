# Shield Emitter

## Funktion & Rolle
Absorbiert 100% eingehenden Schaden. Energie-Kosten steigen mit der
absorbierten Menge. Zentraler Verteidigungs-Baustein. Handbuch §9.2.

## Vision / Stimmung
Defensiv-würdevoll. Ein Kristall-getriebener Schild-Projektor, der bei
Aktivität eine leuchtende Kuppel über sich erzeugt. Wirkt "beschützend"
— Shield-Blau dominant, kein Rot. Das einzige wirklich "heldenhafte"
Gebäude der War-Seite.

## Silhouette
**7-Hex-Fläche** (R=2). **Runder Sockel** mit einem **zentralen
Kristall-Dom** in der Mitte und einem **Ring von kleineren
Schild-Emittern** um den Sockel. Der Dom ist das Herzstück —
durchscheinend, leuchtend.

## Materialien & Farben
- **Sockel:** Stein-hell (`#808286`), fast Marmor-weiß
- **Kristall-Dom:** transparenter Kristall mit Shield-Blau Tönung
- **Emitter-Ring:** Metall-mittel mit Shield-Blau LED-Augen
- **Ziergravuren:** Shield-Blau emissive auf dem Sockel
- **Schild-Bubble (bei Aktivität):** Shield-Blau `#38bdf8` halbtransparent

## Ausbaustufen

### Stage 1 — Einzel-Emitter (2 Anchors)
Kleiner Sockel mit einem Emitter und einem kleinen Kristall-Dom. Kein
Ring.

### Stage 2 — Kristall-Station (4 Anchors)
Voller runder Sockel, mittlerer Kristall-Dom, ein Ring aus vier
Emittern um den Sockel. Stufen-Zugang zum Sockel.

### Stage 3 — Festungs-Schild-Station (6 Anchors)
Großer Sockel, imposanter Kristall-Dom, sechs Emitter im Ring +
**sekundärer Ring aus kleineren Emittern** darüber, hexagonaler
Fuß-Teppich aus Ziergravuren. Wirkt wie ein Sakral-Bauwerk mit
Technik-Elementen.

## Pipe-Anchors
Anchors sind **Energie-Einlässe** am Sockel, ausgeführt als
**Shield-Blau leuchtende Flansche** mit Kristall-Inlays.

- Stage 1: `anchor_0`, `anchor_3`
- Stage 2: +`anchor_1`, `anchor_4`
- Stage 3: alle 6

## Schornsteine & Emissionen
- **Kein Schornstein.**
- **Keine Kontaminations-Emission.**
- **Emission-Glow:**
  - **Kristall-Dom pulsiert permanent** Shield-Blau (Ambient, 3s Zyklus)
  - Emitter-LEDs (am Ring) pulsieren synchron
  - Ziergravuren auf dem Sockel pulsieren sanft
  - **Bei aktivem Schild:** Zusätzlich entsteht eine **halbtransparente
    hexagonale Schild-Kuppel** (Shield-Blau, Shader-Vertex auf
    Kuppel-Mesh) über dem Gebäude und dem Schutzradius

## Animationen

### Ambient (läuft immer)
- Kristall-Dom-Puls (Shader, Emission-Uniform × Zeit)
- `anim_spin_y` auf dem oberen Dom-Stern (Stage 3), 0.2 rad/s
- Ziergravuren Shader-Puls

### State-gekoppelt
- **Bei aktivem Schild:** Schild-Kuppel sichtbar, Emitter werfen
  Shield-Blau-Partikel nach außen (`emitter_sparks` Shield-Blau),
  Dom-Puls schneller
- **Bei eintreffendem Schaden:** Schild-Kuppel **flackert kurz am
  Einschlagpunkt** (Shader-Ripple, sichtbar 0.5s), kleine Shield-Blau-
  Funken-Explosion am Einschlag
- **Bei Energie-Mangel:** Dom-Puls wird flacher, Emitter-LEDs
  wechseln zu Warnung-Rot, Schild-Kuppel wird durchsichtiger

## Condition-Varianten

### Condition 100
Kristall klar, Marmor weiß, Gravuren leuchtend.

### Condition 50
Kristall-Dom hat Risse, Marmor-Sockel rissig, zwei Emitter-LEDs dunkel,
Gravuren teilweise erloschen.

### Condition ruin
Kristall-Dom zerbrochen (Scherben am Sockel verstreut), Sockel in
Stücken, keine Emission, kein Schild möglich.

## Condition × Stage Matrix
Sockel konstant, Kristall-Dom und Emitter-Ringe wachsen mit Stufen.
Ruin-Variante: Kristall-Scherben sind charakteristisch sichtbar, fast
"tragisch".

## Umgebungsinteraktion
- Sockel erhöht (~0.1 Units über Boden).
- **Schild-Kuppel** (bei Aktivität) reicht über angrenzende Hexes
  aus und zeigt, welche Zone geschützt ist — **wichtiger Gameplay-
  Indikator**.
- Muss auf War-Seite-Terrain stehen.

## Gameplay-Hinweise
- **Tier:** 2 (War-Seite)
- **Radius:** 2 Hex (7-Hex-Footprint)
- **Schaden-Absorption:** 100%
- **Kosten:** 20 Energy + 2× absorbierte % pro Tick
- **Terrain-Bonus:** Berg reduziert Kosten um 30%
- Handbuch-Referenz: §9.2 Shield Emitter
