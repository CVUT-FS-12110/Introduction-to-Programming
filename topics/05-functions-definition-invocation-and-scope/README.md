# Funkce — definice, volání a rozsah platnosti

Funkce je pojmenovaný kus kódu, který můžeme opakovaně použít. Díky
funkcím je program kratší, čitelnější a snáze se testuje. V této lekci
se naučíme funkce psát, volat a rozumět tomu, **kde která proměnná platí**.

## Prerekvizity

- Podmínky a cykly
  ([předchozí téma](../04-control-flow-loops-and-conditionals/README.md))
- Datové typy a kontejnery Pythonu
  ([téma Datové typy a vstup/výstup](../03-data-types-io/README.md))

## Cíle

- Definovat vlastní funkci pomocí `def` a zavolat ji.
- Předávat funkci parametry a vracet výsledek pomocí `return`.
- Používat výchozí hodnoty parametrů a pojmenované argumenty.
- Rozlišit lokální a globální proměnnou a vysvětlit rozsah platnosti (scope).
- Rozdělit delší program na několik krátkých funkcí.

## Přednáška

- [Slajdy: Funkce](lecture/presentation.pdf)
- [Komentované příklady](seminar/README.md)

V komentovaných příkladech rozdělíme delší program na funkce, porovnáme
`print` a `return` a budeme sledovat lokální a globální rozsah platnosti.

## Domácí příprava

[Zadání domácí přípravy: vlastní funkce a rozsah platnosti](prework/README.md)

## Cvičení

Samostatné psaní vlastních funkcí a jejich skládání do většího celku.

[Zadání cvičení](lab/assignment.md)

## Zdroje

- [Python Tutorial: Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) — oficiální úvod do funkcí
- [Python FAQ: What are the rules for local and global variables?](https://docs.python.org/3/faq/programming.html#what-are-the-rules-for-local-and-global-variables-in-python) — pravidla rozsahu platnosti
- [PEP 8: Function names](https://peps.python.org/pep-0008/#function-and-variable-names) — jak funkce pojmenovávat
