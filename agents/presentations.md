# Doporučení pro tvorbu prezentací

## Základní požadavky

- Každá prezentace má být navržena přibližně na 45 minut výuky.
- Pro 45minutovou přednášku počítejte orientačně s 25–35 slajdy. Upřednostňujte více stručných slajdů, mezi kterými lze rychle přecházet, před několika přeplněnými slajdy.
- Na přednášku navazuje 90minutový seminář a 90minutové cvičení, proto se soustřeďte především na teorii, definice a vztahy mezi pojmy.
- Pro sazbu používejte [projektovou LaTeXovou šablonu](../utils/presentation-template/README.md), která vychází z motivu ČVUT a nevyžaduje externí fonty.
- Každé téma má vlastní prezentaci uloženou jako `topics/*/lecture/presentation.pdf`.
- Ve stejné složce uchovávejte také všechny zdrojové soubory konkrétní prezentace, zejména soubor `.tex`, vlastní obrázky a případná data.
- Do složky tématu nekopírujte soubory centrální šablony ani pomocné soubory LaTeXu. Verzujte pouze zdrojové soubory, výsledné PDF a skutečné podklady prezentace.
- Prezentace musí být sestavitelná ze zdrojových souborů bez ručních dodatečných úprav.

## Obsah a struktura

- Na začátku stručně uveďte:
  - co se studenti naučí,
  - proč je téma důležité,
  - na jaké předchozí znalosti navazuje.
- Obsah rozdělte do několika krátkých, logicky navazujících částí.
- Kdykoli je to vhodné, stavte výklad kolem otázek a odpovědí.
- Zaměřte se hlavně na definice a pojmy, které studenti potřebují znát.
- Každý nový pojem:
  - stručně vysvětlete,
  - pokud je vhodné, ukažte na konkrétním příkladu,
  - pokud je dále vhodné, upozorněte na častou chybu nebo nedorozumění.
- Každý odborný pojem uvedený v diagramu, schématu nebo srovnání musí být v prezentaci také vysvětlen. Nepředpokládejte například, že studenti znají pojmy jako linker, runtime, bytecode nebo staging area.
- Složitější proces rozdělte na:
  - přehledový slajd ukazující celý proces,
  - navazující krátké slajdy vysvětlující jednotlivé kroky.
- Postupujte od jednoduchého příkladu ke složitějšímu.
- Neuvádějte obecné zdroje k dalšímu studiu na konci prezentace. Jejich místo je v `README.md` daného tématu, aby se informace neduplikovaly.
- Zdroj uvádějte přímo v prezentaci pouze tehdy, když je nezbytný pro konkrétní převzatý obrázek, graf, citaci nebo tvrzení.

## Podoba slajdů

- Jeden slajd by měl sdělovat jednu hlavní myšlenku.
- Používejte stručné odrážky místo dlouhých souvislých odstavců.
- Pokud slajd obsahuje více samostatných definic nebo kroků, zvažte jeho rozdělení na několik slajdů.
- Udržujte jednotné názvosloví, formátování, barvy a typografii.
- Dbejte na dostatečně velké písmo a dobrý kontrast.
- Slajdy nepřeplňujte; podrobnosti patří do výkladu nebo doprovodných materiálů.
- Zvýrazňujte pouze nejdůležitější části kódu nebo textu.
- Obrázky, grafy a schémata musí být čitelné, relevantní a opatřené uvedením zdroje, pokud nejsou vlastní.
- Obrázky nikdy nedeformujte nezávislým nastavením šířky a výšky. Zachovávejte jejich poměr stran; zvláštní pozornost věnujte logům a značkám.
- Používejte správnou češtinu a před odevzdáním proveďte jazykovou kontrolu.

## Úvodní slajd

- Název konkrétní přednášky (hlavní nadpis)
- Doplňující informace uveďte na samostatných řádcích:
  - Základy programování
  - Matouš Cejnek (případně jiný přednášející dle pokynů)
  - U12110, FS, ČVUT v Praze

## Kontrola před dokončením

- Ověřte, že prezentace odpovídá přibližně 45 minutám výuky a obsahuje časovou rezervu na dotazy.
- Sestavte prezentaci z čistého stavu a zkontrolujte, že nevznikají chyby ani chybějící odkazy.
- Projděte výsledné PDF a zkontrolujte čitelnost textu, kódu, obrázků a rovnic.
- Vizuálně zkontrolujte alespoň titulní slajd, nejhustší textový slajd a všechny typy diagramů použitých v prezentaci.
- Zkontrolujte, že žádný obsah nepřetéká mimo slajd a že loga ani ostatní obrázky nejsou roztažené nebo stlačené.
- Ověřte správnost všech příkladů kódu a jejich výstupů.
- Zkontrolujte, že v PDF nezůstaly pracovní poznámky, dočasné slajdy ani nevyřešené značky typu TODO.
- Ujistěte se, že PDF i jeho zdrojové soubory jsou uložené ve správné složce tématu.

## Sestavení v pracovním prostředí Windows/MiKTeX

Při automatizovaném sestavení na tomto stroji nenechávejte úplný výstup
`pdflatex` proudit do terminálu nástroje. Výstup je velmi dlouhý a po zaplnění
výstupní roury může proces zůstat viset, přestože v LaTeXovém zdroji není
chyba. Typickým příznakem je stále běžící proces `pdflatex` a nedokončený
soubor `.log`.

Spolehlivý postup v PowerShellu:

1. Pracujte ze složky `topics/<tema>/lecture/`.
2. Sestavujte pod izolovaným názvem úlohy, aby po předchozím přerušeném běhu
   nezůstaly zamčené pracovní soubory.
3. Každý průchod spusťte samostatně, podrobný terminálový výstup přesměrujte a
   vždy zkontrolujte návratový kód.

```powershell
$presentationBuildName = "presentation-build"

pdflatex -jobname=$presentationBuildName -interaction=nonstopmode -halt-on-error presentation.tex *> $null
if ($LASTEXITCODE -ne 0) { throw "První průchod pdflatex selhal: $LASTEXITCODE" }

pdflatex -jobname=$presentationBuildName -interaction=nonstopmode -halt-on-error presentation.tex *> $null
if ($LASTEXITCODE -ne 0) { throw "Druhý průchod pdflatex selhal: $LASTEXITCODE" }

Copy-Item -LiteralPath "$presentationBuildName.pdf" -Destination "presentation.pdf" -Force
```

MiKTeX zapisuje uživatelské logy a cache do profilu uživatele. V omezeném
automatizovaném prostředí proto může být nutné spustit `pdflatex` s povolením
zápisu mimo sandbox. Neobcházejte chybu opakovaným spouštěním dalších procesů;
nejprve ověřte, zda nezůstal viset předchozí `pdflatex`, a případně ukončete
pouze tento konkrétní proces.

Po úspěšném sestavení ponechte ve verzovaných souborech jen
`presentation.tex`, výsledný `presentation.pdf` a skutečné podklady
prezentace. Pomocné soubory `presentation-build.*` odstraňte až po ověření, že
výsledné PDF existuje a má očekávaný počet stran.
