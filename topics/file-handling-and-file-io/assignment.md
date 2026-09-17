# Úkoly

## Úloha na doma — osobní poznámkový soubor

Vytvořte ručně textový soubor `poznamky.txt`, který bude obsahovat alespoň:

- 5 řádků textu,
- alespoň jeden řádek s českými znaky,
- alespoň jeden prázdný řádek.

Potom napište program `analyza_poznamek.py`, který:

1. soubor bezpečně otevře pro čtení,
2. vypíše všechny neprázdné řádky očíslované od 1,
3. na konci vypíše:
   - celkový počet řádků,
   - počet neprázdných řádků,
   - počet znaků bez konců řádků.

Program musí používat:

- `with open(...)`,
- explicitní `encoding="utf-8"`,
- zpracování po řádcích, ne načtení celého souboru jedním `read()`.

### Smysl domácí přípravy

Studenti si ještě před seminářem sáhnou na:

- rozdíl mezi „soubor existuje na disku“ a „program s ním pracuje“,
- konce řádků a prázdné řádky,
- základní důvod, proč uvádět kódování.

