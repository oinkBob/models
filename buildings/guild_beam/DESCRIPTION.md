# GildBeam

## Funktion & Rolle
Verbindet den Spieler mit seiner Gilde über große Distanz — stellt
Kommunikation, Ressourcen-Sharing und Gildenbuffs bereit. Handbuch §8.1.

## Vision / Stimmung
Technisch-mystisch, wie eine kleine Kristall-Antenne. Soll "schwebt
leicht, lebendig" wirken, mit permanenter sichtbarer Energie. Das
Gebäude ist ein Zeichen "ich bin Teil von etwas Größerem".

## Silhouette
Schlanker **Metallturm mit einem schwebenden Kristall-Ring** oben.
Der Ring umschwebt die Turmspitze ohne sichtbare Verbindung (visuell
schwebend). Bei Gilden-Betrieb wird der Ring zum zentralen Feature.

## Materialien & Farben
- **Turm:** Metall, mittel-grau mit dunklen Streben
- **Kristall-Ring:** transparenter Kristall, **Gildenfarbe zur Laufzeit
  getönt** (primärer Tint — pro Gilde unterschiedlich)
- **Kernkristall in der Mitte:** Flow-Grün (`#4ade80`) dominant
- **Sockel:** Stein-hell
- **Runen-Einlassungen** am Turm: Shield-Blau LED-Linien

## Ausbaustufen

### Stage 1 — Signaler (2 Anchors)
Kurzer Metallturm, ein einzelner Kristall oben (kein Ring). Sockel
schlicht.

### Stage 2 — Ring-Antenne (4 Anchors)
Turm doppelt so hoch, ein schwebender Kristall-Ring mit 6 einzelnen
Kristallen umschwebt die Spitze. Sockel mit Runen-Mustern.

### Stage 3 — Gilden-Leuchtfeuer (6 Anchors)
Dreifache Höhe, zwei schwebende Ringe übereinander (gegenläufig
rotierend), Kernkristall dominant, Sockel wird eine breite Plattform
mit 6 Runen-Pfeilern.

## Pipe-Anchors
Anchors sind **Energie-Flansche am Sockel**, umrahmt von einem kleinen
Runen-Muster. Alle auf etwa der gleichen Höhe.

- Stage 1: `anchor_0`, `anchor_3` (y≈0.25)
- Stage 2: +`anchor_1`, `anchor_4`
- Stage 3: alle 6

## Schornsteine & Emissionen
- **Kein Schornstein.**
- **Keine Kontaminations-Emission.**
- **Emission-Glow:**
  - Kernkristall pulst permanent Flow-Grün (Ambient, 3s Zyklus)
  - Schwebender Ring leuchtet in Gildenfarbe (Runtime-Tint)
  - Runen am Turm/Sockel pulsieren sanft blau (Shader-Puls)

## Animationen

### Ambient (läuft immer)
- `anim_spin_y` auf dem Kristall-Ring (Stage 2), ~0.3 rad/s
- `anim_spin_y` + `anim_spin_y_counter` auf den zwei Ringen (Stage 3),
  gegenläufig, 0.2 / -0.25 rad/s
- Kernkristall pulst Shader-synchronisiert
- Runen "wandern" langsam am Turm entlang (Shader-UV-Scroll)

### State-gekoppelt
- **Bei aktivem Gilden-Broadcast:** Ringe rotieren schneller, Kristall-
  Partikel (Flow-Grün) schießen nach oben (`emitter_flow` am Kern)
- **Beim Verlassen/Beitreten der Gilde:** großer Puls-Flash, Ringfarbe
  wechselt weich zum neuen Tint

## Condition-Varianten

### Condition 100
Turm geputzt, Runen leuchten hell, Ring schwebt stabil.

### Condition 50
Ein Kristall im Ring fehlt (Lücke), Turm-Runen teilweise erloschen,
Kernkristall flackert.

### Condition ruin
Turm geknickt, Ring zerbrochen auf dem Boden verstreut, Kernkristall
grau und tot.

## Condition × Stage Matrix
Sockel + unterer Turm konstant. Ringe und Spitzen wachsen mit Stufen.
Ring schwebt nur wenn Stage 2+ — Stage 1 hat nur einen einfachen
Kristall.

→ Artist-Tipp: Der Ring sollte als eigenes Mesh ohne Verbindung zum
Turm gebaut sein (kein sichtbares Kabel). Der schwebende Eindruck ist
wichtig.

## Umgebungsinteraktion
- Dezente Bodenrunen um den Sockel (als Textur auf Stein-Platten).
- Stage 3: Kristall-Fragmente liegen dekorativ am Sockel verstreut.
- Keine Terrain-Präferenz.

## Gameplay-Hinweise
- **Tier:** 1
- **Radius:** 1 Hex
- **Build-Cost:** 3000
- **Upkeep:** 25/Tick
- **Rolle:** Gilden-Anbindung (Chat, Ressourcen, Buffs)
- Handbuch-Referenz: §8.1 GildBeam
