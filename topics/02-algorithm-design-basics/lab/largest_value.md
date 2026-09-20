# Hledání největší hodnoty

Navrhněte algoritmus, který načte **pět čísel** a vypíše největší z nich.
Nepoužívejte vestavěnou funkci `max()`. Cílem je procvičit průběžné
zpracování vstupů: program si pamatuje dosud největší hodnotu a s každým
novým číslem ji případně aktualizuje.

Největší hodnotu neinicializujte nulou — všechna zadaná čísla mohou být
záporná. Jako první hodnotu proto použijte první skutečně načtené číslo.

## Vývojový diagram

```mermaid
flowchart TD
    start([Start]) --> first["Načti první číslo"]
    first --> init["largest = první číslo<br/>i = 2"]
    init --> loop{"i <= 5?"}
    loop -- ne --> output["Vypiš largest"]
    output --> stop([Konec])
    loop -- ano --> read["Načti x"]
    read --> compare{"x > largest?"}
    compare -- ano --> replace["largest = x"]
    compare -- ne --> increment["i = i + 1"]
    replace --> increment
    increment --> loop
```

## Pseudokód

```text
NAČTI první číslo
largest = první číslo

PRO i od 2 do 5
    NAČTI x
    POKUD x > largest
        largest = x
    KONEC POKUD
KONEC PRO

VYPIŠ largest
```

## Ukázková implementace v Pythonu

```python
largest = float(input("Value #1: "))

for i in range(2, 6):
    value = float(input(f"Value #{i}: "))
    if value > largest:
        largest = value

print("Largest value:", largest)
```

## Rozšíření

Upravte algoritmus tak, aby zároveň našel nejmenší hodnotu a pozici prvního
výskytu největší hodnoty.
