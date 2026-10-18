# Knihovny a dokumentování kódu

Knihovny umožňují stavět na práci ostatních místo opakovaného řešení stejných
problémů. V této lekci se naučíme knihovnu najít a nainstalovat, pracovat s její
dokumentací a dokumentovat vlastní kód.

## Prerekvizity

- Základní orientace v terminálu a práce se soubory
  ([předchozí téma](../07-file-handling-and-file-io/README.md))
- Funkce, moduly, datové typy a ošetření běžných chyb

## Cíle

- Rozlišit modul, balíček, knihovnu a závislost.
- Vytvořit vlastní balíček s několika spolupracujícími moduly a veřejným rozhraním.
- Vyhledat balíček na PyPI a ověřit jeho dokumentaci a způsob instalace.
- Instalovat balíčky pomocí `python -m pip` a zaznamenat závislosti.
- Použít dokumentaci knihovny k vyřešení konkrétní úlohy.
- Psát výstižné docstringy a typové nápovědy veřejných funkcí.

## Přednáška

- [Prezentace](lecture/presentation.pdf)

- [Komentované příklady: knihovny a dokumentování kódu](seminar/README.md)


## Domácí příprava

[Zadání domácí přípravy: průzkum knihoven na PyPI](prework/README.md)

## Cvičení

Samostatně vytvoříte vlastní knihovnu `textkit`. Začnete dvěma jednoduchými
funkcemi a postupně přidáte analýzu slov, veřejné rozhraní balíčku, práci se
soubory, docstringy a dokumentaci. Nakonec nad knihovnou vytvoříte tenké
příkazové rozhraní pomocí Clicku.

[Zadání cvičení](lab/assignment.md)

## Zdroje

- [Python Tutorial: Modules](https://docs.python.org/3/tutorial/modules.html)
- [Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/installing-packages/)
- [Python Package Index (PyPI)](https://pypi.org/)
- [PEP 257 — Docstring Conventions](https://peps.python.org/pep-0257/)
- [Python dokumentace: `typing`](https://docs.python.org/3/library/typing.html)
