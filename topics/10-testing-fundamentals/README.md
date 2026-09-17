# Základní principy testování

Kód, který funguje „na první pohled", ještě nemusí být správný. Tato lekce
ukazuje, jak správnost **ověřovat automaticky** — pomocí testů. V době AI
je to dvojnásob důležité: testy jsou způsob, jak zadat AI přesnou specifikaci
a jak zkontrolovat, že vygenerovaný kód opravdu dělá, co má.

## Prerekvizity

- Funkce — definice, volání, výjimky
  ([téma Funkce](../05-functions-definition-invocation-and-scope/README.md))
- Základy objektově orientovaného programování
  ([téma Úvod do OOP](../06-introduction-to-object-oriented-programming/README.md))
- Práce se soubory a instalace knihoven přes pip
  ([Práce se soubory](../file-handling-and-file-io/README.md),
  [Používání knihoven](../libraries-and-documentation/README.md))

## Cíle

- Napsat kontrolní výraz pomocí `assert` a spustit testy pytestem.
- Strukturovat test podle vzoru Arrange–Act–Assert.
- Navrhnout testy pro hraniční případy (prázdné vstupy, nuly, hranice pásem).
- Otestovat chybové stavy pomocí `pytest.raises`.
- Porovnávat desetinná čísla pomocí `pytest.approx`.
- Otestovat třídu včetně změn jejího stavu.
- Použít testy jako specifikaci pro AI a posoudit kvalitu vygenerovaného kódu.

## Přednáška

[Výkladový notebook](lecture/testing-fundamentals.ipynb) — od `assert`
přes pytest, edge cases, výjimky a testování tříd až po fixtures.
Slouží i k samostudiu před cvičením.

## Domácí příprava

[Pre-work notebook](prework/prework.ipynb) — 4 úkoly (40–50 minut).
Výstupem je soubor `test_prework.py`, který se odevzdává do Moodlu
před začátkem cvičení.

## Seminář

_Zadání připravujeme_ — [úlohy na seminář](seminar/README.md).

## Cvičení

Kolektivní Red Team: celá skupina nejprve prolamuje záměrně slabou testovací
sadu, pak ji společně zpevňuje a nakonec dokončuje třídu `ScoreTracker`
z domácí přípravy.

[Notebook na cvičení](lab/lab-session.ipynb) —
pro vyučující je k dispozici [průvodce cvičením](TEACHING-GUIDE.md).

## Zdroje

- [pytest dokumentace](https://docs.pytest.org/) — oficiální dokumentace frameworku
- [Real Python: Getting Started With Testing in Python](https://realpython.com/python-testing/) — podrobný tutoriál
- [Python Tutorial: Floating Point Arithmetic](https://docs.python.org/3/tutorial/floatingpoint.html) — proč `0.1 + 0.2 != 0.3`
