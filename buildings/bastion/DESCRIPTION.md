# Bastion

## Funktion & Rolle
Massive Festung. Bei Vollendung wird sie zum **Welt-Wunder** und
setzt ein server-weites Signal. Eines der teuersten Gebäude im Spiel.
Handbuch §9.3.

## Vision / Stimmung
Monumental, symbolisch, weithin sichtbar. Soll "hier steht etwas
Bedeutendes" ausstrahlen — das "Lebenswerk" eines Spielers/einer Gilde.
Mächtiger als jedes andere War-Gebäude, mit einer Aura von
Unverwüstlichkeit.

## Silhouette
**19-Hex-Fläche** (R=3). **Gigantische Festungsanlage** mit:
- Zentralem **Hauptturm** (sehr hoch, ca. 5 Units, alles andere
  überragend)
- Vier **Ecktürmen** mit Zinnen
- **Wehrmauern** dazwischen, auf denen Wachposten laufen
- Großem **Tor-Komplex** als Eingang
- **Wachfeuern** in Eisenkörben auf den Zinnen

Auf 50+ Hex erkennbar. Größte Silhouette des Spiels außerhalb der
Exchange.

## Materialien & Farben
- **Mauern und Türme:** Stein-hell (`#808286`) + Stein-dunkel
  (`#5a5c5e`) Wechsel (Quaderwerk)
- **Fundament:** Stein-dunkel massiv
- **Tore:** Metall schwer mit Harvester-Gelb Beschlägen
- **Dächer:** War-Rot Schindeln
- **Fahnen:** War-Rot mit Spielerfarbe-Tönung (Runtime)
- **Wachfeuer:** Heat-Orange Emission (`emitter_sparks`)
- **Hauptturm-Spitze:** Kristall-Element für den World-Wonder-Strahl
  (Shield-Blau + Flow-Grün Mischung)

## Ausbaustufen

### Stage 1 — Kernturm + Fundament (2 Anchors)
Großes Stein-Fundament (voller R=3 Footprint schon vorhanden),
**zentraler Kernturm** mit Zinnen, erste Fundamente der Mauern
angedeutet. Wirkt wie eine Baustelle, die bereits mächtig ist.

### Stage 2 — Mauern + Ecktürme (4 Anchors)
Vollständige Wehrmauern, zwei der vier Ecktürme fertig, Tor-Komplex
im Bau sichtbar, erste Wachfeuer an den Mauern.

### Stage 3 — Volle Festung (6 Anchors)
**Alle vier Ecktürme**, **vollständige Wehrmauern** mit Zinnen, **großer
Tor-Komplex** mit Fallgitter sichtbar, **Hauptturm** wird höher und
bekommt eine **Kristall-Krone** (für den World-Wonder-Strahl), Wachfeuer
an allen Zinnen. Imposant.

## Pipe-Anchors
Anchors sind **gepanzerte Tore in den Mauern** — **breite
Flansch-Portale** mit sichtbarem Fallgitter darüber. Sehen aus wie
militärische Kasernen-Tore.

- Stage 1: `anchor_0`, `anchor_3` am Fundament (y≈0.3)
- Stage 2: +`anchor_1`, `anchor_4`
- Stage 3: alle 6 rundum (je einer pro Hex-Kante des äußeren Rings)

## Schornsteine & Emissionen
- **Kein klassischer Schornstein** — aber die Wachfeuer-Körbe
  produzieren dünnen grauen Rauch (`emitter_smoke` × 6–12 je nach
  Stufe).
- **Keine Kontaminations-Emission.**
- **Emission-Glow:**
  - Wachfeuer-Körbe: Heat-Orange pulsierend (Shader-Noise), sehr
    warm-einladend trotz militärischem Kontext
  - Fenster in Mauern und Türmen: warmweiß bei Nacht
  - Kristall-Krone am Hauptturm (Stage 3): **pulsiert permanent**
    Shield-Blau + Flow-Grün Mischung

## Animationen

### Ambient (läuft immer)
- Fahnen auf Ecktürmen Shader-Wind (viele Fahnen, verschieden groß)
- Wachfeuer Shader-Flacker
- Stage 3: Kristall-Krone hat langsam rotierendes Element
  (`anim_spin_y`, 0.15 rad/s)
- **Wachposten-Silhouetten** auf den Mauern bewegen sich langsam
  (procedural auf festen Bahnen — stilisiert, nicht realistisch)

### State-gekoppelt
- **Bei Bastion-Vollendung (Stage 3, Condition 100):** großer
  einmaliger Event-Effekt — **World-Wonder-Strahl** schießt senkrecht
  in den Himmel aus der Kristall-Krone, sichtbar inselweit, ca. 5s
  lang, dann Permanent-Status: Krone leuchtet etwas stärker als Ambient
- **Bei Belagerung / Schaden:** Wachfeuer flackern schnell, `emitter_sparks`
  War-Rot an Einschlag-Stellen
- **Bei Alarm:** Tor-Fallgitter senkt sich (procedural)

## Condition-Varianten

### Condition 100
Stein makellos, Fahnen frisch, Wachfeuer hell, Kristall-Krone leuchtend.

### Condition 50
Einzelne Steine aus Mauern gebrochen, Fahnen zerfetzt, ein Eckturm
beschädigt, zwei Wachfeuer erloschen.

### Condition ruin
Zwei der Ecktürme kollabiert, Hauptturm in der Mitte gebrochen,
Mauern an mehreren Stellen eingestürzt, kein Feuer, Kristall-Krone
zerbrochen. Tragisch — der Verlust eines Welt-Wunders.

## Condition × Stage Matrix
Fundament und Zentralturm-Basis konstant. Ecktürme, Mauern, Tor und
Kristall-Krone wachsen mit Stufen. Ruin ist besonders dramatisch bei
Stage 3 (gefallenes Welt-Wunder).

→ Artist-Tipp: Modular bauen — Mauersegmente, Ecktürme, Tor-Komplex
als separate wiederverwendbare Meshes.

## Umgebungsinteraktion
- Erhöhtes Stein-Plateau (0.3 Units über Boden).
- **Blutige Kiesel** / Kampf-Reste auf dem Boden davor (Textur-Deko).
- Bei Nacht sehr auffällig durch Wachfeuer und Kristall-Krone.
- Muss auf War-Seite-Terrain stehen (Gameplay).
- Bei World-Wonder-Status: globales Partikel-System über die ganze
  Insel legt sich (subtiler Glow im Himmel in Richtung Bastion).

## Gameplay-Hinweise
- **Tier:** 3 (War-Seite)
- **Radius:** 3 Hex (19-Hex-Footprint)
- **Build-Cost:** 50000
- **Sondermerkmal:** Bei Vollendung → Welt-Wunder-Status, inselweiter
  Effekt
- Handbuch-Referenz: §9.3 Bastion
