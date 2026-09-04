# Datové typy a vstup/výstup

Tato lekce se ptá, **co hodnota v programu znamená a jak je uložená**.
Podíváme se, jak počítač pracuje s bity a bajty, jaké základní datové typy
nabízí Python a jak program komunikuje s okolím pomocí vstupu a výstupu.

## Prerekvizity

- Schopnost používat Git
- Nastavené IDE pro psaní a spouštění Pythonních programů
- Základy algoritmizace — pseudokód a vývojové diagramy
  ([předchozí téma](../algorithm-design-basics/README.md))

## Cíle

- Vysvětlit, jak počítač ukládá čísla a text pomocí bitů a bajtů.
- Rozpoznat a používat základní datové typy Pythonu
  (`int`, `float`, `bool`, `str`, `None`).
- Vědět, proč desetinná čísla nejsou uložena přesně, a počítat s tím.
- Vědomě převádět hodnoty mezi typy.
- Načíst vstup od uživatele a vypsat výsledek.
- Vybrat vhodný kontejner (`list`, `tuple`, `set`, `dict`) pro daná data.

## Přednáška

[Prezentace: Datové typy a vstup/výstup](lecture/presentation.pdf)

## Domácí příprava

_Připravujeme_ — [zadání domácí přípravy](prework/README.md).

## Seminář

Na semináři si vyzkoušíme, co se v paměti opravdu děje: jak se chová
celočíselné dělení, kde vzniká zaokrouhlovací chyba u `float`, proč
`"5" + 5` skončí chybou a jak správně použít `int()`, `float()` nebo `str()`.
Dále projdeme čtyři základní kontejnery a jejich typické použití.

_Zadání připravujeme_ — [úlohy na seminář](seminar/README.md).

## Cvičení

Samostatná práce s malými programy, které něco načtou, převedou a vypíšou.

_Zadání připravujeme_ — [zadání cvičení](lab/assigments.md).

## Zdroje

- [Dokumentace Pythonu: Built-in Types](https://docs.python.org/3/library/stdtypes.html) — přehled všech základních typů
- [Dokumentace Pythonu: Floating Point Arithmetic](https://docs.python.org/3/tutorial/floatingpoint.html) — proč `0.1 + 0.2 != 0.3`
- [Python Tutorial: Input and Output](https://docs.python.org/3/tutorial/inputoutput.html) — formátování výstupu
