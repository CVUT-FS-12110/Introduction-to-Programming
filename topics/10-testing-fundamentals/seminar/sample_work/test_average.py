"""Testy pro average.py — stav po společném průchodu."""

import pytest

from average import average, read_numbers_from_file


# --- Běžné případy (Arrange–Act–Assert) ---


def test_average_of_five_numbers():
    numbers = [2, 4, 6, 8, 10]  # Arrange
    result = average(numbers)  # Act
    assert result == 6  # Assert


# --- Hraniční případy ---


def test_average_of_single_number_is_that_number():
    assert average([7]) == 7


def test_average_of_negative_numbers():
    assert average([-2, -4]) == -3


def test_average_of_floats_uses_tolerance():
    assert average([0.1, 0.2, 0.4]) == pytest.approx(0.7 / 3)


# --- Chybové případy ---


def test_average_of_empty_list_raises_value_error():
    with pytest.raises(ValueError, match="empty"):
        average([])


# --- Totéž přehledněji: tabulka případů ---


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([2, 4, 6, 8, 10], 6),  # běžný případ
        ([7], 7),  # jeden prvek
        ([-2, -4], -3),  # záporná čísla
        ([0, 0, 0], 0),  # samé nuly
        ([1, 2], 1.5),  # neceločíselný výsledek
    ],
)
def test_average_cases(numbers, expected):
    assert average(numbers) == expected


# --- Soubor jako vstup: dočasná složka tmp_path ---


def test_read_numbers_from_file(tmp_path):
    data_file = tmp_path / "numbers.txt"
    data_file.write_text("1\n2\n\n3\n", encoding="utf-8")

    assert read_numbers_from_file(data_file) == [1, 2, 3]


def test_read_numbers_from_empty_file_returns_empty_list(tmp_path):
    data_file = tmp_path / "empty.txt"
    data_file.write_text("", encoding="utf-8")

    assert read_numbers_from_file(data_file) == []
