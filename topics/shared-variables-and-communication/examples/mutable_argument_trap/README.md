# Záludnost mutabilních argumentů

Tento příklad ukazuje dvě časté chyby způsobené tím, že Python předává
mutabilní objekty (seznamy, slovníky) **odkazem**, nikoli kopií.

## Pravidlo

> Funkce by neměla měnit obsah argumentů, které dostane, pokud to není
> jejím výslovným účelem.

Toto pravidlo vychází z principu **čistých funkcí** (pure functions):
funkce, která vrací hodnotu, by neměla mít vedlejší efekty na svých vstupech.

Python ho demonstruje na vlastním standardním rozhraní:
- `sorted(items)` — vrátí **nový** seřazený seznam, původní nezmění
- `items.sort()` — seřadí seznam **na místě**, vrátí `None`

Pokud vaše funkce vrací hodnotu, zacházejte s argumenty jako se vstupem
pouze ke čtení.

## Spuštění

```bash
python main.py
```

## Chyba 1: Mutabilní výchozí parametr

Výchozí hodnota parametru se vyhodnotí **jednou při definici funkce**,
ne při každém volání. Pokud je výchozí hodnotou seznam nebo slovník,
všechna volání bez tohoto argumentu sdílejí ten samý objekt.

## Chyba 2: Nechtěná modifikace argumentu

Funkce, která dostane seznam a zavolá na něm `.sort()`, změní i původní
seznam volajícího — aniž by to bylo zřejmé z její signatury nebo názvu.
