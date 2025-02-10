from dataclasses import dataclass, field
from .cell import Cell
import pygame


@dataclass
class Grid:
    width: int = 10
    height: int = 10
    cells: list[list] = field(default_factory=list, init=False)

    def __post_init__(self):
        self.cells = [
            [Cell(x, y) for x in range(self.width)] for y in range(self.height)
        ]

    def set_cells(self, cells: list[list]):
        self.cells = cells

    def print_cells(self):
        for row in self.cells:
            for col in row:
                print("0", end="")
            print()

    def draw(self, screen: pygame.display, cell_size: int):
        for y in range(0, len(self.cells)):
            for x in range(0, len(self.cells[y])):
                walls = self.cells[y][x].walls
                for wall in walls:
                    match wall:
                        case "n":
                            pygame.draw.line(
                                screen,
                                (0, 0, 0),
                                (cell_size * x, cell_size * y),
                                (cell_size * x + cell_size, cell_size * y),
                                1,
                            )

                        case "e":
                            pygame.draw.line(
                                screen,
                                (0, 0, 0),
                                (cell_size * x + cell_size, cell_size * y),
                                (cell_size * x + cell_size,
                                 cell_size * y + cell_size),
                                1,
                            )

                        case "s":
                            pygame.draw.line(
                                screen,
                                (0, 0, 0),
                                (cell_size * x, cell_size * y + cell_size),
                                (cell_size * x + cell_size,
                                 cell_size * y + cell_size),
                                1,
                            )

                        case "w":
                            pygame.draw.line(
                                screen,
                                (0, 0, 0),
                                (cell_size * x, cell_size * y),
                                (cell_size * x, cell_size * y + cell_size),
                                1,
                            )
