"""Testy pro palindrome.py včetně regresního testu."""

import pytest

from palindrome import is_palindrome


@pytest.mark.parametrize(
    "text, expected",
    [
        ("racecar", True),
        ("hello", False),
        ("a", True),  # jeden znak
        ("", True),  # prázdný řetězec: čte se stejně z obou stran
        ("nurses run", True),  # mezery se ignorují
    ],
)
def test_is_palindrome_cases(text, expected):
    assert is_palindrome(text) is expected


def test_is_palindrome_ignores_letter_case():
    """Regresní test: původní verze velká písmena nezohlednila."""
    assert is_palindrome("Racecar") is True
    assert is_palindrome("A man a plan a canal Panama") is True
