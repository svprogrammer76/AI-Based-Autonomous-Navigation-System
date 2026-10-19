"""Occupancy-grid world and deterministic obstacle layout."""

from dataclasses import dataclass, field

from .config import GRID_HEIGHT, GRID_WIDTH

Cell = tuple[int, int]


@dataclass
class GridWorld:
    width: int = GRID_WIDTH
    height: int = GRID_HEIGHT
    start: Cell = (1, 1)
    goal: Cell = (22, 16)
    obstacles: set[Cell] = field(default_factory=set)

    def __post_init__(self) -> None:
        if not self.obstacles:
            self.obstacles = self._default_obstacles()

    def _default_obstacles(self) -> set[Cell]:
        blocks: set[Cell] = set()
        # Two staggered walls leave visible gaps for the planner to discover.
        for y in range(2, 15):
            if y not in (6, 12):
                blocks.add((7, y))
        for y in range(0, 15):
            if y not in (3, 9):
                blocks.add((15, y))
        for x in range(9, 14):
            blocks.add((x, 10))
        return blocks

    def in_bounds(self, cell: Cell) -> bool:
        x, y = cell
        return 0 <= x < self.width and 0 <= y < self.height

    def is_free(self, cell: Cell) -> bool:
        return self.in_bounds(cell) and cell not in self.obstacles

    def neighbors(self, cell: Cell) -> list[Cell]:
        x, y = cell
        candidates = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        return [candidate for candidate in candidates if self.is_free(candidate)]
