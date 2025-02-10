from abc import ABC, abstractmethod
from src.maze.grid import Grid
from src.maze.cell import Cell


class MazeGenerator(ABC):
    """Class for representing maze generator"""

    @abstractmethod
    def generate_maze(self, width: int, height: int, draw: bool) -> Grid:
        pass

    def create_connection(self, cell1: Cell, cell2: Cell, choice: str):
        match choice:
            case "n":
                cell1.remove_wall("n")
                cell2.remove_wall("s")

            case "e":
                cell1.remove_wall("e")
                cell2.remove_wall("w")

            case "s":
                cell1.remove_wall("s")
                cell2.remove_wall("n")

            case "w":
                cell1.remove_wall("w")
                cell2.remove_wall("e")
