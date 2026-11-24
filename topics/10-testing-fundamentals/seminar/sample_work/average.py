"""Průměr čísel: logika oddělená od vstupu a výstupu."""

from pathlib import Path


def average(numbers: list[float]) -> float:
    """Return the arithmetic mean of numbers.

    Raises ValueError if numbers is empty.
    """
    if not numbers:
        raise ValueError("average of an empty list is undefined")
    return sum(numbers) / len(numbers)


def read_numbers(count: int) -> list[float]:
    """Read count numbers from the user, one per line."""
    return [float(input(f"Value #{i}: ")) for i in range(1, count + 1)]


def read_numbers_from_file(path: Path) -> list[float]:
    """Read numbers from a text file, one per line. Blank lines are skipped."""
    numbers = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                numbers.append(float(line))
    return numbers


def main() -> None:
    numbers = read_numbers(5)
    print("Average value:", average(numbers))


if __name__ == "__main__":
    main()
