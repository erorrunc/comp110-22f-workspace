"""EX07 - Inverts a dictionary, determines most frequent colors in a dictionary, and counts values in a list."""


__author__: str = "730555076"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts the key and values of a given dictionary."""
    inverted_dictionary: dict[str, str] = {}
    for key in dictionary:
        if dictionary[key] in inverted_dictionary:
            raise KeyError("Error. Values cannot be the same.")
        else:
            inverted_dictionary[dictionary[key]] = key
    return inverted_dictionary


def favorite_color(colors: dict[str, str]) -> str:
    """Determines the color that appears most frequently in a given dictionary."""
    frequency_count: dict[str, int] = {}
    if colors == {}:
        return ""
    for key in colors:
        if colors[key] in frequency_count:
            frequency_count[colors[key]] += 1
        else:
            frequency_count[colors[key]] = 1
    biggest_value: int = 0
    for key in frequency_count:
        if frequency_count[key] > biggest_value:
            biggest_value = frequency_count[key]
            most_frequent_color: str = key
    return most_frequent_color


def count(list_of_values: list[str]) -> dict[str, int]:
    """Counts the number of times a value appears in a list."""
    frequency_count: dict[str, int] = {}
    i: int = 0
    while i < len(list_of_values):
        if list_of_values[i] in frequency_count:
            frequency_count[list_of_values[i]] += 1
        else:
            frequency_count[list_of_values[i]] = 1
        i += 1
    return frequency_count
