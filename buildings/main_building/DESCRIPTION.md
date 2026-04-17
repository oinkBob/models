# Main Building

## Funktion & Rolle
Das Herzstück jedes Spielers — Spawn-Punkt, zentraler Energie- und
Item-Speicher, und die **einzige Brücke zwischen Economy- und War-
Seite**. Wird bei Spielstart automatisch im Start-Hex platziert und
kann nicht abgerissen werden, solange der Spieler aktiv ist. Handbuch §8.2.

## Vision / Stimmung
Monumentales, einladendes Zentralgebäude mit **zwei klaren Hälften** —
warme, bewohnt wirkende Economy-Seite oben und funktional-robuste
War-Seite unten. Soll wie eine kleine Burg / Station wirken, die
Identität und Wahrzeichen zugleich ist. Der Spieler sieht das eigene
Main Building als "Zuhause".

## Silhouette
**Siebenhexige Grundfläche** (R=2). Zweigeteilt durch eine horizontale
Mittelebene — oben eine wohnlichere Halle mit Dach/Kuppel, unten ein
robuster Sockel-Ring (War-Seite). **Zentraler vertikaler Turm** in der
Mitte trägt eine Energiekugel oder Spitze — das Fernerkennungsmerkmal.

Silhouette auf 100m muss den Spieler das eigene Main Building von
fremden unterscheiden lassen — Flaggenfarbe / Beleuchtung am Turm
personalisiert.

## Materialien & Farben
- **Sockel (War-Seite):** Stein-dunkel (`#5a5c5e`) + Stein-hell
  (`#808286`), massiv
- **Obere Halle (Economy):** Holz (`#8B6914`) + Holz-dunkel-Balken +
  Dach-Schindeln in Grass-dunkel (`#4a8a28`) als warmer Kontrast
- **Turm:** Metall, gräulich-blau
- **Energiekugel (Turmspitze):** Flow-Grün (`#4ade80`), emissive,
  pulst
- **Fahne:** Spieler-Farbe (zur Laufzeit getönt), Shader-Wind
- **Akzente:** Shield-Blau (`#38bdf8`) als Zierstreifen am War-Sockel

## Ausbaustufen

### Stage 1 — Außenposten (2 Anchors)
Schlicht: ein einfacher zweigeschossiger Bau mit kleinem Turm. Dach
ist ein einfacher Satteldach. Der Turm ist gedrungen, Energiekugel
klein und blass. Wirkt wie ein "Pioneer-Camp".

### Stage 2 — Ausgebaute Station (4 Anchors)
Fundament verbreitert auf volle 7-Hex-Fläche, Seitenflügel (Ost/West)
kommen dazu, Turm wird höher und bekommt einen Ring von Rundfenstern.
Energiekugel deutlich größer, kräftiger leuchtend. Fahnenmast wächst
aus dem Dach. Kleiner Balkon umläuft den Turm.

### Stage 3 — Zentral-Zitadelle (6 Anchors)
Zweistufiges Dach mit Kuppel, Turm bricht durch die Kuppel und trägt
eine von Säulen umringte Energiekugel. War-Sockel bekommt ausfahrbare
Verteidigungsbastionen an jeder Hex-Ecke. Sechs markante Rohr-Anschluss-
Türme rund um den Sockel (jeder ein Anchor). Wirkt wie ein kleines
Schloss — noch immer zweigeteilt, aber majestätisch.

## Pipe-Anchors
Jeder Anchor ist ein **gemauerter Anschluss-Turm** am War-Sockel, der
aus der Seitenwand hervorsteht. Deutlich sichtbar mit Flansch am Ende
und einem Ventilrad daneben.

- **Stage 1:** `anchor_0` (Ost), `anchor_3` (West) — auf halber
  Sockel-Höhe (y≈0.5)
- **Stage 2:** zusätzlich `anchor_1` (NO), `anchor_4` (SW)
- **Stage 3:** alle 6 Anchors, je einer pro Hex-Kante, alle als
  Anschluss-Türmchen ausgeführt

