# Organizace výukových témat (`topics`)

Tento dokument určuje výchozí strukturu veřejných výukových materiálů. Před
úpravou tématu si vždy přečtěte také kořenový `AGENTS.md`, `README.md` daného
tématu a případné specializované pokyny v `agents/`.

## Umístění a základní struktura

Každé téma patří do samostatné složky:

```text
topics/<topic-name>/
├── README.md
├── lecture/
├── prework/
├── seminar/
└── lab/
```

- Název `<topic-name>` zapisujte anglicky, malými písmeny a s pomlčkami.
- Zachovávejte již použitý název tématu. Složku nepřejmenovávejte bez
  výslovného požadavku.
- Všechny čtyři podsložky vytvořte i tehdy, když pro některou část zatím není
  materiál.
- Prázdnou složku, která má zůstat v Gitu, opatřete souborem `.gitkeep`.
- Jakmile do složky přibude skutečný podklad, nepotřebný `.gitkeep` odstraňte.
- Nevkládejte mezi téma a tyto čtyři složky další obecnou vrstvu typu
  `examples/`, `materials/` nebo `tasks/`.

## Co patří do jednotlivých částí

### `lecture/` — přednáška

Patří sem výklad vedený vyučujícím, zejména:

- `presentation.tex`,
- výsledný `presentation.pdf`,
- obrázky, data a další skutečné zdroje konkrétní prezentace.

Pro tvorbu a sestavení prezentací platí [pokyny pro
prezentace](presentations.md). Centrální šablonu z
`utils/presentation-template/` do tématu nekopírujte. Šablona musí zůstat
kompletní a verzovaná ve svém původním umístění.

Pomocné soubory LaTeXu (`.aux`, `.log`, `.nav`, `.out`, `.snm`, `.toc` a
podobné) nejsou podklady a nesmějí se verzovat. Jejich ignorování ověřte přes
`git status --ignored`.

### `prework/` — domácí příprava

Patří sem práce, kterou má student udělat nebo alespoň zkusit před výukou.

- Uveďte cíl, předpoklady, zadání a očekávanou přípravu.
- Neprozrazujte řešení, pokud o ně uživatel výslovně nepožádá.
- Prework může být stejný jako úloha probíraná na semináři nebo může
  připravovat část následného cvičení.
- Pokud je prework stejný jako seminární úloha, udržujte jedno autoritativní
  zadání a ze semináře na něj odkažte. Nekopírujte dvě verze textu, které by se
  mohly časem rozejít.

### `seminar/` — komentovaný průchod

Na semináři pracuje především vyučující společně se studenty. Materiál má být
podrobný a vysvětlující.

- Popište postup, souvislosti a důvody jednotlivých kroků.
- Uveďte časté chyby, otázky k diskusi a místa vhodná k demonstraci.
- Pokud seminář prochází prework, napište to výslovně a odkažte na stejné
  zadání.
- Návody a referenční taháky používané při semináři ukládejte sem.
- Veřejné seminární podklady nesmějí obsahovat skryté učitelské řešení.

### `lab/` — samostatné cvičení

Na cvičení pracují studenti převážně samostatně.

- Zadání formulujte jako jasnou posloupnost úkolů nebo dosažitelný výsledek.
- Přidejte potřebný výchozí stav, omezení a bezpečnostní upozornění.
- Obtížnost a rozsah přizpůsobte času určenému uživatelem.
- Standardně neuvádějte, co vyučující kontroluje, bodování ani povinné
  odevzdání: výsledek samostatného cvičení se běžně nekontroluje.
- Kontrolní body lze použít jako sebekontrolu nebo orientaci v delším zadání,
  nikoli automaticky jako hodnoticí kritéria.
- Sekci o odevzdání či hodnocení přidejte pouze na výslovný pokyn uživatele.

## `README.md` tématu

Každé téma musí mít hlavní `README.md`, ze kterého jsou dostupné všechny
studentské podklady. Doporučené pořadí:

1. název tématu,
2. prerekvizity,
3. cíle,
4. přednáška,
5. domácí příprava,
6. seminář,
7. cvičení,
8. zdroje.

Pravidla pro odkazy:

- Používejte relativní odkazy, například
  `lecture/presentation.pdf`, `prework/assignment.md` nebo `lab/task.md`.
- Každý studentský podklad musí být z hlavního `README.md` dosažitelný.
- Návod vztahující se ke konkrétnímu zadání odkažte také přímo ze zadání.
- Po přesunu souborů vyhledejte v celém repozitáři starou cestu pomocí `rg` a
  opravte všechny výskyty.
- Nadpisy v README rozdělte na `Seminář` a `Cvičení`; neslučujte je do jedné
  sekce.

## Veřejné a učitelské materiály

Repozitář `Introduction-to-Programming/` je veřejný. Patří sem zadání, studijní
texty, prezentace, návody a veřejné příklady.

Řešení, metodické poznámky, skrytá zadání, testy a banky otázek patří do
`Introduction-to-Programming-Teacher/`. Obsah z učitelského repozitáře nikdy
nekopírujte do veřejného repozitáře bez výslovného pokynu uživatele. Související
témata v obou repozitářích pojmenovávejte stejně.

## Postup agenta při změně tématu

1. Ověřte, ve kterém ze dvou repozitářů pracujete.
2. Přečtěte kořenový `AGENTS.md`, tento dokument a místní `README.md`.
3. Zmapujte strom cílového tématu a vyhledejte odkazy na přesouvané soubory.
4. Zařaďte každý podklad podle jeho účelu do `lecture`, `prework`, `seminar`
   nebo `lab`.
5. Zachovejte uživatelské změny a nepřepisujte nesouvisející rozpracovanou
   práci.
6. Aktualizujte hlavní README a všechny vnitřní relativní odkazy.
7. Při změně `presentation.tex` znovu sestavte `presentation.pdf` podle
   `agents/presentations.md`.
8. Odstraňte pouze prokazatelně dočasné soubory vytvořené během vlastní práce.
9. Proveďte závěrečnou kontrolu níže.

## Závěrečná kontrola

Před dokončením ověřte:

- téma obsahuje `README.md` a přesně čtyři základní podsložky,
- všechny podklady jsou ve složce odpovídající jejich účelu,
- prázdné požadované složky mají `.gitkeep`,
- žádná cesta stále neodkazuje na staré umístění souboru,
- všechny relativní odkazy vedou na existující soubory,
- veřejný repozitář neobsahuje skryté řešení ani učitelské poznámky,
- čeština, názvosloví a názvy souborů jsou konzistentní,
- `git diff --check` nehlásí chyby formátování,
- `git status --short --ignored` potvrzuje, že pomocné LaTeX soubory jsou
  ignorované a skutečné zdroje zůstávají verzované,
- změněná prezentace se sestavila ve dvou průchodech a její problematické
  slajdy byly vizuálně zkontrolovány.
