from typing import Optional


def filter_and_format_names(names: list[str], max_length: Optional[int] = None) -> list[str]:
    """
    Filters names by maximum length and converts them to uppercase.

    This documentation format is called a docstring. If a function accepts
    complex arguments or has special behavior, it should be described here.

    Args:
        names: A list of names (strings) to process.
        max_length: The maximum allowed length of a name. If None,
                    no limit is applied. The length must not be negative.

    Returns:
        A new list containing the formatted (uppercase) names.

    Raises:
        ValueError: If max_length is less than 0.
    """
    if max_length is not None and max_length < 0:
        raise ValueError("max_length cannot be a negative number.")

    result = []
    for name in names:
        if max_length is None or len(name) <= max_length:
            result.append(name.upper())

    return result


if __name__ == "__main__":
    # Usage example:
    people = ["John", "Magdalena", "Alexander", "Eve"]

    filtered = filter_and_format_names(people, max_length=5)
    print("Filtered names:", filtered)

    print("-" * 40)
    print("Example of what a user (or IDE) sees when calling help():\n")

    # The help() function in the terminal prints the function's docstring!
    help(filter_and_format_names)
