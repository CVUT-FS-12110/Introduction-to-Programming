# Kompilace kódu a verzování

## Prerekvizity

- Připravte si vlastní účet na Github (nebo ekvivalentní službě)
kam se dokážete během cvičení připojit.
- Pokud chcete používat vlastní počítač (doporučeno),
  nainstalujte si vhodné IDE - Visual Studio Code

## Cíle

- Vysvětlit rozdíl mezi kompilací a interpretací.
- Nakonfigurovat IDE pro editaci, sestavení a spouštění malých programů.
- Online běhová prostředí – notebooky, Colab apod.
- Používat Git pro základní workflow verzování (init, commit, branch).

## Přednáška

[Prezentace: Kompilace kódu a verzování](lecture/presentation.pdf)

## Domácí příprava

[Zadání domácí přípravy: základní Git workflow](prework/assignment.md)

## Seminář

Seminář se zaměřuje na to, jak se zdrojový kód stává spustitelným softwarem
a jaké nástroje tento proces podporují. Studenti se seznámí s rozdílem mezi
kompilací a interpretací, se základy verzování pomocí Gitu a s klíčovými funkcemi a workflow v IDE, které urychlují vývoj a ladění.

### Osnova

1. Kompilace vs. interpretace (jak se kód stává spustitelným)
2. Nástroje: kompilátory, interprety, runtime prostředí
3. Základy verzování pomocí Gitu
4. Funkce IDE: editace, ladění, klávesové zkratky
5. Doporučené workflow a osvědčené postupy

Na semináři se společně projde [stejné zadání jako v domácí
přípravě](prework/assignment.md). Jednotlivé kroky budou doplněny komentářem,
podrobnějším vysvětlením příkazů a ukázkami řešení obvyklých problémů.

## Cvičení

Cvičení je věnováno rozsáhlejšímu Git workflow, které propojuje práci s
větvemi, vzdáleným repozitářem, konflikty a úpravy historie.

[Zadání cvičení: pokročilé Git workflow](lab/advanced_git_workflow.md)

### Ukázkový kód (Python)

Spusťte následující kód ve vašem IDE a ukažte cvičícímu.
```python
# hello.py
def main():
    print("Hello, world!")

if __name__ == "__main__":
    main()
```
Pokud vám zbude čas, věnujte ho pochopení a vylepšení programu výše.

## Zdroje

- [Pro Git, 2nd Edition](https://git-scm.com/book/en/v2)
- [Dokumentace jazyka Python](https://docs.python.org/3/)
- [Python Developer's Guide – compiler](https://devguide.python.org/internals/compiler/)
- [GNU Compiler Collection – dokumentace](https://gcc.gnu.org/onlinedocs/)
