"""Testing Utils."""


from utils import only_evens, sub, concat


__author__ = "730555076"


def test_empty_list() -> None:
    """Tests if an empty string given results in an empty string."""
    list_given: list[int] = []
    assert list_given == []


def test_even_first_index() -> None:
    """Tests if the first index of a list is even."""
    list_given: list[int] = [2, 3, 4]
    assert list_given[0] % 2 == 0
    

def test_only_evens() -> None:
    """Tests if only evens are pulled out from a given list."""
    list_given: list[int] = [1, 4, 6]
    assert only_evens(list_given) == [4, 6]


def test_only_evens_with_odds() -> None:
    """Tests if blank list returns when only odds are given."""
    list_given: list[int] = [1, 3, 5]
    assert only_evens(list_given) == []


def test_empty_concat() -> None:
    """Tests if two empty lists added results in an empty list."""
    list_1: list[int] = []
    list_2: list[int] = []
    assert concat(list_1, list_2) == []


def test_one_empty_concat() -> None:
    """Tests if one list is empty, only return the other list."""
    list_1: list[int] = []
    list_2: list[int] = [1, 2, 3]
    assert concat(list_1, list_2) == [1, 2, 3]


def test_concat() -> None:
    """Tests if two lists are concatenated to one list without changes."""
    list_1: list[int] = [1, 2, 3]
    list_2: list[int] = [4, 5, 6]
    assert concat(list_1, list_2) == [1, 2, 3, 4, 5, 6]


def test_concat_unequal_length() -> None:
    """Tests if two lists are concatenated to another list when they are unequal in length."""
    list_1: list[int] = [3, 1]
    list_2: list[int] = [9, 4, 2]
    assert concat(list_1, list_2) == [3, 1, 9, 4, 2]


def test_empty_sub() -> None:
    """Tests if an empty list is returned when an empty list is given."""
    a_list: list[int] = []
    start: int = 1
    end: int = 3
    assert sub(a_list, start, end) == []


def test_sub() -> None:
    """Tests if the correct subset of the list is given."""
    a_list: list[int] = [10, 20, 30, 40]
    start: int = 1
    end: int = 3
    assert sub(a_list, start, end) == [20, 30]


def test_negative_start() -> None:
    """Tests if a negative start value begins with the first index of the list."""
    a_list: list[int] = [10, 20, 30, 40]
    start: int = -1
    end: int = 3
    assert sub(a_list, start, end) == [10, 20, 30]


def test_greater_end() -> None:
    """Tests if an end value greater than the length of the list ends."""
    a_list: list[int] = [10, 20, 30]
    start: int = 1
    end: int = 5
    assert sub(a_list, start, end) == [20, 30]