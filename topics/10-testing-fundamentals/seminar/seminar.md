# Komentované příklady: základní principy testování

Ve druhé polovině semestru smíte při řešení úloh používat AI. Tím se mění,
co je na programování těžké: napsat kód je levné, ale **vědět, co má kód
dělat, a ověřit, že to dělá**, zůstává na vás. Test je způsob, jak to
zapsat tak, aby to šlo kdykoli znovu spustit.

Společně projdeme cestu od programu, který otestovat nejde, přes první
testy v pytestu až k situaci, kdy všechny testy projdou, a kód je přesto
špatně. Právě ta poslední situace je v době AI nejdůležitější.

Kód ze společného průchodu je ve složce [`sample_work/`](sample_work/)
ve stavu, ve kterém skončí na konci hodiny.

Na 90 minut jsou určeny části 1–7. Návodné úkoly označené *na místě*
se řeší během hodiny, ostatní jsou *doma* k procvičení. Části 8 a 9 jsou
pro případ, že zbyde čas, jinak slouží k samostudiu.

## Co byste měli po společném průchodu umět

- oddělit logiku programu od vstupu a výstupu tak, aby šla testovat,
- napsat test podle vzoru Arrange–Act–Assert a spustit ho pytestem,
- přečíst výpis selhání a rozhodnout, zda je špatně test, nebo kód,
- odvodit očekávanou hodnotu ze zadání, ne ze spuštění kódu,
- vybrat běžné, hraniční a chybové případy a zapsat je parametrizací,
- zachytit nalezenou chybu regresním testem,
- poznat slabé testy a vysvětlit, proč je AI splní doslova, a zadání přesto ne,
- použít `tmp_path` a fixture pro testy se souborem a stavem objektu.

---

## 0. Příprava

Pytest je externí knihovna, instaluje se jako v tématu o knihovnách:

```powershell
python -m pip install pytest
```

Pracujeme v jedné nové složce. Testy spouštíme příkazem

```powershell
python -m pytest
```

Pytest sám najde soubory `test_*.py` a v nich funkce `test_*`. Nic dalšího
registrovat nemusíme.

---

## 1. Program, který nejde otestovat

Ve druhém týdnu jste psali program na průměr pěti čísel
([zadání](../../02-algorithm-design-basics/lab/average_value.md)):

```python
N = 5
total = 0

print(f"Enter {N} numbers:")

for i in range(1, N + 1):
    x = float(input(f"Value #{i}: "))
    total = total + x

average = total / N
print("Average value:", average)
```

Zkuste si odpovědět: jak by vypadal test tohoto programu? Test by musel
pět hodnot *zadat z klávesnice* a výsledek *přečíst z obrazovky*. Výpočet je
propletený se vstupem a výstupem, a proto se k němu test nedostane.

Řešení není nový nástroj, ale jiné rozdělení programu. Logiku přesuneme
do funkce, která **dostane data jako argument a vrátí výsledek**. Vstup
a výstup zůstanou stranou:

```python
def average(numbers: list[float]) -> float:
    """Return the arithmetic mean of numbers."""
    return sum(numbers) / len(numbers)


def read_numbers(count: int) -> list[float]:
    return [float(input(f"Value #{i}: ")) for i in range(1, count + 1)]


def main() -> None:
    numbers = read_numbers(5)
    print("Average value:", average(numbers))


if __name__ == "__main__":
    main()
```

Program se chová navenek stejně, ale funkce `average` je teď samostatná:
dá se zavolat z jiného souboru, s libovolnými daty a bez klávesnice.

Tohle je nejdůležitější dovednost celé hodiny. Většina programů, které
jste letos napsali, se dá otestovat až po tomto kroku.

### Návodný úkol (na místě)

Vezměte program na převod teplot
([zadání](../../02-algorithm-design-basics/lab/temperature_conversion.md))
a rozdělte ho stejně: funkce `to_fahrenheit(celsius)`, funkce
`to_kelvin(celsius)` a `main()`, které se stará o `input()` a `print()`.

---

## 2. První test a čtení výsledku

