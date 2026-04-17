# Resonance Trap

## Funktion & Rolle
Versteckte Falle auf gegnerischem Gebiet. **Sondergebäude** — nutzt die
Ausnahme der Shared-Ownership-Regel: kann auf einem Hex liegen, auf dem
ein anderer Spieler etwas hat. Ausgelöst durch spezifische Gegner-
Aktionen. Handbuch §9.1.

## Vision / Stimmung
Unheimlich unauffällig. Tarnt sich in das Terrain. Soll "fast unsichtbar"
aussehen — der Gegner muss erst merken, dass hier eine Falle ist. Nur
bei Auslösung wird das Gebäude plötzlich bedrohlich sichtbar.

## Silhouette
**Flach**, fast in den Boden eingelassen. Aus der Vogelperspektive
kaum erkennbar. Nur eine **dünne, hexagonale Metallscheibe** auf
Bodenniveau, evtl. mit Runen-Gravuren. Aus der Normal-Spielperspektive
erkennt man schwach, dass hier etwas im Boden liegt.

## Materialien & Farben
- **Scheibe:** Metall-dunkel, nahezu passend zum Terrain-Ton
- **Gravuren:** im Idle-Zustand sehr dunkel, fast schwarz
- **Glow (bei Auslösung):** **War-Rot intensiv**
- **Kontrast zur Umgebung:** **bewusst niedrig** — das Ziel ist Tarnung

## Ausbaustufen

### Stage 1 — Einzelplatte (2 Anchors)
Eine einzelne flache Metall-Hexagon-Platte. Minimal erkennbar.

### Stage 2 — Doppelplatte (4 Anchors)
Zwei gekoppelte Platten nebeneinander. Etwas größer, aber weiterhin flach.

### Stage 3 — Platten-Muster (6 Anchors)
Ein sternförmiges Muster aus mehreren Platten (eine zentrale + sechs
kleinere an den Ecken). Gesamt-Footprint immer noch klein und flach —
aber komplexer Falle-Mechanismus.

## Pipe-Anchors
Anchors sind **versteckte Einlässe** — sichtbar als **kleine
Metallvertiefungen** am Rand der Platte(n), ohne auffällige Flansche.
Der Artist soll hier bewusst **weniger sichtbar** modellieren als
andere Gebäude.

- Stage 1: `anchor_0`, `anchor_3` auf Bodenhöhe (y≈0.05)
- Stage 2: +`anchor_1`, `anchor_4`
- Stage 3: alle 6

## Schornsteine & Emissionen
- **Kein Schornstein.**
- **Keine Kontaminations-Emission.**
- **Emission-Glow:**
  - **Idle:** keine oder extrem schwache Emission (Runen kaum sichtbar)
  - **Armed aber nicht ausgelöst:** schwacher dunkelroter Glow unter
    der Platte (nur bei Nacht sichtbar)
  - **Ausgelöst:** **plötzlicher intensiver War-Rot-Flash**, Runen
    leuchten hell, Schockwelle-Partikel nach außen

## Animationen

### Ambient (läuft immer)
- **Bewusst sehr wenig** — die Falle soll statisch wirken
- Sehr langsamer Shader-Puls auf den Runen (0.1 Hz, kaum wahrnehmbar)

### State-gekoppelt
- **Bei Auslösung (einmalig, dramatisch):**
  - Schlagartiger War-Rot-Flash (Emission springt von 0 auf Maximum)
  - Schockwellen-Partikel ringförmig vom Zentrum
  - `emitter_sparks` War-Rot stark
  - Nach ~2 Sekunden: Emission erlischt, Gebäude wirkt "verbraucht"
- **Nach Auslösung:** Condition wechselt automatisch zu `ruin`
  (ausgebranntes Aussehen, schwarze Rußränder um die Scheibe)

## Condition-Varianten

### Condition 100
Saubere dunkle Metallplatte(n), Runen kaum sichtbar, perfekt getarnt.

### Condition 50
Kleine Sprünge in den Platten, Runen teilweise verwittert, Kontrast
zur Umgebung etwas höher (Tarnung nicht mehr perfekt).

### Condition ruin
Ausgebrannte Platte mit schwarzen Ruß-Flecken, Runen aufgesprungen,
möglicherweise ein Kraterchen im Zentrum. Wirkt "verbraucht" — hat
ihren Zweck erfüllt.

## Condition × Stage Matrix
Platten-Anzahl wächst mit Stufen. Condition-Degradation ist bei Resonance
Trap besonders wichtig — der Unterschied zwischen "scharf" und "ausgelöst"
wird vor allem durch Condition visualisiert.

## Umgebungsinteraktion
- **Adaptive Tarnung:** Der Client soll beim Rendern die Grundfarbe der
  Scheibe leicht zum umgebenden Terrain-Ton hin tinten (z.B. bräunlich
  auf Gras, gräulich auf Berg). Nicht perfekte Tarnung, aber Annäherung.
- **Staub und Dreck** auf der Oberseite (Textur) verstärken den
  Tarn-Effekt.
- **Besonderheit:** Trap kann auf fremdem Hex liegen — Artist und Client
  müssen beachten, dass die Scheibe nie über ein anderes Gebäude ragt,
  immer nur am Boden.

## Gameplay-Hinweise
- **Tier:** 1 (War-Seite)
- **Radius:** 1 Hex
- **Sondermerkmal:** Kann auf gegnerischen Hexes platziert werden
  (versteckt für Gegner bis Auslösung)
- **Auslösung:** einmalig; danach ruin
- Handbuch-Referenz: §9.1 Resonance Trap
