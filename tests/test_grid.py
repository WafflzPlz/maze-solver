import unittest
from src.maze.grid import Grid


class TestGrid(unittest.TestCase):

    def test_grid_creation_default_successful(self):
        grid = Grid()
        self.assertEqual(grid.height, 10)
        self.assertEqual(grid.width, 10)
        self.assertEqual(len(grid.cells), 10)
        self.assertEqual(len(grid.cells[0]), 10)

    def test_grid_creation_different_size_successful(self):
        grid = Grid(15, 20)
        self.assertEqual(grid.height, 20)
        self.assertEqual(grid.width, 15)
        self.assertEqual(len(grid.cells), 20)
        self.assertEqual(len(grid.cells[0]), 15)


if __name__ == "__main__":
    unittest.main()
