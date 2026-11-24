"""Testy pro longest_word.py — zpevněná sada."""

import pytest

from longest_word import find_longest_word


# Původní slabá sada: oba testy projdou i implementaci `sentence.split()[-1]`.
def test_longest_word_at_the_end():
    assert find_longest_word("ahoj světe") == "světe"


def test_longest_word_is_last_of_three():
    assert find_longest_word("a bb ccc") == "ccc"


# Testy doplněné při společném průchodu: každý zavírá jednu díru.
def test_longest_word_in_the_middle():
    assert find_longest_word("a nejdelší b") == "nejdelší"


def test_first_of_equally_long_words_wins():
    assert find_longest_word("kos pes") == "kos"


def test_punctuation_is_ignored():
    assert find_longest_word("Ahoj, světe!") == "světe"


def test_empty_sentence_raises_value_error():
    with pytest.raises(ValueError):
        find_longest_word("")
