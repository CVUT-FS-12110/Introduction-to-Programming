# Ukázková prezentace: `range()`

**Délka prezentace:** přibližně 5 minut  
**Rozsah kódu:** 5–20 řádků  
**Cíl:** Ukázat použití `range()` v Pythonu a vysvětlit jeho fungování.

## 1. Ukázkový kód

*Tohle nahrajete do Moodle.*

```python
# Čísla od 0 do 4
for i in range(5):
    print(i)

# Čísla od 3 do 7
for i in range(3, 8):
    print(i)

# Sudá čísla od 2 do 10
for i in range(2, 11, 2):
    print(i)

# Odpočítávání
for i in range(5, 0, -1):
    print(i)

# Průchod seznamem pomocí indexů
names = ["Anna", "Petr", "Eva"]
for i in range(len(names)):
    print(i, names[i])
```

## 2. Co by měl student / měla studentka vysvětlit

*Tohle vysvětlíte před třídou u svého kódu.*

Funkce `range()` slouží k vytváření posloupnosti celých čísel. Nejčastěji se používá v cyklu `for`, například když chceme nějakou operaci několikrát zopakovat.

`range()` může mít jeden, dva nebo tři argumenty:

- `range(stop)` – čísla od 0 do `stop - 1`.
- `range(start, stop)` – čísla od `start` do `stop - 1`.
- `range(start, stop, step)` – posloupnost s určeným krokem.

**Důležité je, že koncová hodnota `stop` není součástí posloupnosti.**

V prvním příkladu `range(5)` získáme čísla 0 až 4.

Ve druhém příkladu `range(3, 8)` začínáme na čísle 3 a končíme na 7.

Ve třetím příkladu `range(2, 11, 2)` používáme krok 2, takže získáme sudá čísla od 2 do 10.

Krok může být také záporný. Ve čtvrtém příkladu odpočítáváme od 5 do 1.

V posledním příkladu používáme `range(len(names))` pro získání indexů seznamu. Pokud ale potřebujeme index i hodnotu, bývá vhodnější použít `enumerate()`.

**`range()` nevytváří seznam čísel.** Vrací objekt typu `range`, který reprezentuje číselnou posloupnost, aniž by musel ukládat všechny její prvky jednotlivě do paměti.

## 3. Otázky učitele a očekávané odpovědi

*Tohle bude následovat po prezentaci.*

### Otázka 1

**Co vypíše `range(3)` při průchodu cyklem `for`?**

Očekávaná odpověď: `0, 1, 2`. Koncová hodnota 3 není zahrnuta.

### Otázka 2

**Co se stane při `range(5, 5)`?**

Očekávaná odpověď: Vznikne prázdná posloupnost. Cyklus se nevykoná ani jednou.

### Otázka 3

**Co vypíše `range(5, 0)`?**

Očekávaná odpověď: Nic. Výchozí krok je +1, takže posloupnost je prázdná.

### Otázka 4

**Co se stane při `range(0, 10, 0)`?**

Očekávaná odpověď: Python vyvolá `ValueError`, protože krok nesmí být nulový.

### Otázka 5

**Jak vytvoříš posloupnost 10, 8, 6, 4, 2?**

Očekávaná odpověď: `range(10, 0, -2)`.

### Otázka 6

**Jaký je rozdíl mezi `range(1000000)` a `list(range(1000000))`?**

Očekávaná odpověď: `range` reprezentuje posloupnost úsporně, zatímco `list` vytvoří a uloží milion jednotlivých čísel.

### Otázka 7

**Kdy je vhodnější použít `enumerate()` než `range(len(...))`?**

Očekávaná odpověď: Když potřebujeme současně index a hodnotu prvku seznamu. Pokud potřebujeme pouze hodnoty, můžeme procházet seznam přímo.

## 4. Co se hodnotí

- **Správnost kódu:** Ukázka funguje a demonstruje různé způsoby použití.
- **Porozumění:** Student/studentka dokáže vysvětlit argumenty `start`, `stop` a `step`.
- **Praktické využití:** Student/studentka ví, kdy a proč `range()` použít.
- **Schopnost odpovídat:** Student/studentka dokáže reagovat na doplňující otázky.
- **Srozumitelnost prezentace:** Student/studentka vysvětluje vlastní kód a dodrží časový limit.