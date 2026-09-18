# Práce se soubory — čtení a zápis

Soubory dovolují programu načítat vstupy a uchovat výsledky i po jeho
ukončení. V této lekci se zaměříme na bezpečnou práci s textovými soubory,
kódování, cesty a základní ošetření chyb.

## Prerekvizity

- Funkce, parametry a návratové hodnoty
  ([téma Funkce](../05-functions-definition-invocation-and-scope/README.md))
- Třídy a objekty
  ([téma Úvod do OOP](../06-introduction-to-object-oriented-programming/README.md))
- Řetězce, seznamy, cykly a podmínky

## Cíle

- Bezpečně otevírat a zavírat soubory pomocí `with`.
- Rozlišit režimy čtení, zápisu, přidávání a binární režim.
- Číst text po řádcích a zapisovat výsledky programu.
- Pracovat s kódováním UTF-8 a cestami pomocí `pathlib`.
- Ošetřit chybějící soubor a další očekávatelné chyby vstupu.
- Oddělit načtení dat, jejich zpracování a zápis výsledku.

## Přednáška

Slajdy zatím nejsou k dispozici.

- [Komentované příklady: práce se soubory](seminar/seminar.md)

Komentované příklady procházejí životní cyklus souboru, režimy otevření,
čtení po řádcích, UTF-8, ošetření chyb a práci s cestami. Navazující ukázky
vytvoří jednoduchý deník a textový výstup pro jiný program.

## Domácí příprava

[Zadání domácí přípravy: analýza osobního poznámkového souboru](prework/README.md)

## Cvičení

Samostatná práce začíná analýzou textu a postupně přechází k deníku,
zpracování měření, bezpečným cestám, generování SVG a práci s binárními daty.

[Zadání cvičení](lab/assignment.md)

## Zdroje

- [Python Tutorial: Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Python dokumentace: `pathlib`](https://docs.python.org/3/library/pathlib.html)
- [Python dokumentace: `io`](https://docs.python.org/3/library/io.html)
