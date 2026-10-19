# AI-Based Autonomous Navigation System

A beginner-friendly, fully virtual navigation project. A small simulated rover plans a route across a 2D occupancy grid with A*, avoids obstacles, follows waypoints, and reports its progress. It runs on a regular laptop and does not require a robot, camera, GPU, ROS, or a pretrained model.

> **Scope:** this is a transparent educational simulation. It demonstrates grid-based planning and simple waypoint control; it is not a safety-certified autonomous vehicle and does not perform camera-based object detection.

## Demo and results

Run `python main.py` to open the simulator. The display shows free cells, obstacles, start/goal, the planned route, and the rover. Press **R** to reset, **Space** to pause/resume, **S** to save a PostScript snapshot, and **Esc** to quit. On arrival, a run summary is written to `outputs/run_summary.csv`.

## Problem and approach

Autonomous navigation turns observations about the world into safe movement toward a goal. In this project, the map is already represented as a grid: each cell is free or occupied. A* searches that grid, then a waypoint follower moves the rover along the route. The simulator checks for collisions and displays the result.

This small model illustrates concepts used in mobile robotics, warehouse automation, delivery robots, drones, and autonomous vehicle research. Real systems add sensors, localization, richer perception, uncertainty handling, dynamic replanning, and safety engineering.

## Architecture

```text
Occupancy grid + start/goal
          │
          ▼
     A* path planner ── no route ──> status message
          │ route (grid cells)
          ▼
   Waypoint controller
          │ rover position
          ▼
 Collision check + Tkinter visualization
          │
          ├── screen / saved screenshot
          └── completion metrics → outputs/run_summary.csv
```

Modules: `world.py` owns the map and obstacles; `planner.py` implements A*; `controller.py` follows waypoints; `simulation.py` coordinates the run and metrics; `visualization.py` draws the scene with Tkinter; `main.py` starts the app.

## Tech stack options

| Option | Tools | Difficulty / GPU | Outcome |
|---|---|---|---|
| A: Custom 2D grid (selected) | Python, Tkinter, standard library | Beginner; no GPU | Interactive map, A*, waypoint following, collision checks |
| B: Camera perception | Python, OpenCV, custom/Tkinter scene | Intermediate; GPU optional | Image processing and perception pipeline prototype |
| C: 3D robotics simulation | ROS 2 with Gazebo or CARLA | Advanced; GPU helpful | Sensor-rich 3D simulation and middleware integration |

Option A is the quickest strong, explainable portfolio foundation. It avoids a large simulator install and external model downloads. The project can later grow toward B or C.

## Folder structure

```text
AI-Based Autonomous Navigation System/
├── main.py                    # Application entry point
├── requirements.txt           # No external runtime dependencies
├── .gitignore
├── README.md
├── src/autonav/
│   ├── __init__.py
│   ├── config.py               # Display and motion settings
│   ├── world.py                # Grid map and obstacle layout
│   ├── planner.py              # A* search
│   ├── controller.py           # Waypoint follower
│   ├── simulation.py           # State, collision, run metrics
│   └── visualization.py        # Tkinter rendering and controls
├── docs/
│   └── project_guide.md        # Build phases, publishing, interview guide
├── images/                     # Add your own screenshots here
└── outputs/                    # Run summary CSV and optional captures
```

## Installation

Python 3.10 or newer is recommended. The project uses only the Python standard library, including Tkinter.

### Windows PowerShell

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -c "import tkinter; print('Tkinter is available')"
```

If PowerShell blocks activation, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` in that terminal, then activate again.

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -c "import tkinter; print('Tkinter is available')"
```

## Run it

From the repository root with the virtual environment activated:

```bash
python main.py
```

The route is computed at startup. The rover moves automatically and stops at the goal. If a route cannot be found, the app reports that status. Use **S** to save a PostScript capture as `outputs/simulation.ps`; completion appends run time, path length, and visited-node count to `outputs/run_summary.csv`.

## Simulation workflow

1. Create a virtual environment and confirm Tkinter is available.
2. Start the app; `world.py` creates the occupancy grid and fixed obstacle map.
3. A* expands free neighboring cells from start to goal.
4. The controller targets each route cell in sequence and advances at a configured speed.
5. The simulation checks each updated position for wall/obstacle collision.
6. The renderer displays map, route, rover, goal, and status.
7. Save a screenshot with **S** and capture your own screen recording if useful for your portfolio.

## Results 

The simulator displays the route and current rover position. Metrics include elapsed simulation time, number of route cells, and A* expanded nodes. These are measurements from this simple deterministic simulation, not real-vehicle performance claims.

## Testing ideas

Try changing start/goal and obstacle cells in `src/autonav/world.py`. Confirm that the route changes, that blocked/unreachable goals are reported, and that the rover reaches the goal without intersecting blocked cells. Automated tests are not included yet; see the future-work section in the guide.

## Limitations and future work

- The map is known in advance; no camera, lidar, localization, or object detector is included.
- Obstacles are static and the rover uses a point model on a grid.
- A* uses 4-connected movement and Manhattan distance.
- Potential upgrades: unit tests, diagonal motion, dynamic obstacle replanning, OpenCV perception, ROS 2, Gazebo/CARLA, SLAM, multi-agent planning, or a physical robot after electrical and safety review.

## Learning outcomes

Grid maps, graph search, A*, heuristic functions, waypoint tracking, simulation loops, basic collision checks, and communicating engineering scope and limitations.

## Author

Shraddha Verma, B.Tech in Computer Science and Engineering.

