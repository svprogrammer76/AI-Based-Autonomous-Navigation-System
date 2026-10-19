"""A* search over a four-connected occupancy grid."""

from heapq import heappop, heappush
from itertools import count

from .world import Cell, GridWorld


def heuristic(a: Cell, b: Cell) -> int:
    """Manhattan distance is admissible for four-direction movement."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(world: GridWorld, start: Cell, goal: Cell) -> tuple[list[Cell], int]:
    """Return (path including endpoints, expanded-node count); empty if unreachable."""
    if not world.is_free(start) or not world.is_free(goal):
        return [], 0

    tie_breaker = count()
    frontier: list[tuple[int, int, Cell]] = []
    heappush(frontier, (heuristic(start, goal), next(tie_breaker), start))
    came_from: dict[Cell, Cell | None] = {start: None}
    cost_so_far = {start: 0}
    expanded = 0

    while frontier:
        _, _, current = heappop(frontier)
        if current == goal:
            break
        expanded += 1
        for neighbor in world.neighbors(current):
            new_cost = cost_so_far[current] + 1
            if new_cost < cost_so_far.get(neighbor, float("inf")):
                cost_so_far[neighbor] = new_cost
                came_from[neighbor] = current
                priority = new_cost + heuristic(neighbor, goal)
                heappush(frontier, (priority, next(tie_breaker), neighbor))

    if goal not in came_from:
        return [], expanded

    path = []
    current: Cell | None = goal
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path, expanded
