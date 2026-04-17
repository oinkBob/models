# Phalanx

## Funktion & Rolle
Schwere, stationäre, **gerichtete** Waffenplattform. 2% Condition-Schaden
pro Tick, 15-Tick-Aufwärmzeit. Die erste "echte" Angriffswaffe der
War-Seite. Handbuch §9.2.

## Vision / Stimmung
Schwere Artillerie-Plattform. Gerichtet und unbeweglich — muss beim
Bauen ausgerichtet werden, kann nicht 360° schwenken. Wirkt
bedrohlich, aber mechanisch. Soll "fest verankert, zielt in eine
Richtung" ausstrahlen.

## Silhouette
**7-Hex-Fläche** (R=2). Breiter Stein-Sockel mit **einer großen
gerichteten Kanone** (Laser-/Schienen-Lauf), die aus dem Sockel
herausragt. Kanone ist **klar nach vorne orientiert** — kein
Rundum-Design. Große Kühlrippen seitlich.

## Materialien & Farben
- **Sockel:** Stein-dunkel (`#5a5c5e`) massiv
- **Kanone (Lauf):** Metall-dunkel mit Kupfer-Innenringen
  (Harvester-Gelb getönt)
- **Laser-Emitter an der Spitze:** War-Rot (`#dc2626`) — im Warmup
  Heat-Orange (`#f97316`)
- **Kühlrippen:** Metall-mittel, Shield-Blau LED zwischen den Rippen
- **Munitions-Anzeige:** Harvester-Gelb
- **Warnmarkierungen:** gelb-schwarz am Sockel

## Ausbaustufen

### Stage 1 — Kleine Kanone (2 Anchors)
Einfacher Sockel, eine mittlere Kanone, zwei Kühlrippen. Kompakt.

### Stage 2 — Erweiterte Plattform (4 Anchors)
Breiterer Sockel, **längere Kanone** mit mehr Kühlrippen, Munitions-
Magazin dahinter sichtbar. Steg seitlich.

### Stage 3 — Doppel- oder Dreifach-Waffe (6 Anchors)
Massiver Sockel, **drei parallele Kanonen-Läufe** (wie eine Gatling-
Konfiguration, aber stationär), mehrere Kühlrippen-Reihen,
Munitions-Förderband sichtbar. Imposant.

## Pipe-Anchors
Anchors sind **Munitions- und Energie-Einlässe** am Sockel. **Nicht am
Lauf** — der Lauf ist die Waffe. Ausgeführt als **große
Kupplungs-Schächte** mit Munitions-Gurt-Anmutung.

- Stage 1: `anchor_0`, `anchor_3` am Sockel (y≈0.35)
- Stage 2: +`anchor_1`, `anchor_4`
- Stage 3: alle 6

**Wichtig:** Die Kanonen-Ausrichtung ist **unabhängig** vom Anchor-System
— Anchors zeigen in Hex-Richtungen wie §7.2, die Kanonen-Richtung wird
separat beim Bauen festgelegt (Hex-Ausrichtungs-Parameter im Spiel).

## Schornsteine & Emissionen
- **Kein klassischer Schornstein**, aber **Kanonen-Mündung emittiert
  Hitze** bei Betrieb (`emitter_sparks` Heat-Orange).
- **Keine Kontaminations-Emission** (sauberer Energie-/Schienen-Schuss).
- **Emission-Glow:**
  - Kupfer-Innenringe im Lauf leuchten dezent Heat-Orange (Ambient)
  - Laser-Emitter vorne pulst War-Rot im Idle
  - Kühlrippen-LEDs Shield-Blau
  - **Im Warmup:** Lauf leuchtet progressiv Heat-Orange → War-Rot
    über die 15 Ticks

## Animationen

### Ambient (läuft immer)
- Kühlrippen pulsieren Shield-Blau dezent (Shader)
- Laser-Emitter pulst langsam (1s)
- Fahne auf der Plattform Shader-Wind

### State-gekoppelt
- **Warmup (15 Ticks):** Lauf-Emission wird über die Zeit intensiver
  (Shader-Uniform gekoppelt an Warmup-Progress), Kühlrippen-LEDs
  wechseln zu Heat-Orange, `emitter_sparks` zunehmend
- **Schuss:** intensiver War-Rot-Flash, Partikel-Explosion
  (`emitter_sparks` Max), Recoil-Animation (Lauf zuckt zurück,
  procedural)
- **Abkühlung nach Schuss:** Dampf-Partikel (weißer `emitter_smoke`
  kurzzeitig) aus den Kühlrippen

## Condition-Varianten

### Condition 100
Metall geputzt, Kupfer hell, Kanonen-Lauf gerade.

### Condition 50
Lauf hat Einschuss-Spuren (nicht die eigenen), Kühlrippen verbogen,
ein Beschlag abgeplatzt, Munitions-Anzeige kaputt.

### Condition ruin
Kanonen-Lauf gebrochen, Sockel gerissen, Kühlrippen abgefallen, keine
Emission. Möglicherweise Explosions-Krater im Boden.

## Condition × Stage Matrix
Sockel konstant, Kanonen-Anzahl und Kühlrippen wachsen mit Stufen.
Ruin zerstört primär die Kanone — Sockel bleibt meist erhalten.

## Umgebungsinteraktion
- Muss auf War-Seite-Terrain stehen.
- Leichte Verbrennungs-Spuren in Schussrichtung auf dem Boden (Textur
  am Hex in Front-Richtung).
- Munitions-Kisten als Deko am Sockel.

## Gameplay-Hinweise
- **Tier:** 2 (War-Seite)
- **Radius:** 2 Hex (7-Hex-Footprint)
- **Schaden:** 2% Condition/Tick (auf Ziel)
- **Warmup:** 15 Ticks
- **Gerichtet:** feste Schussrichtung beim Bauen festgelegt
- Handbuch-Referenz: §9.2 Phalanx
