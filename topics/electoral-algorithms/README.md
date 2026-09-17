# 🗳️ Volební algoritmy

## Prerekvizity
- Smyčky (`for`, `while`)
- Podmínky (`if`, `elif`, `else`)
- Seznamy (`list`) a slovníky (`dict`)
- Základní operace: `max()`, `sum()`, `//` (celočíselné dělení), `%` (zbytek)

## Cíle

- Převést reálný problém (rozdělení mandátů) na algoritmus krok za krokem.
- Implementovat **D'Hondtovu metodu** a porozumět její logice.
- Porovnat různé volební algoritmy a pochopit jejich vliv na výsledky voleb.
- Analyzovat vliv **volební klauzule** na zastoupení stran.
- Porozumět **skutečnému českému volebnímu systému** (dvě skrutinia).

## Klíčová slova

Proporční volební systém, D'Hondt, Sainte-Laguë, mandát, kvocient, volební klauzule,
Imperialiho kvóta, Hagenbach-Bischoffova kvóta, skrutinium

## Materiály

| Soubor | Popis |
|---|---|
| `electoral-algorithms.ipynb` | Hlavní notebook — výklad algoritmů s vizualizacemi |
| `tasks.ipynb` | Úkoly pro studenty (kostry k doimplementování) |
| `solutions/solutions.ipynb` | Kompletní řešení úkolů |

## Přednáška / Seminář

Hlavní notebook `electoral-algorithms.ipynb` pokrývá:

1. **D'Hondtova metoda** — nejpoužívanější volební algoritmus v Evropě
   - Princip, ruční výpočet, implementace v Pythonu
   - Aplikace na reálná data z **voleb do Poslanecké sněmovny 2021**
2. **Sainte-Laguë metoda** — férovější alternativa
   - Porovnání s D'Hondt na stejných datech
3. **Volební klauzule** — analýza vlivu 5% hranice
   - Co by se stalo bez klauzule? S jinou výší?
4. **Český volební systém** — jak to funguje doopravdy
   - Imperialiho kvóta v krajích → Hagenbach-Bischoff celostátně

## Cvičení

[Úkoly pro studenty](tasks.ipynb)

## Zdroje

- [Volby.cz](https://www.volby.cz) — Český statistický úřad, oficiální výsledky voleb
- [D'Hondt method (Wikipedia)](https://en.wikipedia.org/wiki/D%27Hondt_method)
- [Sainte-Laguë method (Wikipedia)](https://en.wikipedia.org/wiki/Sainte-Lagu%C3%AB_method)
- Zákon č. 247/1995 Sb. o volbách do Parlamentu České republiky
