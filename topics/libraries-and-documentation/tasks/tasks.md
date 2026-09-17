# Instrukce ke cvičení

Vaším úkolem je samostatně najít, nainstalovat a použít knihovnu třetí strany.
Pracujte vždy v aktivovaném virtuálním prostředí.

## Organizace práce

- Máte čas omezený trváním cvičení.
- Úloh je více – **vaším cílem je vyřešit jich co nejvíce**.
- Začněte od první (nejjednodušší) a pokračujte dále podle obtížnosti.

## Důležité

- Veškerá práce probíhá uvnitř virtuálního prostředí (`venv`).
- Po dokončení úloh zmrazte závislosti do `requirements.txt`.
- Kód musí být spustitelný příkazem `python main.py ...` z terminálu.

---

## Domácí příprava

Před cvičením si na [PyPI](https://pypi.org) najděte **dvě libovolné knihovny**, které vás zaujmou.
Pro každou si poznamenejte:
- Co knihovna dělá (jednou větou)
- Jak se nainstaluje
- Kdy byla naposledy aktualizována a kolik má stažení
- Důvod proč vás zaujala

Přijďte připraveni o svých knihovnách říct ostatním.

---

## Zadání úloh

### Úloha 1 — Najdi a nainstaluj knihovnu

Dostáváš pouze odkaz na GitHub repozitář knihovny:
👉 https://github.com/pallets/click/

Tvým úkolem je:
1. Zjistit název balíčku na [PyPI](https://pypi.org)
2. Vytvořit virtuální prostředí a aktivovat ho
3. Nainstalovat knihovnu pomocí `pip`
4. Ověřit instalaci pomocí `pip list`
5. Zmrazit závislosti do `requirements.txt`

### Úloha 2 — První CLI příkaz

Napiš skript `main.py`, který pomocí knihovny `click` vytvoří jednoduchý CLI nástroj.

Nástroj musí:
- přijmout argument `--name` (jméno osoby)
- vypsat pozdrav: `Hello, <name>!`
- mít výchozí hodnotu `--name World` pokud argument není zadán

Očekávané chování:
```
python main.py --name Pavel
Hello, Pavel!

python main.py
Hello, World!
```

> Nápověda: podívej se na sekci **Quickstart** v dokumentaci knihovny click.

### Úloha 3 — Opakování pozdravu

Rozšiř skript z Úlohy 2 o volitelný argument `--count`, který určuje,
kolikrát se pozdrav vypíše. Výchozí hodnota je `1`.

Očekávané chování:
```
python main.py --name Pavel --count 3
Hello, Pavel!
Hello, Pavel!
Hello, Pavel!
```

### Úloha 4 — Docstringy a typové nápovědy (`typing`)

Doplňte do svého skriptu takzvané **docstrings** a **type hints** pro všechny funkce a argumenty.

### Úloha 5 — Více příkazů (bonus)

Rozšiř nástroj o druhý příkaz `add`, který přijme dvě celá čísla jako argumenty
a vypíše jejich součet.

Očekávané chování:
```
python main.py greet --name Pavel
Hello, Pavel!

python main.py add 3 5
8
```

> Nápověda: podívej se na `@click.group()` a `@click.argument()` v dokumentaci.
