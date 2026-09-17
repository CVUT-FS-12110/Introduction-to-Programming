# Teaching Guide: Volební algoritmy — Průvodce pro cvičícího

## Kontext

### Proč volební algoritmy?
- **Reálný svět**: Studenti vidí, jak jednoduchá smyčka rozhoduje o složení parlamentu.
- **Algoritmické myšlení**: D'Hondt je elegantní greedy algoritmus — najdi maximum, přiděl, opakuj.
- **Kritické myšlení**: Různé metody dávají různé výsledky → neexistuje "objektivně spravedlivý" systém.
- **Motivace**: Data z českých voleb 2021 jsou studentům blízká a výsledky je překvapí.

### Kde v sylabu?
Týden 4 — Smyčky a podmínky. Volební algoritmy jsou ideální aplikační úloha:
- `for` cyklus (iterace přes mandáty, přes strany)
- `if` podmínka (najdi maximum, filtruj klauzuli)
- Slovníky (strana → hlasy, strana → mandáty)
- Celočíselné dělení `//` a zbytek `%` (české skrutinium)

### Co studenti znají?
- `for`, `while`, `if/elif/else`
- Seznamy, základní operace se slovníky
- `print()`, f-stringy
- **Neznají:** funkce (definice), knihovny, třídy

> ⚠️ V notebooku se používá `matplotlib` pro vizualizace. Studenti ho ještě neznají
> podrobně — kód pro grafy je připravený, stačí spustit. Zmíňte, že se knihovny
> naučí v týdnu 8.

---

## Přednáška / Seminář (90 min)

### Doporučený průběh

| Čas | Sekce | Poznámky |
|---|---|---|
| 0–10 | Motivace | *„Jak si myslíte, že se rozděluje 200 křesel ve sněmovně?"* Brainstorm. |
| 10–20 | D'Hondt teorie | Tabulka kvocientů na tabuli. Malý příklad (3 strany, 5 mandátů). |
| 20–35 | Live-coding D'Hondt | Společně budujeme funkci. Ptejte se: *„Co potřebujeme v každém kole?"* |
| 35–45 | Volby 2021 | Spustíme na reálných datech. *„Překvapuje vás výsledek?"* |
| 45–55 | Vizualizace | Grafy: mandáty vs poměr hlasů. *„Kdo je zvýhodněný?"* |
| 55–70 | Sainte-Laguë | *„Co kdybychom dělili jinak?"* Porovnání. Diskuse o férovosti. |
| 70–80 | Klauzule | *„Co kdyby neexistovala 5% hranice?"* Analýza. |
| 80–90 | Český systém | Imperialiho kvóta + Hagenbach-Bischoff. Konceptuální vysvětlení. |

### Klíčové momenty

1. **AHA moment #1** (D'Hondt vs poměr): ANO má méně hlasů než SPOLU, ale víc mandátů.
   Proč? → Protože záleží na poměrech, ne absolutních číslech.

2. **AHA moment #2** (Klauzule): Bez 5% hranice by ČSSD a KSČM měly mandáty
   a ostatní strany by jich měly méně. *„Je 5% hranice spravedlivá?"*

3. **AHA moment #3** (Metody): D'Hondt vs Sainte-Laguë dává různé výsledky
   na stejných datech. *„Neexistuje objektivně nejlepší systém."*

### Tipy pro výuku

- **Začněte na tabuli**, ne v kódu. Tabulka kvocientů je vizuální a intuitivní.
- **Ptejte se PŘEDTÍM**, než ukážete kód: *„Jak byste to naprogramovali?"*
- **Nechte je hádat** výsledky před spuštěním: *„Kolik mandátů dostane ANO?"*
- **Politicky neutrální** — nekomentujte, jestli je výsledek "dobrý" nebo "špatný".
  Nechte studenty diskutovat.

---

## Cvičení (90 min)

### Materiál
`tasks.ipynb`

### Minutový plán

#### 0–5: Rekapitulace
- *„Kdo mi řekne, jak funguje D'Hondt jednou větou?"*

#### 5–35: Úkol 1 — Implementace D'Hondt (★★☆)
- Studenti mají kostru funkce, doplní jádro algoritmu
- Ověří na malém příkladu + volby 2021
- **Vy obcházíte a pomáháte** — typické problémy: zapomenou `+ 1` v děliteli,
  neaktualizují mandáty

#### 35–55: Úkol 2 — Sainte-Laguë + porovnání (★★★)
- Modifikace D'Hondt: jiné dělitele
- Porovnání výsledků a odpovědi na otázky
- **Diskuzní otázka**: *„Která metoda je férovější? A pro koho?"*

#### 55–75: Úkol 3 — Analýza klauzule (★★★☆)
- Smyčka přes různé klauzule
- Vizualizace výsledků
- *„Kolik hlasů je ztracených při 5%? A při 10%?"*

#### 75–85: Úkol 4 — Bonus: Modifikovaný D'Hondt (★★★★)
- Pro rychlé studenty: první dělitel 1.42 místo 1
- *„Proč zrovna √2?"*

#### 85–90: Shrnutí
- *„Co nového jste se dnes naučili?"*
- *„Změnil se váš pohled na volby?"*

---

## Časté problémy

| Problém | Řešení |
|---|---|
| Student neví, kde začít s D'Hondt | Napovězte: *„V každém kole hledáš stranu s nejvyšším kvocientem. Co je kvocient?"* |
| Zapomene `+ 1` v děliteli | *„Co se stane, když strana ještě nemá žádný mandát? Čím dělíš?"* |
| Nerozumí celočíselnému dělení | Připomeňte `//` vs `/` — ukažte na příkladu `7 // 3 = 2` |
| Graf nefunguje | Zkontrolujte `import matplotlib.pyplot as plt`. Případně `pip install matplotlib`. |
| Student je hotový rychle | Bonus úkol 4 (modifikovaný D'Hondt) nebo je pošlete na český systém |

---

## Diskuzní otázky pro pokročilejší studenty

1. *„Existuje volební systém, který je 100% spravedlivý?"*
2. *„Proč velké strany preferují D'Hondt a malé Sainte-Laguë?"*
3. *„Co se stane, když dvě strany mají stejný kvocient? Jak rozhodneš?"*
4. *„Jaký vliv má počet krajů na výsledek? Co kdyby byl jen 1 kraj?"*
5. *„Proč se v ČR přešlo z D'Hondtovy metody na systém dvou skrutinií?"*
