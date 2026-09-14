# Domácí příprava: podmínky a cykly

Krátké zopakování podmínek a cyklů. Úkol 1 řešte nejprve bez počítače,
pak program spusťte a porovnejte. Ukázková řešení otevřete až po
vlastním pokusu.

## Úkol 1: Sledujte stav programu

```python
values = [3, 8, -1, 6, 0, 5]
total = 0
count = 0

for v in values:
    if v < 0:
        continue
    if v == 0:
        break
    total += v
    count += 1

print(count, total)
```

Pro každý průchod cyklem si zapište hodnoty `v`, `total` a `count`.
Co program vypíše a který prvek seznamu se nezpracuje vůbec?

<details>
<summary>Ukázkové řešení</summary>

| Průchod | `v` | Co se stane | `total` | `count` |
|---------|-----|-------------|---------|---------|
| 1 | `3` | přičte se | 3 | 1 |
| 2 | `8` | přičte se | 11 | 2 |
| 3 | `-1` | `continue` — přeskočí zbytek těla | 11 | 2 |
| 4 | `6` | přičte se | 17 | 3 |
| 5 | `0` | `break` — cyklus končí | 17 | 3 |

Program vypíše `3 17`. Poslední prvek `5` se nezpracuje, protože cyklus
skončil už na nule.

</details>

## Úkol 2: Statistika zadaných čísel

Napište program, který načítá celá čísla, dokud uživatel nezadá prázdný
řádek (jen stiskne Enter). Potom vypíše počet čísel a největší z nich.
Nepoužívejte funkci `max()`. Pokud uživatel nic nezadá, vypíše
`Nebylo zadáno žádné číslo.`

```
Číslo (Enter = konec): 4
Číslo (Enter = konec): 11
Číslo (Enter = konec): -3
Číslo (Enter = konec):
Počet: 3
Maximum: 11
```

<details>
<summary>Ukázkové řešení</summary>

```python
count = 0
largest = None

while True:
    line = input("Číslo (Enter = konec): ")
    if line == "":
        break

    number = int(line)
    count += 1
    if largest is None or number > largest:
        largest = number

if count == 0:
    print("Nebylo zadáno žádné číslo.")
else:
    print("Počet:", count)
    print("Maximum:", largest)
```

Cyklus `while` je zde vhodnější než `for`, protože předem nevíme, kolik
čísel uživatel zadá. Počáteční hodnota `None` místo `0` zajistí správný
výsledek, i když uživatel zadá jen záporná čísla.

</details>
