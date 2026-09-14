# Cvičení: úvod do OOP

Cvičení je **samostatná práce na 90 minut**. Úlohy jsou seřazené od
nejjednodušších po nejtěžší a nepočítá se s tím, že stihnete všechny —
poslední úlohy jsou výzvou i pro zkušené programátory. Začněte tam, kde
se cítíte jistí. Pokud už programovat umíte, klidně první úlohy přeskočte.

| Obtížnost | Co znamená |
|-----------|------------|
| ★ | procvičení základů z přednášky |
| ★★ | je potřeba spojit více věcí dohromady |
| ★★★ | vyžaduje vlastní úvahu a hledání v dokumentaci |
| ★★★★ | výzva pro ty, kdo chtějí jít dál |

Každou úlohu řešte v samostatném souboru (například `task1.py`) a průběžně
ji commitujte do svého repozitáře `progintro`. Ukázky běhu slouží ke
kontrole — výstup se nemusí shodovat do posledního znaku, výsledky ano.
Části označené **Rozšíření** jsou nepovinné pokračování pro ty, kdo
základní zadání zvládli.

---

## 1. Obdélník ★

Napište třídu `Rectangle` s atributy `width` a `height` a metodami:

- `area()` a `perimeter()` — obsah a obvod,
- `is_square()` — vrátí `True`, pokud je obdélník čtverec,
- `scale(factor)` — zvětší oba rozměry `factor`krát,
- `describe()` — vrátí řetězec, například `Obdélník 3 × 4, obsah 12`.

Vytvořte seznam alespoň tří obdélníků, vypište jejich popis a najděte
ten s největším obsahem.

## 2. Vektor v rovině ★★

Napište třídu `Vector2D` se souřadnicemi `x` a `y` a metodami:

- `length()` — délka vektoru,
- `add(other)` — vrátí **nový** vektor, který je součtem obou,
- `scale(k)` — vrátí nový vektor `k`krát delší,
- `dot(other)` — skalární součin,
- `angle_to(other)` — úhel mezi vektory ve stupních.

Aby šel vektor rozumně vypsat pomocí `print()`, doplňte speciální metodu
`__str__`.

```python
u = Vector2D(3, 4)
v = Vector2D(1, 0)
print(u, u.length())                    # (3, 4) 5.0
print(u.add(v))                         # (4, 4)
print(v.angle_to(Vector2D(0, 1)))       # 90.0
```

Proč `add` vrací nový vektor, místo aby změnil ten stávající?

**Rozšíření:** Doplňte speciální metody `__add__`, `__mul__` a `__eq__`,
aby fungovaly zápisy `u + v`, `u * 2` a `u == v`.

## 3. Sklad ★★

Napište dvě spolupracující třídy:

- `Item` — položka skladu s atributy `name`, `unit_price` a `quantity`,
- `Warehouse` — sklad, který uchovává seznam položek a má metody:
  - `add(name, unit_price, quantity)` — přidá položku. Pokud už ve skladu
    je, jen navýší množství,
  - `remove(name, quantity)` — vydá zboží. Vrátí `False`, pokud
    položka neexistuje nebo jí je málo,
  - `find(name)` — vrátí objekt `Item`, nebo `None`,
  - `total_value()` — celková hodnota skladu,
  - `low_stock(limit)` — seznam názvů položek, kterých je méně než `limit`,
  - `report()` — vypíše přehlednou tabulku skladu.

Napište krátký scénář, který sklad naplní, několikrát z něj vydá zboží
(i neúspěšně) a vypíše závěrečný přehled.

**Rozšíření:** Sklad si vede historii všech pohybů (příjem a výdej, datum,
množství) a umí vypsat historii jedné položky.

## 4. Zlomky ★★★

Napište třídu `Fraction` pro přesné počítání se zlomky:

- zlomek se po vytvoření vždy **zkrátí** (`math.gcd`) a znaménko je jen
  v čitateli,
