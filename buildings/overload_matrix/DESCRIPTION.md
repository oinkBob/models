# Overload Matrix

## Funktion & Rolle
**Einzige Waffe gegen die Economy-Seite.** Exponentielle Energie-
Kosten pro Tick (1000 → 1500 → 2250...), 50-Tick-Warmup, Radius-Ziel.
**Verteidiger wird beim Baustart sofort benachrichtigt** — das Spiel
kennt kein heimliches Anlegen dieser Waffe. Handbuch §9.3.

## Vision / Stimmung
**Katastrophal bedrohlich.** Ein Tesla-getriebener Hochspannungs-Turm
mit rotierenden Ringen und einem zentralen Energieball. Soll Panik
auslösen. Die Overload Matrix ist die **apokalyptische** Endgame-
Waffe — ihre Existenz allein ändert das strategische Klima der
Insel.

## Silhouette
**19-Hex-Fläche** (R=3). **Hoher Zentralturm** (~6 Units, höchstes
Gebäude im Spiel) mit:
- **Mehreren rotierenden Energie-Ringen** in verschiedenen Höhen
- **Tesla-Spulen** außen am Turm, zwischen denen Blitze springen
- **Zentralem Energie-Ball** (Kugel, schwebend, ca. 1.5 Units
  Durchmesser) nahe der Turmspitze
- **Abspann-Kabeln** zu vier Außen-Verankerungs-Pylonen im 90°-Winkel
- **Gravuren und Warnmarkierungen** überall am Sockel

Inselweit sichtbar, unverkennbar.

## Materialien & Farben
- **Turm:** Metall-dunkel mit Stein-dunkel Fundament
- **Ringe:** Metall mit glühenden Kanten
- **Tesla-Spulen:** Kupfer-getönt (dunkel)
- **Energie-Ball:** **War-Rot** (`#dc2626`) dominant mit violett-Kern
- **Blitze:** Shader-gerendert, **violett + War-Rot Mischung**
- **Warnmarkierungen:** gelb-schwarze Schraffur, riesig
- **Abspann-Kabel:** dicke schwarze Seile mit glühend-roten
  Isolator-Knoten
- **Akzente:** Heat-Orange an den Spulen-Basen

## Ausbaustufen

### Stage 1 — Tesla-Turm (2 Anchors)
Grundturm mit einem ersten Energie-Ring, vier kleinen Tesla-Spulen,
kleiner Energie-Ball. Bereits bedrohlich — die Insel weiß "hier wird
etwas Schlimmes gebaut".

### Stage 2 — Hochspannungs-Station (4 Anchors)
Turm wächst, zwei Energie-Ringe, acht Tesla-Spulen, zwei
Verankerungs-Pylonen, größerer Energie-Ball. Blitze zwischen den
Spulen permanent sichtbar.

### Stage 3 — Vollständige Matrix (6 Anchors)
Voller Turm mit drei Energie-Ringen, zwölf Tesla-Spulen rundum, vier
Verankerungs-Pylonen im Quadrat, **gigantischer Energie-Ball** mit
permanenten Blitzen nach außen, alle 6 Anchors als massive Hochspannungs-
Einlässe. **Apokalyptisch.**

## Pipe-Anchors
Anchors sind **massive Hochspannungs-Einlässe** am Sockel — ausgeführt
als **dicke Rohr-Bündel mit Keramik-Isolatoren** und sichtbar
glühenden Knoten. Deutlich größer und bedrohlicher als alle anderen
Anchors.

- Stage 1: `anchor_0`, `anchor_3`
- Stage 2: +`anchor_1`, `anchor_4`
- Stage 3: alle 6

## Schornsteine & Emissionen
- **Kein klassischer Schornstein**, aber **Ozon-Dampf** aus den Spulen-
  Basen (`emitter_haze` mit violett-getöntem Nebel).
- **Kontaminations-Beitrag: ja, deutlich.** Die Overload Matrix
  kontaminiert massiv (passend zur Lore als gefährliches Artefakt).
