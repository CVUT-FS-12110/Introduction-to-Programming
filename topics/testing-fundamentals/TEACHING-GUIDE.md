# Teaching Guide: Testování — Průvodce pro cvičícího

## Model výuky: Flipped Classroom

Tento kurz používá **flipped classroom** model:

```
DOMA (před cvikem):                      NA CVIKU:
┌─────────────────────────┐              ┌──────────────────────────────┐
│ Přečte notebook (010)   │              │ Red Team Challenge           │
│ Splní pre-work (020)    │   ───────>   │ Diskuse, prezentace          │
│ Odevzdá do Moodlu       │              │ Rozšíření úlohy, pair work   │
└─────────────────────────┘              └──────────────────────────────┘
       Apply, Understand                    Analyze, Evaluate, Create
       (OK s AI)                            (AI nepomůže)
```

**Proč:** Kódování (dolní patro Bloomovy taxonomie) zvládnou doma i s AI.
Na cviku trénujeme to, co AI nahradit nemůže: kritické myšlení, komunikaci,
adversariální analýzu, obhajobu vlastního řešení.

---

### Klíčový narativ

**NEŘÍKEJTE:** _„Testování je důležité, protože to firmy vyžadují."_

**ŘÍKEJTE:** _„Kdo píše testy, ten definuje, co software dělá. To je role lídra."_

---

## Materiály

| Soubor                           | Kdy                     | Popis                                    |
| -------------------------------- | ----------------------- | ---------------------------------------- |
| `010-testing-fundamentals.ipynb` | Přednáška / samostudium | Kompletní výklad (13 sekcí)              |
| `020-prework.ipynb`              | Doma, před cvikem       | 4 úkoly, 40-50 min, odevzdání do Moodlu  |
| `030-lab-session.ipynb`          | Na cvičení              | Red Team + rozšíření + AI+TDD prezentace |

---

## Pre-work

### Co studenti dělají doma

Notebook `020-prework.ipynb` — 4 úkoly, 40–50 min:

1. **calculate_grade** — napsat testy pro správnou funkci (10 min)
2. **count_words** — najít bug v buggy funkci pomocí testů (10 min)
3. **ScoreTracker** — test-first pro třídu: napsat testy, pak implementovat (15 min)
4. **AI-driven TDD** — vybrat si problém, napsat testy, poslat AI, zdokumentovat proces (15 min)

### Odevzdání

Student nahraje `test_prework.py` + AI implementaci do Moodlu. Deadline: před začátkem cvika.

### Automatická kontrola (doporučená)

```bash
# 1. Syntaxe OK?
python -c "import test_prework"

# 2. Alespoň 12 test funkcí?
python -c "
import ast, sys
tree = ast.parse(open('test_prework.py').read())
tests = [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name.startswith('test_')]
print(f'{len(tests)} tests found')
sys.exit(0 if len(tests) >= 12 else 1)
"

# 3. Testy pro grade_calculator procházejí?
pytest test_prework.py -k "grade" --tb=no -q

# 4. Alespoň 1 test pro count_words selhává?
pytest test_prework.py -k "count" --tb=no -q  # expect failures
```

### Co s tím, kdo neodevzdá?

- **Ztráta bodů** (2 body za včasné odevzdání, pass/fail)
- Volitelně: dobrovolník ze skupiny se jich může ujmout
- Nepřipravení studenti mohou sledovat Red Team ostatních, ale nemají svou úlohu

---

## Cvičení (90 min)

### Materiál

`030-lab-session.ipynb`

### Příprava před cvikem

- [ ] Stáhnout odevzdané `test_prework.py` soubory z Moodlu
- [ ] Připravit náhodné přiřazení (kdo dostane čí testy) — ideálně python skript
- [ ] **Týden předem** oznámit 3 studenty na prezentaci (přes Moodle/email)
- [ ] Mít záložní plán pokud studentů < 10 (menší skupiny)

### Minutový plán

#### 0–2: Check-in

- _„Kdo odevzdal pre-work? Ruce nahoru."_
- Rozdejte přiřazení (kdo dostane čí testy)

#### 2–17: Prezentace: AI + TDD (3 studenti × 5 min)

