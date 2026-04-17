# Battery Factory

## Funktion & Rolle
Wandelt 250 Roh-Energie pro Batterie um. Batterien sind die mobile,
transportable Energieform für Wartung und Logistik. Handbuch §8.1.

## Vision / Stimmung
Eine kleine, aktive Werkstatt. Funken, Dampf, Fließband. Industriell
aber nicht monumental — wie eine Dorfschmiede kombiniert mit einer
frühen Elektrizitäts-Werkstatt. Deutlich in Betrieb.

## Silhouette
Kompakter Rechteckbau mit schrägem Pultdach, darauf ein **markanter
Transformator-Aufbau** (Kupferspulen mit Isolatoren). An der Seite ein
**Schornstein** mit dünnem Rauchauslass. Durch eine große Tür sichtbar:
kurzes Fließband.

## Materialien & Farben
- **Basis:** Stein-dunkel (`#5a5c5e`) Fundament
- **Wände:** Holz-dunkel (`#5c4710`) + Metall-Bleche
- **Transformator:** Kupfer-getönt (Mix aus Harvester-Gelb und Heat-Orange)
- **Isolatoren:** Shield-Blau (`#38bdf8`) — Keramik-Look
- **Schornstein:** Stein-hell mit Rußflecken
- **Emission:** Heat-Orange (`#f97316`) zwischen den Spulen

## Ausbaustufen

### Stage 1 — Kleine Werkstatt (2 Anchors)
Einfaches Rechteckgebäude mit einem Transformator auf dem Dach.
Schornstein klein. Energie-Eingang Ost, Batterie-Ausgang West.

### Stage 2 — Zwei-Linien-Fabrik (4 Anchors)
Zweites Fließband parallel, Dach mit zwei Transformatoren (Tandem).
Schornstein höher. Laderampe an der Südseite.

### Stage 3 — Voll-Produktionsanlage (6 Anchors)
Dreistöckig mit drei Transformator-Türmen in Dreiecksanordnung, großem
zentralem Schornstein, sechs Anschlüssen, Kupferrohr-Verbindungen
zwischen den Transformatoren. Mini-Kraftwerk-Look.

## Pipe-Anchors
Anchors sind **Energie-Einlass-Flansche** und **Batterie-Auslass-
Schächte**. Visuell durch Farbe unterscheidbar — Einlass Flow-Grün LED,
Auslass Harvester-Gelb LED.

- Stage 1: `anchor_0` (Batterie-out), `anchor_3` (Energie-in)
- Stage 2: +`anchor_1` (Batterie-out #2), `anchor_4` (Energie-in #2)
- Stage 3: alle 6 — Konvention: gerade Indices = Auslass, ungerade = Einlass

## Schornsteine & Emissionen
- **1 Schornstein** (Stage 1/2), **3 Schornsteine** (Stage 3).
  `emitter_smoke` jeweils oben.
- **Rauchfarbe:** dunkelgrau mit leichtem Heat-Orange Funken-Akzent.
- **Kontaminations-Beitrag:** ja, mäßig (Produktion erzeugt Kontamination).
- **Emission-Glow:** Transformator-Spulen pulsen Heat-Orange synchron
  mit dem Batterie-Ausstoß-Rhythmus.
- **Sparks:** `emitter_sparks` am Transformator (permanent bei
  Produktion).

## Animationen

### Ambient (läuft immer)
- Transformator-Isolatoren pulsen dezent (Shader, 0.7s Zyklus)
- Schornstein-Rauch (leicht) auch bei Idle
- Stage 3: Kupferrohre haben animierten Vertex-Shader-"Puls"

### State-gekoppelt
- **Bei Produktion:** Rauch stärker, Heat-Orange Funken am
  Transformator, Fließband läuft (Textur-Scroll Shader), Batterie-
  Auslass pulst gelb.
- **Bei Kontamination hoch:** Rauch düsterer, Giftgrün-Anteil im
  `emitter_smoke`.

## Condition-Varianten

### Condition 100
Kupfer poliert, Wände gestrichen, Schornstein frisch.

### Condition 50
Kupfer patiniert (grünlich), Rußspuren am Schornstein, ein Dachblech
abgeblättert, eine Transformator-Spule beschädigt.

### Condition ruin
Schornstein zusammengestürzt, Transformator schief, Dach hängt durch,
Kupfer oxidiert grün, Fließband gebrochen. Keine Emission mehr.

## Condition × Stage Matrix
Stein-Sockel + Grundquader konstant. Transformator-Aufbau wächst mit
Stufen. Condition-50/ruin-Varianten degradieren primär Transformator
und Dach.

## Umgebungsinteraktion
- Bodenplatten um den Sockel zeigen Öl/Ruß-Flecken (Textur).
- Stage 3: kleine Kupferdraht-Rollen als Deko um die Basis.
- Keine Terrain-Präferenz.

## Gameplay-Hinweise
- **Tier:** 1
- **Radius:** 1 Hex
- **Build-Cost:** 1000
- **Upkeep:** 25/Tick
- **Rezept:** 250 Energie → 1 Batterie
- Handbuch-Referenz: §8.1 Battery Factory
