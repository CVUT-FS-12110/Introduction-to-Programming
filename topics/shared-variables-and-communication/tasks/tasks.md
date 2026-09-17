# Instrukce ke cvičení

Vaším úkolem je analyzovat kód trpící problémy se sdíleným stavem, opravit ho
a porozumět záludnostem mutabilních argumentů v Pythonu.

## Organizace práce

- Máte čas omezený trváním cvičení.
- Úloh je více — **vaším cílem je vyřešit jich co nejvíce**.
- Začněte od první (nejjednodušší) a pokračujte dále podle obtížnosti.

## Důležité

- Každou úlohu řešte v samostatné složce s vlastním souborem `main.py`.
- Kód musí být spustitelný příkazem `python main.py` z terminálu.

---

## Domácí příprava

### Čtení

Nastudujte pravidla viditelnosti proměnných v Pythonu — tzv. pravidlo
**LEGB** (Local, Enclosing, Global, Built-in).

Výchozí bod: [Real Python — Python Scope & the LEGB Rule](https://realpython.com/python-scope-legb-rule/)

Zaměřte se zejména na:
- co přesně znamená „globální proměnná" v Pythonu
- co dělá klíčové slovo `global` uvnitř funkce
- proč je používání `global` ve větších projektech problematické

### Praktická část

Otevřete soubor [`examples/global_variable_problem/main.py`](../examples/global_variable_problem/main.py)
a spusťte ho.

Poté zkuste kód rozšířit o třetího hráče **Charlie**, jehož odpovědi se
*střídají s Alicenými* (tzn. Alice odpoví, pak Charlie, pak Alice, pak Charlie…).
Přijďte připraveni odpovědět na tyto otázky:

1. Je to bez úpravy stávajících funkcí vůbec možné?
2. Co se stane, když zapomenete zavolat `reset()` před Bobem?
3. Jak byste napsali test, který ověří, že `answer_question(True)` přičte 10 bodů —
   aniž byste se spoléhali na globální stav?

---

## Zadání úloh

### Úloha 1 — Analýza globálního stavu

Otevřete [`examples/global_variable_problem/main.py`](../examples/global_variable_problem/main.py).

Prostudujte kód a odpovězte na tyto otázky (stačí krátký komentář přímo v kódu):

1. Vypište všechny globální proměnné, které program používá.
2. Co se stane, pokud přidáte třetí kolo pro **Charlie** bez zavolání `reset()`
   po Alicině kole?
3. Proč je obtížné funkci `answer_question` testovat v izolaci?

Poté si otevřete [`examples/explicit_state_passing/main.py`](../examples/explicit_state_passing/main.py)
a porovnejte přístup s verzí výše.

---

### Úloha 2 — Refaktoring: z globálních proměnných na explicitní předávání

Níže je kód nákupního košíku, který k uchovávání stavu používá globální proměnné.

```python
# Global state - bad practice!
cart_items = []
cart_total = 0.0


def add_item(name: str, price: float) -> None:
    global cart_items, cart_total
    cart_items.append(name)
    cart_total += price


def remove_item(name: str, price: float) -> None:
    global cart_items, cart_total
    if name in cart_items:
        cart_items.remove(name)
        cart_total -= price


def get_summary() -> str:
    return f"Items: {cart_items}, Total: {cart_total:.2f} CZK"


if __name__ == "__main__":
    add_item("Kniha", 299.0)
    add_item("Pero", 25.0)
    add_item("Sešit", 45.0)
    remove_item("Pero", 25.0)
    print(get_summary())
```

**Vaším úkolem je:**

1. Přepište kód tak, aby funkce nepracovaly s globálním stavem.
2. Stav košíku reprezentujte jako slovník (např. `{"items": [], "total": 0.0}`).
3. Napište funkci `create_cart()`, která vrátí nový prázdný košík.
4. Zajistěte, aby šlo mít dva **nezávislé** košíky — pro Alici a Boba.

Očekávaný výstup:
```
Alice: Items: ['Kniha', 'Sešit'], Total: 344.00 CZK
Bob:   Items: ['Pero'], Total: 25.00 CZK
```

---

### Úloha 3 — Záludný parametr

Níže jsou dvě funkce. Obě mají chybu spojenou s mutabilními argumenty.

```python
# Bug 1
def register_for_course(student: str, enrolled: list = []) -> list:
    enrolled.append(student)
    return enrolled


# Bug 2
def get_best_grades(grades: list[int], n: int) -> list[int]:
    grades.sort(reverse=True)
    return grades[:n]
```

**Vaším úkolem je:**

1. Pro každou funkci vysvětlete (komentářem), co je na ní špatně.
2. Napište kód, který chybu **demonstruje** — tj. zavolejte funkci tak,
   aby se projevilo neočekávané chování.
3. Obě funkce opravte.

> **Pravidlo:** Funkce by neměla měnit obsah argumentů, které dostane,
> pokud to není jejím výslovným účelem. Funkce, která vrací hodnotu,
> by měla zacházet se svými argumenty jako se vstupem pouze ke čtení.
> Python to demonstruje na vlastním standardním rozhraní: `sorted(items)`
> vrátí nový seznam, zatímco `items.sort()` seřadí seznam na místě
> a vrátí `None`.

Viz také příklad [`examples/mutable_argument_trap/main.py`](../examples/mutable_argument_trap/main.py).

---

### Úloha 4 — Třída jako nosič stavu (bonus)

Přepište vaše řešení z Úlohy 2 jako třídu `ShoppingCart`.

Třída musí:
- uchovávat seznam položek a celkovou cenu jako atributy instance
- mít metody `add_item(name, price)` a `remove_item(name, price)`
- mít metodu `summary()`, která vrátí textový přehled košíku jako řetězec

Očekávané chování:
```python
cart = ShoppingCart()
cart.add_item("Kniha", 299.0)
cart.add_item("Pero", 25.0)
cart.remove_item("Pero", 25.0)
print(cart.summary())  # Items: ['Kniha'], Total: 299.00 CZK
```

Inspirujte se příkladem [`examples/shared_state_with_class/main.py`](../examples/shared_state_with_class/main.py).
