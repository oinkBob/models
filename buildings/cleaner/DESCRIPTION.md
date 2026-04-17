# Cleaner

## Funktion & Rolle
Filtert Kontamination aus Pipes und der Umgebung. Wichtig gegen den
Contamination-Spread. Handbuch §8.2.

## Vision / Stimmung
Sauber-industriell, fast medizinisch. Weißes Metall, klare Linien,
blaue Akzente. Soll das Gegenteil der dreckigen Battery Factory sein —
das Gebäude, das "aufräumt". Gibt Vertrauen.

## Silhouette
**7-Hex-Fläche** (R=2). Flacher breiter Bau mit **zwei markanten
runden Filter-Tanks** (wie chemische Reaktoren), dazwischen Querrohre.
Oben auf jedem Tank ein **Luftauslass-Röhrchen**, aus dem saubere Luft
austritt. Wirkt wie eine kleine Wasseraufbereitungs-Anlage.

## Materialien & Farben
- **Basis:** Stein-hell (`#808286`), fast weiß
- **Filter-Tanks:** Weißes Metall (fast reines Weiß, leicht kühl getönt)
- **Ringe um Tanks:** Shield-Blau (`#38bdf8`)
- **Querrohre:** Metall-mittel-grau
- **Luftauslässe:** Shield-Blau emissive-Ring
- **Glas-Elemente (Kontroll-Fenster):** Shield-Blau transparent

## Ausbaustufen

### Stage 1 — Einzeltank (2 Anchors)
Ein Filter-Tank auf einem Stein-Sockel. Ein Zu- und ein Abflussrohr.
Funktional wie ein erster Versuch.

### Stage 2 — Doppeltank-Anlage (4 Anchors)
Zwei Filter-Tanks nebeneinander, verbunden durch Querrohre. Ein
kleines Kontrollzentrum zwischen den Tanks (Glas-Kabine). Vier
Anschlüsse.

### Stage 3 — Voll-Filter-Station (6 Anchors)
Drei Filter-Tanks in Dreiecksanordnung, zentrales Kontroll-Haus in
der Mitte, sechs Anschlüsse sternförmig. Komplexes Rohrnetz oberhalb
verbindet alle Tanks.

## Pipe-Anchors
Anchors sind **große Filter-Flansche** mit **runden Glas-Inspektions-
Fenstern** direkt daneben — der Spieler kann visuell erkennen, ob
durch den Anschluss sauberes (flow-grün) oder kontaminiertes (giftgrün)
Medium fließt.

- Stage 1: `anchor_0`, `anchor_3`
- Stage 2: +`anchor_1`, `anchor_4`
- Stage 3: alle 6

## Schornsteine & Emissionen
- **Luftauslässe auf den Filter-Tanks** sind keine Schornsteine im
  klassischen Sinn — sie emittieren **saubere Luft** (sehr leichter,
  weißer Dunst via `emitter_smoke` mit weißer Farbe).
- **Keine Kontaminations-Emission** (Cleaner ist das Gegenteil).
- **Emission-Glow:**
  - Ringe um die Filter-Tanks pulsieren Shield-Blau bei Aktivität
  - Glas-Kontrollfenster leuchten sanft Shield-Blau
  - Bei Nacht sehr klinisch-hell

## Animationen

### Ambient (läuft immer)
- Leichter weißer Dunst aus Luftauslässen (Partikel, sanft)
- Filter-Ringe pulsen Shield-Blau (Shader, 2s Zyklus)
- Stage 3: Rohrnetz hat Shader-Flow-Animation

### State-gekoppelt
- **Bei aktiver Filterung:** Eingangsseite Glas-Fenster zeigt giftgrüne
  Trübung, Ausgangsseite Glas-Fenster zeigt klares Flow-Grün — deutlicher
  visueller Kontrast. Luftauslass emittiert stärker, `emitter_haze`
  (umgekehrt, weißer Dampf).
- **Bei Überlastung:** Ringe wechseln zu Warnung-Rot, weißer Dampf
  unterbricht pulsierend.

## Condition-Varianten

### Condition 100
Metall weiß und glänzend, Glas klar, Ringe leuchten hell.

### Condition 50
Metall mit Kratzern und Kontaminations-Verfärbungen, ein Glas-Fenster
mit grünlicher Innenverfärbung, ein Ring erloschen.

### Condition ruin
Tanks gerissen mit Giftgrün-Leckage am Boden, Kontrollhaus-Glas
zersplittert, Rohre abgeknickt. Kontamination sichtbar, gefährlich.

## Condition × Stage Matrix
Stein-Sockel + Positionen der Tanks bleiben konstant. Zahl der Tanks
und Rohrnetz wächst mit Stufen. Ruin zeigt Giftgrün-Pools — das
visuell deutlichste Ruin aller Gebäude (ironisch: der Cleaner ist
kaputt → Kontamination sichtbar).

## Umgebungsinteraktion
- Stein-Bodenplatten unter der Basis, leicht angehoben.
- Umliegendes Hex bekommt kleinen Flow-Grün-Dunst-Effekt (Stage 3),
  simuliert die Reinigungs-Zone.
- Keine Terrain-Präferenz.

## Gameplay-Hinweise
- **Tier:** 2
- **Radius:** 2 Hex (7-Hex-Footprint)
- **Build-Cost:** 2000
- **Upkeep:** 15/Tick
- **Rolle:** Filtert Kontamination aus angeschlossenen Pipes
- Handbuch-Referenz: §8.2 Cleaner