Do souboru `test_average.py` napíšeme první test:

```python
from average import average


def test_average_of_five_numbers():
    numbers = [2, 4, 6, 8, 10]  # Arrange: připrav data
    result = average(numbers)  # Act: zavolej testovanou funkci
    assert result == 6  # Assert: ověř výsledek
```

Tři komentáře označují vzor **Arrange–Act–Assert**. Když test selže, hned
víme, ve které části hledat.

Spusťte `python -m pytest`. Pak očekávanou hodnotu úmyslně změňte na `7`
a spusťte znovu. Výpis si přečtěte celý:

```text
    def test_average_of_five_numbers():
        numbers = [2, 4, 6, 8, 10]
        result = average(numbers)
>       assert result == 7
E       assert 6.0 == 7
```

Pytest ukáže řádek, kde se porovnání nepovedlo, a obě hodnoty. Nemusíme
psát vlastní chybové zprávy.

Teď ta důležitější otázka: **kdo má pravdu, test, nebo kód?** Tady je
chyba zjevně v testu. V praxi to zjevné nebývá a právě tohle rozhodnutí
za vás nikdo neudělá. Kdo opraví test podle kódu, jen aby prošel, ověřil
tím pouze, že kód dělá to, co dělá.

### Návodný úkol (doma)

Napište první test pro `to_fahrenheit`: při 100 °C má vyjít 212. Zkuste
test záměrně rozbít a přečtěte si výpis.

---

## 3. Odkud se bere očekávaná hodnota

Představte si, že jste funkci `average` přepsali ve spěchu a nechali v ní
původní konstantu:

```python
def average(numbers):
    return sum(numbers) / 5
```

Potřebujete test, tak funkci spustíte, vidíte `average([1, 2, 3])` →
`1.2` a napíšete:

```python
def test_average_of_three():
    assert average([1, 2, 3]) == 1.2  # opsáno z výstupu programu
```

Test projde. Chyba se stala součástí testu a od této chvíle ji test
**chrání** před opravou: kdo funkci opraví, tomu test spadne.

Očekávaná hodnota musí přijít **odjinud než z testovaného kódu**: ze
zadání, z ručního výpočtu (1 + 2 + 3 = 6, 6 / 3 = 2), z tabulek nebo
z nezávislého výpočtu. Na slajdech se tomuto zdroji správné odpovědi
říká **testovací orákulum**.

Totéž platí dvojnásob, když testy generuje AI ke kódu, který už existuje.
Model nezná vaše zadání, zná jen kód, a tak do testů opíše jeho chování,
včetně chyb. K tomu se vrátíme v části 7.

### Návodný úkol (doma)

Pro `to_kelvin` napište tři testy s hodnotami, které spočítáte ručně
nebo víte z fyziky (např. 0 °C, −273,15 °C). Teprve potom funkci spusťte.
Pokud test selže o nepatrný zlomek (např. `273.15000000000003`), není to
chyba ve výpočtu; vysvětlení a nástroj najdete v části 4.

---

## 4. Které případy testovat

Jeden test na běžná data nestačí. Slajdy rozdělují vstupy do tří skupin,
projdeme je na `average`.

**Běžné**: obvyklá data, test z části 2.

**Hraniční**: kraje toho, co má smysl.

```python
def test_average_of_single_number_is_that_number():
    assert average([7]) == 7


def test_average_of_negative_numbers():
    assert average([-2, -4]) == -3
```

**Chybové**: co má funkce udělat s nesmyslným vstupem. Průměr prázdného
seznamu není definovaný. Tohle rozhodnutí patří do zadání (docstringu)
a test ho ověřuje stejně jako návratovou hodnotu:

```python
def average(numbers: list[float]) -> float:
    """Return the arithmetic mean of numbers.

    Raises ValueError if numbers is empty.
    """
    if not numbers:
        raise ValueError("average of an empty list is undefined")
    return sum(numbers) / len(numbers)
```

```python
import pytest


def test_average_of_empty_list_raises_value_error():
    with pytest.raises(ValueError, match="empty"):
        average([])
```

