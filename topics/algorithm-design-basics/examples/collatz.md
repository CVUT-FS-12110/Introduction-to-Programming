# Collatzova posloupnost

Collatzova posloupnost začíná libovolným kladným celým číslem:

- je-li aktuální číslo sudé, vydělí se dvěma,
- je-li aktuální číslo liché, vynásobí se třemi a přičte se jedna,
- postup se opakuje, dokud posloupnost nedojde k číslu 1.

## Zadání

Přečtěte si následující program, projděte jeho průběh pro několik různých vstupů a nakreslete diagram (flowchart / UML activity diagram), který jeho průběh znázorní.

```python
n = int(input("Zadejte kladné celé číslo: "))
steps = 0

while n != 1:
    print(n)

    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1

    steps += 1

print(n)
print("Počet kroků:", steps)
```

Při kreslení diagramu se zaměřte na:

- podmínku ukončení cyklu,
- rozlišení sudého a lichého čísla,
- aktualizaci hodnot `n` a `steps`,
- pořadí výpisů programu.