- jmenovatel 0 vyvolá výjimku: `raise ValueError("Jmenovatel nesmí být 0")`,
- speciální metody `__str__`, `__add__`, `__sub__`, `__mul__`,
  `__truediv__`, `__eq__` a `__lt__`,
- metoda `to_float()`.

```python
print(Fraction(1, 2) + Fraction(1, 3))    # 5/6
print(Fraction(2, -4))                    # -1/2
print(Fraction(1, 3) < Fraction(1, 2))    # True
```

Sečtěte zlomky 1/1 + 1/2 + … + 1/10 (vyjde 7381/2520) a výsledek porovnejte
se stejným součtem v `float`.

**Rozšíření:** Podporujte i počítání s celými čísly (`Fraction(1, 2) + 1`
i `1 + Fraction(1, 2)`). Hledejte v dokumentaci metodu `__radd__`.

## 5. Geometrické tvary a dědičnost ★★★

Navrhněte hierarchii tříd:

- `Shape` — obecný tvar se jménem. Metody `area()` a `perimeter()` jen
  vyvolají `NotImplementedError`. Metoda `describe()` je napsaná jen
  jednou, zde, a používá `area()` a `perimeter()`,
- `Circle`, `Rectangle` a `Triangle` (obsah podle Heronova vzorce) dědí
  ze `Shape`,
- `Square` dědí z `Rectangle`,
- `Triangle` při vytvoření ověří trojúhelníkovou nerovnost a pro
  neplatné strany vyvolá `ValueError`.

Vytvořte seznam různých tvarů a v **jednom** cyklu vypište jejich popisy,
celkový obsah a tvar s největším obvodem. Kde v programu se projevuje
polymorfismus?

**Rozšíření:** Tvary seřaďte podle obsahu pomocí `sorted()` s parametrem
`key`. Pak doplňte speciální metodu `__lt__`, aby šlo použít `sorted()`
bez `key`.

## 6. Matice ★★★

Napište třídu `Matrix`, která uchovává matici jako seznam seznamů:

- konstruktor ověří, že všechny řádky mají stejnou délku,
- `shape()` vrátí dvojici (počet řádků, počet sloupců),
- `__str__` vypíše matici se zarovnanými sloupci,
- `transpose()` vrátí novou transponovanou matici,
- `__add__` a `__mul__` — součet a maticový součin. Pokud rozměry
  nesedí, vyvolají `ValueError`,
- `identity(n)` — jednotková matice; zjistěte, co je `@staticmethod`.

**Rozšíření:** Doplňte výpočet determinantu (rozvojem podle řádku,
rekurzivně) a inverzní matice. Pak s nimi vyřešte obvod s rezistory
ze semináře k tématu
[Datové typy a vstup/výstup](../../03-data-types-io/README.md).

## 7. Piškvorky ★★★★

Naprogramujte piškvorky pro dva hráče na hrací ploše `n × n`, kde vyhrává
ten, kdo má `k` svých značek v řadě (vodorovně, svisle nebo úhlopříčně).

Navrhněte třídy:

- `Board` — hrací plocha: položení značky, kontrola volného pole,
  zjištění vítěze, `__str__` pro vykreslení,
- `Player` — společný předek hráčů s metodou `choose_move(board)`,
- `HumanPlayer` — tah načte od uživatele,
- `RandomPlayer` — táhne náhodně na volné pole,
- `SmartPlayer` — vyhraje, může-li. Jinak zablokuje soupeřovu výhru.
  Jinak táhne náhodně,
- `Game` — střídá hráče, dokud někdo nevyhraje nebo není plocha plná.

Třída `Game` nesmí vědět, jaký typ hráče zrovna táhne — jen zavolá
`choose_move`.

**Rozšíření:**

- Sehrajte 1000 her `RandomPlayer` proti `SmartPlayer` a vypište statistiku.
- Pro plochu 3 × 3 napište hráče používajícího algoritmus *minimax*,
  který nikdy neprohraje.
