# Howitzer

## Funktion & Rolle
Langstrecken-Artillerie. 8% Condition-Schaden pro Schuss, 1 Schuss /
10 Ticks, braucht **Munition** über Pipes. 20-Tick-Aufwärmzeit.
Handbuch §9.3.

## Vision / Stimmung
Monumentale Belagerungs-Kanone. Unglaublich schwer, langsam,
verheerend. Soll "wenn die schießt, merkt es die halbe Insel"
ausstrahlen. Kontrast zur Phalanx (schneller, leichter).

## Silhouette
**19-Hex-Fläche** (R=3). **Gewaltiger Stein-Sockel** mit darauf
montiertem **langem Lauf**, der schräg nach oben zeigt (Richtung
Himmel). Schienen-System unter dem Lauf für Rückstoß-Dämpfung.
**Munitions-Hebeanlage** dahinter. Wirkt wie eine Weltkriegs-
Belagerungs-Waffe im Molanex-Stil.

## Materialien & Farben
- **Sockel:** Stein-dunkel (`#5a5c5e`) massiv, viele Stufen
- **Lauf:** Metall-dunkel mit Kupfer-Innenringen (Harvester-Gelb)
- **Schienen:** Metall-mittel, sichtbare Verschraubungen
- **Mündungs-Emitter:** War-Rot + Heat-Orange (Warmup)
- **Munitions-Hebeanlage:** Holz-dunkel Rahmen + Metall-Ketten
- **Munition (Deko):** große Granaten/Projektile in Harvester-Gelb
- **Kühlrohre:** Shield-Blau LEDs

## Ausbaustufen

### Stage 1 — Einzelne Kanone (2 Anchors)
Ein großer Lauf auf massivem Sockel, einfache Schienen, kleine
Munitions-Einzeleinheit. Wirkt wie eine "Proto-Howitzer".

### Stage 2 — Ausgebaute Artillerie (4 Anchors)
Sockel breiter mit mehrstöckigem Sockel-Unterbau, Lauf länger, sichtbare
Kühlrohre, Munitions-Lager im Sockel mit Förderband zur Kanone.

### Stage 3 — Dreifach-Lauf / Mehrlauf-Artillerie (6 Anchors)
**Drei parallele Läufe** (können sequentiell feuern) auf einem
gigantischen Stein-Sockel, automatische Nachladung über sichtbares
Kettenförderer-System, massive Rückstoß-Schienen, Munitions-
Lagerhaus an der Seite. Monumental.

## Pipe-Anchors
Anchors sind **Munitions-Zufuhr-Schächte** am Sockel, ausgeführt als
**schwere Stahltore mit Rohr-Förderern sichtbar**. Im Gegensatz zur
Phalanx führen diese explizit **Munition und nicht nur Energie**.

- Stage 1: `anchor_0`, `anchor_3` am Sockel (y≈0.4)
- Stage 2: +`anchor_1`, `anchor_4`
- Stage 3: alle 6

## Schornsteine & Emissionen
- **Der Lauf selbst ist der "Schornstein"** — nach einem Schuss raucht
  die Mündung stark (`emitter_smoke` am Lauf-Ende, dunkelgrau-schwarz,
  Pulver-Rauch).
- **Kontaminations-Beitrag: kleiner** (Pulver-Rauch kontaminiert die
  Umgebung leicht).
- **Emission-Glow:**
  - Kühlrohr-LEDs Shield-Blau Ambient
  - Lauf-Mündung pulst dezent Heat-Orange im Idle
  - **Im Warmup (20 Ticks):** Lauf glüht progressiv — von Heat-Orange
    zu intensivem War-Rot, Shader-Emission wächst synchron
  - Munitions-Anzeige (Harvester-Gelb LEDs) zeigt den Munitionsstand

## Animationen

### Ambient (läuft immer)
- Kühlrohr-LEDs Shader-Puls
- Munitions-Ketten (Stage 3) bewegen sich langsam (Shader-UV-Scroll)
- Fahnen Shader-Wind

### State-gekoppelt
- **Warmup (20 Ticks):** Lauf hebt sich leicht (procedural Animation),
  Emission wächst, `emitter_sparks` Heat-Orange stärker, ein langsames
  Laden-Geräusch (akustisch)
- **Schuss:**
  - Extremer Rückstoß: Lauf zuckt auf den Schienen deutlich zurück
    (procedural, ~0.3 Units)
  - **Großer Feuerball-Effekt** aus der Mündung (`emitter_sparks` Max,
    War-Rot + Heat-Orange Mix)
  - Dunkler Pulver-Rauch für ca. 3s nach dem Schuss
  - Partikel-Schockwelle auf dem Boden vor der Kanone
- **Abkühlung:** Dampf (`emitter_smoke` weißlich) aus Kühlrohren für
  ca. 5s nach dem Schuss
- **Bei Munitionsmangel:** Lauf-Emission erlischt, Munitions-Anzeige
  wechselt zu Warnung-Rot

## Condition-Varianten

### Condition 100
Lauf poliert, Kupfer hell, Munition ordentlich gelagert, Sockel
sauber.

### Condition 50
Lauf-Außen mit Einschuss-Spuren (Gegenangriff), Schienen verbogen,
Munition wirr, Sockel gerissen.

### Condition ruin
Lauf **explodiert** (in mehrere Teile zerrissen), Sockel geborsten,
Munitions-Kisten geplatzt mit Trümmern. Besonders dramatisch und
gefährlich aussehend.

## Condition × Stage Matrix
Sockel konstant in Position, Lauf-Anzahl und Munitions-System wachsen
mit Stufen. Ruin ist immer dramatisch — der Lauf zerreißt.

## Umgebungsinteraktion
- Sockel leicht in den Boden eingelassen (0.1 Units, zeigt das Gewicht).
- **Verbrannter Ring** auf dem Boden vor der Kanone (Textur-Overlay auf
  angrenzendem Hex in Schussrichtung) — die Überreste vieler Schüsse.
- Kleine Granatsplitter als Deko am Sockel.
- Muss auf War-Seite-Terrain stehen.

## Gameplay-Hinweise
- **Tier:** 3 (War-Seite)
- **Radius:** 3 Hex (19-Hex-Footprint)
- **Build-Cost:** 30000
- **Schaden:** 8% Condition/Schuss
- **Rate:** 1 Schuss / 10 Ticks
- **Warmup:** 20 Ticks
- **Besonderheit:** braucht Munition über Pipes
- Handbuch-Referenz: §9.3 Howitzer
