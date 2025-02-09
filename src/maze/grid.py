from dataclasses import dataclass, field
from .cell import Cell


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
