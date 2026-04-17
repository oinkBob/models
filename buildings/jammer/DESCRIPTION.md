# Jammer

## Funktion & Rolle
Stört feindliche Sichtweite und Kommunikation im Umkreis. Asymmetrische
Elektronik-Waffe gegen Aufklärung. Handbuch §9.1.

## Vision / Stimmung
Chaotisch-elektronisch. Wirkt wie ein zusammengebasteltes, experimentelles
Störgerät mit wilden Antennen in alle Richtungen. Soll das Gegenteil der
geordneten Control-Projector-Ästhetik sein. Unberechenbar, "piept und
zuckt".

## Silhouette
Unregelmäßiger Bau mit einer **unübersichtlichen Menge von Antennen**
verschiedener Größen und Winkel. Keine Symmetrie. Ein zentraler dicker
Kabel-Knoten in der Mitte. Dach mit schrägen Platten.

## Materialien & Farben
- **Basis:** Stein-dunkel (`#5a5c5e`) grober Sockel
- **Gehäuse:** Metall mit Blech-Patchwork
- **Antennen:** dunkles Metall, unterschiedlich lang und dick
- **Kabel-Bündel:** schwarz mit violett-War-Rot-Isolierstreifen
- **LEDs:** chaotisch verteilt, War-Rot + violett blinkend
- **Warnmarkierungen:** gelb-schwarz

## Ausbaustufen

### Stage 1 — Störgerät (2 Anchors)
Kompakter Kubus mit drei bis vier Antennen in verschiedene Richtungen.
Einfach, fast improvisiert.

### Stage 2 — Antennenfeld (4 Anchors)
Bau wird breiter, acht bis zehn Antennen, chaotisch verteilt. Einige
Antennen schief, einige spiralförmig.

### Stage 3 — Chaos-Antennen-Garten (6 Anchors)
Großer Bau mit zwölf bis fünfzehn Antennen verschiedenster Formen, ein
paar rotieren, ein paar blinken unkontrolliert. Wirkt wie eine
verrückte Wissenschaftler-Station.

## Pipe-Anchors
Anchors sind **schwere Kabel-Eingänge** — sichtbar als **dicke Kabel-
Bündel, die in die Wand münden**, mit einem Flansch-Übergang.

- Stage 1: `anchor_0`, `anchor_3` (y≈0.2)
- Stage 2: +`anchor_1`, `anchor_4`
- Stage 3: alle 6

## Schornsteine & Emissionen
- **Kein Schornstein.**
- **Keine Kontaminations-Emission.**
- **Emission-Glow:**
  - **Chaotische LED-Blinker** an den Antennenspitzen — jede in
    anderem Rhythmus, War-Rot und violett
  - Gelegentliche **violette Blitz-Arcs** zwischen benachbarten
    Antennen (Shader-Noise gesteuert)
  - Kabel-Bündel pulsieren unregelmäßig

## Animationen

### Ambient (läuft immer)
- Einzelne Antennen zucken/drehen ungleichmäßig (Shader mit Noise-
  Input, simuliert Störsender)
- LED-Flackern überall (Shader-Noise)
- Stage 2+3: gelegentliche Shader-Blitze zwischen Antennen

### State-gekoppelt
- **Bei aktivem Jamming:** Blitz-Arcs **permanent und intensiv**,
  kleine violette Partikel-Wolken (`emitter_sparks` violett getönt),
  alle Antennen zucken kräftiger, schriller LED-Rhythmus
- **Bei Gegner-Detection:** Alle LEDs wechseln kurz zu gleichförmigem
  War-Rot-Puls (Warnung)

## Condition-Varianten

### Condition 100
Chaotisch, aber funktional — LEDs blinken, Antennen stehen aufrecht.

### Condition 50
Zwei Antennen abgebrochen, mehrere LEDs kaputt, ein Kabel-Bündel
hängt lose mit Funken-Partikeln.

### Condition ruin
Bau zusammengestürzt, Antennen umgefallen und zerbrochen, Kabel
gebrochen mit Funken-Ausfall, keine LEDs mehr.

## Condition × Stage Matrix
Grundsockel konstant, Antennen-Anzahl wächst — aber die "Ordnung" der
Antennen nimmt ab (Stage 3 ist am chaotischsten). Ruin lässt Antennen
fallen; genauso charakteristisch wie das funktionierende Chaos.

→ Artist-Tipp: **Bewusst unsymmetrisch modellieren.** Ungleiche
Antennen-Längen, verschiedene Winkel — das ist das visuelle Gegenstück
zum Control Projector.

## Umgebungsinteraktion
- Gelegentliche violette Blitze im Umkreis (Partikel-Effekt).
- Muss auf War-Seite-Terrain stehen.
- Bei Nacht beunruhigend durch chaotisches Licht.

## Gameplay-Hinweise
- **Tier:** 1 (War-Seite)
- **Radius:** 1 Hex
- **Rolle:** Stört Feindsicht und Kommunikation
- Handbuch-Referenz: §9.1 Jammer
