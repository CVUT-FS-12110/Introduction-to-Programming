# Úvod do Bashe a práce v terminálu

> Materiál k [tématu 01](../README.md). Krátký přehled toho, co potřebujete k tomu, abyste se v terminálu neztratili. Většina příkazů funguje stejně v Linuxu, ve [WSL](wsl.md), na macOS i v Git Bashi; kde se liší, je to uvedeno (např. `sudo` a `apt` jsou jen v Linuxu / WSL).

## Základní pojmy

- **Terminál** je okno (program), do kterého píšete příkazy a vidíte jejich výstup. Sám příkazům nerozumí, jen zprostředkovává vstup a výstup. Příklady: Terminál Windows, terminál ve VS Code, Terminal na macOS.
- **Shell** (příkazový interpret) je program, který běží uvnitř terminálu, čte příkazy, které napíšete, a spouští je. Různé shelly mají různou syntaxi a různé příkazy.
- **Bash** (*Bourne Again Shell*) je nejrozšířenější shell v Linuxu a je výchozí ve většině distribucí včetně Ubuntu ve WSL. Na macOS je výchozí podobný **zsh**; základní příkazy se používají stejně, rozdíly se projeví až u složitějších skriptů.
- **cmd** (Příkazový řádek, `cmd.exe`) je starší shell Windows, který navazuje na příkazový řádek MS-DOS (`COMMAND.COM`). Má omezené možnosti a vlastní syntaxi (`dir`, `cd`, `copy`), s Bashem nekompatibilní.
- **PowerShell** je novější shell Windows (dostupný i pro Linux a macOS). Místo textu pracuje s objekty a má vlastní příkazy (např. `Get-ChildItem`), i když pro pohodlí zná (ve Windows) aliasy jako `ls` nebo `cd`. S Bashem také není kompatibilní.

Pozor na časté zaměňování: *terminál* je okno, *shell* je program v něm. Jeden terminál může spustit libovolný shell, např. Terminál Windows umí otevřít PowerShell, cmd i Bash z WSL.

| | Platforma | Poznámka |
|---|---|---|
| Bash | Linux, WSL, (macOS, Git Bash) | **tento text**, standard v prostředí vývojářů |
| zsh | macOS | základní příkazy stejné jako v Bashi, ve skriptech drobné rozdíly |
| PowerShell | Windows (i Linux, macOS) | objektový, jiné příkazy |
| cmd | Windows | starší, omezený |

## Proč nás zajímá linuxový shell

V kurzu budeme pracovat hlavně s **linuxovým shellem (Bashem)**, protože:

- návody k Gitu, Pythonu a dalším nástrojům jsou psané pro Bash,
- stejné příkazy použijete na vlastním počítači, na školním serveru i v cloudu,
- servery a automatizace (CI, kontejnery) téměř vždy běží na Linuxu.

Uživatelé Windows si Bash zprovozní přes [WSL](wsl.md) (nebo alespoň Git Bash, který se instaluje společně s Gitem). Na Linuxu je Bash výchozí; na macOS je výchozí zsh, který pro náš kurz stačí.

## Prompt a spouštění příkazů

Řádek s příkazem obvykle začíná tzv. *promptem*, např. `martin@pc:~$`. Prompt nepíšete, píšete až za něj, a příkaz spustíte klávesou **Enter**. V příkladech níže se `$` neuvádí.

## Kde jsem a co tu je

```bash
pwd        # vypíše aktuální složku (print working directory)
ls         # vypíše obsah složky
ls -l      # podrobný výpis (práva, velikost, datum)
ls -a      # včetně skrytých souborů (začínají tečkou)
```

## Pohyb po složkách

```bash
cd projekty     # přejdi do složky "projekty"
cd ..           # o úroveň výš
cd ~            # do domovského adresáře (stejně jako samotné cd)
cd -            # zpět do předchozí složky
```

Cesty mohou být:

- **absolutní** — začínají lomítkem: `/home/martin/projekty`,
- **relativní** — vztahují se k aktuální složce: `projekty/progintro`, `../jina-slozka`.

