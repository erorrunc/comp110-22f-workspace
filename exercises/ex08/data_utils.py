"""Dictionary related utility functions."""

__author__ = "730555076"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Convert data into list of rows with each row as a dictionary."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(column_table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produce a column-based table with only a certain number of rows."""
    result: dict[str, list[str]] = {}
    if N >= len(column_table):
        return column_table
    for key in column_table:
        N_values: list[str] = []
        i: int = 0
        while i < N:
            N_values.append(column_table[key][i])
            i += 1
        result[key] = N_values
    return result


def select(column_table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Produce a column-based table that shows only specific columns."""
    result: dict[str, list[str]] = {}
    for key in columns:
        result[key] = column_table[key]
    return result


def concat(column_table_1: dict[str, list[str]], column_table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a column-based table that combines two column-based tables."""
    result: dict[str, list[str]] = {}
    for key in column_table_1:
        result[key] = column_table_1[key]
    for key in column_table_2:
        if key in result:
            result[key] += column_table_2[key]
        else:
            result[key] = column_table_2[key]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Counts the frequency of values."""
    frequency: dict[str, int] = {}
    i: int = 0
    while i < len(values):
        if values[i] in frequency:
            frequency[values[i]] += 1
        else:
            frequency[values[i]] = 1
        i += 1
    return frequency