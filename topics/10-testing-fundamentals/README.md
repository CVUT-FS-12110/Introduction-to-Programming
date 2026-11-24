# Základní principy testování

## Prerekvizity

- Funkce, výjimky a třídy
  ([Funkce](../05-functions-definition-invocation-and-scope/README.md),
  [Úvod do OOP](../06-introduction-to-object-oriented-programming/README.md))
- Práce se soubory a instalace knihoven přes pip
  ([Práce se soubory](../07-file-handling-and-file-io/README.md),
  [Používání knihoven](../08-libraries-and-documentation/README.md))

## Cíle

- Oddělit logiku programu od vstupu a výstupu, aby šla testovat.
- Napsat test podle vzoru Arrange–Act–Assert a spustit ho pytestem.
- Navrhnout běžné, hraniční a chybové případy a zapsat je parametrizací.
- Otestovat výjimky (`pytest.raises`), desetinná čísla (`pytest.approx`)
  a stav objektu.
- Zachytit nalezenou chybu regresním testem.
- Posoudit, co testy dokazují a co ne, zejména u kódu vygenerovaného AI.

## Klíčová slova

pytest, assert, Arrange–Act–Assert, hraniční případy, parametrizace,
regresní test, fixture, testovací orákulum, mutační testování

## Přednáška

- [Slajdy: Základní principy testování](lecture/presentation.pdf)

Úvod do automatického testování: co test ověřuje a co nezaručuje, jak
volit případy, jak testovat výjimky, desetinná čísla a objekty, a k čemu
jsou testy při práci s AI.

- [Komentované příklady: testování](seminar/seminar.md)

Kód ze společného průchodu je ve složce `seminar/sample_work/`.
K samostudiu slouží také
[výkladový notebook](lecture/testing-fundamentals.ipynb).

### Osnova

1. Program, který nejde otestovat: oddělení logiky od vstupu a výstupu
2. První test, čtení výpisu pytestu, Arrange–Act–Assert
3. Odkud se bere očekávaná hodnota (testovací orákulum)
4. Běžné, hraniční a chybové případy, `pytest.raises`, `pytest.approx`,
   parametrizace
5. Nalezená chyba a regresní test
6. Testy, kterými projde i špatný kód; testy jako zadání pro AI
7. Test se souborem (`tmp_path`), stav objektu a fixture (podle času)

## Domácí příprava

[Zadání domácí přípravy: první testy v pytestu](prework/assignment.md)

## Cvičení

[Zadání cvičení](lab/assignment.md)

Příklad: test s tabulkou případů

```python
import pytest

from average import average


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([2, 4, 6], 4),
        ([7], 7),
        ([-2, -4], -3),
    ],
)
def test_average_cases(numbers, expected):
    assert average(numbers) == expected


def test_average_of_empty_list_raises():
    with pytest.raises(ValueError):
        average([])
```

## Zdroje

- [pytest dokumentace](https://docs.pytest.org/) — oficiální dokumentace frameworku
- [Real Python: Getting Started With Testing in Python](https://realpython.com/python-testing/) — podrobný tutoriál
- [Python Tutorial: Floating Point Arithmetic](https://docs.python.org/3/tutorial/floatingpoint.html) — proč `0.1 + 0.2 != 0.3`
