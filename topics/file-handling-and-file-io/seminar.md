# Seminář: práce se soubory

V tomto semináři se naučíte používat soubory jako jednoduchý způsob, jak:

- načítat data do programu,
- ukládat výsledky i po skončení programu,
- bezpečně pracovat s textem mimo samotný běh aplikace.

Budeme pracovat hlavně s textovými soubory. Na konci se krátce podíváme i na to, že některé objekty se mohou **chovat jako soubor**, i když ve skutečnosti nejsou uložené na disku.

## Co byste měli po semináři umět

Po semináři byste měli zvládnout:

- otevřít soubor pro čtení nebo zápis,
- rozlišit základní režimy otevření souboru,
- bezpečně pracovat se soubory pomocí `with`,
- číst textový soubor po řádcích,
- zapisovat nový obsah i přidávat další řádky na konec,
- používat správné kódování textu,
- ošetřit běžnou chybu, kdy soubor neexistuje,
- chápat základní rozdíl mezi skutečným souborem a bufferem v paměti.

---

## 1. Zápis do souboru a čtení ze souboru

Soubor umožňuje uložit data tak, aby zůstala zachovaná i po skončení programu.

### Zápis

```python
with open("zprava.txt", "w", encoding="utf-8") as file:
    file.write("Ahoj světe!\n")
```

Tento program:

1. otevře soubor `zprava.txt`,
2. zapíše do něj text,
3. po skončení bloku `with` soubor automaticky zavře.

### Čtení

```python
with open("zprava.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

Režim otevření určuje, co se souborem děláme.

| Režim | Význam |
| --- | --- |
| `"r"` | čtení existujícího souboru |
| `"w"` | zápis od začátku, původní obsah se smaže |
| `"a"` | přidávání na konec souboru |
| `"b"` | binární režim, například pro obrázky nebo ZIP archivy |

> Pozor: otevření souboru s režimem `"w"` smaže jeho původní obsah.

---

## 2. Proč používat `with`

Soubor je potřeba po práci zavřít. Jinak může program zbytečně držet systémové prostředky nebo nemusí být zapsaná data správně dokončená.

Méně vhodná varianta:

```python
file = open("data.txt", "r", encoding="utf-8")
content = file.read()
file.close()
```

Doporučená varianta:

```python
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

Blok `with` se postará o zavření souboru automaticky, i kdyby při práci nastala chyba.

---

## 3. Čtení po řádcích

Když pracujeme s textovým souborem, často nechceme načíst všechno najednou. Můžeme procházet řádky postupně:

```python
with open("ukoly.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line)
```

Každý načtený řádek obvykle obsahuje i znak konce řádku. Proto se často používá `strip()` nebo `rstrip()`:

```python
with open("ukoly.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if line:
            print(line)
```

Tento kód:

- odstraní mezery a konce řádků na začátku a konci textu,
- přeskočí prázdné řádky,
- vypíše jen skutečný obsah.

---

## 4. Kódování textu

Text v souboru není uložen přímo jako „písmena“, ale jako bajty podle určitého pravidla zvaného **kódování**.

Proto při práci s textovými soubory běžně uvádíme:

```python
encoding="utf-8"
```

To je důležité hlavně u znaků jako:

```text
ěščřžýáíé
```

Bez správného kódování se může stát, že:

- program soubor nepřečte,
- nebo se text zobrazí nesprávně.

---

## 5. Co když soubor neexistuje

Práce se soubory závisí i na okolním prostředí. Program nemusí vždy najít to, co očekává.

Například:

```python
try:
    with open("ukoly.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Soubor ukoly.txt neexistuje.")
```

Tímto způsobem můžeme místo pádu programu zobrazit uživateli srozumitelnou zprávu.

---

## 6. Přidávání na konec souboru

Když chceme zachovat původní obsah a jen přidat další data, použijeme režim `"a"`.

Například jednoduchý deník:

```python
from datetime import datetime

message = input("Zadej poznámku: ")

with open("denik.txt", "a", encoding="utf-8") as file:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    file.write(f"{timestamp} | {message}\n")
```

Při každém spuštění programu přibude do souboru další řádek.  
Soubor tak slouží jako jednoduchá paměť programu mezi spuštěními.

---

## 7. Cesty k souborům

Soubor nemusí ležet ve stejné složce jako program. Proto je dobré umět pracovat s cestami.

V Pythonu se k tomu často používá `pathlib`:

