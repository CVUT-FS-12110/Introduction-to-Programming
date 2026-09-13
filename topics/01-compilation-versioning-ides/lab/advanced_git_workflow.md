# Cvičení: pokročilé Git workflow

## Cíl

Cílem je projít souvislý pracovní postup podobný vývoji menšího projektu v
týmu. Procvičíte práci s větvemi a vzdáleným repozitářem, slučování změn,
řešení konfliktů i bezpečné úpravy již vytvořené historie.

Zadání je záměrně rozsáhlé. Není navrženo tak, aby je bylo možné celé vyřešit
za 90 minut samostudia. Na cvičení postupujte po jednotlivých kontrolních
bodech, průběžně konzultujte svůj postup a dokončete alespoň části označené
jako základní.

## 1. Fork a příprava repozitáře — základní

Začněte vytvořením vlastní kopie výchozího repozitáře:

1. Na GitHubu otevřete repozitář určený vyučujícím a zvolte **Fork**.
2. Jako vlastníka vyberte svůj účet. Název repozitáře neměňte.
3. Vytvořený fork naklonujte do počítače. Vzdálený repozitář `origin` musí
   směřovat na váš fork, ne na repozitář vyučujícího.
4. Původní repozitář vyučujícího přidejte jako druhý vzdálený repozitář s
   názvem `upstream`.
5. Pomocí `git remote -v` ověřte adresy `origin` a `upstream`.
6. Přepněte se na větev `master` a načtěte aktuální změny z `upstream`.
7. Aktualizujte lokální `master` podle `upstream/master` a odešlete jej do
   `origin/master` ve svém forku.
8. Ověřte příkazem `git status`, že nemáte neuložené změny.
9. Vytvořte soubor `app.py` s jednoduchým programem, který vypíše pozdrav.
10. Vytvořte soubor `CHANGELOG.md` s nadpisem `# Changelog`.
11. Oba soubory uložte v samostatných commitech a odešlete do svého forku.

**Kontrolní bod A:** `origin` ukazuje na váš fork, `upstream` na původní
repozitář a větev `master` ve vašem forku obsahuje dva nové commity.

## Pravidla další práce

- před každým commitem zkontrolujte `git status` a `git diff`,
- každý commit má obsahovat jednu logickou změnu,
- používejte stručné a výstižné zprávy commitů,
- do `master` nepřidávejte rozpracované změny přímo, pokud to zadání výslovně
  nepožaduje,
- po dokončení každé části odešlete příslušnou větev do svého forku,
- pull requesty v tomto cvičení vytvářejte do větve `master` ve svém forku,
  nikoli do původního repozitáře vyučujícího.

## 2. Funkce ve feature větvi — základní

1. Z `master` vytvořte větev `feature/user-name`.
2. Upravte `app.py`, aby se program zeptal na jméno a uživatele pozdravil.
3. Rozdělte změnu do nejméně dvou commitů:
   - načtení vstupu,
   - sestavení a vypsání pozdravu.
4. Do `README.md` přidejte krátký návod ke spuštění programu a vytvořte další
   commit.
5. Zobrazte historii příkazem `git log --oneline --graph --all` a ověřte, že
   větev obsahuje tři nové commity.
6. Odešlete větev do svého forku a vytvořte pull request do `master` ve svém
   forku.
7. Zkontrolujte změny v pull requestu, opravte případné nedostatky novým
   commitem a pull request slučte.
8. Aktualizujte lokální `master` a odstraňte dokončenou větev lokálně i ve
   svém forku.

**Kontrolní bod B:** Program pracuje se jménem uživatele, změna je v `master` a
historie obsahuje několik smysluplně oddělených commitů.

## 3. Dvě souběžné větve a konflikt — základní

1. Z aktuálního `master` vytvořte větev `feature/greeting-style`.
2. Změňte text pozdravu, přidejte změnu do `CHANGELOG.md` a každou úpravu
   commitněte zvlášť.
3. Přepněte se zpět na `master` a vytvořte větev `feature/formal-greeting`.
4. Na stejném řádku v `app.py` vytvořte jinou variantu pozdravu.
5. Také tuto změnu zaznamenejte v `CHANGELOG.md` a vytvořte dva commity.
6. Větev `feature/formal-greeting` slučte přes pull request do `master`.
7. Aktualizujte lokální `master`.
8. Ve větvi `feature/greeting-style` slučte aktuální `master`. Vyřešte konflikt
   v `app.py` tak, aby si uživatel mohl vybrat neformální nebo formální
   pozdrav.
