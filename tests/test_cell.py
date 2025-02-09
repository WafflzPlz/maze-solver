import unittest
from src.maze.cell import Cell


class TestCell(unittest.TestCase):

    def test_set_walls_Successful(self):
        cell = Cell(1, 1)
        self.assertEqual(cell.walls, {"n", "e", "s", "w"})
        cell.set_walls({"n"})
        self.assertEqual(cell.walls, {"n"})

    def test_remove_wall_Successful(self):
        cell = Cell(1, 1)
        self.assertEqual(cell.walls, {"n", "e", "s", "w"})
        cell.remove_wall("n", "s")
        self.assertEqual(cell.walls, {"e", "w"})

    def test_add_wall_Successful(self):
        cell = Cell(1, 1, {"n", "s"})
        self.assertEqual(cell.walls, {"n", "s"})
        cell.add_wall("e", "s", "w")
        self.assertEqual(cell.walls, {"n", "e", "s", "w"})


if __name__ == "__main__":
    unittest.main()
