"""Testing for the Dictionary File."""


__author__: str = "730555076"


from dictionary import invert, favorite_color, count


import pytest


def test_invert_empty_dictionary() -> None:
    """Tests if an empty dictionary inverted results in an empty dictionary."""
    dictionary: dict[str, str] = {}
    assert invert(dictionary) == {}


def test_invert() -> None:
    """Tests if a dictionary returns the key and values inverted."""
    dictionary: dict[str, str] = {'apple': 'cat'}
    assert invert(dictionary) == {'cat': 'apple'}


def test_invert_key_erorr() -> None:
    """Tests if multiple of the same values results in a Key Error message."""
    with pytest.raises(KeyError):
        dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(dictionary)


def test_favorite_color_empty_dictionary() -> None:
    """Tests if an empty dictionary returns an empty string."""
    colors: dict[str, str] = {}
    assert favorite_color(colors) == ""


def test_favorite_color() -> None:
    """Tests if a dictionary returns the most frequent value with 2 frequent values."""
    colors: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(colors) == "blue"


def test_favorite_color_multiple() -> None:
    """Tests if a dictionary returns the most frequent value with 3 frequent values."""
    colors: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Emily": "blue", "Jenn": "yellow"}
    assert favorite_color(colors) == "blue"


def test_favorite_color_tie() -> None:
    """Tests if a tie in biggest value leads to returning the first color."""
    colors: dict[str, str] = {"Marc": "yellow", "Ezri": "blue"}
    assert favorite_color(colors) == "yellow"


def test_count_empty_dictionary() -> None:
    """Tests if an empty list returns an empty dictionary."""
    list_of_values: list[str] = ()
    assert count(list_of_values) == {}


def test_count() -> None:
    """Tests counting the frequency of items in a list."""
    list_of_values: list[str] = ("Mark", "Emily", "Jenn")
    assert count(list_of_values) == {"Mark": 1, "Emily": 1, "Jenn": 1}


def test_count_multiple() -> None:
    """Tests counting the frequency of items in a list with multipe of the same items."""
    list_of_values: list[str] = ("Mark", "Mark", "Emily", "Jenn", "Emily")
    assert count(list_of_values) == {"Mark": 2, "Emily": 2, "Jenn": 1}