Bez vlastní kontroly by funkce spadla na `ZeroDivisionError`. Test musí
chtít **konkrétní** výjimku, ne „nějakou chybu“.

### Desetinná čísla

```python
def test_average_of_floats():
    assert average([0.1, 0.2, 0.4]) == 0.7 / 3
```

Tenhle test může selhat, přestože je matematicky správně: součet
`0.1 + 0.2 + 0.4` není v binární reprezentaci přesně `0.7`. Pro
desetinná čísla porovnáváme s tolerancí:

```python
def test_average_of_floats_uses_tolerance():
    assert average([0.1, 0.2, 0.4]) == pytest.approx(0.7 / 3)
```

### Tabulka případů: parametrizace

Pět podobných testů se liší jen daty. Pytest umí zapsat jeden test
a tabulku případů:

```python
@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([2, 4, 6, 8, 10], 6),  # běžný případ
        ([7], 7),  # jeden prvek
        ([-2, -4], -3),  # záporná čísla
        ([0, 0, 0], 0),  # samé nuly
        ([1, 2], 1.5),  # neceločíselný výsledek
    ],
)
def test_average_cases(numbers, expected):
    assert average(numbers) == expected
```

Každý řádek pytest spustí a vypíše zvlášť. Tabulka má ještě jednu výhodu:
je na ní **vidět, co chybí**. Každý řádek zastupuje jednu skupinu vstupů,
které se mají chovat stejně (na slajdech „ekvivalenční třída“). Když
některá skupina řádek nemá, není otestovaná.

### Návodný úkol (na místě)

Funkce `max_of_three(a, b, c)` vrací největší ze tří čísel. Sestavte pro
ni tabulku případů: nejdřív si na papír napište skupiny vstupů (všechna
různá, dvě stejná, všechna stejná, záporná, nuly), a teprve pak je
přepište do `parametrize`.

---

## 5. Nalezená chyba se zachytí regresním testem

Následující funkce vypadá v pořádku a na běžná slova funguje:

```python
def is_palindrome(text: str) -> bool:
    """Return True if text reads the same forwards and backwards.

    The comparison ignores spaces and letter case.
    """
    cleaned = text.replace(" ", "")
    return cleaned == cleaned[::-1]
```

Porovnejte docstring s kódem. Slibuje, že na velikosti písmen nezáleží,
kód s ní ale nic nedělá. Postup ze slajdů:

1. **Chybu zopakujeme testem** (na slajdech „reprodukujeme“).

   ```python
   def test_is_palindrome_ignores_letter_case():
       assert is_palindrome("Racecar") is True
   ```

2. **Ověříme, že test na starém kódu selže.** Pokud by prošel, netestuje
   to, co si myslíme.
3. **Opravíme funkci**: `cleaned = text.replace(" ", "").lower()`.
4. **Test necháme v souboru.** Až někdo funkci za půl roku přepíše, chyba se
   nevrátí nepozorovaně.

Zbylé případy zapíšeme tabulkou:

```python
@pytest.mark.parametrize(
    "text, expected",
    [
        ("racecar", True),
        ("hello", False),
        ("a", True),
        ("", True),
        ("nurses run", True),
    ],
)
def test_is_palindrome_cases(text, expected):
    assert is_palindrome(text) is expected
```

Všimněte si `is True` místo `== True`: funkce má vracet skutečný `bool`,
ne jen „něco pravdivého“.

### Návodný úkol (doma)

Co má `is_palindrome` vrátit pro `"A man, a plan, a canal: Panama"`?
Docstring o interpunkci mlčí. Rozhodněte, doplňte větu do docstringu
a napište test. Teprve potom upravte kód.

---

## 6. Testy prošly, kód je špatně

Teď to nejdůležitější. Zadání:

```python
def find_longest_word(sentence: str) -> str:
    """Return the longest word in sentence.

    Punctuation is ignored. If several words share the greatest length,
    the first one is returned. Raises ValueError if sentence has no words.
    """
```

Student napsal dva testy:

