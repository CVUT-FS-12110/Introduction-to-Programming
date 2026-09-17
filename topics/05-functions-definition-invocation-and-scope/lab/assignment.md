# Cvičení: funkce

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

Pro všechny úlohy platí:

- funkce, které něco počítají, výsledek **vracejí** a nic nevypisují,
- vstup a výpis patří do funkce `main()` spouštěné pomocí
  `if __name__ == "__main__":`,
- nepoužívejte globální proměnné (kromě konstant).

---

## 1. Hmotnost trubky ★

Napište funkce:

- `circle_area(d)` — obsah kruhu o průměru `d`,
- `tube_cross_section(d_out, d_in)` — obsah průřezu trubky
  (využijte `circle_area`),
- `tube_mass(d_out, d_in, length, density=7850)` — hmotnost trubky v kg.
  Rozměry jsou v metrech, hustota v kg/m³ a výchozí hodnota odpovídá oceli.

Ověřte je:

```python
print(tube_mass(0.060, 0.050, 6))                # ocelová trubka: ≈ 40.69 kg
print(tube_mass(0.060, 0.050, 6, density=2700))  # hliníková: ≈ 14.00 kg
```

**Rozšíření:** Program vypíše tabulku hmotností šestimetrových ocelových
trubek s vnějším průměrem 60 mm a tloušťkou stěny 1 až 5 mm.

## 2. Převod teplot ★

Napište funkci `convert_temperature(value, from_unit, to_unit)`, kde
jednotky jsou `"C"`, `"F"` nebo `"K"`. Pro neznámou jednotku funkce vrátí
`None`. Nápověda: nejjednodušší je převést hodnotu nejdřív na °C a teprve
potom do cílové jednotky.

```python
print(convert_temperature(100, "C", "F"))   # 212.0
print(convert_temperature(0, "K", "C"))     # -273.15
print(convert_temperature(-40, "C", "F"))   # -40.0
print(convert_temperature(20, "C", "X"))    # None
```

Pomocí této funkce pak vypište převodní tabulku °C → °F → K pro teploty
od −40 do 100 °C po 20 stupních.

## 3. Statistika měření ★★

Napište funkce pro seznam naměřených hodnot:

- `mean(values)` — aritmetický průměr,
- `median(values)` — medián,
- `std_dev(values)` — směrodatná odchylka (√(součet (x − průměr)² / n)),
- `min_max(values)` — vrátí **dvojici** (nejmenší, největší) bez použití
  `min()` a `max()`,
- `summary(values)` — vrátí slovník se všemi výsledky výše.

```python
data = [2, 4, 4, 4, 5, 5, 7, 9]
print(summary(data))
# {'mean': 5.0, 'median': 4.5, 'std_dev': 2.0, 'min': 2, 'max': 9}
```

Pozor: funkce `median` potřebuje hodnoty seřadit, ale **nesmí změnit**
seznam, který dostala. Ověřte, že `data` je po zavolání `summary(data)`
stále ve stejném pořadí. Jaký je rozdíl mezi `values.sort()`
a `sorted(values)`?

## 4. Kontrola rodného čísla ★★

Pro rodná čísla ve tvaru `RRMMDD/XXXX` platí (zjednodušeně) tato pravidla:

- celé desetimístné číslo (bez lomítka) je dělitelné 11,
- u žen je k měsíci připočteno 50,
- dvojčíslí roku `00`–`53` znamená roky 2000–2053, `54`–`99` roky 1954–1999.

Napište funkce:

- `normalize(birth_number)` — odstraní lomítko a mezery, vrátí řetězec
  10 číslic, nebo `None`, pokud vstup nemá správný tvar,
- `is_valid(birth_number)` — ověří tvar, dělitelnost 11 a platnost měsíce,
- `gender(birth_number)` — vrátí `"muž"` nebo `"žena"`,
- `birth_date(birth_number)` — vrátí datum narození jako řetězec.

```
736028/5163 → platné, žena, 28. 10. 1973
990101/1230 → platné, muž, 1. 1. 1999
736028/5164 → neplatné
```

**Rozšíření:** Ověřte, že datum opravdu existuje (nepřipustí 30. února),
včetně přestupných roků. Kolik funkcí z předchozích úloh můžete znovu
použít?

