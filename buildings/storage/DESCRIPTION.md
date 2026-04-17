# Storage

## Funktion & Rolle
Lager für Batterien und Items mit gestuften Slots. Eines der am
häufigsten gebauten Gebäude — jeder Spieler hat mehrere. Handbuch §8.1.

## Vision / Stimmung
Ein verlässlicher Lager-Bunker — pragmatisch, robust, fast bäuerlich.
Wirkt wie eine Mischung aus Scheune und kleinem Tresor. Soll dem
Spieler das Gefühl von "sicher verstaut" geben.

## Silhouette
Quaderförmiger Bau mit leicht abfallendem Satteldach. An den Seiten
sichtbare **Lade-Luken** mit Scharnieren und schweren Griffen. Ein
kleiner Lüftungsschacht auf dem Dach (kein Rauch-Emitter!).
Auf Distanz klar als "Kiste mit Tür" erkennbar.

Proportionen Stage 1: ca. 0.7 × 0.7 Units Grundfläche, 0.6 hoch.

## Materialien & Farben
- **Basis:** Stein-hell (`#808286`) Fundament, Holz-Balken darüber
- **Dach:** Grass-dunkel (`#4a8a28`) Schindeln (warmer Kontrast)
- **Luken:** Metall, Harvester-Gelb (`#f59e0b`) Schloss-Beschläge
- **Akzente:** Holz-dunkel (`#5c4710`) Eck-Balken
- **Emission:** warmweißer Schein durch Lüftungsfugen nachts

## Ausbaustufen

### Stage 1 — Einfache Kiste (2 Anchors)
Einzelner Quader mit Satteldach und zwei Luken (Ost/West). Wirkt wie
ein verstärktes Schuppen-Modul. Funktional, nicht mehr.

### Stage 2 — Doppelscheune (4 Anchors)
Zweiter Abschnitt hinten drangebaut, Dach durchgehend. Vier Luken
verteilt, kleine Laufplattform an der Südseite. Flaggenmast mit
kleinem Wimpel.

### Stage 3 — Mehrstöckiger Lagerbunker (6 Anchors)
Zweites Stockwerk mit umlaufendem Holz-Laufsteg, Dachgauben, sechs
Luken rundum. Stein-Sockel massiver. Auf dem Dach ein kleiner
Aussichts-Erker. Wirkt wie ein kleiner Kornspeicher-Turm.

## Pipe-Anchors
Jeder Anchor ist eine **verstärkte Lade-Luke** mit Rahmen und
Metall-Einfassung (kein Rohr-Flansch — Items/Batterien werden
transportiert, daher Förderschacht-Look). Tabelle §7.2.

- Stage 1: `anchor_0`, `anchor_3` auf mittlerer Wandhöhe (y≈0.3)
- Stage 2: +`anchor_1`, `anchor_4`
- Stage 3: alle 6, gleichmäßig verteilt

## Schornsteine & Emissionen
- **Kein Schornstein** (nur Lüftungsschacht, rein visuell).
- **Keine Kontaminations-Emission.**
- **Emission-Glow:** Kleine Fenster + Lüftungsfugen leuchten warmweiß
  (bei `u_daylight < 0.6`). Harvester-Gelb Akzent-LEDs an den
  Schlössern pulsen sehr langsam.

## Animationen

### Ambient (läuft immer)
- Flaggenmast-Wimpel (Stage 2+3): Shader-Wind
- Leichtes Schaukeln der Luken-Scharniere (Stage 3): Shader-Vertex
  minimal

### State-gekoppelt
- **Beim Einlagern/Entnehmen:** Eine der Luken öffnet sich kurz
  (procedural, `anim_door_{n}` auf Y-Scharnier), kleiner Heat-Orange-
  Blitz am Luken-Inneren.
- **Bei Überfüllung:** Luken-LEDs wechseln zu Warnung (`#f87171`).

## Condition-Varianten

### Condition 100
Frisches Holz, Metall geputzt, Dach-Schindeln alle vorhanden.

### Condition 50
Holz vergraut, zwei Schindeln fehlen, ein Luken-Griff abgebrochen,
Rost am Stein-Sockel.

### Condition ruin
Dach teilweise eingestürzt, Luken hängen schief, eine Wand ist
eingesunken. Efeu klettert über den Sockel.

## Condition × Stage Matrix
Grundquader + Sockel sind Shared-Basis über Stufen — nur Anbauten
(Stockwerk, Laufstege) ändern sich pro Stufe. Condition-Degradation
trifft vor allem das Dach und die Luken.

→ Artist-Tipp: Einen Quader-Kernmesh bauen und pro Stufe modular
erweitern.

## Umgebungsinteraktion
- Steht auf einem dezenten Stein-Fundament, 0.05 Units im Hex-Boden
  versenkt.
- Stage 2+3: kleine Holzkisten und Lieferpaletten um den Sockel.
- Keine Terrain-Präferenz.

## Gameplay-Hinweise
- **Tier:** 1
- **Radius:** 1 Hex
- **Build-Cost:** 500 (test value)
- **Rolle:** Batterie- und Item-Speicher mit Tier-Slots
- Handbuch-Referenz: §8.1 Storage