- **Emission-Glow:**
  - **Zentraler Energie-Ball pulsiert War-Rot intensiv** (Ambient,
    permanent, sichtbar von weit)
  - Tesla-Spulen haben Shader-Blitze zwischen sich (Noise-basiert,
    chaotisch)
  - Rotierende Ringe glühen an den Kanten Heat-Orange
  - Gravuren am Sockel pulsieren rot
  - Abspann-Kabel-Isolatoren glühen rot, bei Aufladung heller

## Animationen

### Ambient (läuft immer)
- **Energie-Ringe `anim_spin_y` mit Versatz** — unterster schneller,
  oberster langsamer (0.3, 0.4, 0.5 rad/s)
- **Tesla-Blitze** zwischen den Spulen (Shader-Noise) permanent
- Energie-Ball pulsiert War-Rot (Shader, 1.5s Zyklus)
- Ozon-Dampf aus Spulen-Basen
- Gravuren Shader-Puls

### State-gekoppelt
- **Warmup (50 Ticks) — dramatische progressive Animation:**
  - Ringe rotieren **progressiv schneller** (Shader-Uniform gekoppelt
    an Warmup-Progress)
  - Blitze werden **intensiver und länger**
  - Energie-Ball wächst sichtbar in Größe (procedural Scale-Animation)
  - Warnmarkierungen am Sockel pulsieren immer schneller
  - **Licht-Säule** steigt aus dem Ball nach oben (gegen Ende des
    Warmups)
- **Entladung (Schuss gegen Economy-Hex):**
  - **Gigantischer Energie-Entladungs-Strahl** aus dem Ball zum Ziel-
    Hex (sichtbar inselweit), violett + War-Rot
  - Alle Blitze synchron in Richtung Ziel
  - `emitter_sparks` Max, Partikel-Explosion
- **Abkühlung:** Energie-Ball schrumpft, Ringe verlangsamen, viele
  Sekunden Ozon-Dampf-Auswurf

## Condition-Varianten

### Condition 100
Alles pulsiert kontrolliert, Metall geputzt, Blitze in gleichmäßigem
Rhythmus.

### Condition 50
Ein Ring abgebrochen (auf dem Boden), mehrere Spulen beschädigt
(kein Blitz dort), Energie-Ball flackert, Abspann-Kabel gerissen.

### Condition ruin
**Dramatisch zerstört:**
- Energie-Ball **explodiert** (fehlt komplett, Krater oben am Turm)
- Turm in der Mitte zerrissen oder geknickt
- Verankerungs-Pylonen umgefallen
- Blitze **chaotisch zufällig** zucken noch (nicht kontrolliert)
- Boden um das Gebäude **verbrannt** mit War-Rot-Glut
- **Kontaminations-Nebel** überall

Die Ruin der Overload Matrix ist die **dramatischste Ruin aller
Gebäude** — bewusst als Warnung "was hier passiert ist, war schlimm".

## Condition × Stage Matrix
Turm-Höhe konstant ab Stage 3 (jede Stage davor weniger Höhe), Ringe
und Spulen wachsen mit Stufen. Ruin in allen Stufen dramatisch.

## Umgebungsinteraktion
- **Versengter Boden-Ring** um das Gebäude (Textur-Overlay auf
  angrenzenden Hexes) — die Hexes um die Matrix sind sichtbar
  geschädigt.
- **Kontaminations-Partikel** im ganzen Umkreis.
- **Warnung an Verteidiger** (Gameplay): Sobald Bau beginnt, wird
  der Ziel-Spieler benachrichtigt → das Gebäude ist das "laute"
  Gebäude schlechthin.
- Muss auf War-Seite-Terrain stehen.

## Gameplay-Hinweise
- **Tier:** 3 (War-Seite)
- **Radius:** 3 Hex (19-Hex-Footprint)
- **Build-Cost:** 100000
- **Kosten:** 1000 → 1500 → 2250 Energy/Tick (exponentiell, ~1.5×)
- **Warmup:** 50 Ticks
- **Ziel:** Radius auf Economy-Seite (einzige Waffe dafür!)
- **Besonderheit:** Verteidiger wird beim Baustart sofort informiert
- Handbuch-Referenz: §9.3 Overload Matrix
