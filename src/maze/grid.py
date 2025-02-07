from dataclasses import dataclass


@dataclass
class Grid:
    # TODO: maybe add default_factory
    cells: list[list]
