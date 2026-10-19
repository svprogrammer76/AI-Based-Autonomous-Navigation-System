"""Simulation state, collision checks, and run-summary export."""

import csv
import time
from pathlib import Path

from .config import ROVER_SPEED
from .controller import WaypointController
from .planner import astar
from .world import GridWorld


class Simulation:
    def __init__(self) -> None:
        self.world = GridWorld()
        self.reset()

    def reset(self) -> None:
        self.path, self.expanded_nodes = astar(self.world, self.world.start, self.world.goal)
        self.controller = WaypointController(self.path, ROVER_SPEED)
        self.running = True
        self.paused = False
        self.status = "Following planned route" if self.path else "No valid route found"
        self.started_at = time.perf_counter()
        self.elapsed_seconds = 0.0
        self.summary_written = False

    @property
    def complete(self) -> bool:
        return bool(self.path) and self.controller.finished

    def update(self, dt: float) -> None:
        if self.paused or not self.running or self.complete or not self.path:
            return
        self.controller.update(dt)
        cell = (round(self.controller.x), round(self.controller.y))
        if not self.world.is_free(cell):
            self.status = "Collision detected — simulation stopped"
            self.running = False
            return
        self.elapsed_seconds += dt
        if self.complete:
            self.status = "Goal reached"
            self.write_summary()

    def write_summary(self) -> None:
        if self.summary_written:
            return
        output_dir = Path("outputs")
        output_dir.mkdir(exist_ok=True)
        csv_path = output_dir / "run_summary.csv"
        needs_header = not csv_path.exists() or csv_path.stat().st_size == 0
        with csv_path.open("a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if needs_header:
                writer.writerow(["timestamp", "path_cells", "expanded_nodes", "simulation_seconds"])
            writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), len(self.path), self.expanded_nodes,
                             round(self.elapsed_seconds, 2)])
        self.summary_written = True
