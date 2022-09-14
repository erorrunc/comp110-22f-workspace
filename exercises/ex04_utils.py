"""Creating and playing with lists of integers."""

__author__ = "730555076"


# determining if a value is contained in a list
def all(list_of_integers: list[int], given_int: int) -> bool:
    """Determining if a character is given in a list of integers."""
    i: int = 0
    if len(list_of_integers) == 0:
        return False
    while i < len(list_of_integers):
        if list_of_integers[i] != given_int:
            return False
        i = i + 1
    else:
        return True


# determining the maximum value in a list
def max(input: list[int]) -> int:
    """Finding the maximum value in a list of integers."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0 
    a: int = -100
    while i < len(input):
        if input[i] > a:
            a = input[i]
        i = i + 1
    return a


# determining if two lists are identical 
def is_equal(c: list[int], d: list[int]) -> bool:
    """Determining if two lists of integers are deeply equal."""
    i: int = 0
    a: bool = True
    while i < len(c) and i < len(d):
        if c[i] == d[i]:
            a = True
        else:
            a = False
        i = i + 1
    if len(c) != len(d):
        a = False
    return a