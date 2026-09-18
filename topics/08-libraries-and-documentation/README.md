# Knihovny a dokumentování kódu

Knihovny umožňují stavět na práci ostatních místo opakovaného řešení stejných
problémů. V této lekci se naučíme knihovnu najít, bezpečně nainstalovat do
izolovaného prostředí, pracovat s její dokumentací a dokumentovat vlastní kód.

## Prerekvizity

- Základní orientace v terminálu a práce se soubory
  ([předchozí téma](../07-file-handling-and-file-io/README.md))
- Funkce, moduly, datové typy a ošetření běžných chyb

## Cíle

- Rozlišit modul, balíček, knihovnu a závislost.
- Vyhledat balíček na PyPI a ověřit jeho dokumentaci a způsob instalace.
- Vytvořit a aktivovat virtuální prostředí pomocí `venv`.
- Instalovat balíčky pomocí `python -m pip` a zaznamenat závislosti.
- Použít dokumentaci knihovny k vyřešení konkrétní úlohy.
- Psát výstižné docstringy a typové nápovědy veřejných funkcí.

## Přednáška

Slajdy zatím nejsou k dispozici.

- [Komentované příklady: knihovny a dokumentování kódu](seminar/seminar.md)

Komentované příklady pokrývají konflikt závislostí, vytvoření virtuálního
prostředí, reprodukci závislostí, orientaci v dokumentaci a doplnění
docstringů a typových nápověd.

## Domácí příprava

[Zadání domácí přípravy: průzkum knihoven na PyPI](prework/README.md)

## Cvičení

Samostatně vytvoříte malý nástroj příkazové řádky nad knihovnou `click`,
budete pracovat s její dokumentací a připravíte projekt spustitelný v čistém
virtuálním prostředí.

[Zadání cvičení](lab/assignment.md)

## Zdroje

- [Python Tutorial: Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html)
- [Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/installing-packages/)
- [Python Package Index (PyPI)](https://pypi.org/)
- [PEP 257 — Docstring Conventions](https://peps.python.org/pep-0257/)
- [Python dokumentace: `typing`](https://docs.python.org/3/library/typing.html)
