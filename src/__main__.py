from src.generator.backtracking import MazeGeneratorBacktracking
from src.generator.maze_generator import MazeGenerator
from src.maze.grid import Grid
import pygame


def main():

    generator: MazeGenerator = MazeGeneratorBacktracking()
    grid: Grid = generator.generate_maze(20, 20, True)

    screen: pygame.display = pygame.display.set_mode((500, 500))
    CELL_SIZE = 25

    pygame.display.flip()

    running = True

    while running:
        screen.fill((255, 255, 255))
        grid.draw(screen, CELL_SIZE)
        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()
