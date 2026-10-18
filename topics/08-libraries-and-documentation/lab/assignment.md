# Cvičení: vlastní knihovna a její dokumentace

Cvičení je **samostatná práce na 90 minut**. Všechny úlohy rozšiřují jeden
projekt: vlastní knihovnu `textkit` pro jednoduchou analýzu textu. Nezakládejte
pro každou úlohu nový program — pokračujte ve stejném projektu a průběžně
upravujte jeho dokumentaci.

| Obtížnost | Co znamená |
|-----------|------------|
| ★ | vytvoření balíčku a jednoduchých funkcí |
| ★★ | spolupráce více modulů a návrh rozhraní |
| ★★★ | dokumentace, externí knihovna a ošetření chyb |
| ★★★★ | samostatné rozšíření a kontrola projektu |

Pro celé cvičení platí:

- pracujte v jednom novém adresáři,
- kód knihovny patří do balíčku `textkit`, uživatelské rozhraní do `main.py`,
- funkce knihovny nesmějí používat `input()` ani přímo vypisovat,
- veřejné funkce průběžně opatřujte typovými nápovědami a docstringy,
- do `.gitignore` přidejte pomocné soubory vytvářené Pythonem,
- po přidání závislosti aktualizujte `requirements.txt`.

Výsledná struktura projektu bude postupně vypadat takto:

```text
text-analyzer/
├── textkit/
│   ├── __init__.py
│   ├── core.py
│   └── files.py
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 1. Založte vlastní knihovnu ★

Vytvořte adresář projektu a uvedenou základní strukturu. Soubory `core.py`
a `files.py` mohou být zatím prázdné.

Soubor `textkit/__init__.py` říká Pythonu, že adresář `textkit` tvoří balíček.
Ověřte, že jej lze z kořene projektu importovat:

```powershell
python -c "import textkit; print(textkit.__file__)"
```

Do `.gitignore` zapište alespoň `__pycache__/` a `*.pyc`. Do README přidejte
název projektu a jednu větu vysvětlující, k čemu knihovna slouží.

## 2. První dvě funkce ★

Do `textkit/core.py` implementujte:

```python
def normalize_whitespace(text: str) -> str:
    """Nahradí skupiny bílých znaků jednou mezerou."""

def count_words(text: str) -> int:
    """Vrátí počet slov oddělených bílými znaky."""
```

Požadované chování:

```text
normalize_whitespace("  Ahoj\n  světe  ")  -> "Ahoj světe"
count_words("  Ahoj\n  světe  ")          -> 2
count_words("")                             -> 0
```

Funkce nesmějí načítat vstup od uživatele ani vypisovat. V `main.py` je
importujte z `textkit.core` a ověřte na alespoň třech vlastních řetězcích.

## 3. Rozšiřte analýzu slov ★★

Do stejného modulu přidejte:

```python
def word_frequencies(text: str) -> dict[str, int]:
    """Vrátí četnosti slov bez ohledu na velikost písmen."""

def most_common_words(text: str, limit: int = 5) -> list[tuple[str, int]]:
    """Vrátí nejčastější slova a jejich počty."""
```

Při rozdělení textu nerozlišujte velikost písmen, z konců slov odstraňte
znaky `.,!?;:` a prázdná slova ignorujte.

Pro `"Pes, kočka a pes!"` má funkce `word_frequencies()` vrátit:

```python
{"pes": 2, "kočka": 1, "a": 1}
```

Funkce `most_common_words()` výsledek seřadí nejprve podle četnosti sestupně
a při shodě podle slova abecedně:

```python
[("pes", 2), ("a", 1), ("kočka", 1)]
```

Musí přitom využít `word_frequencies()`, ne znovu implementovat stejný výpočet.

## 4. Navrhněte veřejné rozhraní balíčku ★★

Uživatel knihovny by neměl potřebovat vědět, ve kterém souboru funkce leží.
V `textkit/__init__.py` proto zveřejněte vybrané funkce:

```python
from .core import count_words, most_common_words, normalize_whitespace
from .core import word_frequencies
```

Upravte `main.py`, aby používal pouze veřejné rozhraní:

```python
from textkit import count_words, most_common_words
```

Ověřte import z kořene projektu a do README přidejte krátkou ukázku použití.
Při přidání nové veřejné funkce od této chvíle aktualizujte také `__init__.py`.

## 5. Přidejte práci se soubory ★★

Knihovnu rozšiřte o modul `textkit/files.py`:

```python
from pathlib import Path

def read_text(path: Path) -> str:
    """Načte textový soubor v UTF-8."""

def write_text(path: Path, content: str) -> None:
    """Zapíše textový soubor v UTF-8."""
```

Obě funkce zveřejněte přes `textkit/__init__.py`. V `main.py` potom načtěte
text, zavolejte analytické funkce, sestavte report a uložte jej pomocí
`write_text()`.

Ověřte chování pro běžný text, prázdný soubor a neexistující cestu. Knihovna
nemá chybu skrývat; `main.py` ji má zachytit a uživateli srozumitelně oznámit.

## 6. Zdokumentujte knihovnu jako její uživatel ★★★

Každá veřejná funkce musí mít:

- typy všech parametrů a návratové hodnoty,
- jednovětý popis účelu,
- vysvětlení parametrů a výsledku,
- popis očekávatelné výjimky, pokud může nastat.

Dokumentaci zobrazte bez čtení zdrojového kódu:

```powershell
python -m pydoc textkit
python -c "from textkit import read_text; help(read_text)"
```

Do README doplňte přehled veřejných funkcí, krátký spustitelný příklad, formát
reportu a chování při neexistujícím vstupu.

## 7. Click jako rozhraní nad vlastní knihovnou ★★★

Nainstalujte knihovnu Click a zaznamenejte závislosti:

```powershell
python -m pip install click
python -m pip freeze > requirements.txt
```

Upravte `main.py` na příkazové rozhraní:

```text
python main.py sample.txt --top 3
python main.py sample.txt --top 3 --output report.txt
python main.py --help
```

Vstupní cesta je povinný argument, `--top` je kladné celé číslo a `--output`
je volitelná cesta. Click se smí importovat pouze v `main.py`; balíček
`textkit` na něm nesmí záviset.

## 8. Vlastní rozšíření a závěrečná kontrola ★★★★

Do knihovny přidejte jednu novou veřejnou funkci, například:

- `unique_words(text)`,
- `longest_words(text, limit=3)`,
- `average_word_length(text)`.

Funkci použijte v reportu, zveřejněte v `__init__.py` a zdokumentujte v README.
Nakonec ověřte veřejné importy, výpis i uložení reportu, `--help` a úplnost
`requirements.txt`.

Do repozitáře patří balíček `textkit`, `main.py`, README, `.gitignore` a
`requirements.txt`. Soubory `__pycache__` a `*.pyc` do něj nepatří.
