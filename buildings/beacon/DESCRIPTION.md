# Beacon

## Funktion & Rolle
Öffentliche Nachrichten-Station — sendet Messages an alle Spieler im
Umkreis. Handbuch §8.1.

## Vision / Stimmung
Leuchtturm des Informationszeitalters — schlank, hoch, würdevoll. Ruhig
und verlässlich. Das Signal pulst regelmäßig wie ein Herzschlag.

## Silhouette
**Schlanker, hoher Turm** — das höchste Tier-1-Gebäude. Rundes
Fundament, zylindrischer Schaft, oben eine **Signallampe unter einer
schmiedeeisernen Kuppel**. Auf 20+ Hex erkennbar.

## Materialien & Farben
- **Fundament:** Stein-hell (`#808286`) Rundsockel
- **Schaft:** Stein-hell mit Stein-dunkel Quaderfugen
- **Kuppel:** Metall, bronze-gefärbt (Harvester-Gelb dunkler getönt)
- **Signallampe:** Kristall mit Flow-Grün (`#4ade80`) Emission
- **Wendeltreppe (sichtbar):** Holz (`#8B6914`)

## Ausbaustufen

### Stage 1 — Signalstand (2 Anchors)
Kurzer Turm (ca. 1.2 Units hoch), einfacher Schaft, kleine Kuppel mit
Lampe. Eine Stufe führt zum Sockel.

### Stage 2 — Leuchtturm (4 Anchors)
Doppelte Höhe, zwei Fensterringe im Schaft, größere Kuppel, schmale
Aussichtsplattform unterhalb der Lampe.

### Stage 3 — Großer Signalturm (6 Anchors)
Dreifache Höhe (~3.5 Units). Mehrere umlaufende Balkone, drei
Fensterringe, kleine Flaggen auf Nebentürmchen, zwei gegenläufig
rotierende Signal-Spiegel neben der Hauptlampe. Monumental.

## Pipe-Anchors
Anchors sind **Kabel-/Signalverbinder** am Fuß des Turms, nicht im
Schaft höher oben. Ausgeführt als **Flanschring mit Signal-LED**.

- Stage 1: `anchor_0`, `anchor_3` am Sockel (y≈0.2)
- Stage 2: +`anchor_1`, `anchor_4`
- Stage 3: alle 6 am Sockel

## Schornsteine & Emissionen
- **Kein Schornstein.**
- **Keine Kontaminations-Emission.**
- **Emission-Glow:**
  - Hauptsignal oben: **pulst permanent** Flow-Grün (Ambient, ~2s
    Zyklus). "Lebenszeichen" des Beacons.
  - Fensterringe glühen warmweiß bei Nacht
  - Stage 3: Nebentürmchen pulsieren versetzt zum Hauptsignal

## Animationen

### Ambient (läuft immer)
- Hauptsignal pulst (Shader, konstant)
- Stage 3: zwei Signal-Spiegel `anim_spin_y` gegenläufig, 0.4 rad/s
- Fahne auf Nebentürmchen: Shader-Wind

### State-gekoppelt
- **Bei aktivem Broadcast:** Hauptsignal blinkt schneller (0.4s
  Zyklus), breiter Lichtkegel strahlt in alle 6 Richtungen (Partikel-
  Overlay), synchron mit Message-Timing.
- **Bei Alarm-Message:** Signal wechselt zu War-Rot.

## Condition-Varianten

### Condition 100
Stein frisch, Kuppel glänzt, Signal hell.

### Condition 50
Steinfugen rissig, Kuppel patiniert, ein Fenster eingeschlagen, Signal
flackert unregelmäßig.

### Condition ruin
Turm in oberem Drittel abgebrochen, Kuppel liegt am Sockel, Signal
erloschen, Efeu wächst an der Turmbasis, Holztreppe zusammengebrochen.

## Condition × Stage Matrix
Rundsockel + unterer Schaft bleiben konstant. Höhe und Balkone kommen
mit Stufen.

→ Artist-Tipp: Schaft modular als Segmente bauen — ein Segment für
Stage 1, plus eines für Stage 2, plus eines für Stage 3.

## Umgebungsinteraktion
- Leichte Bodenplatten-Erhöhung am Sockel (0.05 Units).
- Stage 3: kleine Laternen am Weg zum Sockel.
- Bei Nacht sehr auffällig → wichtiges Landmark.

## Gameplay-Hinweise
- **Tier:** 1
- **Radius:** 1 Hex
- **Build-Cost:** 1200
- **Effekt:** Öffentliche Messaging-Reichweite
- Handbuch-Referenz: §8.1 Beacon
