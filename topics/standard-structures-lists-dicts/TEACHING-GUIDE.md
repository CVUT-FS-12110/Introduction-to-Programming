# Teaching Guide: Standardní struktury — Listy a slovníky (012)

## Model výuky: Flipped Classroom — „les před stromy"

```
DOMA (pre-work):                          NA CVIKU (školní PC, bez AI):
┌─────────────────────────────┐          ┌──────────────────────────────────┐
│ Spustí hotový program        │          │ Ručně skládá kousky toho programu │
│ „Tvůj rok v hudbě" (LES)     │  ─────>  │ strom po stromu (A–G)             │
│ Šťourá do dat, AI smí na     │          │ Cvičící drtí a obchází mezi PC    │
│ VYSVĚTLENÍ řádků             │          │ AI se nepoužívá                   │
│ Mikroodevzdání do Moodlu     │          │                                   │
└─────────────────────────────┘          └──────────────────────────────────┘
   Vidí LES (kontext, motivace)             Buduje STROMY (skutečné pochopení)
   Understand (OK s AI)                     Apply / Analyze (ručně, AI nepomůže)
```

**Proč „les před stromy":** Prvák potřebuje vidět, *k čemu to je*, dřív než
dře mechaniku. Pre-work mu dá hotový funkční program — kontext a motivaci.
Na cviku pak ručně rozebíráme **ten samý program** na základní kousky.
AI-složitá část je samotný les (doma), takže ve třídě není žádný šev
„AI na konci bezAI cvika".

**Tvrdá podmínka návrhu:** každý strom A–G je doslova rozborka kousku
z `prework/rok_v_hudbe.py`. Když student řekne „tohle jsem viděl v lese",
je to záměr, ne náhoda — drž ten provázek.

---

### Klíčový narativ

**NEŘÍKEJTE:** _„Listy a slovníky musíte umět, protože je to v sylabu."_

**ŘÍKEJTE:** _„Doma vám AI ten program vysvětlila. Dnes zjistíte, jestli ho
umíte složit sami — protože jen to, co umíte složit, umíte i opravit,
když to AI příště zvorá."_

---

## Materiály

