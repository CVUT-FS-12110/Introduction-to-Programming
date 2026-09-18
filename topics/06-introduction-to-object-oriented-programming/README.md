# Úvod do objektově orientovaného programování

Objektově orientované programování (OOP) je způsob, jak si program
uspořádat kolem **objektů** — věcí, které mají vlastnosti (data)
a chování (funkce). Například auto má barvu a značku a umí jet.
V této lekci si ukážeme, jak takové objekty v Pythonu vytvářet.

## Prerekvizity

- Funkce, parametry a návratové hodnoty
  ([předchozí téma](../05-functions-definition-invocation-and-scope/README.md))
- Datové typy a kontejnery Pythonu
  ([téma Datové typy a vstup/výstup](../03-data-types-io/README.md))

## Cíle

- Vysvětlit rozdíl mezi třídou (předpisem) a objektem (instancí).
- Napsat vlastní třídu s konstruktorem `__init__` a metodami.
- Pracovat s atributy objektu a rozumět významu `self`.
- Vytvořit potomka existující třídy pomocí dědičnosti a přepsat metodu.
- Rozhodnout, kdy se objekty vyplatí použít místo samostatných funkcí.

## Přednáška

- [Slajdy: Úvod do OOP](lecture/presentation.pdf)
- [Komentované příklady](seminar/README.md)

V komentovaných příkladech postupně vytvoříme třídu s konstruktorem,
atributy a metodami, několik nezávislých objektů a jednoduchou dědičnost.

## Domácí příprava

[Zadání domácí přípravy: třídy a objekty](prework/README.md)

## Cvičení

Samostatný návrh a implementace vlastních tříd pro zadanou úlohu.

[Zadání cvičení](lab/assignment.md)

## Zdroje

- [Python Tutorial: Classes](https://docs.python.org/3/tutorial/classes.html) — oficiální úvod do tříd a objektů
- [Real Python: OOP in Python 3](https://realpython.com/python3-object-oriented-programming/) — vysvětlení krok za krokem s příklady
- [Python Docs: Data model — special methods](https://docs.python.org/3/reference/datamodel.html#special-method-names) — co znamenají metody typu `__init__`