## 5. Numerická integrace ★★★

V Pythonu je funkce také hodnota — lze ji předat jako argument jiné funkci:

```python
import math


def apply_twice(f, x):
    return f(f(x))


print(apply_twice(math.sqrt, 16))  # 2.0
```

Napište funkce, které přibližně spočítají určitý integrál funkce `f`
na intervalu ⟨a, b⟩ rozděleném na `n` dílků:

- `rectangle(f, a, b, n)` — obdélníková metoda (hodnota ve středu dílku),
- `trapezoid(f, a, b, n)` — lichoběžníková metoda,
- `simpson(f, a, b, n)` — Simpsonova metoda (`n` sudé).

Ověřte je na integrálu funkce sin x od 0 do π, který je přesně 2.
Vypište tabulku chyb jednotlivých metod pro n = 4, 8, 16, 32 a 64.
Kolikrát se chyba zmenší, když zdvojnásobíte n? Liší se to u jednotlivých
metod?

**Rozšíření:** Napište funkci `integrate(f, a, b, tolerance)`, která sama
zdvojnásobuje `n`, dokud se dva po sobě jdoucí výsledky neliší méně než
o `tolerance`.

## 6. Rekurze a cena opakovaných výpočtů ★★★

1. Napište rekurzivní funkci `factorial(n)`.
2. Napište rekurzivní funkci `fib(n)` pro n-tý člen Fibonacciho
   posloupnosti (`fib(0) = 0`, `fib(1) = 1`).
3. Zjistěte, kolikrát se `fib` zavolá při výpočtu `fib(10)`, `fib(20)`
   a `fib(25)`. Pro `fib(10)` má vyjít 177 volání. Vymyslete, jak volání
   počítat **bez globální proměnné**.
4. Napište iterativní verzi `fib_iter(n)` a porovnejte dobu výpočtu
   pro n = 30.
5. Napište verzi `fib_memo(n, memo)`, která si už spočítané hodnoty
   ukládá do slovníku `memo` předávaného jako parametr.

## 7. Hanojské věže ★★★

Na tyči A je `n` disků seřazených od největšího (dole) po nejmenší. Úkolem
je přesunout všechny na tyč C. Najednou lze přesunout jen jeden disk
a nikdy nesmí větší disk ležet na menším. Pomocnou tyčí je B.

Napište rekurzivní funkci `hanoi(n, source, target, helper)`, která vypíše
jednotlivé tahy a vrátí jejich počet.

```
Počet disků: 3
A → C
A → B
C → B
A → C
B → A
B → C
A → C
Počet tahů: 7
```

Ověřte, že počet tahů je vždy 2ⁿ − 1.

**Rozšíření:** Uchovávejte obsah všech tří tyčí v seznamech a po každém
tahu vykreslete jejich stav. Zkontrolujte, že se nikdy neporuší pravidlo
o velikosti disků.

## 8. Kalkulačka bez `eval` ★★★★

Napište funkci `evaluate(expression)`, která spočítá hodnotu aritmetického
výrazu zadaného jako řetězec — **bez použití** `eval()`.

```python
print(evaluate("2 * (3 + 4) - 10 / 5"))   # 12.0
print(evaluate("-(1 + 2) * 3"))           # -9.0
```

Doporučený postup:

1. `tokenize(text)` — rozdělí text na seznam tokenů (čísla, operátory,
   závorky).
2. Rozklad podle gramatiky, kde pro každé pravidlo napíšete jednu funkci
   (tzv. *rekurzivní sestup*):
   - výraz = člen, za kterým následuje libovolně mnoho `+` nebo `-` a člen,
   - člen = činitel, za kterým následuje libovolně mnoho `*` nebo `/`
     a činitel,
   - činitel = číslo, nebo výraz v závorkách, nebo `-` a činitel.

Uvědomte si, proč toto rozdělení samo zajistí správnou přednost operátorů.

**Rozšíření:**

- Mocnina `^` (pozor, `2 ^ 3 ^ 2` je 2⁹, ne 8²).
- Proměnné, jejichž hodnoty funkce dostane ve slovníku.
- Srozumitelné chybové hlášení s pozicí chyby (`chybí ")" na pozici 7`).
