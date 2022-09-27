"""List Utility Functions: listing only evens, combining two lists, and generating a subset list."""


__author__ = "730555076"


def only_evens(list_given: list[int]) -> list[int]:
    """Returns elements of a list that are only even values."""
    i: int = 0
    evens: list[int] = list()
    while i < len(list_given):
        if list_given[i] % 2 == 0:
            evens.append(list_given[i])
        i += 1
    return evens


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Combine two lists into a new list."""
    i: int = 0
    idx: int = 0
    concat_list: list[int] = list()
    while i < len(list_1):
        concat_list.append(list_1[i])
        i += 1
    while idx < len(list_2):
        concat_list.append(list_2[idx])
        idx += 1
    return concat_list
    

def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """Generate a list between the given start index and given ending index."""
    sub_list: list[int] = list()
    if len(a_list) == 0 or start > len(a_list) or end <= 0 or start == len(a_list):
        return []

    if start < 0:
        sub_list.append(a_list[0])
        start: int = 0
        i: int = 1
    else:
        sub_list.append(a_list[start])
        i: int = start + 1
        
    if end > len(a_list):
        end = len(a_list)
    
    while i > start and i < end:
        sub_list.append(a_list[i])
        i += 1

    return sub_list
