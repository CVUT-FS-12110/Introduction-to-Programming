# Teaching Guide: Testování — průvodce pro cvičícího

## Model výuky: Flipped Classroom

```
DOMA (před cvikem):                      NA CVIKU:
┌─────────────────────────────┐          ┌──────────────────────────────┐
│ Přečte výkladový notebook   │          │ Kolektivní Red Team          │
│ Splní pre-work              │  ─────>  │ Prezentace AI + TDD          │
│ Odevzdá do Moodlu           │          │ Dokončení ScoreTrackeru      │
└─────────────────────────────┘          └──────────────────────────────┘
       Apply, Understand                    Analyze, Evaluate, Create
       (OK s AI)                            (AI nepomůže)
```

**Proč:** Kódování (dolní patro Bloomovy taxonomie) zvládnou doma i s AI.
Na cviku trénujeme to, co AI nahradit nemůže: kritické myšlení, komunikaci,
adversariální analýzu, obhajobu vlastního řešení.

### Klíčový narativ

**NEŘÍKEJTE:** _„Testování je důležité, protože to firmy vyžadují."_

**ŘÍKEJTE:** _„Kdo píše testy, ten definuje, co software dělá. To je role lídra."_

---

## Materiály

| Soubor                                | Kdy                     | Popis                                     |
| ------------------------------------- | ----------------------- | ----------------------------------------- |
| `lecture/testing-fundamentals.ipynb`  | Přednáška / samostudium | Kompletní výklad (13 sekcí)               |
| `prework/prework.ipynb`               | Doma, před cvikem       | 4 úkoly, 40–50 min, odevzdání do Moodlu   |
| `lab/lab-session.ipynb`               | Na cvičení              | Kolektivní Red Team + ScoreTracker        |

---

## Pre-work

### Co studenti dělají doma

Notebook `prework/prework.ipynb` — 4 úkoly, 40–50 min:

1. **calculate_grade** — napsat testy pro správnou funkci (10 min)
2. **count_words** — najít bug v buggy funkci pomocí testů (10 min)
3. **ScoreTracker** — test-first pro třídu: napsat testy, pak implementovat (15 min)
4. **AI-driven TDD** — vybrat si problém, napsat testy, poslat AI, zdokumentovat proces (15 min)

### Odevzdání

Student nahraje `test_prework.py` + AI implementaci do Moodlu.
Deadline: před začátkem cvika.

### Automatická kontrola (doporučená)

Počítáme jen testy, které **skutečně něco ověřují** (obsahují `assert`
nebo `pytest.raises`) — prázdné funkce s `pass` se nepočítají:

```bash
# 1. Syntaxe OK + alespoň 12 skutečných testů?
python -c "
import ast, sys
tree = ast.parse(open('test_prework.py', encoding='utf-8').read())
testy = [n for n in ast.walk(tree)
         if isinstance(n, ast.FunctionDef) and n.name.startswith('test_')]
plne = [f for f in testy
        if any(isinstance(n, (ast.Assert, ast.With)) for n in ast.walk(f))]
print(f'{len(plne)} skutecnych testu z {len(testy)} funkci')
sys.exit(0 if len(plne) >= 12 else 1)
"

# 2. Testy pro grade_calculator procházejí?
pytest test_prework.py -k "grade" --tb=no -q

# 3. Alespoň 1 test pro count_words selhává? (= našli bug)
pytest test_prework.py -k "count" --tb=no -q  # očekávejte failures
```

### Co s tím, kdo neodevzdá?

- **Ztráta bodů** (2 body za včasné odevzdání, pass/fail)
- Kolektivní Red Team může hrát i bez odevzdaného pre-worku —
  jen mu bude chybět vlastní `test_prework.py` pro část se ScoreTrackerem

---

## Cvičení (90 min)

### Materiál

`lab/lab-session.ipynb`

### Příprava před cvikem

- [ ] **Týden předem** oznámit 3 studenty na prezentaci (přes Moodle/e-mail)
- [ ] Projít odevzdané pre-worky (stačí zběžně — kvůli check-inu a bodům)
- [ ] Připravit projektor: promítat budete slabou sadu a přidávané testy
- [ ] Tabule na sbírání triků (typ díry + jméno)

Slabá testovací sada je přímo v notebooku (`test_grade_weak.py`) —
nic dalšího se nerozdává, žádné párování studentů není potřeba.

### Mapa děr ve slabé sadě (neprozrazovat předem)

| Díra | Testy ji nepokrývají | Typický evil trik |
| --- | --- | --- |
| Hranice pásem | 90, 80, 70, 60, 0, 100 | `>` místo `>=` — 90 vrátí 'B' |
| Pásmo D | žádný test na 60–69 | nikdy nevrací 'D' |
| Nevalidní vstupy | žádný test na ValueError | −5 nebo 150 vrátí 'A' místo výjimky |
| Volný assert | `calculate_grade(75) in 'ABCDF'` | 75 vrátí 'B' a projde |

### Minutový plán

#### 0–2: Check-in

- _„Kdo odevzdal pre-work? Ruce nahoru."_

#### 2–17: Prezentace: AI + TDD (3 studenti × 5 min)

- Studenti vědí **týden dopředu**, že prezentují — měli čas se připravit
- Každý max 3 min prezentace + 2 min otázky
- Student prezentuje svůj **úkol 4 z pre-worku**: jak řídil AI pomocí testů
- **Kód na projektoru** — ne slidy. Ukázat testy, AI output, výsledek.
- **Mikroúkol pro publikum:** každý si během prezentace poznamená jeden
  test, který by prezentujícímu přidal. Po prezentaci 1–2 vylosujte
  a zeptejte se — publikum přestane být pasivní a otázky nejsou trapné ticho.
