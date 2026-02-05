# Kompilace kódu a verzování

## Prerekvizity

- Připravte si vlastní účet na Github (nebo ekvivalentní službě)
kam se dokážete během cvičení připojit.
- Pokud chcete používat vlastní počítač (doporučeno),
  nainstalujte si vhodné IDE - Pycharm, Visual Studio Code

## Cíle

- Vysvětlit rozdíl mezi kompilací a interpretací.
- Nakonfigurovat IDE pro editaci, sestavení a spouštění malých programů.
- Online běhová prostředí – notebooky, Colab apod.
- Používat Git pro základní workflow verzování (init, commit, branch).

## Klíčová slova

Git, IDE, program, algoritmus, strojový kód, zdrojový kód

## Přednáška

TBA (základní pojmy, základní git)

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

## Cvičení

Cvičení má dvě části 

### Git workflow

Úkol je popsán na [tomhle odkazu](assignment.md)

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

- Git (https://git-scm.com/book/en/v2)
- Python: https://docs.python.org/3/
