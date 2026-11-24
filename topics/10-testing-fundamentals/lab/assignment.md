# Cvičení: testování v praxi

Cvičení je **samostatná práce na 90 minut**. Úlohy na sebe navazují a jsou
seřazené od nejjednodušších po nejtěžší. Nečeká se, že stihnete všechny;
pokračujte podle času a jistoty v předchozích krocích.

| Obtížnost | Co znamená |
|-----------|------------|
| ★ | přímé použití testů z domácí přípravy a hledání děr v cizích testech |
| ★★ | doplňování testů a postup „nejdřív testy, pak kód“ |
| ★★★ | zpětné otestování vlastního staršího programu |
| ★★★★ | mutační testování vlastní třídy |

Úlohy 2, 3 a 6 používají jeden společný postup, kterému se říká
**mutační testování**: do kódu se záměrně zanese chyba („mutant“)
a sleduje se, zda ji testy odhalí. Mutant, který testy přežije, ukazuje
díru v testech.

Pro celé cvičení platí:

- pracujte v jednom novém adresáři, testy spouštějte `python -m pytest -v`;
  jen jeden soubor spustíte `python -m pytest test_grade_weak.py -v`,
- každý test si vytváří vlastní data a objekty, testy na sobě nezávisí,
- očekávané hodnoty odvozujte ze zadání, ne ze spuštění kódu,
- cokoli převezmete od AI, musíte umět vysvětlit vlastními slovy.

Budete potřebovat soubory z [domácí přípravy](../prework/assignment.md):
`grade_calculator.py`, `test_grade.py`, `score_tracker.py`
a `test_score_tracker.py`.

---

## Úloha 1 — ScoreTracker podle vlastních testů ★

Zkopírujte si `score_tracker.py` a `test_score_tracker.py` z domácí
přípravy a nahraďte každé `raise NotImplementedError` skutečným kódem.

1. Postupujte po jedné metodě: implementujte, spusťte testy, sledujte,
   kolik jich prošlo.
2. Pokud některý test neprojde, rozhodněte, zda je chyba v kódu,
   nebo v testu. Obojí je možné.
3. Ponechte si funkční verzi; k tomu, jak dobré jsou vaše testy, se
   vrátíte v úloze 6.

### Procvičuje

- psaní kódu podle hotových testů,
- čtení výpisu pytestu a rozhodování „test, nebo kód“.

---

## Úloha 2 — Prolomte slabé testy ★

Uložte následující **záměrně slabé** testy pro `calculate_grade`
z domácí přípravy jako `test_grade_weak.py`:

```python
"""Záměrně slabé testy pro calculate_grade.

Zadání funkce (stejné jako v domácí přípravě):
    90-100 -> 'A', 80-89 -> 'B', 70-79 -> 'C', 60-69 -> 'D', 0-59 -> 'F'
    Vstup mimo 0-100 nebo jiný typ než int -> ValueError
"""

from grade_calculator_bad import calculate_grade


def test_typical_a():
    assert calculate_grade(95) == "A"


def test_typical_b():
    assert calculate_grade(85) == "B"


def test_c_is_a_letter():
    assert calculate_grade(75) in "ABCDF"


def test_typical_f():
    assert calculate_grade(30) == "F"
```

Svůj správný `grade_calculator.py` nechte beze změny. Do nového souboru
`grade_calculator_bad.py` napište **špatnou** verzi funkce
`calculate_grade`, která

1. projde všemi slabými testy,
2. ale na vstupech, které testy nepokrývají, vrací nesmysl,
3. má v komentáři napsáno, jakou díru v testech zneužívá.

Zakázaný trik je výčet konkrétních testovaných hodnot
(`if score == 95: return "A"`): projde vždy a proti každé sadě. Váš trik
musí zneužít konkrétní díru. Začněte tím, že si přečtete, co testy
**netestují**: které pásmo, které hranice, které neplatné vstupy. Když
jste hotovi, hledejte druhou díru jiného typu.

### Procvičuje

- čtení testů očima toho, kdo je chce obejít,
- rozpoznání typů děr: chybějící pásmo, hranice, chybové vstupy, příliš
  volná podmínka v `assert`,
- myšlenku „dobrý test nejde obejít“.

---

## Úloha 3 — Zalátejte díry v testech ★★

Navazujte na `test_grade_weak.py` a svou špatnou verzi funkce z úlohy 2.

1. Ke každé díře, kterou jste našli, doplňte na konec souboru test, který
   ji zavře. Spusťte `python -m pytest test_grade_weak.py -v`: nový test
   musí na vaší špatné verzi **selhat**. To je cíl, ne chyba.
2. Každý doplněný test musí zároveň projít na správné funkci. Přepněte
   v `test_grade_weak.py` import na `from grade_calculator import
   calculate_grade` a spusťte testy znovu: všechny procházejí. Test,
   který padá i na správné funkci, je špatně napsaný; opravte ho. Pak
   import vraťte na `grade_calculator_bad`.
3. Porovnejte doplněné testy se svým `test_grade.py` z domácí přípravy:
   které díry jste doma nechali otevřené?
