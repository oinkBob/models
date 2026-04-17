# Distributor

## Funktion & Rolle
**Pipe-Knotenpunkt** — verteilt Energie- und Item-Flows zwischen bis zu
6 Pipe-Anschlüssen nach vom Spieler konfigurierbaren Routing-Regeln.
Auch ein **Section-Break** für das 50-Hex-Pipe-Limit: längere Pipe-
Läufe müssen einen Distributor dazwischen haben. Handbuch §8.2.

## Vision / Stimmung
Ein funktional-mechanisches Rangiergebäude, halb Umspannwerk, halb
Wasserturm. Im Betrieb sichtbar lebendig durch zahlreiche fließende
Energie-Partikel und rotierende Ventile. Soll das "Nervensystem" des
Wirtschaftsnetzes zeigen — industriell, aber nicht bedrohlich.
Leuchtet bei Nacht deutlich.

## Silhouette
**7-Hex-Fläche** (R=2). Zentral ein vertikaler Zylinder-Turm mit
sichtbaren Ventil-Ringen, umgeben von einem **Sternförmig angeordneten
Rohr-Kranz**. Auf Distanz erkennbar am glühenden flow-grünen Kern und
den rundum verteilten Rohranschlüssen.

## Materialien & Farben
- **Basis:** Stein-hell (`#808286`) Sockel
- **Zylinder-Turm:** Metall, mittel-grau mit Flow-Grün Ventil-Ringen
- **Ventile & Handräder:** Harvester-Gelb (`#f59e0b`) Akzent
- **Rohr-Kranz:** Holz (`#8B6914`) mit Metall-Bändern, Pipe-Active-
  Grün (`#4ade80`) an den Innenflächen (emissive)
- **Kern-Glow:** Flow-Grün, deutlich
- **Ventil-LEDs:** klein, flow-grün oder harvester-gelb

## Ausbaustufen

### Stage 1 — Einfacher Verteiler (2 Anchors)
Kleiner Zylinder mit zwei gegenüberliegenden Rohren, ein einziges
Ventilrad oben. Sockel einfach. Auf 2 Anchors reduziert fungiert er
eher als reiner Section-Break für lange Pipes.

### Stage 2 — Rangier-Distributor (4 Anchors)
Zylinder wird höher und dicker, zweiter Ventilring dazu, vier Rohr-
Anschlüsse kreuzförmig. Ein kleiner Bedien-Steg läuft um den Turm.
Kern-Glow deutlich sichtbar.

### Stage 3 — Voller Knotenpunkt (6 Anchors)
Doppelte Turmhöhe, drei Ventilringe übereinander, alle 6 Rohre in
Stern-Anordnung, Bedien-Steg wird ein voller Rundbalkon mit
Leuchtkugeln. Auf dem Turmhaupt ein rotierender Dispatch-Arm
(mechanisch). Imposant, "Hauptbahnhof des Netzes".

## Pipe-Anchors
Jeder Anchor ist ein **gusseisernes Rohrstück** mit Flansch und einem
daneben montierten **großen Handrad** (Ventil). Klar als Anschlusspunkt
lesbar.

- **Stage 1:** `anchor_0` (Ost), `anchor_3` (West) — auf y≈0.4
- **Stage 2:** zusätzlich `anchor_1`, `anchor_4`
- **Stage 3:** alle 6 Anchors, sternförmig auf y≈0.4 rundum

## Schornsteine & Emissionen
- **Kein Schornstein** — Distributor erzeugt keine Abgase.
- **Keine Kontaminations-Emission**.
- **Emission-Glow:**
  - Zentraler Kern im Turm leuchtet permanent flow-grün (Ambient)
  - Ventilring-LEDs pulsen langsam bei idle
  - Innenflächen der Rohranschlüsse leuchten bei aktivem Flow
- **Partikel:**
  - `emitter_flow` an jedem aktiven Anchor (flow-grüne Energie-
    Partikel wandern in den Turm hinein und wieder heraus)
  - `emitter_sparks` am Dispatch-Arm (Stage 3) bei aktivem Routing

## Animationen

### Ambient (läuft immer)
- `anim_spin_y` am Dispatch-Arm (nur Stage 3) — langsam, 0.3 rad/s
- Kern-Glow pulst per Shader (Emission-Map + Zeit-Uniform), ~1.5s Zyklus
- Ventil-LEDs pulsen versetzt (Shader)

### State-gekoppelt
- **Flow aktiv:** Ventilringe rotieren schrittweise (`anim_spin_y`
  Mid-Ring), Rohr-Innenflächen leuchten flow-grün, `emitter_flow`
  spawnt Partikel
- **Überlastung:** Ventil-LEDs wechseln zu Warnung (`#f87171`), pulsen
  schneller
- **Idle (keine Pipes angeschlossen):** nur Kern-Glow, keine Flow-
  Partikel

## Condition-Varianten

### Condition 100
Frisches Metall, grelle LEDs, Ventilräder poliert.

### Condition 50
Rost an den Rohranschlüssen, ein Ventil-Handrad abgebrochen, LEDs
teilweise dunkel, Kern-Glow flackert. Eine Lücke im Bedien-Steg.

### Condition ruin
Zylinder geknickt / schief, zwei Rohre komplett abgebrochen (auf dem
Boden), Dispatch-Arm auf dem Boden, kein Glow mehr. Der zentrale Kern
dunkel, rissig. Rankpflanzen auf dem Sockel.

## Condition × Stage Matrix
Sockel + unterer Zylinderteil bleiben über Stufen konstant, die
**Turm-Höhe und Ventilring-Anzahl** wachsen mit den Stufen. Condition-
Degradation greift vor allem Ventilräder, Glühelemente und oberste
Zylinder-Segmente an. Ruin kippt den Turm deutlich ab (Silhouette-
Bruch).

→ Artist-Tipp: Modularer Aufbau — ein Zylinder-Segment pro Stufe
wiederverwenden, oben/unten-Kappen je Stufe neu.

## Umgebungsinteraktion
- Leichte Bodenplatten um den Sockel, 0.03 Units in den Hex-Boden.
- Nachts besonders auffällig durch starke Emission (Fenster/LEDs).
- Keine Terrain-Präferenz.

## Gameplay-Hinweise
- **Tier:** 2
- **Radius:** 2 Hex (7-Hex-Footprint)
- **Build-Cost:** 5000
- **Upkeep:** 20/Tick
- **Funktion:** 6-in/6-out Routing (voll ausgebaut), konfigurierbare
  Flow-Regeln, Pflicht-Station für Pipe-Sections > 50 Hex
- Handbuch-Referenz: §8.2 Distributor