```python
def test_longest_word_at_the_end():
    assert find_longest_word("ahoj světe") == "světe"


def test_longest_word_is_last_of_three():
    assert find_longest_word("a bb ccc") == "ccc"
```

a poslal je AI s pokynem *„napiš funkci, která projde těmito testy“*.
Zkuste před dalším čtením odhadnout, jaká nejkratší funkce oběma testy
projde.

```python
def find_longest_word(sentence):
    return sentence.split()[-1]
```

Vrací poslední slovo. Oba testy projdou, protože v obou je nejdelší slovo
náhodou poslední. Takhle hloupou funkci vám AI typicky nedá, ale princip
platí: **model se snaží projít vašimi testy, ne splnit váš záměr.** Co
v testech není, to není zadáno. Ze zadání psaného slovy si model vybere
nejjednodušší výklad, který testy pustí.

Testy mají díry. Společně je zalátáme; u každého nového testu řekněte
nahlas, jakou díru zavírá:

```python
def test_longest_word_in_the_middle():
    assert find_longest_word("a nejdelší b") == "nejdelší"


def test_first_of_equally_long_words_wins():
    assert find_longest_word("kos pes") == "kos"


def test_punctuation_is_ignored():
    assert find_longest_word("Ahoj, světe!") == "světe"


def test_empty_sentence_raises_value_error():
    with pytest.raises(ValueError):
        find_longest_word("")
```

Každá věta docstringu má teď svůj test. To je smysl rčení ze slajdů
„testy jsou spustitelná specifikace“, tedy zadání, které se dá spustit:
kdo píše testy, rozhoduje, co program dělá.

Na cvičení si tuto situaci vyzkoušíte z druhé strany: dostanete slabé
testy a budete hledat kód, který jimi projde a je přesto špatně.

### Návodný úkol (na místě)

Pošlete AI všech šest testů (bez docstringu) a nechte ji napsat funkci.
Spusťte testy. Pokud něco neprošlo, rozhodněte: je špatně test, nebo kód?
Pokud prošlo vše, zkuste vymyslet vstup, na kterém funkce přesto selže,
a přidejte test.

---

## 7. Když AI testuje AI

Opačná situace: kód už existuje a chceme k němu testy. Vezměte **chybnou**
verzi `find_longest_word` z části 6, odstraňte docstring a požádejte AI:
*„Napiš pytest testy pro tuto funkci.“*

Typický výsledek vypadá takto:

```python
def test_single_word():
    assert find_longest_word("hello") == "hello"


def test_returns_last_word():
    assert find_longest_word("the quick brown fox") == "fox"
```

Testy prošly na první pokus. A přitom druhý test **potvrzuje chybu**:
nejdelší slova jsou `quick` a `brown`, správná odpověď podle zadání je
`quick`. Model neznal zadání, viděl jen kód, a tak popsal, co kód dělá.
Je to ověřování v kruhu: kód a testy mají stejný zdroj a vzájemně se
potvrzují.

Teď dejte AI stejný kód **i s docstringem** a zopakujte prosbu. Testy
budou jiné a část z nich na chybném kódu selže. Rozdíl nedělá model, ale
zadání, které jste mu dali.

Totéž platí pro nejběžnější situaci: když si necháte jedním dotazem
vygenerovat funkci **i** testy k ní. Oba výstupy mají stejný zdroj
a stejné nepochopení zadání, takže prošlé testy neověřují nic.

Z toho plyne, kde AI při testování skutečně pomáhá:

| Co | AI | Vy |
| --- | --- | --- |
| Zapsat testy podle tabulky případů | ano, je to rutina | zkontrolovat |
| Navrhnout případy, na které jste zapomněli | ano, ptejte se: *„Jaké hraniční případy mi chybí?“* | vybrat a rozhodnout |
| Určit očekávanou hodnotu | ne | ze zadání nebo ručně |
| Rozhodnout, zda je špatně test, nebo kód | ne | vždy vy |
| Napsat kód k hotovým testům | ano | spustit testy a přečíst výsledek |

### Návodný úkol (doma)

