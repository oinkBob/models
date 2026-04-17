# {Building Name}

> Template. Kopiere dieses Dokument nach `assets/buildings/{name}/DESCRIPTION.md`
> und fülle alle Sektionen aus. Siehe `assets/STYLE_GUIDE.md` für die
> allgemeinen Regeln.

## Funktion & Rolle
Ein bis zwei Sätze: was tut das Gebäude im Spiel? Referenz auf das
Handbuch (`docs/Molanex_Handbuch_v3.1.md` §8.x).

## Vision / Stimmung
2–3 Sätze Prosa. Welchen Eindruck hinterlässt das Gebäude? Freundlich,
industriell, bedrohlich, geheimnisvoll? Welche Assoziation soll der
Spieler auf 100m Distanz haben?

## Silhouette
Grundform und Proportionen. Das Gebäude muss allein anhand seiner
Silhouette erkennbar sein — auch auf Distanz, auch bei Dämmerung.
Beschreibe die charakteristische Form (Kegel, Turm, Kuppel, Halle, ...).

## Materialien & Farben
- Welche Material-Anteile (Holz / Metall / Stein / Glas / Kristall)?
- Hauptfarben aus der Palette (§5 STYLE_GUIDE)
- Akzentfarben (Emissive, Warnung, Gebäude-spezifisch)

## Ausbaustufen (Stage 1 / 2 / 3)

### Stage 1 — Funktional (2 Pipe-Anchors)
Klein, reduziert, wie ein Prototyp oder Erstausbau. Beschreibe die Form.

### Stage 2 — Ausgebaut (4 Pipe-Anchors)
Erkennbar erweitert — zusätzliche Anbauten, zweites Stockwerk, mehr
Röhren, sichtbare Funktionalität. Was kommt dazu?

### Stage 3 — Voll ausgebaut (6 Pipe-Anchors)
Imposant und visuell markant. Wie sieht die "Meisterstufe" aus?
Was macht sie unverwechselbar?

## Pipe-Anchors
Exakte Position und Ausführung pro Stufe. Jeder Anchor muss visuell
markiert sein (Flansch, Ventil, Kupplung, Röhren-Ende).

- **Stage 1:** anchor_0 (Ost), anchor_3 (West) — wo am Modell?
- **Stage 2:** +anchor_1, anchor_4 — wo?
- **Stage 3:** +anchor_2, anchor_5 — wo?

## Schornsteine & Emissionen
- Anzahl und Position der Schornsteine (`emitter_smoke`)
- Rauchfarbe (dunkelgrau, weiß, giftgrün, ...)
- Kontaminations-Beitrag: ja/nein (Gameplay-seitig)
- Emission-Glow: welche Teile leuchten? Welche Farbe (flow-grün,
  heat-orange, shield-blau, war-rot)?
- Andere Emitter (`emitter_sparks`, `emitter_haze`)?

## Animationen

### Ambient (läuft immer)
- `anim_*`-Node-Namen + Beschreibung (Rotor dreht 0.5 rad/s, Pump
  oszilliert, Flagge wiegt)
- Shader-Anims (wenn Flaggen, Kleinteile im Wind)

### State-gekoppelt (nur bei aktivem Server-State)
- Bei Produktion: welche Partikel/Emission aktiv?
- Bei aktivem Flow: welche Pipe-Teile leuchten?
- Bei Alarm/Schaden: visuelles Feedback?
- Bei Kontamination: wie sichtbar?

## Condition-Varianten

### Condition 100 (intakt)
Sauber, neu gestrichen, alle Teile funktionsfähig, leichter Glanz.

### Condition 50 (beschädigt)
Rost, Risse, abblätternde Farbe, fehlende Kleinteile, gedämpfte Farben.
Grundsilhouette bleibt erkennbar.

### Condition ruin (zerfallen)
Kollabiert, überwuchert, Teile fehlen komplett, Vegetation wächst
durch. Für den Spieler klar als "funktioniert nicht mehr" lesbar.

## Condition × Stage Matrix
Was bleibt konstant über Stufen (Grundsilhouette, Fundament), was
ändert sich mit den Ausbaustufen? Hinweise für effizientes Modellieren
(gemeinsame Basis-Mesh wiederverwenden).

## Umgebungsinteraktion
- Wie steht es im Terrain? Fundament, eingegraben, schwebend?
- Interagiert es mit dem Boden (Röhren ins Terrain, Bodenplatten)?
- Bevorzugtes Terrain (wenn Gameplay-relevant, aus Handbuch)?
- Lokale Umwelt-Effekte (Bodennebel, Wärmeflimmern, etc.)?

## Gameplay-Hinweise
- Radius (R=1/2/3)
- Build-Cost, Upkeep (aus Handbuch)
- Gameplay-Rolle kurz zusammengefasst
- Handbuch-Referenz: §8.x