4. Přepište `grade_calculator_bad.py` novou špatnou verzí, která projde
   i doplněnými testy. Pokud se to povede, doplňte další test. Pokud ne,
   testy už tímto způsobem obejít nejdou.

### Procvičuje

- test, který odhalí konkrétní špatný kód,
- hranice pásem a chybové vstupy jako samostatné případy,
- opakování prolom – zalátej jako způsob, jak testy zlepšovat.

---

## Úloha 4 — Nová metoda: nejdřív testy, pak kód ★★

Rozšiřte `ScoreTracker` z úlohy 1 o metodu

```python
def get_percentile(self, score: float) -> float:
    """Return the percentage of stored scores that are strictly below score.

    Example: with scores [10, 20, 30, 40, 50], get_percentile(30)
    returns 40.0 (2 of 5 scores are below 30).
    Raises ValueError if no scores are stored.
    """
```

Pořadí je závazné:

1. Napište testy do `test_score_tracker.py`: běžný případ, skóre nižší
   než všechna (0 %), vyšší než všechna (100 %), skóre **rovné** některému
   uloženému, stejné skóre uložené dvakrát, prázdný tracker a případ se
   třemi skóre,
   kde výsledek není „hezké“ číslo (např. 1 ze 3 → 33,33… %).
2. Spusťte testy a ověřte, že selžou.
3. Teprve potom metodu implementujte. Výsledek je desetinné číslo; kde
   porovnáváte výsledek dělení, použijte `pytest.approx`.

### Procvičuje

- testy jako zápis zadání dřív, než existuje kód,
- hraniční případy u porovnání („strictly below“),
- `pytest.approx` u desetinných výsledků.

---

## Úloha 5 — Otestujte svůj starší program ★★★

Vyberte si jeden ze svých programů z dřívějších cvičení, například
[počítání typů čísel](../../02-algorithm-design-basics/lab/count_number_types.md)
nebo úlohu ze [cvičení k podmínkám a cyklům](../../04-control-flow-loops-and-conditionals/lab/assignment.md).
Program pravděpodobně čte
vstup přes `input()` a výsledky rovnou tiskne, takže se testovat nedá.

1. Oddělte výpočet od vstupu a výstupu: logiku přesuňte do funkce, která
   dostane data jako argumenty a vrátí výsledek; `input()` a `print()`
   zůstanou ve funkci `main()`.
2. Ověřte, že se program navenek chová stejně jako předtím.
3. Napište testy: běžný případ, hraniční případy (prázdný vstup, nula,
   záporné číslo, jeden prvek) a chybové vstupy.
4. Podobné případy zapište pomocí `@pytest.mark.parametrize`.

Zapište si, zda testy našly chybu v programu, který jste dřív považovali
za hotový.

### Procvičuje

- oddělení logiky od vstupu a výstupu jako podmínku testovatelnosti,
- návrh běžných, hraničních a chybových případů pro vlastní kód,
- parametrizaci.

---

## Úloha 6 — Mutační testování vlastní třídy ★★★★

Vraťte se k `ScoreTracker` z úlohy 1 a otočte role: teď budete svoje
testy prolamovat sami.

1. Zkopírujte `score_tracker.py` do `score_tracker_mutant.py` a zaneste
   do kopie **jednu** záměrnou chybu („mutanta“), například:
   - `get_highest` vrací poslední přidané skóre,
   - `add_score` odmítne i skóre `0`,
   - `get_average` dělí počtem o jedna větším,
   - `reset` smaže jen první skóre.
2. V `test_score_tracker.py` přepněte import na
   `from score_tracker_mutant import ScoreTracker` a spusťte testy.
   Pokud alespoň jeden selže, mutant je **odhalený** (v hantýrce
   „zabitý“). Pokud projdou všechny, mutant **přežil** a ukazuje díru
   v testech: doplňte test, který ho odhalí.
3. Zopakujte pro všechny čtyři mutanty výše a alespoň jednoho vlastního.
   Zapište si, kolik mutantů přežilo první pokus.
4. Import vraťte na `from score_tracker import ScoreTracker` a ověřte,
   že všechny testy procházejí.

Tohle je mutační testování z úvodu cvičení v čisté podobě: tentokrát
mutanty vyrábíte a odhalujete sami, na vlastní třídě.

### Procvičuje

- hodnocení kvality testů podle toho, co jimi projde,
- cyklus prolom – zalátej z úloh 2 a 3 na vlastní třídě,
- typy chyb, které testy snadno přehlédnou (hranice, výpočet z více
  hodnot, stav objektu).

### Bonus

- Doma vyzkoušejte nástroj [`mutmut`](https://mutmut.readthedocs.io/),
  který mutanty vytváří automaticky, a porovnejte jeho přeživší mutanty
  s těmi vašimi.
- Odpovězte si: když vám AI vygeneruje kód a všechny vaše testy projdou,
  co to dokazuje a co ne?

Testy, které jste dnes psali, jsou přesně to, co na prezentaci podle
[pravidel předmětu](../../../RULES.md) ukážete jako důkaz, **jak jste
výstupy AI ověřili**.