Zkratky: `.` je aktuální složka, `..` nadřazená, `~` domovská.

Název s mezerou dejte do uvozovek (`cd "moje slozka"`) nebo mezeru uvozte zpětným lomítkem (`cd moje\ slozka`). V názvech souborů se mezerám raději vyhýbejte.

## Soubory a složky

```bash
mkdir projekty              # vytvoř složku
mkdir -p a/b/c              # vytvoř i chybějící nadřazené složky
touch poznamky.txt          # vytvoř prázdný soubor
cp poznamky.txt kopie.txt   # zkopíruj soubor
cp -r slozka zaloha         # zkopíruj složku včetně obsahu
mv kopie.txt novy_nazev.txt # přejmenuj / přesuň
rm novy_nazev.txt           # smaž soubor
rm -r zaloha                # smaž složku včetně obsahu
```

> **Pozor:** `rm` maže nenávratně — žádný koš neexistuje. Před smazáním si ověřte, co `ls` ukazuje, a opatrně s `rm -r`.

## Čtení obsahu souborů

```bash
cat poznamky.txt         # vypíše celý soubor
head -n 5 poznamky.txt   # prvních 5 řádků
tail -n 5 poznamky.txt   # posledních 5 řádků
less poznamky.txt        # prohlížení po stránkách (ukončení klávesou q)
```

Chcete-li soubor upravit, nejjednodušší je `nano poznamky.txt` (ukládání `Ctrl+O`, konec `Ctrl+X`) nebo `code poznamky.txt`, pokud máte VS Code.

## Nápověda

```bash
man ls          # manuál příkazu (ukončení klávesou q)
ls --help       # stručná nápověda
```

> `ls --help` funguje v Linuxu a WSL; na macOS použijte `man ls`. V Git Bashi příkaz `man` není, tam pomůže `příkaz --help` nebo internet.

