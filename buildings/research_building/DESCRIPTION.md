# Research Building

## Funktion & Rolle
Schaltet Tier-2- und Tier-3-Gebäude frei. Zentrum der Progression
für den Spieler. Handbuch §8.2.

## Vision / Stimmung
Labor und Akademie zugleich, wissenschaftlich-mystisch. Experimente
blitzen in Kuppeln, Bücher und Diagramme überall sichtbar. Soll
"hier wird Zukunft gemacht" ausstrahlen. Heller als Analysis Center,
aber ebenfalls blau-kühl dominiert.

## Silhouette
**7-Hex-Fläche** (R=2). Mehrstöckige Halle mit **zentraler Glaskuppel**,
darauf ein **hoher Schornstein mit Energieblitzen**, umgeben von
mehreren kleineren Kuppeln und einer umlaufenden Balkon-Galerie.
Erkennbar am Blitz-Emission-Strich über der Kuppel.

## Materialien & Farben
- **Basis:** Stein-hell (`#808286`) massiver Sockel
- **Wände:** Stein-hell + Holz-Balken (Fachwerk-Akzent)
- **Kuppel:** Glas mit Shield-Blau Tönung + Kupfer-Rahmen (`#b86a1c`)
- **Schornstein:** Stein-hell mit Metall-Ringen
- **Akzente:** Heat-Orange (`#f97316`) an Lab-Elementen, Flow-Grün an
  aktiven Experimenten
- **Energieblitze:** Shield-Blau emissive + Warnung-Rot Mischung

## Ausbaustufen

### Stage 1 — Kleines Labor (2 Anchors)
Einfacher zweistöckiger Bau mit einer kleinen Kuppel und einem kurzen
Schornstein. Ein sichtbares Lab-Fenster mit Experiment-Glow.

### Stage 2 — Forschungs-Observatorium (4 Anchors)
Vollständige zentrale Kuppel, zwei kleinere Kuppeln seitlich, höherer
Schornstein mit ersten sichtbaren Energieblitzen, Balkon-Galerie
zwischen erstem und zweitem Stock.

### Stage 3 — Akademie (6 Anchors)
Dreistöckig, große Kuppel dominant, vier kleinere Kuppeln an den
Ecken, massiver Schornstein mit permanenten Energieblitzen,
sternförmige Balkon-Galerien, sichtbare Teleskope/Instrumente auf
dem Dach.

## Pipe-Anchors
Anchors sind **Labor-Einlässe** — Flansche mit einem **Mini-Fenster**
daneben, durch das kleine funkelnde Kristalle sichtbar sind.

- Stage 1: `anchor_0`, `anchor_3` (y≈0.4)
- Stage 2: +`anchor_1`, `anchor_4`
- Stage 3: alle 6

## Schornsteine & Emissionen
- **1 kleiner Schornstein** (alle Stufen, wächst mit Stufen). Leichter
  weißer Dampf, kein Rauch.
- **Keine Kontaminations-Emission** (saubere Forschung).
- **Emission-Glow:**
  - Zentrale Kuppel pulsiert Shield-Blau wenn Experimente laufen
  - Energieblitze am Schornstein permanent (Shader-Noise-Animation)
  - Fenster leuchten kühlweiß bei Nacht
  - Aktive Experiment-Glows in Heat-Orange oder Flow-Grün (zufällig
    pro Fenster)

## Animationen

### Ambient (läuft immer)
- Energieblitze am Schornstein pulsieren chaotisch (Shader, Noise-
  basiert)
- `anim_spin_y` auf einem Teleskop-Dach-Instrument (Stage 3)
- Fenster-Glows flackern mit Shader-Noise (simuliert Laborarbeit)

### State-gekoppelt
- **Bei aktiver Forschung (Unlock läuft):** Blitze intensiver und
  gerichtet (rhythmisch), zentrale Kuppel pulsiert kräftiger,
  `emitter_sparks` Shield-Blau am Schornstein-Fuß
- **Bei Freischaltung (Research completed):** großer Licht-Flash —
  die ganze Kuppel glüht kurz hell auf und strahlt Partikel nach oben
  (feierlicher Moment)

## Condition-Varianten

### Condition 100
Glas klar, Kupfer frisch, Blitze kontrolliert.

### Condition 50
Kuppel-Glas mit Sprüngen, Kupfer patiniert, einzelne Blitze
unkontrolliert, eine kleine Nebenkuppel fehlt.

### Condition ruin
Zentrale Kuppel eingestürzt (Glas auf dem Boden), Schornstein geknickt,
keine Blitze, verkohlte Stellen an den Wänden. Wirkt verlassen und
möglicherweise gefährlich.

## Condition × Stage Matrix
Sockel und erstes Stockwerk konstant, Kuppel und Obergeschosse wachsen
mit Stufen. Ruin löst die Kuppel visuell auf.

## Umgebungsinteraktion
- Großzügige Stein-Bodenplatten vor dem Eingang.
- Stage 3: kleine Deko-Bücher-Stapel, Kristallformationen, Diagramme
  an der Basis.
- Bevorzugt Gras-Terrain (Stimmung), keine harte Anforderung.

## Gameplay-Hinweise
- **Tier:** 2
- **Radius:** 2 Hex (7-Hex-Footprint)
- **Build-Cost:** 6000
- **Upkeep:** 30/Tick
- **Rolle:** Unlock-Punkt für Tier 2 und Tier 3 Gebäude
- Handbuch-Referenz: §8.2 Research Building
