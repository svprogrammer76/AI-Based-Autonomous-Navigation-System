"""Simple waypoint follower for the grid-based rover."""

from math import hypot

from .world import Cell


class WaypointController:
    def __init__(self, path: list[Cell], speed: float) -> None:
        self.path = path
        self.speed = speed
        self.index = 1 if len(path) > 1 else len(path)
        self.x, self.y = (float(v) for v in path[0]) if path else (0.0, 0.0)

    @property
    def finished(self) -> bool:
        return not self.path or self.index >= len(self.path)

    def update(self, dt: float) -> None:
        """Move toward the active waypoint, carrying leftover travel across cells."""
        distance_left = self.speed * dt
        while distance_left > 0 and not self.finished:
            target_x, target_y = self.path[self.index]
            dx, dy = target_x - self.x, target_y - self.y
            distance = hypot(dx, dy)
            if distance <= distance_left or distance == 0:
                self.x, self.y = float(target_x), float(target_y)
                distance_left -= distance
                self.index += 1
            else:
                self.x += dx / distance * distance_left
                self.y += dy / distance * distance_left
                distance_left = 0
