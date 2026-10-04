# WSL — Linux přímo ve Windows

> Materiál k [tématu 01](../README.md). Nepovinný text pro ty, kdo pracují na Windows a chtějí si vyzkoušet linuxové prostředí (terminál, Git, Python) bez instalace dvou systémů vedle sebe. Základy práce v terminálu najdete v navazujícím textu [Úvod do Bashe](bash.md).

## Co je WSL

**WSL** (*Windows Subsystem for Linux*) umožňuje spouštět linuxovou distribuci (nejčastěji Ubuntu) přímo ve Windows, bez nutnosti instalovat a spravovat klasický virtuální stroj (WSL 2 interně používá odlehčený virtuální stroj, o který se nemusíte starat). Dostanete plnohodnotný linuxový terminál (Bash), balíčkovací systém (`apt`) a nástroje jako `git` nebo `python3`, a to vše vedle běžných Windows aplikací.

Proč se to hodí:

- většina návodů, serverů a vývojářských nástrojů počítá s Linuxem / Bashem,
- většina základních příkazů funguje stejně na Linuxu, macOS i ve WSL,
- Windows soubory i linuxové soubory jsou dostupné z obou světů,
- VS Code se umí k WSL připojit a editovat kód přímo v něm.

> Uživatelé Linuxu a macOS WSL nepotřebují — mají unixový terminál k dispozici nativně (na macOS je výchozí shell zsh, pro základní příkazy z našeho kurzu je rozdíl zanedbatelný).

## Požadavky

- Windows 10 (verze 2004 / build 19041 a novější) nebo Windows 11,
- zapnutá virtualizace v BIOSu / UEFI (u novějších počítačů bývá zapnutá ve výchozím stavu),
- práva administrátora pro instalaci.

## Instalace

1. Otevřete **PowerShell** nebo **Příkazový řádek** jako správce (pravé tlačítko → *Spustit jako správce*).
2. Spusťte:

   ```powershell
   wsl --install
   ```

   Příkaz zapne potřebné funkce Windows a nainstaluje výchozí distribuci (Ubuntu).
3. **Restartujte počítač.**
4. Po restartu (nebo už po dokončení instalace) se obvykle otevře okno distribuce a dokončí instalaci. Pokud se neotevřelo, spusťte *Ubuntu* z nabídky Start. Zadejte **uživatelské jméno** a **heslo** pro Linux (nemusí se shodovat s Windows účtem; při psaní hesla se nic nezobrazuje).

Pokud něco nefunguje:

- `wsl --install` jen vypíše nápovědu (WSL už je nainstalované) → použijte:

  ```powershell
  wsl --install -d Ubuntu
  ```

- instalace se zasekla na 0,0 % → zkuste:

  ```powershell
  wsl --install --web-download -d Ubuntu
  ```

Jinou distribuci vyberete takto:

```powershell
wsl --list --online          # seznam dostupných distribucí
wsl --install -d <NázevDistribuce>
```

Oficiální návod včetně řešení problémů: [Instalace WSL (Microsoft Learn)](https://learn.microsoft.com/cs-cz/windows/wsl/install)

> České verze stránek Microsoftu jsou strojově překládané a občas znějí neohrabaně. V případě nejasností přepněte adresu na anglickou verzi (`en-us` místo `cs-cz`).

## Základní použití

Linux spustíte z nabídky Start (např. *Ubuntu*), z aplikace *Terminál Windows*, nebo příkazem `wsl` v PowerShellu.

Užitečné příkazy ve Windows (PowerShell):

| Příkaz | Význam |
|---|---|
| `wsl` | spustí výchozí distribuci |
| `wsl --list --verbose` | seznam nainstalovaných distribucí a jejich stav |
| `wsl --shutdown` | vypne všechny běžící distribuce |
| `wsl --update` | aktualizuje WSL |

První kroky uvnitř Linuxu:

```bash
sudo apt update && sudo apt upgrade   # aktualizace balíčků (potvrďte klávesou Y)
sudo apt install git python3 python3-venv python3-pip
python3 --version
git --version
```

Ubuntu už `git` a `python3` často obsahuje, příkaz tedy hlavně doplní `venv` a `pip`.

Základní orientaci v terminálu popisuje [Úvod do Bashe](bash.md).

### Práce se soubory

- Windows disky jsou v Linuxu dostupné v `/mnt/`, např. `C:\` je `/mnt/c/`.
- Linuxové soubory jsou ve Windows vidět v Průzkumníku přes adresu `\\wsl.localhost\Ubuntu` (starší zápis `\\wsl$\Ubuntu`; přesný název distribuce zjistíte příkazem `wsl -l -v`, může být např. `Ubuntu-24.04`). Nejjednodušší je napsat v terminálu WSL `explorer.exe .`.
- **Doporučení:** projekty, se kterými ve WSL pracujete, mějte uložené v linuxovém domovském adresáři (`~`), ne v `/mnt/c/...`. Práce se soubory je tam výrazně rychlejší.

### VS Code a WSL

1. Nainstalujte ve Windows [Visual Studio Code](https://code.visualstudio.com/). Při instalaci nechte zaškrtnuté **Přidat do PATH** (*Add to PATH*), jinak nebude fungovat příkaz `code` z WSL.
2. Ve VS Code nainstalujte rozšíření **WSL**.
3. V terminálu WSL přejděte do složky projektu a spusťte:

   ```bash
   code .
   ```

VS Code se připojí k WSL a editor poběží ve Windows, zatímco kód, terminál a interpret Pythonu poběží v Linuxu.

Rozšíření, která pracují s kódem (např. **Python**), je potřeba nainstalovat také *uvnitř WSL* — VS Code to nabízí tlačítkem **Install in WSL**.

Návod: [Začněte používat VS Code s WSL](https://learn.microsoft.com/cs-cz/windows/wsl/tutorials/wsl-vscode)

## Další zdroje

- [Dokumentace WSL (Microsoft Learn)](https://learn.microsoft.com/cs-cz/windows/wsl/)
- [Základní příkazy WSL](https://learn.microsoft.com/cs-cz/windows/wsl/basic-commands)
- [Práce napříč systémy souborů](https://learn.microsoft.com/cs-cz/windows/wsl/filesystems)
- [Začínáme používat Git ve WSL](https://learn.microsoft.com/cs-cz/windows/wsl/tutorials/wsl-git)
