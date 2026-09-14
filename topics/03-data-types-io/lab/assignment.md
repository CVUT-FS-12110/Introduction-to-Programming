# Cvičení: datové typy a vstup/výstup

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

## 1. Převodník délek ★

Program načte délku v milimetrech (desetinné číslo) a vypíše ji
v centimetrech, metrech a palcích (1 palec = 25,4 mm). Všechny hodnoty
vypište na 3 desetinná místa.

```
Délka [mm]: 1250
1250.000 mm = 125.000 cm = 1.250 m = 49.213 in
```

## 2. Sekundy na hodiny ★

Program načte počet sekund (celé číslo) a vypíše ho ve tvaru `h:mm:ss`.
Použijte operátory `//` a `%`.

```
Počet sekund: 3725
1:02:05
```

**Rozšíření:** Je-li čas delší než jeden den, vypište i dny
(`90061` → `1 d 1:01:01`).

## 3. Rozbor slova ★

Program načte slovo a vypíše počet znaků, první a poslední znak, slovo
velkými písmeny, slovo pozpátku a informaci, zda jde o palindrom
(slovo, které se čte stejně zepředu i zezadu, bez ohledu na velikost
písmen).

```
Slovo: Nepotopen
Počet znaků: 9
První znak: N
Poslední znak: n
Velkými písmeny: NEPOTOPEN
Pozpátku: nepotopeN
Palindrom: True
```

Nápověda: podívejte se, co udělá zápis `word[::-1]`.

## 4. Rozsahy celých čísel ★★

Pomocí cyklu vypište pro 8, 16, 32 a 64 bitů, jaký rozsah hodnot má
celé číslo **bez znaménka** a **se znaménkem** (v doplňkovém kódu).
Hodnoty nepište ručně — spočítejte je z počtu bitů.

```
 8 bitů: 0 až 255, -128 až 127
16 bitů: 0 až 65535, -32768 až 32767
32 bitů: 0 až 4294967295, -2147483648 až 2147483647
64 bitů: 0 až 18446744073709551615, -9223372036854775808 až 9223372036854775807
```

**Rozšíření:** Zarovnejte čísla do sloupců a oddělte tisíce (hledejte
v dokumentaci *Format Specification Mini-Language*).

## 5. Dvojková soustava ručně ★★

Program načte nezáporné celé číslo a převede ho do dvojkové soustavy
opakovaným dělením dvěma. Funkci `bin()` použijte jen pro kontrolu.
Vypište také počet bitů a počet jedniček. Nezapomeňte na vstup `0`.

```
Číslo: 202
Dvojkově: 11001010
Kontrola: 0b11001010
Počet bitů: 8
Počet jedniček: 4
```

**Rozšíření:**

- Převod opačným směrem: z řetězce nul a jedniček spočítejte číslo bez
  použití `int(text, 2)`.
- Převod do šestnáctkové soustavy stejným postupem.

## 6. Znaky a bajty ★★

Program načte text a pro každý znak vypíše samotný znak, jeho kód
v Unicode a počet bajtů, které zabírá v kódování UTF-8. Nakonec vypíše
celkový počet znaků a bajtů.

```
Text: Kůň
K  U+004B  1 B
ů  U+016F  2 B
ň  U+0148  2 B
Znaků: 3, bajtů: 5
```

Nápověda: kód znaku vrací funkce `ord()`, bajty získáte metodou
`text.encode("utf-8")`. Kód vypíšete šestnáctkově pomocí `f"{code:04X}"`.

Vyzkoušejte text *Příliš žluťoučký kůň úpěl ďábelské ódy*. Kolik má
znaků a kolik bajtů? Proč se ta čísla liší?

## 7. Četnost písmen ★★★

Program načte větu a spočítá, kolikrát se v ní vyskytuje každé písmeno.
Velikost písmen nerozlišuje, mezery a interpunkci ignoruje. Četnosti
uloží do slovníku a vypíše je seřazené od nejčastějšího písmene (při
shodě abecedně). Nakonec vypíše počet různých písmen.

```
Věta: Jelen jede lesem
e: 6
j: 2
l: 2
d: 1
m: 1
n: 1
s: 1
Různých písmen: 7
```

Nápověda: podívejte se na metodu `str.isalpha()` a na parametr `key`
funkce `sorted()`.

**Rozšíření:** Místo čísel vykreslete vodorovný histogram z hvězdiček
(`e ******`). Zkuste program spustit na delším textu, například na
odstavci z Wikipedie. Které písmeno je v češtině nejčastější?

## 8. Kde končí přesnost `float` ★★★

Napište program, který postupně zjistí:

1. Kolik vyjde, když v cyklu desetkrát přičtete `0.1` k nule? Porovnejte
   výsledek s `1.0` pomocí `==` a pomocí `math.isclose()` a vypište
   rozdíl.
2. Jaké je **strojové epsilon** — nejmenší mocnina dvou `eps`, pro kterou
   ještě platí `1.0 + eps != 1.0`? Začněte s `eps = 1.0` a v cyklu ho
   půlte. Výsledek porovnejte s hodnotou `sys.float_info.epsilon`.
3. Od jakého exponentu `n` už `float` neumí rozlišit čísla `2**n`
   a `2**n + 1`? Co to znamená pro počítání s velkými celými čísly
   v `float`?

Ke každému výsledku napište do komentáře jednou větou, co znamená.

## 9. IEEE 754 zblízka ★★★★

Program načte desetinné číslo a vypíše jeho 64bitovou reprezentaci podle
IEEE 754: znaménko (1 bit), exponent (11 bitů) a mantisu (52 bitů).
Z těchto tří částí pak podle vzorce
(−1)<sup>s</sup> × (1 + m / 2<sup>52</sup>) × 2<sup>e − 1023</sup>
spočítejte hodnotu zpět a ověřte, že vyjde původní číslo.

```
Číslo: 0.1
Znaménko: 0
Exponent: 01111111011 (1019, tj. 2^-4)
Mantisa: 1001100110011001100110011001100110011001100110011010
Zpětně: 0.1
Přesně uložená hodnota: 0.1000000000000000055511151231257827021181583404541015625
```

Nápověda:

- bity čísla `x` jako jedno celé číslo získáte pomocí
  `struct.unpack(">Q", struct.pack(">d", x))[0]`,
- jednotlivé části z něj vytáhnete bitovým posunem `>>` a maskou `&`,
- přesně uloženou hodnotu ukáže `decimal.Decimal(x)`.

**Rozšíření:** Vyzkoušejte speciální hodnoty `-0.0`, `float("inf")`,
`float("nan")` a velmi malé číslo `5e-324`. Čím se liší jejich exponent
a mantisa? Pro které z nich vzorec výše neplatí?
