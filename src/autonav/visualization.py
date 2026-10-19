"""Tkinter display and keyboard controls (standard library only)."""

from pathlib import Path
import tkinter as tk

from .config import (
    BACKGROUND, CELL_SIZE, FREE_COLOR, GOAL_COLOR, GRID_COLOR, OBSTACLE_COLOR,
    PANEL_HEIGHT, PATH_COLOR, ROVER_COLOR, START_COLOR, TEXT_COLOR,
)
from .simulation import Simulation


class NavigationApp:
    def __init__(self, simulation: Simulation) -> None:
        self.simulation = simulation
        self.root = tk.Tk()
        self.root.title("AI-Based Autonomous Navigation System")
        self.root.resizable(False, False)
        width = simulation.world.width * CELL_SIZE
        height = simulation.world.height * CELL_SIZE
        self.canvas = tk.Canvas(self.root, width=width, height=height, highlightthickness=0, bg=_hex(BACKGROUND))
        self.canvas.pack()
        self.status = tk.StringVar()
        self.details = tk.StringVar()
        panel = tk.Frame(self.root, bg=_hex(BACKGROUND), height=PANEL_HEIGHT)
        panel.pack(fill="x")
        tk.Label(panel, textvariable=self.status, fg=_hex(TEXT_COLOR), bg=_hex(BACKGROUND),
                 font=("Segoe UI", 12, "bold"), anchor="w").pack(fill="x", padx=12, pady=(8, 0))
        tk.Label(panel, textvariable=self.details, fg=_hex(TEXT_COLOR), bg=_hex(BACKGROUND),
                 font=("Segoe UI", 9), anchor="w").pack(fill="x", padx=12, pady=2)
        tk.Label(panel, text="Space: pause   R: reset   S: save screenshot   Esc: quit",
                 fg=_hex(TEXT_COLOR), bg=_hex(BACKGROUND), font=("Segoe UI", 9), anchor="w").pack(fill="x", padx=12)
        self.root.bind("<space>", self.toggle_pause)
        self.root.bind("r", self.reset)
        self.root.bind("R", self.reset)
        self.root.bind("s", self.save_screenshot)
        self.root.bind("S", self.save_screenshot)
        self.root.bind("<Escape>", lambda _event: self.root.destroy())
        self.last_tick = 0
        self.draw()
        self.tick()

    def toggle_pause(self, _event=None) -> None:
        self.simulation.paused = not self.simulation.paused
        self.draw()

    def reset(self, _event=None) -> None:
        self.simulation.reset()
        self.draw()

    def save_screenshot(self, _event=None) -> None:
        """Save the map as a portable PostScript image using Tk's canvas exporter."""
        output_dir = Path("outputs")
        output_dir.mkdir(exist_ok=True)
        target = output_dir / "simulation.ps"
        self.canvas.postscript(file=str(target), colormode="color")
        self.status.set(f"Screenshot saved to {target}")

    def tick(self) -> None:
        import time
        current = time.perf_counter()
        dt = min(current - self.last_tick, 0.05) if self.last_tick else 0.0
        self.last_tick = current
        self.simulation.update(dt)
        self.draw()
        self.root.after(16, self.tick)

    def draw(self) -> None:
        sim, world = self.simulation, self.simulation.world
        self.canvas.delete("all")
        for y in range(world.height):
            for x in range(world.width):
                cell = (x, y)
                color = OBSTACLE_COLOR if cell in world.obstacles else FREE_COLOR
                self.canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE,
                                             (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE,
                                             fill=_hex(color), outline=_hex(GRID_COLOR))
        if sim.path:
            points = []
            for x, y in sim.path:
                points.extend(((x + 0.5) * CELL_SIZE, (y + 0.5) * CELL_SIZE))
            if len(points) >= 4:
                self.canvas.create_line(*points, fill=_hex(PATH_COLOR), width=5, capstyle=tk.ROUND)
        _draw_cell(self.canvas, world.start, START_COLOR)
        _draw_cell(self.canvas, world.goal, GOAL_COLOR)
        x = (sim.controller.x + 0.5) * CELL_SIZE
        y = (sim.controller.y + 0.5) * CELL_SIZE
        radius = CELL_SIZE / 3
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius,
                                fill=_hex(ROVER_COLOR), outline="#374151", width=2)
        state = "Paused" if sim.paused else sim.status
        self.status.set(state)
        self.details.set(f"Path: {len(sim.path)} cells   A* expanded: {sim.expanded_nodes}   Time: {sim.elapsed_seconds:.1f}s")

    def run(self) -> None:
        self.root.mainloop()


def _hex(color: tuple[int, int, int]) -> str:
    return "#{:02x}{:02x}{:02x}".format(*color)


def _draw_cell(canvas: tk.Canvas, cell: tuple[int, int], color: tuple[int, int, int]) -> None:
    x, y = cell
    inset = 4
    canvas.create_rectangle(x * CELL_SIZE + inset, y * CELL_SIZE + inset,
                            (x + 1) * CELL_SIZE - inset, (y + 1) * CELL_SIZE - inset,
                            fill=_hex(color), outline="")


def run_app(simulation: Simulation) -> None:
    NavigationApp(simulation).run()
