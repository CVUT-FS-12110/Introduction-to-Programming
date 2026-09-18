# Volání API pomocí knihovny requests

Tento příklad ukazuje, jak nainstalovat a použít knihovnu třetí strany.
Pomocí knihovny `requests` zavoláme jednoduché veřejné API a zpracujeme odpověď.

## Prerekvizity

Aktivované virtuální prostředí s nainstalovanou knihovnou `requests`:

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/macOS
pip install requests
```

## Ukázkový kód

```python
import requests

try:
    response = requests.get("https://httpbin.org/get", timeout=10)
    response.raise_for_status()
except requests.RequestException as error:
    print("Request failed:", error)
else:
    print("Status code:", response.status_code)
    print("Requested URL:", response.json()["url"])
```

## Očekávaný výstup
```text
Status code: 200
Requested URL: https://httpbin.org/get
```

Časový limit brání tomu, aby program při nedostupné síti čekal neomezeně.
`raise_for_status()` převede neúspěšný HTTP stav na výjimku, kterou lze
společně s ostatními síťovými problémy srozumitelně ošetřit.
