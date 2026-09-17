# Cvičení: podmínky a cykly

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

## 1. Kontrola rozměrů ★

Hřídel má jmenovitý průměr 25,00 mm s tolerancí ±0,05 mm. Naměřené
průměry deseti kusů máte v programu:

```python
diameters = [25.01, 24.97, 25.06, 25.00, 24.94, 25.03, 25.05, 24.95, 25.10, 24.99]
```

Pro každý kus vypište pořadí, průměr a výsledek `OK`, `MALÝ` nebo `VELKÝ`.
Nakonec vypište počet zmetků a jejich podíl v procentech.

```
 1: 25.01 mm  OK
 2: 24.97 mm  OK
 3: 25.06 mm  VELKÝ
 ...
Zmetků: 3 z 10 (30.0 %)
```

Pozor: kusy s průměrem přesně 25,05 a 24,95 mm jsou ještě v toleranci.
Zkuste podmínku zapsat i jako `abs(d - 25.00) <= 0.05`. Vyjde stejně?
Proč?

## 2. Přestupné roky ★

Rok je přestupný, pokud je dělitelný čtyřmi — kromě roků dělitelných
stem, které přestupné nejsou. Výjimkou z výjimky jsou roky dělitelné
čtyřmi sty, které přestupné jsou.

1. Program načte rok a vypíše, zda je přestupný. Celé pravidlo zapište
   jednou podmínkou pomocí `and`, `or` a `not`.
2. Vypište všechny přestupné roky od 1890 do 2030 (včetně), deset
   na řádek, a jejich počet (má vyjít 34).

## 3. Prvočísla ★★

1. Program načte celé číslo `n` a zjistí, zda je prvočíslo. Dělitele
   stačí zkoušet do √n — proč?
2. Vypište všechna prvočísla menší než 100 a jejich počet. Zkuste
   k tomu použít konstrukci `for … else`.
3. Rozložte zadané číslo na prvočinitele:

   ```
   Číslo: 360
   360 = 2 * 2 * 2 * 3 * 3 * 5
   ```

**Rozšíření:** Implementujte Eratosthenovo síto a porovnejte, jak dlouho
trvá najít všechna prvočísla do milionu oběma způsoby (modul `time`).

## 4. Kosočtverec ★★

Program načte liché číslo `n` a vykreslí kosočtverec z hvězdiček o výšce `n`.

```
Výška: 7
   *
  ***
 *****
*******
 *****
  ***
   *
```

Pokud uživatel zadá sudé nebo záporné číslo, program ho vyzve, aby zadal
jiné.

**Rozšíření:** Vykreslete jen obrys kosočtverce, šachovnici `n × n`
a písmeno X.

## 5. Ciferné hrátky ★★

V této úloze pracujte s číslicemi jen pomocí `//` a `%`, bez převodu
čísla na řetězec.

1. Najděte všechna trojmístná čísla, která se rovnají součtu třetích
   mocnin svých číslic (například 153 = 1³ + 5³ + 3³). Taková čísla jsou
   čtyři.
2. Program načte číslo a opakovaně počítá jeho ciferný součet, dokud
   nevyjde jednomístné číslo. Vypište celou posloupnost:

   ```
   Číslo: 987654321
   987654321 → 45 → 9
   ```

**Rozšíření:** Najděte všechna taková čísla (bod 1) pro čtyřmístná
a pětimístná čísla, s mocninou rovnou počtu číslic.

## 6. Kořen rovnice půlením intervalu ★★★

Rovnice x³ − 2x − 5 = 0 má jeden kořen v intervalu ⟨2, 3⟩. Metoda půlení
intervalu (bisekce) funguje takto:

- spočítá střed intervalu,
- podle znaménka funkce v krajních bodech a ve středu určí, ve které
  polovině kořen leží,
- s touto polovinou pokračuje, dokud není interval kratší než požadovaná
  přesnost.

Najděte kořen s přesností 10⁻⁶ a vypište ho spolu s počtem iterací
(vyjde jich zhruba 20). Kořen je přibližně 2,094551.

**Rozšíření:** Stejný kořen najděte Newtonovou metodou
(xₙ₊₁ = xₙ − f(xₙ) / f′(xₙ)) a porovnejte počet iterací. Co se stane,
když Newtonovu metodu spustíte z bodu x = 0?

## 7. Šikmý vrh ★★★

Těleso je vrženo rychlostí v₀ = 20 m/s pod úhlem 45° (g = 9,81 m/s²,
bez odporu vzduchu). Simulujte jeho let po malých časových krocích `dt`.
V každém kroku aktualizujte polohu i rychlost a pokračujte, dokud těleso
nedopadne (y < 0).

Vypište dolet, maximální výšku a dobu letu. Výsledky porovnejte
s přesnými hodnotami: dolet 40,77 m, výška 10,19 m, doba letu 2,88 s.
Simulaci spusťte pro `dt` = 0,1, 0,01 a 0,001 a vypište tabulku odchylek
od přesných hodnot.

**Rozšíření:** Přidejte odpor vzduchu, který působí proti pohybu a je
úměrný druhé mocnině rychlosti. V cyklu přes úhly 0–90° najděte úhel
s největším doletem. Vyjde s odporem vzduchu více, nebo méně než 45°?

## 8. Řazení bez `sort()` ★★★

1. Seřaďte seznam čísel algoritmem **bubble sort** — bez funkcí `sort()`
   a `sorted()`. Počítejte, kolik porovnání a kolik prohození
   algoritmus provedl.
2. Upravte algoritmus tak, aby skončil dřív, pokud při jednom průchodu
   nic neprohodil.
3. Spusťte ho na seznamu se 100 prvky, který je (a) už seřazený, (b)
   seřazený opačně, (c) náhodný (modul `random`). Porovnejte počty
   porovnání.

**Rozšíření:** Implementujte také řazení výběrem (*selection sort*)
a vkládáním (*insertion sort*). Jak roste počet porovnání, když délku
seznamu zdvojnásobíte? Souvisí to s intuicí o složitosti z tématu
[Základy návrhu algoritmů](../../02-algorithm-design-basics/README.md)?

## 9. Hra života ★★★★

[Hra života](https://cs.wikipedia.org/wiki/Hra_%C5%BEivota) Johna Conwaye
probíhá na čtvercové mřížce buněk, které jsou živé nebo mrtvé. Každá
buňka má osm sousedů a nová generace vzniká podle pravidel:

- živá buňka se 2 nebo 3 živými sousedy přežije, jinak zemře,
- mrtvá buňka s právě 3 živými sousedy ožije.

Mřížku 10 × 10 uložte jako seznam seznamů. Začněte s „kluzákem“ (anglicky
*glider*) v levém horním rohu a vypište prvních 10 generací (živá buňka
`#`, mrtvá `.`):

```
.#........
..#.......
###.......
..........
```

Pozor: novou generaci musíte počítat z celé staré generace, ne z mřížky,
kterou zrovna přepisujete.

**Rozšíření:**

- Okraje mřížky propojte (co vyjede vpravo, vrátí se zleva).
- Rozpoznejte, že se stav mřížky opakuje, a program ukončete.
- Počáteční stav načtěte z textu, kde je každý řádek mřížky jeden řádek
  vstupu.
