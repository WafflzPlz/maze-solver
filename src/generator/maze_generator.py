import random
from src.maze.grid import Grid
from src.maze.cell import Cell


class MazeGenerator:
    """Class for representing maze generator"""

    def generate_maze(self, width: int, height: int) -> Grid:
        grid = Grid(width, height)
        cells = grid.cells

        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        current = cells[y][x]
        visited = set()
        visited.add(current)
        stack = [current]

        while len(stack) != 0:
            x = current.x
            y = current.y
            popped = False
            choice = random.randint(0, 3)

            for i in range(5):
                if i > 3:
                    current = stack.pop()
                    popped = True
                    break

                match choice:
                    case 0:
                        if y - 1 >= 0:
                            neighbor = cells[y - 1][x]

                            if neighbor not in visited:
                                self.create_connection(current, neighbor, "n")
                                current = neighbor
                                break

                    case 1:
                        if x + 1 < width:
                            neighbor = cells[y][x + 1]

                            if neighbor not in visited:
                                self.create_connection(current, neighbor, "e")
                                current = neighbor
                                break
                    case 2:
                        if y + 1 < height:
                            neighbor = cells[y + 1][x]

                            if neighbor not in visited:
                                self.create_connection(current, neighbor, "s")
                                current = neighbor
                                break

                    case 3:
                        if x - 1 >= 0:
                            neighbor = cells[y][x - 1]

                            if neighbor not in visited:
                                self.create_connection(current, neighbor, "w")
                                current = neighbor
                                break

                choice = (choice + 1) % 4

            if not popped:
                stack.append(current)
                visited.add(current)

        return grid

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
