"""Dictionary related utility functions."""

__author__ = "730567965"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Reading rows and columns."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Changes row table to column."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Returning row of a column."""
    if rows > len(table):
        return table
    result: dict[str, list[str]] = {}
    for key in table:
        x: list[str] = []
        i: int = 0
        while i < rows:
            x.append(table[key][i])
            i += 1
        result[key] = x
    return result


def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Returning the selected column."""
    result: dict[str, list[str]] = {}
    for column in columns:
        result[column] = table[column]
    return result


def concat(table_0: dict[str, list[str]], table_1: dict[str, list[str]]) -> dict[str, list[str]]:
    """Both tables are concated."""
    result: dict[str, list[str]] = {}
    for key in table_0:
        result[key] = table_0[key]
    for key in table_1:
        if key in result:
            result[key] += table_1[key]
        else:
            result[key] = table_1[key]
    return result


def count(list_0: list[str]) -> dict[str, int]:
    """Count total times a character appears."""
    if len(list_0) == 0:
        raise ("Passed")
    elif len(list_0) == 1:
        return {list_0[0]: 1}
    else:
        result: dict[str, int] = {}
        for string in list_0:
            if string in result:
                result[string] += 1
            else:
                result[string] = 1
        return result