Na internetu se hodí i [tldr](https://tldr.sh/) — zkrácené příklady použití příkazů.

## Spouštění programů

```bash
python3 main.py          # spustí Python skript
git status               # příkazy mohou mít podpříkazy a přepínače
```

> V Linuxu, WSL a na macOS se Python obvykle spouští jako `python3`. V Git Bashi ve Windows použijte `python`.

Přepínače (*options*) začínají pomlčkou: krátké `-l`, dlouhé `--help`. Krátké lze spojovat: `ls -la` je totéž co `ls -l -a`.

## Přesměrování a roury

Každý program má výstup, který normálně jde na obrazovku. Můžete ho přesměrovat:

```bash
echo "ahoj" > soubor.txt     # zapíše text do souboru (přepíše ho!)
echo "svete" >> soubor.txt   # připíše na konec souboru
ls | less                    # výstup jednoho příkazu pošle jako vstup druhému (roura)
```

Roury propojují jednoduché příkazy do větších celků, např. počet položek (souborů i složek, bez skrytých) ve složce: `ls | wc -l`.

## Proměnné prostředí a PATH

```bash
echo $HOME      # hodnota proměnné HOME
echo $PATH      # seznam složek, kde shell hledá spustitelné programy
```

Když napíšete `python3`, shell projde složky v `PATH` a spustí první nalezený program toho jména. Proto při instalaci nástrojů často zaznívá „přidejte do PATH".

## Oprávnění souborů

Linux u každého souboru a složky eviduje, kdo s ním smí co dělat. Výpis `ls -l` ukazuje:

```text
-rwxr-xr--  1 martin studenti  120 říj  4 10:15 skript.py
```

- první znak je typ (`-` soubor, `d` složka),
- dalších devět znaků jsou tři trojice oprávnění pro **vlastníka** (`rwx`), **skupinu** (`r-x`) a **ostatní** (`r--`),
- `r` = čtení (*read*), `w` = zápis (*write*), `x` = spuštění (*execute*; u složek právo do ní vstoupit),
- dále následuje počet odkazů (`1`), jméno vlastníka (`martin`), jméno skupiny (`studenti`), velikost v bajtech (`120`), datum poslední změny a název souboru.

V praxi se s tím poprvé setkáte jako s chybou `Permission denied` — zkoušíte něco přečíst, změnit nebo spustit bez oprávnění.

Oprávnění se mění příkazem `chmod`:

```bash
chmod +x skript.sh    # přidá všem právo spuštění
chmod -w poznamky.txt # odebere právo zápisu (chrání proti nechtěnému přepsání, ne proti smazání)
```

Pythonové skripty spouštíte přes `python3 skript.py`, takže právo `x` nepotřebují. Hodí se u shellových skriptů, které spouštíte přímo jako `./skript.sh`.

## Správce systému a `sudo`

V Linuxu existuje speciální uživatel **root** (správce), který smí všechno — včetně změn systémových souborů a instalace programů pro všechny uživatele. Běžný uživatel (vy) toto právo nemá, aby jeho chyba nemohla poškodit systém.

Příkaz `sudo` (*superuser do*) spustí jeden konkrétní příkaz s právy správce, po zadání vašeho hesla (toho, které jste nastavili při instalaci Linuxu, ne zvláštního hesla roota). Heslo si systém na chvíli, zhruba 15 minut, pamatuje.

```bash
apt install tree         # selže: Permission denied (běžný uživatel nesmí instalovat do systému)
sudo apt install tree    # projde: instalace s právy správce (je třeba mít aktuální seznam: sudo apt update)
```

`sudo` potřebujete zejména pro instalaci a aktualizaci systémových balíčků (`apt`) a úpravy systémových nastavení. Pro práci s vlastními soubory ve vašem domovském adresáři ho **nepotřebujete** — pokud vám tam něco hlásí `Permission denied`, obvykle je chyba jinde a `sudo` ji jen zamaskuje (a může vytvořit soubory vlastněné rootem, které pak nepůjdou normálně upravit).

Zásady:

- `sudo` používejte jen u příkazů, kterým rozumíte,
- nikdy bezmyšlenkovitě nespouštějte s `sudo` příkazy zkopírované z internetu — s právy správce mohou smazat nebo poškodit celý systém,
- ve WSL máte `sudo` také. Root ve WSL nezíská administrátorská práva ve Windows, ale přes `/mnt/c` má Linux přístup k vašim souborům ve Windows, takže neopatrný příkaz (s `sudo` i bez něj) může smazat vaše data v distribuci i ve Windows.

## Užitečné klávesové zkratky

| Zkratka | Význam |
|---|---|
| `Tab` | doplní název souboru / příkazu (dvakrát: nabídne možnosti) |
| `↑` / `↓` | listování historií příkazů |
| `Ctrl+C` | přeruší běžící program |
| `Ctrl+L` | vyčistí obrazovku (stejně jako `clear`) |
| `Ctrl+R` | hledání v historii příkazů |
| `Ctrl+A` / `Ctrl+E` | skok na začátek / konec řádku |

`Tab` si osvojte hned — ušetří spoustu psaní i překlepů.

## Mini cvičení

1. Přejděte do domovského adresáře a vytvořte složku `bash-cviceni`.
2. Vstupte do ní a vytvořte soubor `ahoj.txt` s textem „Ahoj, světe" (pomocí `echo` a přesměrování).
3. Zkopírujte ho jako `ahoj2.txt` a vypište obsah obou souborů.
4. Vypište podrobný seznam souborů ve složce (`ls -l`).
5. Přejděte o úroveň výš a složku i s obsahem smažte.
6. Zjistěte pomocí `man` nebo `--help`, co dělá přepínač `-h` u příkazu `ls -l`.

## Další zdroje

- [GNU Bash Reference Manual](https://www.gnu.org/software/bash/manual/bash.html) — oficiální dokumentace
- [The Missing Semester of Your CS Education: The Shell](https://missing.csail.mit.edu/2020/course-shell/) — úvod do shellu z MIT
- [Linux Journey](https://labex.io/linuxjourney) — interaktivní úvod do Linuxu a příkazové řádky
- [Úvod do WSL](wsl.md) — jak si Bash zprovoznit ve Windows
