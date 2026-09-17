# Práce se soubory: čtení ze souborů a zápis do souborů

## Cíle

- Bezpečně otevírat, číst a zapisovat soubory.
- Používat kontextové manažery pro správu prostředků.
- Ošetřovat běžné chyby při práci se soubory a problémy s kódováním.

Příklad: jednoduchý zápis a čtení

```python
with open('data.txt', 'w', encoding='utf-8') as f:
    f.write('Hello\n')

with open('data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())
```

## Klíčová slova

Soubory, IO

## Přednáška

TODO: odkaz na online prezentaci (typy souborů, encoding?)

## Seminář

Studenti se naučí praktickou práci se souborovým vstupem/výstupem: čtení a zápis textových i binárních souborů, používání kontextových manažerů a bezpečné zacházení s kódováním a chybami. Součástí jsou také běžné vzory pro logování dat a jednoduchou perzistenci založenou na souborech.

Podklady:

- [Seminář](seminar.md)


## Cvičení

Úkol pro domácí přípravu je [zde](assignment.md).

Úkoly pro cvičení budou ukázány na hodině.



## Zdroje

- [Python dokumentace: File I/O](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
