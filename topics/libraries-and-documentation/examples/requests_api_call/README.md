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

# Call a simple public API
response = requests.get("https://httpbin.org/get")

print("Status code:", response.status_code)
print("JSON Response:", response.json())
```

## Očekávaný výstup
```text
Status code: 200
JSON Response: {
    'args': {}, 
    'headers': {
        'Accept': '*/*', 
        'Accept-Encoding': 'gzip, 
        deflate', 'Host': 'httpbin.org', 
        'User-Agent': 'python-requests/2.33.1', 
        'X-Amzn-Trace-Id': 'Root=1-69d37f32-582dd6e90ebb694a47b2b613'
    }, 
    'origin': 'X.X.X.X', 
    'url': 'https://httpbin.org/get'
}
```
