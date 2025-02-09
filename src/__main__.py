from src.generator.maze_generator import MazeGenerator
import pygame


def main():

    generator = MazeGenerator()
    grid = generator.generate_maze(20, 20)
    cells = grid.cells

    screen = pygame.display.set_mode((500, 500))
    CELL_SIZE = 25

    pygame.display.flip()

    running = True

    while running:
        screen.fill((255, 255, 255))

        for y in range(0, len(cells)):
            for x in range(0, len(cells[y])):
                walls = cells[y][x].walls
                for wall in walls:
                    match wall:
                        case "n":
                            pygame.draw.line(
                                screen,
                                (0, 0, 0),
                                (CELL_SIZE * x, CELL_SIZE * y),
                                (CELL_SIZE * x + CELL_SIZE, CELL_SIZE * y),
                                1,
                            )

                        case "e":
                            pygame.draw.line(
                                screen,
                                (0, 0, 0),
                                (CELL_SIZE * x + CELL_SIZE, CELL_SIZE * y),
                                (CELL_SIZE * x + CELL_SIZE,
                                 CELL_SIZE * y + CELL_SIZE),
                                1,
                            )

                        case "s":
                            pygame.draw.line(
                                screen,
                                (0, 0, 0),
                                (CELL_SIZE * x, CELL_SIZE * y + CELL_SIZE),
                                (CELL_SIZE * x + CELL_SIZE,
                                 CELL_SIZE * y + CELL_SIZE),
                                1,
                            )

                        case "w":
                            pygame.draw.line(
                                screen,
                                (0, 0, 0),
                                (CELL_SIZE * x, CELL_SIZE * y),
                                (CELL_SIZE * x, CELL_SIZE * y + CELL_SIZE),
                                1,
                            )

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()
