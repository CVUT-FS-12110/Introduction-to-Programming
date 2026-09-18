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

## Bezpečná ukázka ve dvou prostředích

Nevyměňujte kvůli demonstraci globálně nainstalované balíčky. Vytvořte dva
samostatné adresáře a v každém vlastní prostředí:

```bash
# Projekt A
python -m venv project-a/.venv
project-a\.venv\Scripts\python -m pip install urllib3==1.26.20
project-a\.venv\Scripts\python -m pip show urllib3

# Projekt B
python -m venv project-b/.venv
project-b\.venv\Scripts\python -m pip install urllib3==2.6.3
project-b\.venv\Scripts\python -m pip show urllib3
```

Na Linuxu a macOS nahraďte cestu `Scripts\python` cestou `bin/python`.
Obě verze nyní existují současně, ale každá patří jinému projektu.

## Řešení: virtuální prostředí

Konfliktu závislostí se vyhneme izolací projektů do **virtuálních prostředí**.
Každé prostředí může mít své vlastní balíčky a verze, aniž by ovlivňovalo
ostatní projekty nebo systémový Python.

---
