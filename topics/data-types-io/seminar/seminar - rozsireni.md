# Seminář: úlohy


## Úloha 1 - Zadání

Elektrický obvod má 3 rezistory. V následujících krocích provedeme jeho analýzu.

# Úkoly

a)	Jednotlivá napětí jsou 5 V, 10 V, 15 V. Zapiš je do vektoru a poté vytiskni hodnoty pro jednotlivé rezistory např. ve formě „rezistor 1: 5 V“

b)	Definuj resistence matrix tak, že jednotlivé odpory budou ležet na diagonále matice a ostatní pole budou nulová. Např. urči si, že odpor na rezistoru 1 bude 2 ohmy, další 6 ohmy, a poslední 6 ohmů.

c)	Vypočítej celkový odpor v elektrickém obvodu. Nápověda: využij loop k výpočtu sumy jednotlivých elementů na diagonále.

d)	Využij vektor napětí V, a dále vytvoř matici vodivosti G (konduktance), jenž je inverzní maticí odporu. Najdi maximální hodnotu v této matici a urči její polohu (řádek a sloupec). Následně spočítej proud pomocí vzorce I = G V. Ověř, zda je obvod v rovnováze nebo ne. Pokud jsou si všechny proudy rovny, program vytiskne „Circuit is balanced“.

e)	Uprav obvod tak, aby byl v rovnováze. Proveď to tak, že změníš odpor u jednoho rezistoru. Znovu vypočítej proud a zjisti, zda je obvod v rovnováze při použití nových hodnot.

f)	Uprav vektor napětí tak, aby byl transponovaný. (Ze sloupcového vytvoř řádkový.)


## Úloha 2 - Zadání

Vytváříme elektronický volební systém. 

# Úkoly

a)	Máme 3 hlavní oblasti, za které se ve městě vybírají hlasy. Ve volbách se proti sobě utkaly 3 politické strany. Vytvoř matici s počty hlasů, když víš, že sloupce reprezentují jednotlivé strany a řádky reprezentují oblasti. Vytiskni celkový počet hlasů za oblast 1. Vytiskni počet hlasů za oblast 2 pro 2. politickou stranu.

Např. Oblast 1: Praha 1, Oblast 2: Praha 2, Oblast 3: Praha 3. Politické strany: „Květinky“, „NE“, „Barevní“.

b)	Z matice spočítej celkový počet hlasů pro jednotlivé strany a vytiskni je ve formátu: „Politická strana ODS: 360 (hlasů)“.

c)	Najdi výherce voleb a vytiskni informaci ve formátu: „Výherce voleb je: (název politické strany)“.

d)	Spočítej, kolik procent každá politická strana získala. Nápověda: vzorec pro výpočet = (počet hlasů pro stranu / celkový počet hlasů ve volbách) * 100.  Vytiskni informaci ve formátu „Politická strana A: xx % “.

e)	Vytvoř hranici, kterou musí politické strany splnit, aby se dostali do parlamentu. Nápověda: udělej treshold filter a pro politické strany s méně jak 10% hlasů uveď informaci, že nebudou dále postupovat do parlamentu.

f)	Pomocí D’Hondt metody rozdistribuuj sedadla v poslanecké sněmovně pro jednotlivé politické strany. Urči, kolik sedadel dostane každá politická strana a informaci vytiskni.

g)	Vytvoř sloupcový graf, kde je vizualizace výsledků hlasování pro jednotlivé politické strany.

