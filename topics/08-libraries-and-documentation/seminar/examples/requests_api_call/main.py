import requests


def main() -> None:
    """Call a public API and print a small part of its response."""
    try:
        response = requests.get("https://httpbin.org/get", timeout=10)
        response.raise_for_status()
    except requests.RequestException as error:
        print("Request failed:", error)
        return

    data = response.json()
    print("Status code:", response.status_code)
    print("Requested URL:", data["url"])


if __name__ == "__main__":
    main()
