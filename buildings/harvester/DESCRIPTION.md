# Harvester

## Funktion & Rolle
Extrahiert Roh-Energie aus dem Boden des eigenen Hex. Das erste und
günstigste Gebäude im Spiel — jeder Spieler platziert 2–3 Harvester in
der ersten Stunde. Handbuch §8.1.

## Vision / Stimmung
Ein freundlich-pragmatisches Nutzgebäude, wie eine kleine Erdöl-Pumpe
oder ein Brunnen mit gelber Kappe. Soll warm und vertraut wirken,
nicht bedrohlich — der "Hausbrunnen" der Molanex-Welt. Sichtbar in
Bewegung, macht klar: hier wird gearbeitet.

## Silhouette
Runder Sockel auf Hex-Boden, zentral ein **schmaler Turm mit
Rotorkopf** — wie ein kleiner Pumpenkran. Rotorkopf neigt sich
leicht zum Spieler hin (charakteristische Silhouette). Auf Distanz
erkennbar durch das gelbe Kopfelement und den drehenden Rotor.

Proportionen (Stage 1): ca. 0.6 Units Durchmesser Basis, 0.8 Units
hoch bis Rotor-Spitze. Passt entspannt in einen 1-Hex-Kreis (Radius 1.0).

## Materialien & Farben
- **Basis:** Holz (`#8B6914`) oder Stein-hell (`#808286`) für das
  Fundament
- **Turm:** Metall, gräulich mit sichtbaren Verstrebungen
- **Rotorkopf:** Harvester-Gelb (`#f59e0b`) — das Erkennungsmerkmal
- **Akzente:** Heat-Orange (`#f97316`) an heißen Teilen (Lager,
  Auslassrohr)
- **Emission:** dezent am Auslass (heat-orange), pulst bei Produktion

## Ausbaustufen

### Stage 1 — Funktional (2 Anchors)
Einfacher Rundsockel aus Holz, zentraler schmaler Turm, einzelner
Rotorkopf oben. Zwei seitliche Auslassrohre links/rechts (Ost/West)
mit Flanschen. Minimalistisch, wie ein Prototyp.

### Stage 2 — Ausgebaut (4 Anchors)
Sockel wird massiver (Stein-Fundament unter dem Holz), zweiter Turm-
Teil schraubt sich höher, zusätzliche Kühlrippen am Turm. Zwei weitere
Auslassrohre (Nord-Ost, Süd-West). Kleiner Balkon/Steg um den Turm.
Wirkt wie ein "seriös betriebener" Harvester.

### Stage 3 — Voll ausgebaut (6 Anchors)
Markant vergrößerte Basis mit Stein-Säulen, voluminöser Doppel-Rotor
(zwei gelbe Köpfe gegeneinander-rotierend), 6 Auslassrohre rundum
angeordnet wie eine Blume. Dach über der Basis schützt die Mechanik.
Ein paar Kabel-Bündel laufen an der Außenseite. Imposant aber weiter
eindeutig als "Harvester" erkennbar.

## Pipe-Anchors
Alle Anchors als deutliche **Flansch-Ringe** mit Bolzen am Ende eines
kurzen Rohrstummels (sieht aus wie ein Kupplungs-Anschluss).

- **Stage 1:** `anchor_0` (Ost-Rohr), `anchor_3` (West-Rohr) — auf
  Höhe 0.3 Units über Boden, horizontal nach außen zeigend
- **Stage 2:** zusätzlich `anchor_1` (Nord-Ost), `anchor_4` (Süd-West)
- **Stage 3:** zusätzlich `anchor_2` (Nord-West), `anchor_5` (Süd-Ost)

## Schornsteine & Emissionen
- **Kein Schornstein** — Harvester produziert keine Luftverschmutzung.
- **Keine Kontaminations-Emission** (das übernimmt Battery Factory o.ä.)
- **Emission-Glow:** `emitter_sparks` am Rotor-Lager (dezente heat-
  orange Funken bei Produktion), Emission-Map am Auslassrohr pulst
  heat-orange synchron zur Rotor-Umdrehung
- Optional: `emitter_flow` am aktiven Auslass-Anchor (flow-grün wenn
  Pipe angeschlossen und Flow aktiv)

## Animationen

### Ambient (läuft immer)
- `anim_spin_y` — Rotorkopf dreht permanent um Y-Achse, ~0.8 rad/s
  (Stage 1), ~0.5 rad/s (Stage 2, größerer Rotor), Doppel-Rotor
  gegeneinander in Stage 3
- `anim_bob_y` — kleines Gegengewicht am Rotorarm oszilliert leicht
  auf/ab (Stage 2+3)

### State-gekoppelt
- **Bei Produktion aktiv:** `emitter_sparks` spawnt Funken am Lager,
  Emission-Map am Auslassrohr pulst, Rotor-Geschwindigkeit +20%
- **Bei ausgeschaltet / No-Resource:** Rotor dreht langsam idle
  (~0.1 rad/s), keine Sparks, Emission aus
- **Bei Kontamination (auf dem Hex):** Rotor dreht stotternd, optional
  dünner giftgrüner Dunst auf der Basis

## Condition-Varianten

### Condition 100
Frisches Gelb am Rotor, Holz frisch, keine Rostflecken. Kleine
Molanex-Flagge am Turm (winkt per Shader-Wind).

### Condition 50
Rotor-Gelb verblichen, einzelne Bolzen fehlen, Rostspuren am Metall,
Holzbasis zeigt Risse, ein Auslassrohr sichtbar verbogen. Flagge
zerfetzt.

### Condition ruin
Rotorkopf abgefallen (liegt schräg am Turm), Holzbasis eingesackt,
zwei Auslassrohre gebrochen, Gras wächst durch den Sockel. Kein
Glow, kein Rotor-Dreh. Small bush aus dem Fundament heraus.

## Condition × Stage Matrix
Die **Basis-Silhouette pro Stufe** bleibt über Condition konstant
(gleicher Sockel-Durchmesser, gleiche Turm-Höhe). Nur Textur-Overlay
(Rost/Risse) und fehlende/verbogene Kleinteile unterscheiden die
Conditions. Ruin bricht die Silhouette deutlich (Rotor liegt seitlich).

→ Artist-Tipp: Gemeinsame Basis-Mesh pro Stufe bauen, dann drei
Condition-Versionen mit Overlay-Textur + gezielten Mesh-Modifikationen
für ruin.

## Umgebungsinteraktion
- Steht auf einem dezenten Stein-Plattenring, der 0.05 Units in den
  Boden geht (kein freier Rand zwischen Modell und Hex).
- Keine Terrain-Präferenz visuell — Harvester passt überall.
- Gameplay: Produktion = `EnergyYield` × Terrain-Multi (Grass 1.0×,
  Forest 1.5×, Mountain 3.0×, Swamp 0.8×). Terrain-abhängige
  Akzent-Pflanzen am Sockel wären nice-to-have aber nicht nötig.

## Gameplay-Hinweise
- **Tier:** 1
- **Radius:** 1 Hex
- **Build-Cost:** 200 (test value)
- **Upkeep:** 2 Energy/Tick
- **Output:** `EnergyYield` des Hex × Terrain-Multi pro Tick
- Handbuch-Referenz: §8.1 Harvester
