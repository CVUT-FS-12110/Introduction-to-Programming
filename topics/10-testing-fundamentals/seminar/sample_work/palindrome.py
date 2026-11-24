"""Kontrola palindromu — opravená verze (viz regresní test)."""


def is_palindrome(text: str) -> bool:
    """Return True if text reads the same forwards and backwards.

    The comparison ignores spaces and letter case.
    """
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
