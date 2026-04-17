# Maintenance Building

## Funktion & Rolle
Wartet umliegende Gebäude automatisch. Effizienz fällt mit Distanz:
`efficiency = base / (1 + distance²)`. Handbuch §8.2.

## Vision / Stimmung
Werkstatt-Station mit Drohnen-Hangar. Lebendig, aktiv — kleine
Wartungs-Drohnen schwirren zwischen den umliegenden Gebäuden. Soll
"hier arbeitet jemand für andere" ausstrahlen. Warm, industriell,
organisiert.

## Silhouette
**7-Hex-Fläche** (R=2). Flacher Bau mit offenem Innenhof und einem
**zentralen Dach-Hangar**, aus dem **Wartungs-Drohnen** ein- und
ausfliegen. Rund um den Innenhof Werkstatt-Flügel mit offenen
Werkbänken (durch Fenster sichtbar).

## Materialien & Farben
- **Basis:** Stein-dunkel (`#5a5c5e`) Fundament
- **Wände:** Holz-dunkel (`#5c4710`) + Metall-Beschläge
- **Dach-Hangar:** Metall, gräulich, mit aufschiebbaren Panelen
- **Akzente:** Harvester-Gelb (`#f59e0b`) an Werkzeug-Elementen
- **Drohnen:** Harvester-Gelb mit Flow-Grün Triebwerks-Glow
- **Werkstatt-Glow:** Heat-Orange aus den Werkbänken

## Ausbaustufen

### Stage 1 — Werkstatt (2 Anchors)
Einfacher L-förmiger Werkstatt-Bau mit einem kleinen Dach-Hangar.
Eine Drohne auf einer Ladestation auf dem Dach.

### Stage 2 — Drohnen-Depot (4 Anchors)
Vollständige U-Form mit Innenhof, Hangar zentriert, drei Drohnen-
Ladestationen. Kleiner Werkstatt-Turm mit Schornsteinchen.

### Stage 3 — Großes Depot (6 Anchors)
Voller Geviert-Bau mit offenem Innenhof in der Mitte, großem Hangar
auf dem Dach mit **Dach-Luken, die sich öffnen**, 6 Drohnen-
Ladestationen außen, multiple Werkstatt-Flügel.

## Pipe-Anchors
Anchors sind **Werkzeug- und Energie-Einlässe** — als **Werkbank mit
Flansch** ausgeführt. Sichtbares Werkzeug-Regal daneben macht die
Funktion klar.

- Stage 1: `anchor_0`, `anchor_3`
- Stage 2: +`anchor_1`, `anchor_4`
- Stage 3: alle 6

## Schornsteine & Emissionen
- **1 kleiner Schornstein** (Stage 2+3) mit sehr leichtem Rauch — der
  Werkstattbetrieb erzeugt minimal Rauch.
- **Keine Kontaminations-Emission** (Gameplay neutral).
- **Emission-Glow:**
  - Werkstatt-Fenster glühen Heat-Orange bei Nacht (Schweißfeuer-
    Anmutung)
  - Drohnen-Ladestationen pulsen Flow-Grün synchron
  - Dach-Hangar-Innenraum leuchtet (wenn Dachluke auf: starker Glow
    nach oben)

## Animationen

### Ambient (läuft immer)
- **Wartungs-Drohnen** fliegen auf festgelegten Bahnen (Shader mit
  Zeit-Uniform, oder als kleine separate animierte Meshes) zwischen
  Hangar und umliegenden Gebäuden des Besitzers
- Ladestationen pulsen leicht
- Werkstatt-Flackern (Heat-Orange Shader-Noise in Fenstern)

### State-gekoppelt
- **Bei aktiver Wartung:** Dachluken öffnen sich (Stage 3, procedural-
  Animation), mehr Drohnen fliegen raus, `emitter_sparks` an den
  Werkbänken intensiver, Drohnen-Triebwerke Flow-Grün brennen
- **Bei Werkzeug-Mangel:** Ladestationen wechseln zu Warnung-Rot

## Condition-Varianten

### Condition 100
Werkzeuge geordnet, Drohnen alle verfügbar, Dach intakt.

### Condition 50
Zwei Drohnen fehlen (leere Ladestationen), Werkzeug unordentlich,
eine Dachluke hängt schief, Rost am Metall.

### Condition ruin
Drohnen liegen zerbrochen auf dem Boden, Dach eingestürzt,
Werkstatt-Flügel kollabiert, keine Emission mehr.

## Condition × Stage Matrix
Grundriss pro Stufe konstant, Hangar und Drohnen skalieren mit
Ausbau. Ruin-Variante zeigt abgestürzte Drohnen prominenter als jede
andere Degradation.

## Umgebungsinteraktion
- Die Drohnen fliegen sichtbar zu umliegenden Besitzer-Gebäuden →
  **wichtiger visueller Gameplay-Indikator** dafür, welche Gebäude
  automatisch gewartet werden.
- Leichte Werkzeug-Deko (Leitern, Fässer) am Sockel.
- Keine Terrain-Präferenz.

## Gameplay-Hinweise
- **Tier:** 2
- **Radius:** 2 Hex (7-Hex-Footprint)
- **Build-Cost:** 8000
- **Upkeep:** 40/Tick
- **Wartungs-Radius-Formel:** `efficiency = base / (1 + distance²)`
- Handbuch-Referenz: §8.2 Maintenance Building
