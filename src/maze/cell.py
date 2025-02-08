from dataclasses import dataclass, field


@dataclass
class Cell:
    walls: set = field(default_factory=lambda: {"n", "e", "s", "w"})

    def set_walls(self, new_walls: set):
        self.walls = new_walls

    def remove_wall(self, *walls: str):
        for wall in walls:
            self.walls.remove(wall)

    def add_wall(self, *walls: str):
        valid_walls = {"n", "e", "s", "w"}
        for wall in walls:
            if wall in valid_walls:
                self.walls.add(wall)
            else:
                # TODO: change
                print("invalid wall type")
