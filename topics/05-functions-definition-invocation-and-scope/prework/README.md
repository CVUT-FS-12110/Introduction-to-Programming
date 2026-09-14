# Domácí příprava: funkce

Krátké zopakování definice a volání funkcí. Úkol 1 řešte nejprve bez
počítače, pak program spusťte a porovnejte. Ukázková řešení otevřete až
po vlastním pokusu.

## Úkol 1: Co program vypíše?

```python
x = 10


def double_print(x):
    print(x * 2)


def double_return(x):
    return x * 2


a = double_print(5)
b = double_return(5)
print("a =", a)
print("b =", b)
print("x =", x)
```

Proč mají `a` a `b` různou hodnotu? A proč se nezměnila globální
proměnná `x`?

<details>
<summary>Ukázkové řešení</summary>

```
10
a = None
b = 10
x = 10
```

Funkce `double_print` hodnotu jen vypíše. Nemá `return`, a proto vrací
`None`. Funkce `double_return` výsledek vrátí, takže ho lze uložit
do proměnné nebo použít v dalším výpočtu.

Parametr `x` uvnitř funkcí je **lokální** proměnná — existuje jen během
volání funkce a s globální proměnnou `x` nemá nic společného.

</details>

## Úkol 2: Napište vlastní funkce

Napište dvě funkce, které nic nevypisují, jen vracejí výsledek:

1. `max_of_three(a, b, c)` — vrátí největší ze tří čísel (bez použití `max()`),
2. `format_price(amount, currency="Kč")` — vrátí řetězec s částkou
   na dvě desetinná místa a měnou.

Ověřte je těmito voláními:

```python
print(max_of_three(3, 9, 5))             # 9
print(max_of_three(-1, -8, -3))          # -1
print(format_price(1800))                # 1800.00 Kč
print(format_price(72.5, currency="€"))  # 72.50 €
```

<details>
<summary>Ukázkové řešení</summary>

```python
def max_of_three(a, b, c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest


def format_price(amount, currency="Kč"):
    return f"{amount:.2f} {currency}"
```

Parametr `currency` má výchozí hodnotu, a proto ho při volání můžeme
vynechat. Ve volání `format_price(72.5, currency="€")` jsme ho předali
jako **pojmenovaný argument**.

</details>
