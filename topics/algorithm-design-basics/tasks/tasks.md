# Instrukce ke cvičení

Vaším úkolem je pro následující programy nakreslit **UML activity diagram (diagram aktivit)**.

- Každý program si pečlivě přečtěte a pochopte jeho logiku.
- Na papír zakreslete odpovídající diagram aktivit, který vystihuje:
  - tok programu,
  - podmínky (`if`),
  - cykly (`for`, `while`),
  - případná předčasná ukončení (`break`, `continue`).


## Organizace práce

- Máte čas omezený trváním cvičení.
- Úloh je více – **vaším cílem je vyřešit jich co nejvíce**.
- Začněte od první (nejjednodušší) a pokračujte dále podle obtížnosti.


## Důležité

- Diagram musí být **přehledný a správně strukturovaný**.
- Používejte standardní prvky UML activity diagramu:
  - start / end
  - akce (činnosti)
  - rozhodovací uzly (větvení)
  - cykly (zpětné hrany)
- Dbejte na správné zakreslení toku (šipek).

## Doporučení

- Nejprve si zkuste program „projít v hlavě“.
- Zaměřte se na:
  - kdy se podmínky vyhodnocují,
  - kam se program vrací při cyklu,
  - kdy může dojít k ukončení cyklu.

**Cíl:** Nejde jen o kreslení diagramů, ale o pochopení řízení toku programu.

## Zadání úloh

### Úloha 1
```Python
numbers = [3, 8, 1, 6, 5]

sum_even = 0
sum_odd = 0

for n in numbers:
    if n % 2 == 0:
        sum_even += n
    else:
        sum_odd += n

print("Even:", sum_even)
print("Odd:", sum_odd)
```

### Úloha 2
```Python
numbers = [4, 9, 2, 7, 6, 3, 8]

i = 0
total = 0

while i < len(numbers):
    n = numbers[i]

    if n == 7:
        break

    if n % 2 == 0:
        total += n

    i += 1

print(total)
```

### Úloha 3
```Python
numbers = [5, 12, 7, 18, 3, 10, 6]

i = 0
total = 0

while i < len(numbers):
    n = numbers[i]

    if n < 0:
        i += 1
        continue

    for j in range(n):
        if j > 5:
            break

        if j % 2 == 0:
            total += j
        else:
            total -= j

    if total > 20:
        break

    i += 1

print(total)
```

### Úloha 4

```Python
numbers = [4, 7, 2, 9, 5]

total = 0

for n in numbers:
    partial = 0

    for i in range(1, n + 1):
        if i % 2 == 0:
            partial += i
        else:
            partial -= i

        if partial > 3:
            break

    if partial < 0:
        total += 1
    else:
        total += partial

print(total)
```