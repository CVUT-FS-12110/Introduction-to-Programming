# Vytvoření virtuálního prostředí

Tento příklad ukazuje, jak vytvořit a aktivovat virtuální prostředí
pomocí nástroje `venv` a nainstalovat do něj knihovnu třetí strany.

## Postup

```bash
# 1. Vytvoření virtuálního prostředí
python -m venv .venv

# 2. Aktivace (Windows)
.venv\Scripts\activate

# 2. Aktivace (Linux/macOS)
source .venv/bin/activate

# 3. Instalace knihovny
pip install requests

# 4. Ověření instalace
pip list

# 5. Zmrazení závislostí
pip freeze > requirements.txt

# 6. Deaktivace prostředí
deactivate
```

## Obnovení prostředí z requirements.txt

Kdokoli, kdo dostane váš projekt, si může závislosti nainstalovat pomocí `requirements.txt`:

```bash
# 1. Vytvoření virtuálního prostředí (zvolme jiné jméno, aby nedošlo k záměně)
python -m venv .venv2
# 2. Aktivace (Windows)
.venv2\Scripts\activate

# 2. Aktivace (Linux/macOS)
source .venv2/bin/activate

# 3. Instalace závislostí z requirements.txt
pip install -r requirements.txt
```
