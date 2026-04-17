# Analysis Center

## Funktion & Rolle
Bereitet Markt- und Produktionsdaten visuell auf. Zeigt Charts und
Prognosen — wichtige Infrastruktur für strategische Spieler. Handbuch §8.1.

## Vision / Stimmung
Ein kleines Observatorium / Rechenzentrum. Konzentriert, wissenschaftlich,
ruhig-leuchtend. Soll "hier wird gemessen und gedacht" ausstrahlen.
Blauer Grundton hebt es von den warmen Economy-Farben ab.

## Silhouette
Kubisches Gebäude mit **gewölbtem Kuppel-Dach** (Observatoriums-Look).
Auf dem Dach zwei bis drei **schlanke Antennen**, eine davon mit
Parabolantennen-Schüssel. Kleine Fenster mit blaugrünlichen Panelen in
regelmäßigem Raster.

## Materialien & Farben
- **Basis:** Stein-hell (`#808286`)
- **Kuppel:** Metall, mittel-grau
- **Fenster-Panele:** Shield-Blau (`#38bdf8`) — getönte Glas-Anmutung
- **Antennen:** Metall-dunkel
- **Akzente:** Flow-Grün LED-Streifen am Fuß der Antennen
- **Bodenplatten:** Stein-dunkel

## Ausbaustufen

### Stage 1 — Labor-Modul (2 Anchors)
Einfacher Kubus mit flacher Kuppel und einer Antenne. Zwei Fenster-
Reihen. Wirkt wie ein kleines Funkhaus.

### Stage 2 — Observatorium (4 Anchors)
Gebäude größer, vollständige Halbkuppel, zwei Antennen mit einer
Schüssel, mehr Fenster-Reihen. Kleine Aussichts-Galerie auf der Kuppel.

### Stage 3 — Forschungs-Station (6 Anchors)
Dreistöckig, zwei Halbkuppeln nebeneinander, drei Antennen (eine
rotierend, zwei statisch), großer Aussichts-Balkon, sichtbare
Parabolantenne auf Stativ.

## Pipe-Anchors
Anchors sind **Datenschacht-Einlässe** — Flansche mit einer **kleinen
Display-Anzeige** daneben (Mini-Bildschirm shield-blau emissive).

- Stage 1: `anchor_0`, `anchor_3` (y≈0.3)
- Stage 2: +`anchor_1`, `anchor_4`
- Stage 3: alle 6

## Schornsteine & Emissionen
- **Kein Schornstein.**
- **Keine Kontaminations-Emission.**
- **Emission-Glow:**
  - Alle Fenster leuchten Shield-Blau (Ambient, auch tags leicht)
  - Nachts deutlich stärker
  - Antennenspitzen haben kleine blinkende rote Warn-LEDs
  - Stage 3: Rotierende Parabol hat Emission-Strich am Rand

## Animationen

### Ambient (läuft immer)
- `anim_spin_y` auf einer Antenne/Schüssel (langsam, 0.25 rad/s)
- Fenster-Panele flackern dezent (Shader, simuliert Bildschirme)
- Antennen-Warn-LEDs blinken langsam (1s Zyklus)

### State-gekoppelt
- **Bei aktiver Datenverarbeitung:** Fenster-Flackern intensiver, kleine
  `emitter_sparks` an Antennen-Basen (Datenpuls-Visualisierung),
  Parabolantenne dreht schneller
- **Bei Markt-Warnung:** ein Fenster pulst Warnung-Rot

## Condition-Varianten

### Condition 100
Glas klar, Kuppel glänzt, Antennen aufrecht.

### Condition 50
Ein Fenster eingeschlagen, eine Antenne schief, Kuppel-Metall patiniert.

### Condition ruin
Kuppel eingestürzt, alle Antennen am Boden, Fenster zersplittert, kein
Licht.

## Condition × Stage Matrix
Basis + untere Wände konstant, Kuppel und Antennen wachsen. Ruin
zerbricht Kuppel in jeder Stufe anders (Trümmerfeld).

## Umgebungsinteraktion
- Dezente Bodenplatten, wie ein kleiner Platz davor.
- Stage 3: kleine Wetterinstrumente (Anemometer, Thermometer) am Rand
  der Basis als Deko.
- Bevorzugt erhöhte Standorte, aber keine harte Terrain-Anforderung.

## Gameplay-Hinweise
- **Tier:** 1
- **Radius:** 1 Hex
- **Build-Cost:** 1500
- **Effekt:** Visualisiert Markt- und Produktions-Daten für den Besitzer
- Handbuch-Referenz: §8.1 Analysis Center
