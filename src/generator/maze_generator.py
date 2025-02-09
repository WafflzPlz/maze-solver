from src.maze.grid import Grid


class MazeGenerator:
    """Class for representing maze generator"""

    def generate_maze(self, width: int, height: int) -> Grid:
        grid = Grid(width, height)
        return grid
