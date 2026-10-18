# Cvičení: práce se soubory

Cvičení je **samostatná práce na 90 minut**. Úlohy jsou seřazené od
nejjednodušších po nejtěžší a nepočítá se s tím, že stihnete všechny.
Každou úlohu řešte v samostatném souboru a průběžně ji commitujte.

| Obtížnost | Co znamená |
|-----------|------------|
| ★ | procvičení základů z přednášky |
| ★★ | je potřeba spojit více operací dohromady |
| ★★★ | vyžaduje vlastní návrh a práci s dokumentací |
| ★★★★ | rozšiřující výzva |

Pro všechny úlohy platí:

- textové soubory otevírejte pomocí `with` a `encoding="utf-8"`,
- vstupní soubory bez výslovného pokynu nepřepisujte,
- načtení, zpracování a zápis rozdělte do samostatných funkcí,
- uživatelský vstup a výpis patří do `main()` spouštěné pomocí
  `if __name__ == "__main__":`.

---

## 1. Statistika textového souboru ★

Napište funkci `text_statistics(path)`, která načte textový soubor po řádcích
a vrátí slovník obsahující počet všech a neprázdných řádků, počet slov,
počet znaků bez konců řádků a délku nejdelšího řádku.

Program se zeptá na cestu, vypíše výsledky a srozumitelně ošetří
`FileNotFoundError`. Funkce nesmí použít `read()` ani `readlines()`.

**Rozšíření:** Vypište pět nejčastějších slov bez ohledu na velikost písmen.

## 2. Trvalý deník ★

Vytvořte program `journal.py` s příkazy:

- `add` — načte poznámku a přidá ji do `journal.txt`,
- `list` — vypíše všechny záznamy očíslované od 1,
- `search` — vypíše záznamy obsahující hledaný text.

Každý uložený řádek má tvar:

```text
2026-09-17 14:35 | Dokončit laboratorní protokol
```

Použijte režim přidávání a čas vytvořte pomocí `datetime`. Příkaz `list`
musí rozumně fungovat i tehdy, když soubor zatím neexistuje.

**Rozšíření:** Přidejte bezpečné odstranění záznamu podle čísla.

## 3. Zpracování naměřených hodnot ★★

Vstupní soubor `measurements.txt` obsahuje na každém řádku čas a teplotu:

```text
08:00;21.4
09:00;22.1

10:00;chyba
11:00;23.0
```

Napište funkce:

- `load_measurements(path)` — vrátí seznam dvojic `(time, temperature)`,
- `summarize(measurements)` — vrátí minimum, maximum a průměr,
- `write_report(path, measurements, summary)` — uloží textový report.

Prázdné a chybné řádky přeskočte, ale do reportu uveďte jejich čísla.
V této úloze zatím nepoužívejte modul `csv`.

**Rozšíření:** Ověřte formát času a rozumný interval teplot.

## 4. Bezpečné cesty a dávkové přejmenování ★★

Ve složce `photos` jsou soubory například `IMG_0042.JPG`,
`dovolena 1.jpg`, `Poznámka.txt` a `img_0043.jpeg`.

Napište program, který pomocí `pathlib`:

1. najde pouze soubory s příponou `.jpg` nebo `.jpeg` bez ohledu na velikost
   písmen,
2. vypíše plán přejmenování na `photo_001.jpg`, `photo_002.jpg`, …,
3. teprve po potvrzení uživatelem soubory skutečně přejmenuje.

Program nesmí přepsat existující soubor. Testujte jej v nové složce
s kopiemi nebo prázdnými zkušebními soubory.

**Rozšíření:** Uložte změny do `rename.log` a umožněte jejich vrácení.

## 5. Textový a binární soubor ★★★

Uložte celá čísla 0 až 65 535 jednou jako text (jedno číslo na řádku)
a podruhé jako dva bajty bez znaménka pomocí `int.to_bytes()`.

1. Porovnejte velikosti souborů pomocí `Path.stat().st_size`.
2. Oba soubory znovu načtěte.
3. Ověřte, že obnovené seznamy jsou stejné.
4. Vysvětlete, proč binární soubor není čitelný v běžném editoru.

**Rozšíření:** Prozkoumejte pořadí bajtů `"little"` a `"big"`.

## 6. Sloučení měření z více souborů ★★★★

Vedle programu vytvořte pouze dva vstupní soubory. Do
`measurements_a.txt` zkopírujte:

```text
2026-09-15 08:00;20.4
2026-09-15 16:00;22.1
2026-09-16 08:00;20.8
```

Do `measurements_b.txt` zkopírujte:

```text
2026-09-15 12:00;21.7
2026-09-16 12:00;23.1
2026-09-16 16:00;chyba
2026-09-16 20:00;19.7
```

Každý platný řádek tedy obsahuje datum, čas, středník a teplotu. Protože datum
i čas mají pevný formát od největší jednotky k nejmenší, řetězce jako
`2026-09-16 08:00` lze řadit přímo chronologicky.

Vytvořte program, který:

1. postupně načte `measurements_a.txt` a `measurements_b.txt`,
2. spojí platná měření z obou souborů do jednoho seznamu,
3. seřadí je podle data a času,
4. uloží je do `combined_measurements.txt`,
5. pro každý den vypočítá minimum, maximum a průměr,
6. vytvoří `import_report.txt` se souhrny a seznamem chybných vstupů.

U každého chybného vstupu uveďte soubor, číslo řádku a důvod. Chybou může být
například chybějící oddělovač nebo hodnota, kterou nelze převést na `float`.
Jeden chybný řádek nesmí zastavit zpracování ostatních dat.

Rozdělte řešení alespoň do funkcí:

```python
def load_file(path):
    """Načte platná měření a chyby z jednoho souboru."""

def merge_measurements(paths):
    """Spojí a seřadí měření ze zadaných souborů."""

def summarize_by_day(measurements):
    """Vrátí statistiky pro jednotlivé dny."""

def write_outputs(measurements, summaries, errors):
    """Zapíše spojená data a report o importu."""
```

Příklad části reportu:

```text
2026-09-16: min 19.7 °C, max 23.1 °C, průměr 21.2 °C

Přeskočené vstupy:
measurements_b.txt, řádek 3: neplatná teplota "chyba"
```

Vstupní soubory program nesmí měnit ani přepisovat.

**Rozšíření:** Umožněte uživateli zadat libovolný počet vstupních souborů
místo dvou pevně určených názvů.

## 7. Generátor SVG grafu ★★★★

Navazujte na měření z úlohy 3. Vytvořte `temperature_chart.svg`, který lze
otevřít v prohlížeči a obsahuje název, osy, bod pro každé platné měření
a lomenou čáru spojující body.

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="800" height="400">
  <!-- sem program doplní prvky line, circle a text -->
</svg>
```

Souřadnice měření převeďte do prostoru obrázku pomocí samostatných funkcí.

**Rozšíření:** Vyznačte minimum, maximum a čáru průměru.