| Soubor | Kdy | Popis |
| --- | --- | --- |
| `prework/rok_v_hudbe.py` | Doma | LES — hotový funkční program, student ho spustí |
| `prework/README.md` | Doma | Instrukce + mikroodevzdání do Moodlu |
| `seminar/data.py` | Na cviku | Sdílená datová sada (stejný „svět" jako les) |
| `seminar/README.md` | Na cviku | STROMY A–G — zadání pro studenty + poznámky |

---

## Pre-work

### Co studenti dělají doma

1. Spustí `rok_v_hudbe.py`, uvidí výstup „Tvůj rok v hudbě".
2. Změní data (přidají pár přehrání) a spustí znovu.
3. Najdou **jeden řádek, kterému nerozumí**, a smí se AI zeptat na
   *vysvětlení* (ne na přepsání).

### Mikroodevzdání do Moodlu (AI OK, pass/fail, 2 body)

Krátký textový vstup:

- výstup programu pro jejich upravená data (copy-paste),
- **jedna věta:** „Nerozumím řádku `…`, protože …".

Ta věta krmí cvik — cvičící z ní zjistí, kde skupina tápe, a na to zacílí.

### Kdo neodevzdá

- Ztráta 2 bodů (pass/fail).
- Na cviku může sledovat, ale nemá vlastní „větu" do úvodní diskuse.

---

## Cvičení (90 min) — školní PC, bez AI

Cvičící **drtí a obchází mezi počítači**. AI-odolnost řeší správa stroje
a aktivní dohled; dobrý návrh úloh je pojistka (G se odevzdává jako úvaha,
ne kód).

### Minutový plán

#### 0–5: Check-in

- _„Kdo odevzdal? Přečtěte mi svoji větu ‚nerozumím řádku…'."_
- Posbírejte 3–4 věty na tabuli — to jsou dnešní cíle z úst studentů.

#### 5–17: A — List od nuly

- Cíl: list creation, indexování (i záporné), slicing, `append`/`pop`,
  přiřazení do řezu.
- Rozborka lesa: jak vznikne seznam jmen skladeb, než se začne počítat.
- Past, na kterou tlačte: `seznam[len(seznam)]` (off-by-one).

#### 17–30: B — Filtr a transformace → comprehension

- Cíl: nejdřív explicitní `for`+`append`, **pak** přepsat na jednu
  comprehension; porovnat čitelnost.
- _„Kdy je comprehension čitelnější a kdy už ne?"_ — nechte je hádat,
  pak ukažte vnořenou comprehension jako odstrašující příklad.

#### 30–42: C — Slovník jako sčítadlo

- Cíl: `pocty[k] = pocty.get(k, 0) + 1`, iterace přes `.items()`.
- _„Proč ne dva paralelní seznamy?"_ — to je most do stromu E.

#### 42–55: E — Která struktura a co to stojí

- Cíl: hledání ve **velkém katalogu** (`in` přes list ≈10 000 položek)
  vs. přes `set`. Klíč: pomalá je *velikost prohledávané struktury*,
  ne počet dotazů.
- Nechte je **odhadnout**, co bude pomalejší a proč, než to změří.
- Pointa: `in` na listu je O(n), na setu/dictu O(1). Tohle je odpověď
  na „kterou strukturu zvolit".

#### 55–68: F — Pasti: záloha + mazání při iteraci

- Dvě rychlé chyby za sebou: `zaloha = playlist` (alias) a mazání
  prvků během `for` přes ten samý list.
- _„Kdo má ‚zálohu', která se taky zamíchala? Ruku nahoru."_
- Model: reference vs. kopie, `is` vs. `==`, `.copy()`/řez;
  neměň kolekci, přes kterou iteruješ.

#### 68–80: G — Přečti a najdi chybu (capstone)

- 10řádkový úryvek = kombinace bugu z C (špatný default) a z F (alias).
- **Odevzdává se na papír / do komentáře:** predikovaný výstup,
  lokace chyby, jedna věta proč. NE opravený program.
- Tohle je nejvíc AI-odolné formou — deliverable je úvaha.

#### 80–90: Debrief

- Projděte G společně. _„Kdo predikoval správně? Kdo našel obě chyby?"_
- _„Který strom byl dnes v lese, co jste měli doma?"_ — uzavřít provázek.

### Rychlí jsou hotoví → D (extension)

Strom **D — Seřaď podle hodnot (Top 5) + `enumerate`/`zip`**. Kdo má A–G,
dostane D; kdo zvládne D, jde dělat „konzultanta" sousedovi.

### Časté problémy

| Problém | Řešení |
| --- | --- |
| Student v F bug „nevidí" (vše funguje) | Nechte ho vypsat `id()` obou seznamů |
| B: rovnou píše comprehension zpaměti z lesa | Vynuťte nejdřív `for`-verzi — test pochopení |
| E: „je to stejně rychlé" | Zvětšete *katalog*: `katalog(100000)`, ne počet dotazů |
| Hotový za 5 min | Roli „red team": ať najde, čím A–F obejít |
| Půl třídy neodevzdalo pre-work | Les promítněte na 3 min na začátku, pak A |

---

## Mapování na cíle tématu (012)

| Cíl / osnova | Pokrývá strom |
| --- | --- |
| Lists: creation, indexing, slicing | A (+ F, E) |
| Dict: keys, values, lookups | C (+ G) |
| Iteration & **comprehension** | B (+ D) |
| Choose structure: lookup vs ordered | E |
| Brief complexity notes | E |
| Mutation, reference vs copy | F |
| Čtení a debug struktur | G |

---

## Řešení a očekávané výstupy (pro cvičícího)

Data v `030-lab-session.ipynb` (`data.py`): 12 přehrání.

- **A** — `skladby` má 12 prvků; `skladby[0]='Sen'`, `skladby[-1]='Medvidek'`,
  `skladby[:5]=['Sen','Pohoda','Amerika','Vrat mi ji','Burlaci']`;
  `pop()` vrátí `'Bonus'`; `skladby[0:2]=['A','B','C']` **prodlouží** délku o 1
  (řez nahradí 2 prvky třemi). `skladby[len(skladby)]` → IndexError (poslední
  index je `len-1`).
- **B** — výsledek (nepřeskočené & >200 s):
  `['Sen','Amerika','Vrat mi ji','Burlaci','Sen','Amerika']`. Comprehence:
  `[p['skladba'] for p in prehravani if not p['preskoceno'] and p['delka_s']>200]`.
- **C** — `pocty = {'Lucie':5,'Kabat':3,'Chinaski':2,'Mig 21':2}`;
  nejhranější `'Lucie'`. Paralelní seznamy = ruční hledání indexu → strom E.
- **E** — list `in` ≈ 1–2 s, set `in` ≈ 0,001 s (stovky–tisíce×).
  Zvětšení *katalogu* zpomalí list lineárně, set ne. Závěr: vyhledávání →
  set/dict (O(1)), pořadí/posloupnost → list.
- **F1** — `zaloha is playlist` → `True`, stejné `id`. Oprava:
  `zaloha = playlist.copy()` nebo `playlist[:]`.
  **F2** — mazání při iteraci přeskočí prvky (index se posune pod nohama);
  oprava: iterovat přes kopii `for s in playlist[:]:` nebo postavit nový list.
- **G** — Část 1 vypíše `{'Lucie': 3, 'Kabat': 2}` (chyba: default `1` místo
  `0` → počty +1). Část 2 vypíše `['Sen', 'Pohoda', 'Punk']` (chyba: `zaloha`
  je alias `playlist`, `append` mění obojí).
- **D** — `[('Lucie',5),('Kabat',3),('Chinaski',2),('Mig 21',2)]`, žebříček
  číslovaný od 1 přes `enumerate(..., start=1)`.
