# Komentované příklady: od cizí knihovny k reprodukovatelnému projektu

Materiál je vedený jako jeden průchod životním cyklem malého projektu.
Studenti pracují ve dvojicích, ale příkazy spouští každý ve vlastním adresáři.

## Co byste měli po společném průchodu umět

- vysvětlit, proč projekt potřebuje vlastní virtuální prostředí,
- vytvořit prostředí a ověřit, který Python a `pip` právě používáte,
- nainstalovat knihovnu a zaznamenat její verzi,
- obnovit závislosti projektu podle `requirements.txt`,
- najít v dokumentaci použití funkce a význam návratové hodnoty,
- popsat vlastní funkci docstringem a typovými nápovědami.

---

## 1. Kde vzniká konflikt závislostí

Společně projděte [scénář dvou projektů](examples/dependency_conflict/README.md).
Než spustíte příkazy, odpovězte:

1. Může jedna instalace obsahovat dvě různé verze stejného balíčku?
2. Co se stane s projektem A po aktualizaci balíčku pro projekt B?
3. Které soubory patří projektu a které do prostředí počítače?

Na školním ani osobním počítači kvůli demonstraci neměňte globální balíčky.
Konflikt ověříme ve dvou oddělených virtuálních prostředích.

## 2. Vytvoření izolovaného projektu

Podle [návodu k virtuálnímu prostředí](examples/virtual_environment_setup/README.md)
vytvořte prázdný adresář projektu a prostředí `.venv`.

Po aktivaci ověřte:

```powershell
python -c "import sys; print(sys.executable)"
python -m pip --version
```

Oba příkazy mají ukazovat dovnitř `.venv`. Diskutujte, proč je zápis
`python -m pip` jednoznačnější než samotné `pip`.

## 3. Instalace a reprodukce závislostí

Nainstalujte `requests`, zobrazte jeho metadata a vytvořte seznam závislostí:

```powershell
python -m pip install requests
python -m pip show requests
python -m pip freeze > requirements.txt
```

Prohlédněte `requirements.txt`. Potom vytvořte druhé prostředí `.venv-check`
a obnovte do něj projekt pomocí `python -m pip install -r requirements.txt`.

Otázky k diskusi:

- Proč `.venv` nepatří do Gitu, ale `requirements.txt` ano?
- Jaký je rozdíl mezi přímou a nepřímou závislostí?
- Co získáme přesnými verzemi a jakou nevýhodu mohou mít?

## 4. Dokumentace jako pracovní nástroj

Otevřete dokumentaci `requests` a bez opisování hotového řešení zjistěte:

- jak odeslat požadavek GET,
- kde je stavový kód odpovědi,
- jak nastavit časový limit,
- jak převést JSON odpověď na Python data,
- jaká výjimka může vzniknout při problému se sítí.

Porovnejte své závěry s
[připraveným příkladem](examples/requests_api_call/README.md). Potom příklad
upravte tak, aby vždy používal konečný `timeout` a chybu sítě uživateli
oznámil bez dlouhého výpisu tracebacku.

## 5. Dokumentujeme vlastní rozhraní

Projděte [ukázku docstringů a typových nápověd](examples/docstrings_and_typing/README.md).
U jedné vlastní funkce doplňte:

- typy všech parametrů,
- návratový typ,
- stručný docstring popisující účel,
- význam parametrů a návratové hodnoty,
- výjimku, pokud ji má volající očekávat.

Ověřte výsledek pomocí `help(nazev_funkce)`. Typové nápovědy běh Pythonu
samy nekontrolují; pomáhají čtenáři, IDE a statickým kontrolním nástrojům.

## 6. Závěrečná kontrola projektu

Projekt má obsahovat jen zdrojový kód, dokumentaci a seznam závislostí.
Virtuální prostředí přidejte do `.gitignore`.

Ve dvojici si projekty vyměňte a zkuste odpovědět:

1. Je z README jasné, jak program připravit a spustit?
2. Lze prostředí obnovit bez hádání názvů balíčků?
3. Pomohou docstringy použít funkce bez čtení jejich těla?
4. Je z chybové zprávy jasné, zda selhal program, síť, nebo vstup uživatele?
