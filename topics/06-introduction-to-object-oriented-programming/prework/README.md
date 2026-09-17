# Domácí příprava: úvod do OOP

Krátké zopakování tříd a objektů. Úkol 1 řešte nejprve bez počítače,
pak program spusťte a porovnejte. Ukázková řešení otevřete až po
vlastním pokusu.

## Úkol 1: Přečtěte třídu

```python
class Counter:
    def __init__(self, start=0):
        self.value = start

    def increment(self, step=1):
        self.value += step


a = Counter()
b = Counter(10)
a.increment()
a.increment(5)
b.increment()
print(a.value, b.value)
```

Co program vypíše? Kolik objektů vznikne a na co odkazuje `self` při
volání `a.increment(5)`?

<details>
<summary>Ukázkové řešení</summary>

Program vypíše `6 11`.

Vzniknou **dva** objekty, `a` a `b`, a každý má svůj vlastní atribut
`value`. Třída `Counter` je jen předpis, podle kterého se objekty vytvářejí.

Volání `a.increment(5)` Python provede jako `Counter.increment(a, 5)` —
`self` tedy odkazuje na objekt `a`.

</details>

## Úkol 2: Bankovní účet

Napište třídu `BankAccount`:

- konstruktor `__init__(self, owner, balance=0)` uloží jméno majitele
  a zůstatek,
- metoda `deposit(amount)` vloží peníze,
- metoda `withdraw(amount)` peníze vybere, nebo při nedostatku vypíše
  `Nedostatek prostředků` a zůstatek nezmění,
- metoda `describe()` vrátí řetězec ve tvaru `Jana: 700.00 Kč`.

Ověřte ji tímto kódem:

```python
acc = BankAccount("Jana")
acc.deposit(1000)
acc.withdraw(300)
acc.withdraw(5000)       # Nedostatek prostředků
print(acc.describe())    # Jana: 700.00 Kč
```

<details>
<summary>Ukázkové řešení</summary>

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Nedostatek prostředků")
            return
        self.balance -= amount

    def describe(self):
        return f"{self.owner}: {self.balance:.2f} Kč"
```

Data (majitel a zůstatek) jsou pohromadě s operacemi, které s nimi
pracují. Když potřebujeme další účet, stačí vytvořit další objekt.

</details>
