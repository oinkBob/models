# Harbor

## Funktion & Rolle
Inter-Insel-Transport und Fracht-Umschlag. Ermöglicht Warenverkehr
zwischen Inseln. Handbuch §8.2.

## Vision / Stimmung
Majestätischer Seehafen — lebendig, weitläufig, industriell-maritim.
Kräne bewegen Fracht, Boote schaukeln im Wasser, Signal-Leuchten
warnen. Soll "hier geht es raus in die Welt" ausstrahlen.

## Silhouette
**19-Hex-Fläche** (R=3). Langer **Kai mit mehreren Landeplätzen**,
davor zwei bis drei **Kräne mit langen Schwenkarmen**, ein zentraler
**Leuchtturm am Ende des Kais**. Rund um den Landbereich Lagerhäuser
und Lade-Plattformen.

## Materialien & Farben
- **Kai-Fundament:** Stein-hell (`#808286`) mit Stein-dunkel-Absätzen
- **Lagerhäuser:** Holz (`#8B6914`) mit Metall-Verstärkungen
- **Kräne:** Metall, Harvester-Gelb Akzente
- **Leuchtturm:** Stein-hell Rundturm mit Shield-Blau Lampe
- **Boote (Deko):** Holz mit Stoff-Segeln in Grass-dunkel
- **Wasser am Kai:** Flow-Grün Schaum-Akzente
- **Fahnen:** Harvester-Gelb oder Spielerfarbe

## Ausbaustufen

### Stage 1 — Einfacher Anleger (2 Anchors)
Ein Holz-Kai mit einer kleinen Kran-Plattform, einem Lagerhaus und
einem kleinen Boot vertäut. Noch kein Leuchtturm.

### Stage 2 — Hafen mit Lagerhaus (4 Anchors)
Stein-Kai, zwei Kräne, zwei Lagerhäuser, ein kurzer Leuchtturm am
Kai-Ende, zwei Boote. Signal-Feuer an den Kanten.

### Stage 3 — Voller Hafen (6 Anchors)
Großzügiger Stein-Kai mit drei Kränen in Reihe, mehreren Lagerhäusern,
hohem Leuchtturm mit rotierender Lampe, drei Booten verschiedener
Größen. Laternen rund um den Kai, Fahnenmasten mit Fahnen.

## Pipe-Anchors
Anchors sind **Lade-Rampen** im Kai mit **Rohr-Flanschen für
Massenware** (Energie/Batterie/Item-Lieferung). Als große
Hafen-Poller-artige Strukturen ausgeführt, mit sichtbaren Ketten
und Kupplungen.

- Stage 1: `anchor_0`, `anchor_3` am Kai-Rand (y≈0.3)
- Stage 2: +`anchor_1`, `anchor_4`
- Stage 3: alle 6 rundum

## Schornsteine & Emissionen
- **Kein Schornstein** (Hafen selbst). Boote haben kleine Schornsteine
  mit dünnem dunkelgrauem Rauch (Deko, `emitter_smoke` sehr reduziert).
- **Keine Kontaminations-Emission.**
- **Emission-Glow:**
  - Leuchtturm-Lampe pulsiert Shield-Blau (Ambient, 3s Zyklus)
  - Kran-Signallichter (Warnung-Rot) blinken an den Spitzen
  - Laternen am Kai leuchten warmweiß bei Nacht

## Animationen

### Ambient (läuft immer)
- `anim_spin_y` am Leuchtturm-Reflektor (Stage 2+3), 0.5 rad/s
- Kran-Schwenkarme `anim_spin_y` sehr langsam (0.1 rad/s, simuliert
  Patrouille)
- Boote schaukeln minimal (Shader-Vertex, Wellen-animiert)
- Fahnen Shader-Wind
- Wasser-Schaum am Kai-Rand (Shader-Vertex Wellen)

### State-gekoppelt
- **Bei aktivem Transport:** Kran hebt sichtbar Fracht (procedural-
  Animation `anim_crane_up`), Boot bewegt sich zum Kai, Lagerhaus-
  Tore öffnen, `emitter_sparks` an den Kran-Motoren
- **Bei Wartung/Ankunft:** Leuchtturm-Puls schneller, Signal-Feuer
  intensiver

## Condition-Varianten

### Condition 100
Holz frisch lackiert, Metall geputzt, Fahnen hell, Boote intakt.

### Condition 50
Kai-Stein teilweise gerissen, ein Kran-Arm schief, ein Lagerhaus-Dach
teilweise fehlend, ein Boot hängt schief im Wasser.

### Condition ruin
Kai eingestürzt mit Lücken im Stein, alle Kräne am Boden, Leuchtturm
abgebrochen, Boote versunken (nur Mast ragt aus dem Wasser), Lagerhäuser
kollabiert. Dramatisch.

## Condition × Stage Matrix
Kai-Fundament bleibt konstant in der Position, Ausstattung (Kräne,
Gebäude, Leuchtturm, Boote) wächst mit Stufen. Ruin zeigt immer
versunkene Boote — charakteristisch.

## Umgebungsinteraktion
- **Harbor muss am Wasser stehen** — Modelliere so, dass ein großer
  Teil des Kais ins Wasser ragt. Minimum 2-3 Wasser-Hexes angrenzend.
- Wasser-Schaum-Effekte am Kai und um Boote.
- Kleine Fische-Sprung-Partikel gelegentlich (Deko-Detail).
- Bei Kontamination: Wasser um den Hafen trübt sich grünlich.

## Gameplay-Hinweise
- **Tier:** 3
- **Radius:** 3 Hex (19-Hex-Footprint)
- **Build-Cost:** 10000
- **Upkeep:** 30/Tick
- **Rolle:** Inter-Insel-Fracht und Transport
- Handbuch-Referenz: §8.2 Harbor
