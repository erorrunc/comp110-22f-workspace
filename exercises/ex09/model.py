"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730555076" 


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> int:
        """Determines the distance between two points."""
        return sqrt(((other.x - self.x) ** 2) + ((other.y - self.y) ** 2))


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Reassign the object's location attribute."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()

    def color(self) -> str:
        """Produces the color of infected or vulnerable cells."""
        if self.is_vulnerable():
            return "gray"
        if self.is_infected():
            return "pink"
        if self.is_immune():
            return "green"
        return "hello"    

    def contract_disease(self) -> None:
        """Determines if a cell contracts a disease."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Determines if a cell is vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return True
        else: 
            return False

    def is_infected(self) -> bool:
        """Determines if a cell is infected."""
        if self.sickness >= constants.INFECTED:
            return True
        else: 
            return False

    def contact_with(self, other: Cell) -> None:
        """Determines if vulnerable cells contract the disease."""
        if self.is_infected() and other.is_vulnerable():
            other.contract_disease()
        if other.is_infected() and self.is_vulnerable():
            self.contract_disease()

    def immunize(self) -> None:
        """Assigns immune constant to sickness attribute of cell."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Determines if cell's sickness attribute is equal to Immune Constant."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, initially_sick: int, initially_immune: int = 0):
        """Initialize the cells with random locations and directions."""
        if initially_sick >= cells or initially_sick <= 0:
            raise ValueError("Error. Cells initially sick must fall within proper bounds.")
        if initially_immune >= cells or initially_immune < 0:
            raise ValueError("Error. Cells initially immune must fall within proper bounds.")
        self.population = []
        for i in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
            if i in range(initially_sick):
                self.population[i].contract_disease()
            if i in range(initially_sick, initially_sick + initially_immune):
                self.population[i].immunize()

    def check_contacts(self) -> None:
        """Compare the distance between every cell's location and position."""
        for i in range(len(self.population)):
            for j in range(i + 1, len(self.population)):
                cell1: Cell = self.population[i]
                cell2: Cell = self.population[j]
                if cell1.location.distance(cell2.location) < constants.CELL_RADIUS:
                    cell1.contact_with(cell2)

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cell in self.population:
            if cell.is_infected():
                return False
        return True