# Domácí příprava a seminář: základní Git workflow

## Domácí příprava

- vyzkoušejte si úkol vyřešit doma (repozitář si pojmenujte jinak)
- na hodině budete pracovat z nuly dle instrukcí
- domácí příprava vás má připravit na rychlé řešení úkolů

Na semináři se projde stejné zadání krok za krokem. Vyučující jednotlivé
operace okomentuje, podrobněji vysvětlí jejich význam a ukáže řešení častých
problémů. Před seminářem se proto pokuste celé zadání dokončit samostatně a
poznamenejte si kroky, kterým nerozumíte nebo u kterých jste se zasekli.

## Co a jak odevzdat

- Odkaz na váš **veřejný GitHub repozitář**.
- Odevzdejte v systému moodle.

## Úkol 1
Postupujte přesně v daném pořadí.

- Vytvořte **veřejný repozitář na GitHubu** (nebo ekvivalentní službě) s názvem `progintro` ve svém účtu.
- Naklonujte repozitář do svého počítače.
- Vytvořte soubor `README.md` a vložte do něj text zadaný vyučujícím na cvičení.
- Vytvořte commit s tímto souborem a odešlete jej do repozitáře se zprávou **added readme“**.
- Ve svém počítači vytvořte novou větev s názvem **`dev`**. Do souboru `README.md` přidejte řádek s textem **Under development**.
- V této větvi přidejte nový **prázdný textový soubor**.
- Proveďte commit změn (soubor `README.md` a nový soubor) a odešlete větev **`dev`** na GitHub.
- Upravte soubor `README.md` přímo v online rozhraní GitHubu ve větvi **`dev`** a použijte zprávu commitu **„edited online“**.
- Proveďte sloučení (merge) větve **`dev`** do větve **`master`** přímo na GitHubu.
- Vytvořte **release** repozitáře s názvem **`v0.1`** (tag může být také `v0.1`).

## Úkol 2

Tento úkol navazuje na **Úkol 1**. Pracujte ve
stejném repozitáři `progintro`. Cílem je naučit se
pracovat s větvemi a vyřešit konflikt při slučování.

Postupujte podle kroků:

1. Ujistěte se, že jste ve větvi **`master`** a máte aktuální verzi repozitáře.

2. Vytvořte novou větev s názvem **`conflict-test`** a přepněte se do ní.

3. V této větvi upravte soubor `README.md`:
   - změňte nebo přepište jeden konkrétní řádek (např. přidejte vlastní text).

4. Změny commitněte.

5. Přepněte se zpět do větve **`master`**.

6. Ve stejné části souboru `README.md` proveďte jinou změnu (upravit stejný řádek jako v předchozí větvi).

7. Změny commitněte.

8. Pokuste se sloučit větev **`conflict-test`** do **`master`**.

9. Vznikne konflikt:
   - otevřete soubor `README.md`,
   - ručně upravte obsah tak, aby dával smysl (zachovejte nebo vhodně spojte změny),
   - odstraňte konfliktní značky (`<<<<<<<`, `=======`, `>>>>>>>`).

10. Po vyřešení konfliktu:
    - přidejte soubor do stage,
    - dokončete merge commit.

11. Výsledek odešlete na GitHub.
