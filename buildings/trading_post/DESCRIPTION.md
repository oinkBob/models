# Trading Post

## Funktion & Rolle
Lokaler Handelsknoten. Erhöht die Sichtweite um 5 Hex — dient damit
auch als ziviler Aussichtspunkt. Handbuch §8.1.

## Vision / Stimmung
Einladend, lebendig, warm. Ein Marktplatz in Miniatur: Fahnen im
Wind, Baldachin, Laternen. Soll Spieler optisch anziehen und klar
als Handels-Knotenpunkt lesbar sein.

## Silhouette
Offener Pavillon unter einem **großen Stoff-Baldachin**, daneben ein
schlanker **Aussichtsturm mit Fahne**. Der Baldachin sitzt auf vier
Holzpfeilern. Der Turm überragt den Baldachin deutlich — auf mehrere
Hex erkennbar.

## Materialien & Farben
- **Baldachin:** Stoff in Grass-dunkel (`#4a8a28`) + Sand (`#d4bc7a`)
  Streifen (Markt-Farben)
- **Holzpfeiler + Turm:** Holz (`#8B6914`)
- **Fahne:** Harvester-Gelb (`#f59e0b`)
- **Metall-Beschläge:** Stein-hell
- **Laternen:** Flow-grün (`#4ade80`) emissive bei Nacht
- **Bodenplatten:** Stein-hell

## Ausbaustufen

### Stage 1 — Marktstand (2 Anchors)
Vier Pfeiler, einfacher Baldachin, ein Verkaufsstand, eine kleine Flagge.
Wirkt wie ein Wochenmarkt-Stand.

### Stage 2 — Handelspavillon (4 Anchors)
Baldachin größer, zweistöckiger Holzbau an der Nordseite (eigentlicher
Verkaufsraum), hölzerner Aussichtsturm mit Plattform und Flagge. Bänke
um den Baldachin.

### Stage 3 — Markthalle mit Turm (6 Anchors)
Voller Holz-Pavillon mit Stein-Sockel, mehreren Fahnen, hohem
Aussichtsturm mit umlaufender Balkon-Galerie und einer Glocke auf der
Spitze. An allen 6 Seiten kleine Liefer-Anschlüsse (Anchors).

## Pipe-Anchors
Anchors sind **Liefer-Schächte** im Stein-Sockel — als **Holztor mit
Ladeluke** ausgeführt. Daneben ein kleiner "Handels-Tresen" mit
Gewichts-Anzeige.

- Stage 1: `anchor_0`, `anchor_3` auf y≈0.25 (bodennah)
- Stage 2: +`anchor_1`, `anchor_4`
- Stage 3: alle 6

## Schornsteine & Emissionen
- **Kein Schornstein** — Trading Post produziert nichts.
- **Keine Kontaminations-Emission.**
- **Emission-Glow:** Laternen rund um den Baldachin leuchten Flow-Grün
  warm bei Nacht. Fahnenspitze (Stage 3) mit kleinem Leucht-Stern.
- Bei aktivem Handel: Laternen pulsieren freundlich.

## Animationen

### Ambient (läuft immer)
- Baldachin und Fahnen wehen im Wind (Shader §8.2 mit `wind_mask`)
- Glocke auf Stage 3 schwingt sanft (anim_bob_y minimal)
- Laternen flackern mit subtiler Shader-Animation

### State-gekoppelt
- **Bei aktivem Trade:** Laternen pulsieren stärker, kleiner
  `emitter_sparks` mit Harvester-Gelb am Handels-Tresen
- **Bei Gildenzugehörigkeit:** Gildenfarbe als sekundärer Wimpel am
  Turm (Runtime-Tint)

## Condition-Varianten

### Condition 100
Stoff frisch gefärbt, Holz poliert, Fahne leuchtend.

### Condition 50
Stoff verblasst und geflickt, ein Pfeiler wackelt (visuell leicht
schief), Fahne zerfranst, Laterne kaputt.

### Condition ruin
Baldachin zerfetzt, hängt teilweise herunter. Turm schief und ohne
Flagge, Verkaufsstand umgeworfen. Efeu an Pfeilern.

## Condition × Stage Matrix
Grundsockel + Pfeiler-Anordnung bleiben über Stufen konstant — der
Baldachin und der Turm wachsen. Ruin zieht den Baldachin zerrissen
zu Boden; Silhouette bricht deutlich.

## Umgebungsinteraktion
- Stein-Bodenplatten strahlen ein paar Hex-Meter aus (aber innerhalb
  des Hex).
- Stage 2+3: kleine Deko-Kisten, Fässer, Warenballen am Sockel.
- Bevorzugt Gras-Terrain (Stimmung passt), keine harte Anforderung.

## Gameplay-Hinweise
- **Tier:** 1
- **Radius:** 1 Hex
- **Build-Cost:** 800
- **Effekt:** +5 Hex Sichtweite, lokaler Handel
- Handbuch-Referenz: §8.1 Trading Post
