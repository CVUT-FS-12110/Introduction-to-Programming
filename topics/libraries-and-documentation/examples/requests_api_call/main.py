import requests

# Call a simple public API
response = requests.get("https://httpbin.org/get")

print("Status code:", response.status_code)
print("JSON Response:", response.json())
