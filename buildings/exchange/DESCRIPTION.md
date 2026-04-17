# Exchange

## Funktion & Rolle
Staats-Börse. 3 pro Insel (platziert bei Insel-Generierung im 120°-
Raster), **unzerstörbar**, 3% Handels-Gebühr als Energie-Senke.
Handbuch §8.2.

## Vision / Stimmung
Monumentaler Tempel. Würdevoll, zeitlos, autoritär — deutlich
abgehoben vom Rest der Spieler-Architektur. Die Exchange ist nicht
"gehört jemandem", sie **ist**. Gold-Akzente, Marmor-Anmutung, keine
Degradation.

## Silhouette
**19-Hex-Fläche** (R=3). **Großer Säulengebäude-Tempel** mit
zentraler Kuppel und breiter Treppe davor. Acht Säulen im vorderen
Portikus. Die zentrale Kuppel ist **goldgeschmiedet** und weithin
sichtbar.

## Materialien & Farben
- **Fundament + Säulen:** Stein-hell (`#808286`, fast Marmor-weiß)
- **Kapitell + Zierbänder:** Harvester-Gelb (`#f59e0b`, gold-Anmutung)
- **Kuppel:** Harvester-Gelb dominant, goldene Schuppen
- **Dach-Schindeln:** Stein-dunkel
- **Ewiges Feuer im Zentrum:** Flow-Grün + Harvester-Gelb Mischung
- **Fahnen:** neutral-weiß mit gold-Rand (keine Spielerfarbe)

## Ausbaustufen

### Sonderregel: Keine Ausbaustufen, keine Condition-Degradation

Die Exchange ist unzerstörbar und wird in **Stage 3 mit Condition 100**
platziert — und **bleibt so**. Der Spieler kann sie nicht aufrüsten
oder beschädigen. Daher:
- Keine S1/S2-Varianten nötig
- Keine Condition-50/ruin-Varianten
- **Nur eine Variante: `exchange_s3_100.glb`** (plus LOD1)

Trotzdem hat sie alle 6 Pipe-Anchors, damit Spieler sie an beliebiger
Kante anschließen können.

## Pipe-Anchors
**Alle 6 Anchors vorhanden.** Ausgeführt als **gold-gerahmte
Anschluss-Nischen** im Fundament, mit Säulenportalen umrahmt — jede
Nische wirkt wie ein kleiner Altar. Die Anchors selbst liegen in den
sechs Haupt-Kompass-Richtungen.

Alle anchor_0..5 auf y≈0.4 (eine Stufe über dem Boden).

## Schornsteine & Emissionen
- **Kein Schornstein.**
- **Keine Kontaminations-Emission.**
- **Emission-Glow:**
  - **Zentrales "ewiges Feuer"** unter der Kuppel pulst permanent
    in Harvester-Gelb (durch einen zentralen Oberlicht-Schacht
    sichtbar)
  - Säulenkapitelle haben goldene Emission, leuchten bei Nacht
  - Ziergravuren an den Wänden (Shield-Blau, dezent)

## Animationen

### Ambient (läuft immer)
- Fahnen auf Ecktürmchen wehen im Wind (Shader)
- Ewiges Feuer flackert (Shader-Noise, Heat-Orange + Flow-Grün)
- Kuppel-Glanz-Hotspot bewegt sich langsam (Shader-Fake-Spekular)

### State-gekoppelt
- **Bei Handels-Transaktion:** Partikel-Burst (`emitter_sparks` gold)
  aus der Kuppel-Oberlicht, kurzer Anstieg des ewigen Feuers
- **Bei hoher Handels-Aktivität:** Kuppel-Glow intensiver, goldene
  Aschefunken rund um den Tempel

## Condition-Varianten
**Entfällt.** Exchange ist unzerstörbar. Nur Condition 100.

## Condition × Stage Matrix
**Entfällt** — nur eine einzige Variante.

## Umgebungsinteraktion
- Exchange steht auf einem **erhöhten Stein-Plateau** mit umlaufender
  Treppe (sichtbar 0.3 Units über Bodenniveau erhöht).
- Deko: goldene Münzen verstreut am Fuß der Säulen, Kristall-Obelisken
  an den Ecken des Plateaus.
- Die Exchange wird bei Inselgenerierung automatisch auf Gras-Terrain
  platziert (120° verteilt auf Radius ~20 Hex vom Zentrum).
- Kontamination um die Exchange hat **keinen visuellen Effekt** auf
  das Gebäude (unzerstörbar).

## Gameplay-Hinweise
- **Tier:** 3 (Sondergebäude)
- **Radius:** 3 Hex (19-Hex-Footprint)
- **Build-Cost:** — (automatisch bei Inselstart platziert)
- **Upkeep:** — (keine)
- **Anzahl:** genau 3 pro Insel, in 120°-Raster
- **Sonderregel:** Unzerstörbar, 3% Gebühr als Energie-Senke
- Handbuch-Referenz: §8.2 Exchange
