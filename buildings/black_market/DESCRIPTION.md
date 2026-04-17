# Black Market

## Funktion & Rolle
Spielergebauter Escrow für grauen Handel. Günstig (400 Build) und
schnell abreißbar — der Escrow ist ein realer Spieler, der auch
betrügen kann. Hohes Risiko, hohe Belohnung. Handbuch §8.1.

## Vision / Stimmung
Improvisiert, zwielichtig, halb-illegal. Wirkt wie ein
zusammengezimmerter Hinterhof-Schuppen, fast heruntergekommen schon
bei Stage 1. Bewusst gegen den sauberen Stil der anderen Economy-
Gebäude designt. Kontrast zum Trading Post — hier ist nichts
offiziell.

## Silhouette
Unregelmäßiger, leicht schiefer Holzverschlag mit Plane drüber. Kein
symmetrisches Design — wirkt wie aus Resten gebaut. Rostige
Blechdach-Abdeckung, verhülltes Schild ("?") an der Front.

## Materialien & Farben
- **Holz:** Holz-dunkel (`#5c4710`) dominant, verwittert
- **Plane:** Grass-dunkel verblasst bis gräulich
- **Blech:** verrostete Metallteile
- **Akzente:** kleines War-Rot-LED am Schild (gedimmt)
- **Keine** hellen Farben, keine sauberen Akzente — alles muted

## Ausbaustufen

### Stage 1 — Bretterverschlag (2 Anchors)
Einfacher Hütten-Torso aus ungleichen Brettern, Blechdach schief
aufgelegt, zwei dunkle Eingänge mit Vorhang-Plane. Kein Fenster.

### Stage 2 — Zwei-Schuppen-System (4 Anchors)
Zweiter Verschlag dahinter, mit Durchgang dazwischen. Vier Vorhang-
Eingänge. Rostige Blechkisten vor dem Eingang gestapelt.

### Stage 3 — Hinterhof-Netzwerk (6 Anchors)
Drei miteinander verbundene Schuppen in loser Anordnung, mit
überdachtem Innenhof in der Mitte. Keine eindeutige "Front" mehr —
sechs unauffällige Eingänge. Eine kaputte Straßenlaterne über dem
Innenhof flackert.

## Pipe-Anchors
Anchors sind **tiefhängende, gedeckte Lade-Öffnungen** — nicht
auffällig markiert. Jeweils mit einer Stoffplane halb verhängt,
verrostete Rohrstummel statt Flansche.

- Stage 1: `anchor_0`, `anchor_3` (y≈0.2, halb im Boden)
- Stage 2: +`anchor_1`, `anchor_4`
- Stage 3: alle 6

## Schornsteine & Emissionen
- **Kein Schornstein** — aber eine kleine Lüftungsöffnung mit dünnem
  grauen Rauchfaden (`emitter_smoke` sehr reduziert, fast idle)
  suggeriert Aktivität.
- **Keine Kontaminations-Emission** (Gameplay-seitig neutral).
- **Emission-Glow:** minimal. Stage 3: Laterne über dem Innenhof
  flackert unruhig (War-Rot + Warnung gemischt). Einzelne Kerzen-LEDs
  an Eingängen (warm-rot, sehr gedimmt).

## Animationen

### Ambient (läuft immer)
- Vorhänge an den Eingängen wehen unregelmäßig (Shader, stärker als
  bei anderen Gebäuden — suggeriert "Zug durchs Gebäude")
- Stage 3: Laterne flackert mit zufälligem Shader-Noise
- Blechdach-Ecken klappern minimal (Shader)

### State-gekoppelt
- **Bei aktivem Trade:** kurze War-Rot-LED-Pulse an den Eingängen
  (jemand hebt den Vorhang → Emission-Blinzeln), dünner grauer Rauch
  aus der Lüftung stärker.
- **Bei Betrug / Escrow-Bruch:** War-Rot-Puls an allen Eingängen,
  kleiner `emitter_sparks` — visuelles Alarm-Signal.

## Condition-Varianten

### Condition 100
"Frisch" gebaut — Bretter neu, aber bewusst schief verbaut. Plane
noch nicht löchrig. So intakt wie ein Black Market überhaupt sein kann.

### Condition 50
Plane eingerissen, Bretter gesplittert, ein Vorhang fehlt komplett.
Blechdach hat sichtbare Löcher.

### Condition ruin
Kollabiert fast vollständig. Dach eingefallen, ein Verschlag liegt
zur Seite, Kisten umgeworfen. Gras und Moos überwuchern die Reste.

## Condition × Stage Matrix
Grundverschlag bleibt über Stufen als Kern, andere Schuppen werden
drangebaut. Condition-Degradation ist hier fließender — auch 100 sieht
schon "gebraucht" aus.

→ Artist-Tipp: Hier darf und soll unsauber modelliert werden —
leicht schiefe Bretter, asymmetrische Dächer, keine geraden Winkel.
Das visuelle Gegenstück zum Trading Post.

## Umgebungsinteraktion
- Kein Stein-Fundament, sitzt direkt auf dem Hex-Boden. Schlamm-Spuren
  um die Eingänge.
- Deko-Details: leere Flaschen, aufgewühlte Erde, eine Schubkarre.
- Keine Terrain-Präferenz.

## Gameplay-Hinweise
- **Tier:** 1
- **Radius:** 1 Hex
- **Build-Cost:** 400
- **Abriss:** schnell, billig — Design wirkt "wegwerfbar"
- **Rolle:** Escrow ist realer Spieler; Betrugsrisiko eingebaut
- Handbuch-Referenz: §8.1 Black Market