- Po prezentacích shrnutí: _„Vidíte — kvalita testů = kvalita výstupu od AI."_

#### 17–38: Kolo 1: Prolom

1. **Nejdřív rituálně předveďte a zakažte hardcode** (1 min):
   napište na projektoru `if score == 95: return 'A'`… a řekněte
   _„Tohle projde vždy a proti každé sadě — proto je to nuda a proto je to
   zakázané. Váš trik musí zneužít konkrétní díru v testech."_
   Slabší studenti díky tomu aspoň uvidí, jak exploit vypadá.
2. Studenti píší evil implementace proti společné slabé sadě.
3. **AI norma:** prvních 5 minut bez AI, pak povolena — ale trik musí
   student vysvětlit vlastními slovy. Vysvětlení je vstupenka na tabuli.
4. **Sbírejte triky na tabuli** (typ díry + jméno). Obcházejte a provokujte:
   - _„Projde to na záporné číslo?"_
   - _„Co vrací tvoje implementace pro 90?"_
   - _„Které pásmo testy vůbec nezmiňují?"_

#### 38–55: Kolo 2: Zpevni

- Vyvolávejte **podle tabule, po typech děr** — ne hlásící se dobrovolníky:
  _„Kdo měl díru na hranici pásma? … Nadiktuj test, který tvůj trik zabije."_
- Diktovaný test přidejte do promítané sady; studenti si ho přepisují
  do svých notebooků a průběžně pouštějí pytest — jejich evil implementace
  postupně umírají.
- Reálné tempo je **2–3 minuty na test** — stihnete ~8 testů. Cíl je pokrýt
  všechny **typy** děr z tabule, ne každý jednotlivý trik. Řekněte to nahlas
  předem, ať nikdo nečeká, že dojde na všechny.

#### 55–63: Kolo 3: Přežij (bonus)

- **Zmrazte sadu** — od teď se nemění.
- 5 minut: napsat **novou** evil implementaci, která projde celou zpevněnou
  sadou. Hardcode stále zakázán.
- Kdo přežije, předvede implementaci na projektoru a bere **bonusové body**
  (např. +1, v logice bonusů za dobrovolné prezentace).
- **Když nepřežije nikdo, je to výhra** — pojmenujte ji:
  _„Naše sada je neprůstřelná. Přesně tohle je cíl testování."_

#### 63–85: ScoreTracker

- Studenti si zkopírují **vlastní** `test_prework.py` z pre-worku
- Dokončí implementaci ScoreTrackeru (testy z pre-worku musí projít)
- Pak rozšíření: metoda `get_percentile(score)` — **test-first**
- **Checkpoint na konci cvika:** testy pro percentil + kostra implementace;
  doladění doma. Vyhlaste to předem, ať nikdo nepanikaří, že nestíhá.
- Pomáhejte těm, kdo se zasekli

#### 85–90: Debrief

- **Pojmenujte, co dělali:** _„Tomu, co jste dnes dělali ručně, se říká
  mutační testování. Nástroje jako mutmut vytvářejí evil mutace automaticky
  a měří, kolik jich vaše testy zabijí."_
- _„Jaká díra tě nejvíc překvapila?"_
- _„Co bys v pre-worku příště udělal/a jinak?"_

### Časté problémy

| Problém | Řešení |
| --- | --- |
| Většina najde stejnou díru (hranice pásem) | V pořádku — na tabuli sbírejte **typy** děr; v kole 2 vyvolávejte tak, aby došlo na všechny typy |
| Student neví, jak začít | Napovězte: „Přečti si, co testy NEtestují. Které pásmo tam chybí?" |
| Někdo obchází zákaz hardcodu | Připomeňte rituál ze začátku; trik bez vysvětlené díry nejde na tabuli |
| V kole 3 přežije hardcode | Neplatí — zákaz trvá celé cvičení |
| V kole 3 nepřežije nikdo | To je úspěch, ne problém — viz debrief |
| Rychlý student je hotový v kole 1 | Ať zkusí najít **druhou, jinou** díru (jiný typ než první) |
| Evil kód je „ošklivý" | Nekomentujte styl — jediná metrika je projde/neprojde a proč |

---

## Prezentace — systém rotace

### Co studenti prezentují

Svůj **úkol 4 z pre-worku: AI-driven TDD proces.** Každý student si vybral
jiný problém + měl jinou interakci s AI → každá prezentace je unikátní.

### Systém

- Na každém cviku prezentují **max 3 studenti** (3+2 min)
- Každý student musí prezentovat **alespoň 2× za semestr** (podmínka zápočtu)
- Dobrovolné prezentace navíc: **+2 bonusové body** za každou
- **Studenty oznamte týden předem** přes Moodle/e-mail — ne na začátku hodiny
- Tracking: tabulka v Moodlu/Excelu, kdo kdy prezentoval

### Proč AI+TDD jako téma prezentace

- **Každá prezentace je unikátní** — jiný problém, jiná AI konverzace
- **Neprůstřelné proti AI cheatu** — student musí vysvětlit PROCES, ne jen výsledek
- **Učí technickou komunikaci** — „jak jsem řídil AI" = „jak jsem specifikoval požadavky"
- **Ukazuje limity AI** — spolužáci vidí, kde AI selhává a proč záleží na kvalitě testů
