from .generator.maze_generator import MazeGenerator
from .maze.grid import Grid


def main():
    grid = Grid(20, 20)

    grid.print_cells()


if __name__ == "__main__":
    main()
