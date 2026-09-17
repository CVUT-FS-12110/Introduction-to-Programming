# Konflikt závislostí

Tento příklad ukazuje, proč je globální instalace balíčků problematická.
Dva projekty mohou vyžadovat různé verze stejné knihovny — bez izolace
dojde ke konfliktu.

## Scénář

Představte si dva projekty:
- **Projekt A** vyžaduje `urllib3==1.26`
- **Projekt B** vyžaduje `urllib3==2.0`

Při globální instalaci nelze mít obě verze zároveň. Instalace jedné verze
přepíše druhou a jeden z projektů přestane fungovat.

## Ukázka

Spusťte následující příkazy v terminálu a sledujte, co se stane:

```bash
# Instalace starší verze
pip install urllib3==1.26

# Zobrazení nainstalované verze
pip show urllib3

# Instalace novější verze — přepíše předchozí!
pip install urllib3==2.6.3 

# Starší verze je pryč
pip show urllib3
```

Projekt, který potřeboval `urllib3==1.26`, nyní nebude fungovat, protožemá k dispozici pouze `urllib3==2.6.3`.

Než budeme pokračovat, odinstalujte `urllib3` globálně, abychom měli čisté prostředí pro další cvičení:

```bash
pip uninstall urllib3
```

## Řešení: virtuální prostředí

Konfliktu závislostí se vyhneme izolací projektů do **virtuálních prostředí**. Každé prostředí může mít své vlastní balíčky a verze, aniž by ovlivňovalo ostatní projekty.

---