## Schornsteine & Emissionen
- **Kein Schornstein** — Main Building produziert nichts und verschmutzt
  nicht.
- **Emission-Glow:**
  - Turmspitzen-Energiekugel pulst permanent in Flow-Grün (Ambient,
    auch wenn keine Produktion läuft — das ist das "Lebenszeichen"
    des Spielers)
  - Rundfenster in der oberen Halle leuchten bei Dämmerung/Nacht
    warmweiß (via Emission-Map + `u_daylight`-Kopplung)
  - Shield-Blau-Zierstreifen pulsen langsam wenn der Spieler in Start-
    Protection ist
- **Optional:** `emitter_flow` an jedem belegten Pipe-Anchor

## Animationen

### Ambient (läuft immer)
- Turmspitzen-Energiekugel: langsame Emission-Puls-Animation (Shader,
  2s Zyklus)
- Fahne auf dem Turm: Shader-Wind (§8.2)
- Keine mechanischen Rotor-Teile — das Main Building ist statisch

### State-gekoppelt
- **Start-Protection aktiv:** Shield-Blau-Zierstreifen pulsen, um den
  Sockel zieht ein dünnes Partikel-Schild-Overlay
- **Alarm (angegriffen):** War-Rot-Licht pulst über allen Fenstern,
  Turm-Kugel wechselt kurz zu War-Rot
- **Guild-verbunden:** Fahne zusätzlich mit Gildenfarbe (sekundäre
  Farbe); kleiner zweiter Wimpel unter der Hauptfahne
- **Nacht:** Fenster + Turm-Basis leuchten warm

## Condition-Varianten

### Condition 100
Frische Farben, Fahne leuchtet, alle Fenster funktional, Sockel
geputzt.

### Condition 50
Rissiges Mauerwerk am Sockel, eine der Holzbalken-Dachschindeln fehlt,
Fahne zerschlissen, ein Rundfenster eingeschlagen, Turm-Kugel pulst
unregelmäßig.

### Condition ruin
Dach teilweise eingestürzt (obere Halle), Turm abgebrochen — Kugel
liegt auf dem Boden (leuchtet schwach weiter). Sockel-Ecken
zusammengebrochen. Rankpflanzen wachsen aus den Rissen. War-Seite
zeigt Brandspuren.

## Condition × Stage Matrix
Der Sockel-Ring (War-Seite, 7 Hex-Footprint) bleibt visuell konstant
über alle Stufen — nur seine Details (Anschluss-Türmchen, Bastionen)
kommen mit den Stufen hinzu. Die **obere Halle und der zentrale Turm**
ändern sich am meisten mit den Stufen. Condition-Degradation betrifft
vor allem die obere Halle + den Turm (bricht sichtbar ab), Sockel bleibt
länger stabil.

→ Artist-Tipp: Sockel einmal bauen (3 Varianten für Anchor-Ausbau),
obere Hälfte pro Stufe komplett neu.

## Umgebungsinteraktion
- Steht auf einem bewusst erhöhten Stein-Fundament (~0.15 Units über
  Boden-Level) — das Main Building thront immer leicht über dem Hex.
- Zieht im Fundament Grass-helle Pflanzen an (Stage 2+3: kleine
  Blumenbeete entlang der Seitenflügel).
- In der War-Side-Ansicht (umgedrehte Kamera) zeigt sich die War-Seite
  mit ihren Bastionen / Waffen-Ports — dieselbe Modell-Instanz, nur
  von unten betrachtet.

## Gameplay-Hinweise
- **Tier:** 2 (besondere Rolle, wird pre-placed)
- **Radius:** 2 Hex (7-Hex Footprint)
- **Build-Cost:** — (pre-placed, kann nicht regulär gebaut werden)
- **Upkeep:** 15/Tick
- Storage: Batterien, Items, Energie
- **Einzige Brücke** zwischen Economy- und War-Side
- Handbuch-Referenz: §8.2 Main Building
