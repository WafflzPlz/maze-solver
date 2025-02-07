from dataclasses import dataclass


@dataclass
class MazeGenerator:
    """Class for representing maze generator"""
    height: int
    width: int

    def print_message(self, message: str):
        print(message)