```python
from pathlib import Path

path = Path("vystupy") / "report.txt"
path.parent.mkdir(exist_ok=True)
path.write_text("hotovo\n", encoding="utf-8")
```

Tento kód:

1. vytvoří cestu `vystupy/report.txt`,
2. zajistí existenci složky `vystupy`,
3. zapíše text do souboru.

`pathlib` je čitelnější a bezpečnější než ruční skládání cest pomocí řetězců.

### Vytváření složek

Složku můžeme vytvořit samostatně:

```python
from pathlib import Path

output_dir = Path("vystupy")
output_dir.mkdir(exist_ok=True)
```

Pokud potřebujeme vytvořit i více vnořených složek najednou, použijeme `parents=True`:

```python
from pathlib import Path

images_dir = Path("vystupy") / "obrazky" / "svg"
images_dir.mkdir(parents=True, exist_ok=True)
```

To je užitečné ve chvíli, kdy program sám připravuje místo pro své výstupy.

---

## 8. Jednoduché ukládání tabulkových dat

CSV soubor je obyčejný textový soubor, ve kterém jednotlivé hodnoty oddělujeme například čárkou.

Na první pokus ho můžeme vytvořit i úplně ručně:

```python
from pathlib import Path

csv_path = Path("measurements.csv")

if not csv_path.exists():
    with open(csv_path, "w", encoding="utf-8") as file:
        file.write("temperature,humidity\n")

temperature = 22.5
humidity = 41

with open(csv_path, "a", encoding="utf-8") as file:
    file.write(f"{temperature},{humidity}\n")
```

Při prvním spuštění se zapíše hlavička:

```text
temperature,humidity
```

Při každém dalším spuštění už program jen přidá nový řádek s daty:

```text
22.5,41
```

Tento způsob je záměrně jednoduchý. Pro složitější CSV soubory je později lepší použít modul `csv`, ale ruční varianta dobře ukazuje:

- kdy použít `"w"` a kdy `"a"`,
- proč je potřeba hlavičku zapsat jen jednou,
- že i běžné datové formáty jsou často jen textové soubory s dohodnutou strukturou.

---

## 9. Generování souboru, který otevře jiný program

Soubor nemusí být jen vstup nebo log. Program může vytvořit i soubor, který pak otevřeme v jiné aplikaci.

Například jednoduchý SVG obrázek:

```python
width = 320
height = 180
background_color = "#1f2937"
text_color = "#ffffff"
label = "Ahoj SVG"

svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">
  <rect width="100%" height="100%" fill="{background_color}" />
  <text
    x="50%"
    y="50%"
    fill="{text_color}"
    font-size="28"
    text-anchor="middle"
    dominant-baseline="middle"
  >
    {label}
  </text>
</svg>
"""

with open("obrazek.svg", "w", encoding="utf-8") as file:
    file.write(svg_content)
```

Po spuštění programu vznikne soubor `obrazek.svg`, který lze otevřít v prohlížeči.

Tento příklad ukazuje důležitou myšlenku:  
**program může generovat jiné soubory tím, že správně sestaví text podle známého formátu.**

Stejný princip později použijete například pro:

- HTML stránky,
- konfigurační soubory,
- exporty dat,
- nebo reporty.

---

## 10. Souborové objekty nemusí být jen na disku

Některé objekty se chovají jako soubor, i když jsou jen v paměti.

Například `StringIO`:

```python
from io import StringIO

buffer = StringIO()
buffer.write("první řádek\n")
buffer.write("druhý řádek\n")

print(buffer.getvalue())
```

`buffer` má metody podobné skutečnému souboru, ale data se neukládají na disk.

To je užitečné například:

- při testování,
- při dočasném skládání textu,
- nebo při práci s knihovnami, které umějí číst „cokoliv, co se chová jako soubor“.

---

## Shrnutí

Nejdůležitější vzor této hodiny je:

```python
with open("soubor.txt", "r", encoding="utf-8") as file:
    for line in file:
        ...
```

Pokud si z hodiny odnesete jistotu v těchto bodech, máte dobrý základ:

1. zvolit správný režim otevření,
2. používat `with`,
3. uvádět `encoding="utf-8"`,
4. rozumět tomu, co přesně program ze souboru čte nebo do něj zapisuje.

Na cvičení na tento základ navážete úlohami, kde budete:

- analyzovat textový soubor,
- vytvářet jednoduchý deník,
- převádět textový popis na strukturu složek a souborů,
- pracovat s virtuálními soubory a ZIP archivy.