- Studenti vědí **týden dopředu**, že prezentují — měli čas se připravit
- Každý max 3 min prezentace + 2 min otázky
- Student prezentuje svůj **úkol 4 z pre-worku**: jak řídil AI pomocí testů
- Formát: (1) jaký problém (2) moje testy (3) co AI vrátilo (4) iterace (5) ponaučení
- **Kód na projektoru** — ne slidy. Ukázat testy, AI output, výsledek.
- Otázky od publika: _„Proč jsi netestoval X?"_, _„Bylo AI lepší na druhý pokus?"_
- Po prezentacích krátké shrnutí: _„Vidíte — kvalita testů = kvalita výstupu od AI."_

#### 17–37: 🔴 Red Team Challenge

- Studenti mají `test_prework.py` od spolužáka
- Úkol: napsat evil implementaci, která projde jeho testy ale je špatná
- **Vy obcházíte a provokujete:**
  - _„A co kdybys vrátil hardcoded hodnotu?"_
  - _„Projde to na záporné číslo?"_
  - _„Zkus ignorovat celou validaci"_
- Po 15 min: _„Kdo dokázal obejít testy? Ukažte ruku."_

**Typické evil triky studentů:**

```python
# Hardcoded pro konkrétní hodnoty z testů
def calculate_grade(score):
    if score == 95: return 'A'
    if score == 50: return 'F'
    return 'C'  # default — projde slabými testy

# Ignoruje validaci
def count_words(text):
    return len(text.split())  # funguje, ale nevaliduje vstup
```

#### 37–42: 💬 Diskuse

- _„Jaké edge cases chyběly nejčastěji?"_
- Shromážděte na tabuli: typicky chybí hraniční hodnoty, prázdné vstupy, záporná čísla
- Pointa: _„Vidíte — i s AI jde napsat slabé testy. Kvalita testů = vaše dovednost."_

#### 42–65: 🔨 Live Extension (ScoreTracker)

- Studenti dokončí implementaci ScoreTracker (mají testy z pre-worku)
- Pak rozšíření: metoda `get_percentile(score)` — kolik % skóre je pod danou hodnotou
- **Test-first:** nejdřív testy pro novou metodu, pak implementace
- Pomáhejte těm, kdo se zasekli

#### 65–85: ⚔️ Adversarial Pairs

- Napsat funkci s jemným bugem → soused testuje
- **Nechte je být kreativní**, neřiďte moc
- Dobrý bug = nenápadný, funkce funguje na většině vstupů

#### 85–90: 📝 Debrief

- _„Co nového ses naučil/a od spolužáka?"_
- _„Co bys příště udělal/a jinak?"_

### Časté problémy

| Problém                                      | Řešení                                                 |
| -------------------------------------------- | ------------------------------------------------------ |
| Student neví, jak napsat evil implementaci   | Napovězte: „Co kdybys vrátil vždycky stejnou hodnotu?" |
| Red Team je příliš snadný (testy jsou slabé) | To je učební moment! Diskutujte PROČ.                  |
| Red Team je příliš těžký (testy jsou dobré)  | Pochvalte autora testů. To je cíl!                     |
| Student je hotový rychle                     | Dejte mu roli „red team konzultant" pro ostatní        |

---

## Prezentace — systém rotace

### Co studenti prezentují

Svůj **úkol 4 z pre-worku: AI-driven TDD proces.** Každý student si vybral
jiný problém + měl jinou interakci s AI → každá prezentace je unikátní.

### Systém

- Na každém cviku prezentují **max 3 studenti** (3+2 min)
- Každý student musí prezentovat **alespoň 2× za semestr** (podmínka zápočtu)
- Dobrovolné prezentace navíc: **+2 bonusové body** za každou
- **Studenty oznamte týden předem** přes Moodle/email — ne na začátku hodiny
- Tracking: tabulka v Moodlu/Excelu, kdo kdy prezentoval

### Proč AI+TDD jako téma prezentace

- **Každá prezentace je unikátní** — jiný problém, jiná AI konverzace
- **Neprůstřelné proti AI cheatu** — student musí vysvětlit PROCES, ne jen výsledek
- **Učí technickou komunikaci** — „jak jsem řídil AI" = „jak jsem specifikoval požadavky"
- **Ukazuje limity AI** — spolužáci vidí, kde AI selhává a proč záleží na kvalitě testů
