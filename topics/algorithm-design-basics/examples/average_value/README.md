# Výpočet průměrné hodnoty

Tento úkol slouží jako úvod do **algoritmizace**, práce se **smyčkami**, **proměnnými** a základního **postupného zpracování dat**.  
Studenti se seznámí s tím, jak lze stejný algoritmus popsat pomocí **diagramu**, **pseudokódu** a **programu v Pythonu**.


## UML Activity diagram

Následující diagram znázorňuje krok za krokem algoritmus pro výpočet průměrné hodnoty z pevně daného počtu vstupů:

![Activity diagram – výpočet průměru](activity.png)


## Pseudokód

```
NASTAV N = 5
NASTAV total = 0

VYPIŠ "Zadej N čísel"

PRO i od 1 do N
NAČTI x
total = total + x
KONEC PRO

average = total / N
VYPIŠ average
```

## Ukázková implementace v Pythonu

```python
# number of values (constant)
N = 5

total = 0

print(f"Enter {N} numbers:")

for i in range(1, N + 1):
    x = float(input(f"Value #{i}: "))
    total = total + x

average = total / N
print("Average value:", average)
```