Zeptejte se AI, jaké hraniční případy chybí ve vaší tabulce pro
`max_of_three` z části 4. Každý návrh posuďte: dává smysl? Už ho pokrývá
jiný řádek? Co má být výsledkem? Přidejte jen ty, které jste schválili.

---

## 8. Test se souborem: `tmp_path` (pokud zbyde čas)

Vraťme se k průměru. V tématu o souborech jste četli data ze souboru;
přidáme funkci, která načte čísla po řádcích:

```python
from pathlib import Path


def read_numbers_from_file(path: Path) -> list[float]:
    """Read numbers from a text file, one per line. Blank lines are skipped."""
    numbers = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                numbers.append(float(line))
    return numbers
```

Test potřebuje soubor. Nechceme ho vytvářet ručně ani ho nechávat na
disku. Pytest nabízí **fixture** `tmp_path`: test ji dostane jako
argument a je to dočasná složka, kterou pytest po testu uklidí.

```python
def test_read_numbers_from_file(tmp_path):
    data_file = tmp_path / "numbers.txt"
    data_file.write_text("1\n2\n\n3\n", encoding="utf-8")

    assert read_numbers_from_file(data_file) == [1, 2, 3]
```

Test si **sám připraví vstup**, nezávisí na tom, co leží na disku, a dá
se spustit v libovolném pořadí s ostatními. Tomu slajdy říkají izolace
testů.

Všimněte si, že `average` jsme vůbec nemuseli upravovat. Zdroj dat
(klávesnice, soubor) je oddělený od výpočtu a obě části se testují
zvlášť.

### Návodný úkol (doma)

Napište test pro prázdný soubor. Co má funkce vrátit? Co se stane, když
tento výsledek předáme do `average`? Je to správné chování, nebo chybí
další kontrola?

---

## 9. Stav objektu a vlastní fixture (pokud zbyde čas)

U třídy netestujeme jen návratovou hodnotu, ale i **změnu stavu**. Vezmeme
třídu `BankAccount` z výkladového notebooku (`deposit`, `withdraw`,
kontrola záporných částek a nedostatečného zůstatku).

Každý test potřebuje nový účet. Místo opakování `BankAccount("Alice",
balance=100)` si napíšeme vlastní fixture:

```python
import pytest

from bank_account import BankAccount


@pytest.fixture
def funded_account():
    return BankAccount("Alice", balance=100)


def test_deposit_increases_balance(funded_account):
    funded_account.deposit(50)
    assert funded_account.balance == 150


def test_withdraw_more_than_balance_raises(funded_account):
    with pytest.raises(ValueError, match="insufficient"):
        funded_account.withdraw(100.01)
    assert funded_account.balance == 100
```

Pytest fixture zavolá pro každý test znovu, takže test o vkladu
neovlivní test o výběru. Poslední test ověřuje dvě věci najednou:
že výběr selže **a** že se zůstatek přitom nezměnil. Chybový stav nemá
objekt poškodit.

### Návodný úkol (doma)

Napište test hranice: výběr přesně celého zůstatku má projít a zůstatek
má být 0. Pak zkuste test přepsat tak, aby použil `funded_account`,
a vysvětlete, proč tenhle test fixture nepotřebuje měnit.

---

## Shrnutí

Pracovní postup, který si odnášíte:

1. Logiku oddělte od vstupu a výstupu. Bez toho se nedá testovat.
2. Očekávanou hodnotu určete **dřív**, než kód spustíte.
3. Vyberte běžné, hraniční a chybové případy a zapište je tabulkou.
4. Každou nalezenou chybu zachyťte regresním testem.
5. Když testy prošly, zeptejte se: jaký špatný kód by jimi taky prošel?

A k AI: model splní testy, které mu dáte, a popíše kód, který mu dáte.
Zadání, očekávané hodnoty a rozhodnutí při selhání jsou vaše práce.
Proto se učíte testovat.

Na cvičení budete slabé testy cíleně prolamovat a pak v nich látat díry.
Vezměte si s sebou otázku z bodu 5.
