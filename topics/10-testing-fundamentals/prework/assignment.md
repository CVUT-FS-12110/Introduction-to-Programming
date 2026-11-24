# Domácí příprava: první testy v pytestu

Cílem je přijít na cvičení s vlastními testy, které tam budete používat.
Počítejte asi se 45 minutami. Pracujte ve svém editoru v nové složce. Pytest nainstalujte příkazem
`python -m pip install pytest`, testy spouštějte `python -m pytest -v`.

Testy pište sami: smyslem je, abyste si **vy** vybrali, co se má ověřit.
AI vám může připomenout syntaxi, výběr případů a očekávané hodnoty jsou
vaše práce.

## Úkol 1: testy pro hotovou funkci

Uložte jako `grade_calculator.py`:

```python
def calculate_grade(score: int) -> str:
    """Convert a numeric score (0-100) to a letter grade.

    Grading scale:
        90-100 -> 'A'
        80-89  -> 'B'
        70-79  -> 'C'
        60-69  -> 'D'
        0-59   -> 'F'

    Raises ValueError if score is not an int or is outside 0-100.
    """
    if not isinstance(score, int):
        raise ValueError("Score must be an integer")
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"
```

Do `test_grade.py` napište **alespoň šest testů**:

1. typickou hodnotu z každého pásma,
2. hranice pásem (přesně 90, 89, 0, 100),
3. neplatné vstupy, které mají vyvolat `ValueError`.

Dvojice vstup–známka zapište pomocí `@pytest.mark.parametrize`, chybové
vstupy jako samostatné testy s `pytest.raises`. Očekávanou známku odvoďte
**z docstringu**, ne ze spuštění funkce. Všechny testy mají projít.

## Úkol 2: najděte chybu

Uložte jako `text_utils.py`:

```python
def count_words(text: str) -> int:
    """Count the number of words in text.

    Words are separated by whitespace. Several consecutive spaces
    count as a single separator. An empty string has 0 words.

    Examples:
        count_words("hello world") -> 2
        count_words("  hello   world  ") -> 2
        count_words("") -> 0
    """
    return len(text.split(" "))
```

Funkce obsahuje chybu. Do `test_count_words.py` napište ke každé větě
a každému příkladu docstringu jeden test. Alespoň jeden test **má selhat**.
Potom funkci opravte, aby všechny testy prošly, a selhávající test nechte
v souboru jako regresní test.

## Úkol 3: testy dřív než kód

Uložte jako `score_tracker.py`:

```python
class ScoreTracker:
    """Tracks scores and computes statistics."""

    def __init__(self):
        """Create an empty tracker."""
        raise NotImplementedError

    def add_score(self, score: float) -> None:
        """Add a score. Raises ValueError if score is negative."""
        raise NotImplementedError

    def get_average(self) -> float:
        """Return the average of all scores. Raises ValueError if empty."""
        raise NotImplementedError

    def get_highest(self) -> float:
        """Return the highest score. Raises ValueError if empty."""
        raise NotImplementedError

    def get_count(self) -> int:
        """Return the number of scores added."""
        raise NotImplementedError

    def reset(self) -> None:
        """Remove all scores."""
        raise NotImplementedError
```

Třídu **neimplementujte**, to uděláte na cvičení. Do `test_score_tracker.py`
napište alespoň čtyři testy podle docstringů: prázdný tracker, jedno
a několik skóre, `reset()`, záporné skóre. Každý test pracuje s vlastním
objektem; pokud chcete, vytvořte ho pomocí fixture jako v části 9
komentovaných příkladů. Všechny testy selžou s `NotImplementedError`;
to je v pořádku.

### Co má být v souborech vidět

- `test_grade.py`: `parametrize` s tabulkou případů a `pytest.raises`,
- `test_count_words.py`: test, který na původní funkci selhal, a opravená
  funkce v `text_utils.py`,
- `test_score_tracker.py`: testy pro každou metodu ze zadání.

### Na co se při kontrole zaměřit

- U `count_words`: na jakém vstupu se funkce chovala jinak, než slibovala?
  Co přesně v docstringu ten vstup popisovalo?
- U `calculate_grade`: ke každému testu si řekněte, která věta docstringu
  ho odůvodňuje. Test bez takové věty testuje něco, co zadání neslibuje.

### Smysl domácí přípravy

Před cvičením si vyzkoušíte:

- napsat testovací soubor pro hotovou funkci podle jejího zadání,
- nechat testy najít chybu v cizím kódu a zachytit ji regresním testem,
- zapsat zadání třídy jako testy dřív, než existuje její kód,
- připravit si soubory, se kterými budete na cvičení pracovat.
