# Práce se soubory: čtení ze souborů a zápis do souborů

## Cíle

- Bezpečně otevírat, číst a zapisovat soubory.
- Používat kontextové manažery pro správu prostředků.
- Ošetřovat běžné chyby při práci se soubory a problémy s kódováním.

## Klíčová slova

Soubory, IO

## Přednáška

TODO: odkaz na online prezentaci (typy souborů, encoding?)

## Seminář

Studenti se naučí praktickou práci se souborovým vstupem/výstupem: čtení a zápis textových i binárních souborů, používání kontextových manažerů a bezpečné zacházení s kódováním a chybami. Součástí jsou také běžné vzory pro logování dat a jednoduchou perzistenci založenou na souborech.

### Osnova

1. Otevírání souborů a režimy
2. Čtení vs. zápis, textové a binární soubory
3. Kontextové manažery (`with`)
4. Kódování a práce s konci řádků
5. Ošetření chyb a cesty k souborům

## Cvičení

- Převeďte textem zapsaný "strom" na souborů složek a souborů (soubory budou listy)
- Vyzkoušejte si práci s virtuálními soubory (buffery)
- Stáhněte si zazipovaný balíček, rozbalte ho v paměti a nakreselte stromovou strukturu obsahu

Příklad: jednoduchý zápis a čtení

```python
with open('data.txt', 'w', encoding='utf-8') as f:
    f.write('Hello\n')

with open('data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())
```

## Zdroje

- [Python dokumentace: File I/O](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
