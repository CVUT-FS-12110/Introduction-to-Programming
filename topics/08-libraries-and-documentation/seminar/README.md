# Komentované příklady: lokální knihovna pro vektory

Společně vytvoříme malý lokální balíček `vectorlib`. Cílem není dokončit
rozsáhlou matematickou knihovnu, ale ukázat, jak se třída rozdělí do vlastního
modulu, zveřejní přes balíček a používá z jiného programu.

## Co byste měli po společném průchodu umět

- založit jednoduchý importovatelný balíček,
- zveřejnit třídu přes `__init__.py`,
- přetížit operátory `+` a `*`,
- kontrolovat kompatibilní rozměry vektorů,
- oddělit kód knihovny od ukázkového programu,
- dohledat význam speciální metody v dokumentaci.

---

## 1. Připravte kostru balíčku

Vytvořte společně strukturu:

```text
vector-project/
├── vectorlib/
│   ├── __init__.py
│   └── vector.py
└── main.py
```

Do `vector.py` vložte třídu `Vector` a přes `__init__.py` umožněte import:

```python
from vectorlib import Vector
```

Diskutujte, proč uživatel knihovny nemusí znát název souboru `vector.py`.

## 2. Uložte souřadnice a popište objekt

Konstruktor přijme seznam souřadnic a uloží jeho kopii. Prázdný vektor
odmítněte pomocí `ValueError`.

Doplňte:

- metodu `dimension()`,
- čitelnou reprezentaci přes `__repr__`,
- typové nápovědy a stručné docstringy.

V `main.py` vytvořte několik vektorů různých rozměrů a sledujte jejich výpis.

## 3. Součet vektorů

Vyhledejte v dokumentaci význam speciální metody `__add__`. Potom ji doplňte
tak, aby výraz

```python
Vector([1, 2, 3]) + Vector([4, 5, 6])
```

vrátil nový `Vector([5, 7, 9])`. Původní objekty musí zůstat beze změny.
Při rozdílných rozměrech vyvolejte `ValueError` se srozumitelnou zprávou.

## 4. Skalární součin

V této ukázce bude operátor `*` mezi dvěma vektory znamenat skalární součin:

```python
Vector([1, 2, 3]) * Vector([4, 5, 6])  # 32
```

Implementujte `__mul__` a použijte stejnou kontrolu rozměrů jako u součtu.
Kontrolní kód neopisujte; přesuňte jej do jedné pomocné metody.

## 5. Rozšiřte třídu

Podle času doplňte některé z následujících operací:

- rozdíl vektorů pomocí `-`,
- délku vektoru metodou `magnitude()`,
- násobení vektoru číslem metodou `scale()`,
- porovnání pomocí `==`.

U každé operace nejprve určete typ výsledku a rozhodněte, které vstupy jsou
neplatné.

## 6. Použijte knihovnu z jiného programu

V `main.py` importujte pouze veřejné rozhraní balíčku. Sestavte krátkou ukázku,
která vytvoří dva vektory, sečte je, vypočítá skalární součin a předvede chybu
při neshodných rozměrech.

`main.py` nesmí přistupovat k vnitřnímu seznamu souřadnic ani importovat přímo
z `vectorlib.vector`.

## 7. Zkontrolujte dokumentaci

Prohlédněte veřejné rozhraní pomocí:

```powershell
python -m pydoc vectorlib
python -c "from vectorlib import Vector; help(Vector)"
```

Ve dvojici ověřte, zda lze podle dokumentace zjistit:

- jak vytvořit vektor,
- co vrací `+` a `*`,
- kdy vznikne `ValueError`,
- zda operace mění původní objekty.

Na samostatném cvičení budete stejný princip balíčku rozvíjet na odlišném
projektu `textkit`, aby nešlo pouze o opisování společné ukázky.
