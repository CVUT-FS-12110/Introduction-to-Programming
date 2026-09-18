# Cvičení: knihovny a dokumentování kódu

Cvičení je **samostatná práce na 90 minut**. Úlohy na sebe navazují a staví
jeden nástroj příkazové řádky. Základní části by měl zvládnout každý;
poslední úlohy jsou rozšíření pro rychlejší studenty.

| Obtížnost | Co znamená |
|-----------|------------|
| ★ | základní práce s prostředím a dokumentací |
| ★★ | propojení knihovny s vlastními funkcemi |
| ★★★ | samostatné dohledání rozhraní a ošetření chyb |
| ★★★★ | návrh distribuovatelného projektu |

Pro celé cvičení platí:

- pracujte v novém adresáři a aktivním prostředí `.venv`,
- balíčky instalujte přes `python -m pip`,
- `.venv` necommitujte; přidejte jej do `.gitignore`,
- po změně závislostí aktualizujte `requirements.txt`,
- program musí jít spustit z terminálu příkazem `python main.py ...`.

---

## 1. Připravte reprodukovatelné prostředí ★

Prozkoumejte repozitář knihovny [Click](https://github.com/pallets/click/)
a její oficiální dokumentaci. Potom:

1. zjistěte název balíčku na PyPI a podporované verze Pythonu,
2. vytvořte a aktivujte `.venv`,
3. nainstalujte knihovnu,
4. ověřte instalaci příkazem
   `python -c "from importlib.metadata import version; print(version('click'))"`,
5. vytvořte `requirements.txt`, `.gitignore` a krátký `README.md`.

Do README zapište přesné příkazy pro přípravu a spuštění projektu.

## 2. První příkaz ★

Napište `main.py`, který pomocí knihovny Click přijme volbu `--name`
a vypíše pozdrav. Výchozí jméno je `World`.

```text
python main.py --name Pavel
Hello, Pavel!

python main.py
Hello, World!
```

Nápovědu hledejte v části Quickstart dokumentace. Ověřte také automaticky
vytvořenou nápovědu příkazem `python main.py --help`.

## 3. Volby, typy a validace ★★

Přidejte volby:

- `--count` — kladné celé číslo, výchozí hodnota `1`,
- `--language` — jedna z hodnot `cs` nebo `en`,
- `--loud` — přepínač, který převede pozdrav na velká písmena.

Neplatné hodnoty má odmítnout Click, nikoli ručně napsaná podmínka po spuštění
příkazu. Z dokumentace zjistěte, jak deklarovat rozsah čísla a výběr z hodnot.

## 4. Oddělte rozhraní od logiky ★★

Přesuňte tvorbu textu do běžné funkce:

```python
def make_greeting(name: str, language: str = "en", loud: bool = False) -> str:
    ...
```

Funkce nesmí importovat Click ani vypisovat na obrazovku. Click příkaz pouze
načte argumenty, zavolá funkci a vypíše návratovou hodnotu požadovaný početkrát.

Doplňte docstring, který popisuje parametry, návratovou hodnotu a přípustné
hodnoty `language`. Ověřte ho pomocí `help(make_greeting)`.

## 5. Více příkazů ★★★

Změňte aplikaci na skupinu se dvěma podpříkazy:

- `greet` — dosavadní pozdrav,
- `add` — přijme dvě celá čísla jako poziční argumenty a vypíše součet.

```text
python main.py greet --name Pavel --language cs
Ahoj, Pavel!

python main.py add 3 5
8
```

Z dokumentace vyhledejte `click.group`, `click.command`, `click.option`
a `click.argument`. Zkontrolujte nápovědu celé skupiny i obou příkazů.

## 6. Vstupní a výstupní soubor ★★★

Přidejte příkaz `stats INPUT`, který spočítá počet řádků, slov a znaků
v textovém souboru. Volitelná volba `--output PATH` uloží výsledek do souboru;
bez ní se výsledek vypíše do terminálu.

Použijte typy cest a souborů, které nabízí Click. Program má srozumitelně
reagovat na neexistující vstup a nesmí omylem přepsat vstupní soubor.
Samotný výpočet opět oddělte do běžné funkce nezávislé na Clicku.

## 7. Dokumentaci ověřte na čistém prostředí ★★★

Deaktivujte `.venv`, vytvořte nové prostředí `.venv-check` a postupujte pouze
podle vlastního README:

1. nainstalujte závislosti z `requirements.txt`,
2. spusťte všechny tři příkazy a jejich `--help`,
3. zkontrolujte, že v README nechybí žádný krok,
4. opravte dokumentaci podle skutečného průběhu.

Po kontrole můžete `.venv-check` odstranit. Do repozitáře patří zdrojové
soubory, README, `.gitignore` a `requirements.txt`, nikoli virtuální prostředí.

## 8. Vlastní knihovna podle dokumentace ★★★★

Vyberte jednu knihovnu z domácí přípravy a přidejte nový příkaz, který ji
smysluplně využije. Příkaz musí:

- přijímat alespoň jeden vstup od uživatele,
- využít veřejné API knihovny dohledané v dokumentaci,
- ošetřit očekávatelnou chybu,
- mít automatickou nápovědu a příklad použití v README,
- mít závislost zaznamenanou v `requirements.txt`.

Na konec README přidejte odkaz na konkrétní stránku dokumentace, podle které
jste postupovali, a dvě věty o tom, co jste z ní museli zjistit.
