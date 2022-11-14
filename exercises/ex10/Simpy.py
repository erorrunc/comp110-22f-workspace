"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730555076"


class Simpy:
    """Implementing a utility class for numerical data."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Initializes values of class Simpy."""
        self.values = values 
    
    def __repr__(self) -> str:
        """Prints results as code."""
        return f"Simpy({self.values})"

    def fill(self, filling_value: float, number_of_values: int) -> None:
        """Fill values with a specific number of repeating values."""
        i: int = 0
        self.values: list[float] = []
        while i < number_of_values:
            self.values.append(filling_value)
            i += 1
        
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill values with range of values as floats."""
        assert step != 0.0
        self.values.append(start)
        i: int = start + step
        if step < 0:
            while i > stop:
                self.values.append(i)
                i += step
        while i > start and i < stop:
            self.values.append(i)
            i += step

    def sum(self) -> float:
        """Compute the sum of all values."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Add each individual value with the same index."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] + rhs.values[i])
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Raise each value of a list to the power of a value with the same index on another list."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] ** rhs.values[i])
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Determines if a value stated is in the given value list."""
        result: list[bool] = []
        if isinstance(rhs, float):
            i: int = 0
            while i < len(self.values):
                if self.values[i] == rhs:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        else:
            for i in range(len(self.values)):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Determines if value is greater than a value in the given value list."""
        result: list[bool] = []
        if isinstance(rhs, float):
            i: int = 0
            while i < len(self.values):
                if self.values[i] > rhs:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        else:
            for i in range(len(self.values)):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Return items at given indices and return masked values."""
        if isinstance(rhs, int):
            result: float = 0.0
            i: int = 0
            while i < len(self.values):
                if rhs == i:
                    result = self.values[i]
                i += 1
        else:
            result: Simpy = Simpy([])
            for i in range(len(rhs)):
                if rhs[i]:
                    result.values.append(self.values[i])
        return result