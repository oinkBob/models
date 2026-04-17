# Watch Tower

## Funktion & Rolle
Erhöht die Sichtweite auf der War-Seite. Klassischer Wachturm —
passives, aber zentrales Frühwarnsystem. Handbuch §9.1.

## Vision / Stimmung
Archetypisch militärisch — ein klassischer Wehrturm mit Zinnen,
Wachposten-Plattform und Suchscheinwerfer. Streng, aufmerksam,
verlässlich. Soll "hier wird beobachtet" ausstrahlen.

## Silhouette
Schmaler hoher Turm mit **Zinnen-Krone** und **Aussichtsplattform**
mit Geländer. Oben ein drehbarer **Suchscheinwerfer**. Am Fuß ein
kleiner Eingangs-Kubus mit Wehrtür.

## Materialien & Farben
- **Turm:** Stein-dunkel (`#5a5c5e`) mit Stein-hell Fugen
- **Holz-Balken (Plattform):** Holz-dunkel (`#5c4710`)
- **Metall-Beschläge:** Metall-mittel
- **Fahne:** War-Rot (`#dc2626`)
- **Suchscheinwerfer:** Metall mit warmweißer Lampe
- **Alarm-LED-Akzente:** War-Rot

## Ausbaustufen

### Stage 1 — Beobachtungsposten (2 Anchors)
Kurzer Turm (~1.5 Units), flache Plattform, ein Suchscheinwerfer, eine
kleine Fahne.

### Stage 2 — Wachturm (4 Anchors)
Doppelt so hoch, Zinnen-Krone dazu, zwei Suchscheinwerfer
(gegenüberliegend), Eingangs-Kubus mit Wehrtür am Fuß.

### Stage 3 — Festungsturm (6 Anchors)
Dreifache Höhe, doppelte Zinnen-Krone (versetzt), vier
Suchscheinwerfer in verschiedene Richtungen, erweiterte Plattform
mit umlaufendem Balkon, Eingangs-Kubus mit Flaggenmast.

## Pipe-Anchors
Anchors sind **militärische Energie-Einlässe** am Fuß des Turms,
ausgeführt als **gepanzerte Flansche mit Warn-LED-Ring**.

- Stage 1: `anchor_0`, `anchor_3` (y≈0.2)
- Stage 2: +`anchor_1`, `anchor_4`
- Stage 3: alle 6

## Schornsteine & Emissionen
- **Kein Schornstein.**
- **Keine Kontaminations-Emission.**
- **Emission-Glow:**
  - Suchscheinwerfer werfen einen **Lichtkegel** (Shader-Vertex auf
    einem Kegel-Mesh) in Such-Richtung
  - Zinnen-LEDs pulsieren langsam (Patrouillen-Rhythmus)
  - Fahne hat keine Emission, aber leuchtet im Tageszyklus

## Animationen

### Ambient (läuft immer)
- `anim_spin_y` auf dem/den Suchscheinwerfern, langsame Patrouillen-
  Rotation (0.15 rad/s Stage 1, 0.2 rad/s Stage 3)
- Fahne Shader-Wind
- Zinnen-LEDs Shader-Puls

### State-gekoppelt
- **Bei Feindsicht:** Suchscheinwerfer wechseln zu War-Rot,
  rotieren **schnell** in Richtung Feind, Alarm-LEDs pulsieren
  schnell, `emitter_sparks` an Zinnen
- **Bei Stromausfall:** Licht aus, Alarm-LEDs blinken Warnung

## Condition-Varianten

### Condition 100
Stein sauber, Holz-Plattform fest, Fahne hell.

### Condition 50
Steinzinnen teils abgebrochen, Holz-Plattform bricht durch, ein
Suchscheinwerfer kaputt, Fahne zerschlissen.

### Condition ruin
Turm in der Mitte abgebrochen (oberer Teil fehlt oder liegt schräg),
Plattform kollabiert, kein Licht, Efeu am Sockel.

## Condition × Stage Matrix
Sockel konstant, Turmhöhe und Plattform-Details wachsen. Ruin bricht
den oberen Turmteil weg.

## Umgebungsinteraktion
- Steht auf einem Stein-Fundament, leicht in den Boden versenkt.
- Leichter Kies-Boden drumherum.
- Nachts wichtige Lichtquelle auf der War-Seite.

## Gameplay-Hinweise
- **Tier:** 1 (War-Seite)
- **Radius:** 1 Hex
- **Rolle:** Erhöht War-Side-Sichtweite, passive Aufklärung
- Handbuch-Referenz: §9.1 Watch Tower
