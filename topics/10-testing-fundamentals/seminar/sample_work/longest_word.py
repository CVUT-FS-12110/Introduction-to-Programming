"""Nejdelší slovo ve větě — verze, která odpovídá zadání."""

import string


def find_longest_word(sentence: str) -> str:
    """Return the longest word in sentence.

    Punctuation is ignored. If several words share the greatest length,
    the first one is returned. Raises ValueError if sentence has no words.
    """
    words = [word.strip(string.punctuation) for word in sentence.split()]
    words = [word for word in words if word]
    if not words:
        raise ValueError("sentence contains no words")
    return max(words, key=len)