9. Ověřte spuštěním obě varianty a dokončete merge commit.
10. Odešlete větev, otevřete pull request a před sloučením zkontrolujte celý
    diff proti `master`.

**Kontrolní bod C:** Obě původní varianty jsou dostupné v jednom programu a v
historii je dohledatelné vyřešení konfliktu.

## 4. Odložení rozpracované změny pomocí stash — základní

1. Vytvořte větev `feature/input-validation`.
2. Začněte přidávat kontrolu, že uživatel zadal neprázdné jméno, ale změnu
   zatím necommitujte.
3. Simulujte naléhavou opravu: rozpracované změny včetně případných nových
   souborů odložte pomocí `git stash`.
4. Přepněte se na `master`, vytvořte větev `hotfix/typo` a opravte překlep v
   dokumentaci.
5. Opravu commitněte, odešlete, slučte přes pull request a aktualizujte
   `master`.
6. Vraťte se do `feature/input-validation`, začleňte aktuální `master` a obnovte
   odložené změny.
7. Dokončete validaci, otestujte prázdný i neprázdný vstup a vytvořte commit.
8. Zkontrolujte seznam stashů a ukliďte již nepotřebný záznam, pokud po
   obnovení zůstal zachován.

**Kontrolní bod D:** Hotfix je v `master` a rozpracovaná validace se při změně
větve neztratila.

## 5. Rebase a úklid historie — rozšiřující

1. Ve větvi `feature/input-validation` vytvořte ještě nejméně tři malé
   commity: chybovou zprávu, opakované načtení vstupu a doplnění dokumentace.
2. Mezitím v `master` upravte `CHANGELOG.md` samostatným commitem a vraťte se do
   pracovní větve.
3. Pomocí rebase přeneste pracovní větev na aktuální `master`.
4. Vyřešte případné konflikty a po každém kroku spusťte program.
5. Interaktivním rebase spojte drobné opravné commity tak, aby historie
   obsahovala několik logických kroků místo řady oprav typu „fix“.
6. Porovnejte historii před a po úpravě pomocí reflogu.
7. Protože se změnily identifikátory commitů, odešlete již publikovanou větev
   bezpečnou variantou force push, která nejprve ověřuje stav vzdálené větve.
8. Vytvořte pull request, zkontrolujte výsledný diff a větev slučte.

**Kontrolní bod E:** Větev vychází z aktuálního `master` a má přehlednou,
lineární historii bez zbytečných opravných commitů.

## 6. Cherry-pick a návrat chybné změny — rozšiřující

1. Z `master` vytvořte větev `experiment/uppercase` a přidejte volitelné vypsání
   pozdravu velkými písmeny.
2. Vytvořte zvlášť commit s implementací a zvlášť commit s dokumentací.
3. Do `master` přeneste pouze dokumentační commit pomocí `cherry-pick`. Vysvětlete,
   proč program zatím popisovanou funkci neobsahuje.
4. Přeneste také implementační commit a program otestujte.
5. Vytvořte další commit, který úmyslně způsobí chybu při spuštění programu, a
   odešlete jej na server.
6. Chybný commit neodstraňujte z publikované historie. Vytvořte nový commit,
   který jeho změny vrátí pomocí `git revert`.
7. Pomocí `git log`, `git show` a `git diff` doložte rozdíl mezi cherry-pickem,
   revertem a běžným sloučením větve.

**Kontrolní bod F:** Historie zachovává chybný commit i commit, který jej
bezpečně vrací, a aktuální program znovu funguje.

## 7. Vydání verze — závěrečná

1. Doplňte do `CHANGELOG.md` souhrn všech funkcí, které se skutečně dostaly do
   `master`.
2. Ověřte čistý pracovní adresář a spusťte finální verzi programu pro několik
   různých vstupů.
3. Vytvořte anotovaný tag `v0.2.0` se zprávou popisující vydání.
4. Odešlete tag na vzdálený repozitář a vytvořte z něj GitHub release.
5. Nakreslete graf výsledné historie nebo přiložte výstup příkazu
   `git log --oneline --graph --decorate --all`.
