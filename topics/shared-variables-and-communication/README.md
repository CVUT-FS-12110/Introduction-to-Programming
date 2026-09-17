# Sdílené proměnné a komunikace mezi částmi programu

## Prerekvizity

- Funkce — parametry, návratové hodnoty, lokální scope (téma 5)
- Základy OOP — třídy a atributy instancí (téma 6)

## Cíle

- Vysvětlit rozdíl mezi lokálním a globálním stavem a důsledky jejich sdílení.
- Předávat data mezi částmi programu explicitně pomocí parametrů a návratových hodnot.
- Rozpoznat záludnosti mutabilních argumentů v Pythonu a naučit se jim vyhýbat.
- Modelovat sdílený stav pomocí třídy jako alternativu ke globálním proměnným.

## Klíčová slova

TODO

## Přednáška

TODO: odkaz na online prezentaci

## Seminář

TODO

Podpůrné příklady:

1. [Problém globálního stavu](examples/global_variable_problem/README.md)
1. [Explicitní předávání stavu](examples/explicit_state_passing/README.md)
1. [Záludnost mutabilních argumentů](examples/mutable_argument_trap/README.md)
1. [Sdílený stav ve třídě](examples/shared_state_with_class/README.md)

### Osnova

1. Co je stav programu — co si program „pamatuje"
1. LEGB — pravidla viditelnosti proměnných v Pythonu
1. Problémy globálního stavu — skryté závislosti, testovatelnost
1. Explicitní předávání dat (parametry, návratové hodnoty)
1. Mutabilní vs. imutabilní typy — sdílení referencí v Pythonu
1. Záludnost mutabilních výchozích parametrů
1. Třída jako nosič stavu
1. Zmínka: souběžnost a sdílený stav (nad rámec kurzu)

## Cvičení

1. [Domácí příprava a úkoly](tasks/tasks.md)

## Zdroje

- TODO
