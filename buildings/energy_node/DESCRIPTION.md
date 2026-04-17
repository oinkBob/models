# Energy Node

## Funktion & Rolle
Verteiler-Knoten für War-Seite-Energie. Wie ein Distributor, aber
kompakter und nur für Kampf-Zwecke. Handbuch §9.1.

## Vision / Stimmung
Kompakter Kristall-Knoten. Fokussiert, gefährlich-schön. Dient als
Energie-Verteiler für Waffen und Schilde, daher das Herzstück eines
War-Hex-Netzes. Rote und violette Pulse betonen die kriegerische
Natur.

## Silhouette
Runder, leicht erhöhter Sockel mit einem **Kristall-Cluster** in der
Mitte. Mehrere geometrische Kristall-Säulen wachsen nach oben, leicht
geneigt, wie eine unnatürliche Formation. Kleiner, kompakter Bau
(anders als Economy-Distributor).

## Materialien & Farben
- **Sockel:** Stein-dunkel (`#5a5c5e`) mit dunkel-metallischen Strebern
- **Kristalle:** durchscheinendes violett-War-Rot (Mischung aus
  `#dc2626` und einem violetten Ton)
- **Ränder/Beschläge:** Metall-dunkel
- **Kern in der Mitte:** War-Rot emissive, pulsiert
- **Warnmarkierungen** am Sockel: gelb-schwarze Schraffur

## Ausbaustufen

### Stage 1 — Einzel-Kristall (2 Anchors)
Ein einzelner Kristall in der Mitte des Sockels, leicht nach oben
zeigend.

### Stage 2 — Drei-Kristall-Formation (4 Anchors)
Drei Kristalle in Dreiecksanordnung, ein zentraler Kern-Kristall
in der Mitte.

### Stage 3 — Sechs-Kristall-Ring (6 Anchors)
Sechs Kristalle im Ring angeordnet, alle geneigt zum Zentrum, dort ein
großer **Zentral-Kristall** nach oben ragend. Wirkt wie eine dunkle
Kristall-Kathedrale.

## Pipe-Anchors
Anchors sind **War-Energie-Flansche** mit **roten LED-Ringen**,
vergleichbar zu Control Projector aber kleiner.

- Stage 1: `anchor_0`, `anchor_3`
- Stage 2: +`anchor_1`, `anchor_4`
- Stage 3: alle 6

## Schornsteine & Emissionen
- **Kein Schornstein.**
- **Keine Kontaminations-Emission.**
- **Emission-Glow:**
  - Alle Kristalle pulsieren War-Rot (Ambient, Shader, 2s Zyklus)
  - Zentral-Kristall pulsiert stärker
  - Bei Nacht extrem auffällig (War-Side-Landmark)

## Animationen

### Ambient (läuft immer)
- Kristall-Puls (Shader, Emission-Map mit Zeit-Uniform)
- Bei Stage 3: leichtes Shader-Flimmern zwischen den Ring-Kristallen
  (simuliert Energie-Verbindung)

### State-gekoppelt
- **Bei aktivem Flow:** Pulse schneller und synchron zur Richtung des
  Flows, `emitter_flow` (War-Rot) an den Anchors
- **Bei Überlastung:** violetter Blitz-Arc zwischen den Kristallen,
  Warnung-Rot-Schimmer
- **Bei Zerstörung der Pipes (Angriff):** einzelne Kristalle erlöschen

## Condition-Varianten

### Condition 100
Kristalle klar, Kern hell, Sockel sauber.

### Condition 50
Ein Kristall hat Sprünge, Kern flackert, Sockel-Markierungen verblasst,
ein Beschlag-Teil abgeplatzt.

### Condition ruin
Mehrere Kristalle zerbrochen und am Sockel verstreut, Kern erloschen,
Sockel gerissen. Kalte, dunkle Stimmung — gegenteiliges der
funktionierenden Version.

## Condition × Stage Matrix
Sockel konstant, Kristall-Anzahl wächst mit Stufen. Ruin lässt
Kristalle brechen — die Anzahl verlorener Kristalle pro Stufe variiert.

## Umgebungsinteraktion
- Muss auf War-Seite-Terrain stehen.
- Dezentes rotes Bodenglühen unter dem Sockel.
- Kein Deko-Gras — War-Seite wirkt karg.

## Gameplay-Hinweise
- **Tier:** 1 (War-Seite)
- **Radius:** 1 Hex
- **Rolle:** Energie-Verteiler für War-Seite-Netzwerke
- Handbuch-Referenz: §9.1 Energy Node
