from .generator.maze_generator import MazeGenerator


def main():
    generator = MazeGenerator(1, 1)
    generator.print_message("hello")


if __name__ == "__main__":
    main()
