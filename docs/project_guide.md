# Project and portfolio guide

This companion guide expands the README with a build sequence, practical GitHub steps, interview notes, and beginner troubleshooting.

## A. What the project demonstrates

In plain language, a navigation system needs to know where it is, understand where it can travel, choose a route, and move toward the destination while avoiding hazards. This simulation starts with a known map and a start/goal cell. A* finds a short route through free cells; a waypoint controller moves the rover; the simulation renders progress and stops at the goal.

In robotics terms, this is a deliberately small planning-and-control stack. The occupancy grid is the environment representation, A* is the global planner, and the waypoint follower is a simple low-level controller. The Tkinter loop is the simulator. The project does not implement perception, SLAM, localization, or real-world actuation. Those distinctions make the demo honest and technically explainable.

Related production areas include warehouse mobile robots, delivery robots, autonomous vehicle research, drones, and industrial mobility. Those systems combine sensor data (cameras, lidar, radar, encoders), localization, perception, behavior planning, trajectory planning, control, and safety monitoring. This repository demonstrates only the map-based planning and simple control concepts.

### Workflow and data flow

```text
Known occupancy map → A* planner → ordered grid-cell waypoints
                                      ↓
Tkinter display ← collision check ← waypoint controller ← simulation clock
       ↓
 screenshot and completion metrics
```

## B. Stack options and selection

| Option | Stack | Difficulty | GPU | Outcome |
|---|---|---|---|---|
| A — selected | Python, Tkinter, built-in data structures | Beginner | No | 2D simulation, route planning, waypoint movement |
| B | Python, OpenCV, a custom scene or recorded images | Intermediate | No for simple vision; optional for learned models | Add image-based lane/obstacle perception |
| C | ROS 2 with Gazebo or CARLA | Advanced | Often useful for 3D workloads | Sensor and middleware integration in a richer simulation |

Option A is a practical first portfolio milestone because it has few dependencies, transparent algorithms, and no large assets to download. CARLA, Gazebo, YOLO, PyTorch, and TensorFlow are not needed for this implementation.

## C. Architecture details

1. **Input/world:** `GridWorld` stores dimensions, start, goal, and blocked cells.
2. **Planning:** A* explores four-connected free neighbors. Manhattan distance estimates remaining cost.
3. **Control:** `WaypointController` moves a point rover toward consecutive path cells.
4. **Safety check:** `Simulation` checks the rover's rounded grid cell against map bounds and obstacles.
5. **Output:** Tkinter draws the map and status. Completion metrics are appended to CSV; **S** saves the map canvas as PostScript.

## D. Implementation phases and completion checks

| Phase | Work and reason | Expected output / completion check | Common mistake |
|---|---|---|---|
| 1. Environment | Install supported Python and create venv | `python --version`, import check succeeds | Installing into a different Python than the one used to run |
| 2. Structure | Keep planner, world, controller, UI in separate modules | Files match the repository tree | Running from inside `src` instead of repository root |
| 3. World | Adjust grid and obstacles | Grid renders with start and goal | Placing start or goal inside an obstacle |
| 4. Planner | Run A* on free cells | Route joins start to goal, or no-route status is clear | Changing neighbor cost without changing heuristic assumptions |
| 5. Control | Follow the route one waypoint at a time | Rover stays on free cells and reaches goal | Large frame steps can skip cells; update clamps elapsed frame time |
| 6. Visualization | Show route, agent, status, and controls | Controls respond; **S** creates a PostScript capture | Saving before the first frame has rendered |
| 7. Verification | Try map variations and unreachable goal | Behavior matches edited map | Assuming a screenshot proves every edge case |
| 8. Documentation | Explain scope, commands, outcomes, limitations | A new reader can install and launch | Claiming camera detection or real-robot performance |
| 9. GitHub | Create repo and push source plus selected proof | Clone and run instructions are visible | Committing `.venv`, generated output, or credentials |
| 10. Presentation | Explain A*, costs, controller, limitations | Clear 60-second project explanation | Describing planned future work as already implemented |

## E. Files and outputs

`src/autonav/` contains the application modules. `main.py` launches the event loop. `docs/project_guide.md` is this extended guide. `images/` is for curated screenshots that you manually choose to commit. `outputs/` receives locally generated CSV and PostScript capture files; generated artifacts are ignored by Git to avoid accidental clutter. Commit a selected screenshot under `images/` after reviewing it.

## F. Exact run and proof workflow

From the repository root, activate the virtual environment and run:

```bash
python main.py
```

Wait for the rover to reach the goal, then press **S** to save a capture. Press **Esc** to close. Inspect `outputs/run_summary.csv`; copy only a useful, genuine screenshot into `images/` and add it to the README. The sample output is a GUI status (`Goal reached`) and a CSV row containing timestamp, path cell count, A* expanded-node count, and simulation seconds. Numeric values can vary if you edit the map or speed.

Suggested screen proof: overview with full route; obstacle corridor; goal reached status; terminal showing launch command; final repository README page. A GIF or short video is optional and should be your own recording. Do not claim a capture or metric that you did not produce.

## G. GitHub publishing

Suggested repository name: `ai-autonomous-navigation-system`. Suggested description: `Educational 2D rover navigation simulation using A*, waypoint following, and Tkinter.` Suggested topics: `python`, `robotics`, `path-planning`, `astar`, `tkinter`, `simulation`, `autonomous-navigation`.

Create an empty public repository on GitHub. From the local project folder (replace `YOUR-USERNAME`):

```bash
git add README.md docs src main.py requirements.txt .gitignore images
git commit -m "Build 2D autonomous navigation simulation"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/ai-autonomous-navigation-system.git
git push -u origin main
```

If a remote is already configured, inspect it with `git remote -v` and do not add a duplicate. Keep commits focused and factual. Example sequence:

| Milestone | Commit message | Proof to capture |
|---|---|---|
| Project skeleton and map | `Add grid world and simulator structure` | Initial map screenshot |
| Planner | `Implement A-star grid path planning` | Route around obstacle screenshot |
| Control and metrics | `Add waypoint following and run summary` | Goal reached and CSV output |
| Docs and portfolio | `Document setup results and project scope` | README preview and repository page |

Pin the repository only after the README is polished, run instructions work, and at least one genuine demo image is added. Never commit tokens, passwords, virtual environments, or unreviewed generated files.

## H. Day-by-day proof plan

This is a suggested cadence, not a claim that each phase already occurred.

| Day | Deliverable | Commit | Evidence / notes |
|---|---|---|---|
| 1 | Environment and skeleton | `Create project skeleton` | Installation check; note Python/Tkinter versions |
| 2 | Grid world and obstacles | `Add occupancy grid simulation world` | Capture map; note cell size and obstacle gaps |
| 3 | A* planner | `Implement A-star route planning` | Capture route; explain Manhattan heuristic |
| 4 | Waypoint movement | `Add rover waypoint controller` | Capture mid-run; note speed and path cells |
| 5 | Collision/status and metrics | `Record navigation run metrics` | Goal and CSV capture; note expanded nodes |
| 6 | Map variations and polish | `Improve simulation presentation` | Capture a changed map and discuss limitations |
| 7 | README and publishing | `Document portfolio demo` | Repository page and README preview |

## I. Resume, LinkedIn, and interview

Use wording that describes what is implemented. Replace bracketed measurements with values from your own run.

**Resume bullets**

- Built an interactive Python/Tkinter 2D rover simulator with an occupancy-grid world and visualized route execution.
- Implemented A* search with Manhattan heuristic and four-connected movement, reporting path length and expanded nodes.
- Added waypoint following, collision checks, keyboard controls, screenshot capture, and CSV run summaries.

**LinkedIn project descriptions**

1. “Built a virtual rover navigation demo in Python. A* plans through a grid map and a waypoint controller drives the rover to the goal; no physical hardware is required.”
2. “Explored the planning and control stages of mobile robotics with an interactive Tkinter simulator, obstacle maps, route visualization, and run metrics.”
3. “Portfolio project: an explainable baseline for autonomous navigation. Next steps include dynamic replanning and sensor-based perception.”

**HR explanation:** “I built a small virtual robot that finds a route through obstacles and follows it to a destination. I made it visual so the planning decisions and result are easy to inspect.”

**Technical explanation:** “The environment is a known occupancy grid. A* uses unit edge costs and Manhattan distance for four-connected motion, reconstructs the route from parent links, and a waypoint follower advances the rover along it. The simulation checks collision against the map and records basic search/run metrics. It is a planning prototype rather than a perception or production autonomy stack.”

### Interview questions and answer outlines

1. **What problem does it solve?** Demonstrates route planning and goal-directed movement in a known obstacle map.
2. **Why A*?** It combines path cost so far with an estimate to the goal; with a suitable heuristic it can efficiently find a shortest path.
3. **Why Manhattan distance?** Each move changes one grid axis by one, so Manhattan distance is admissible for four-connected unit-cost movement.
4. **What is an occupancy grid?** A discretized map whose cells represent traversable or blocked space.
5. **What happens if there is no route?** Search exhausts reachable free cells and returns an empty path; the UI displays a no-route status.
6. **How is collision avoidance implemented?** The planned path excludes blocked cells and each simulated rover update checks the occupied grid cell. This is not a substitute for real robot safety.
7. **What is the controller?** A simple waypoint follower that moves toward each grid-cell target at a configured speed.
8. **What are the limitations?** Known static map, point rover, no sensors/localization, no uncertainty, and no dynamic obstacle replanning.
9. **How would you improve it?** Add map editing and automated tests, then dynamic replanning; later add sensor simulation and localization.
10. **How would you move toward a real robot?** Define a robot interface, use a simulator such as Gazebo/ROS 2 first, model footprint and sensor uncertainty, and validate safety before hardware.

## J. Future improvements

1. Add automated tests for path validity, unreachable goals, and controller completion.
2. Add click-to-place obstacles and replan when the map changes.
3. Add diagonal motion with a matching octile-distance heuristic and corner-cutting checks.
4. Model a rover footprint rather than a point and inflate obstacles by its radius.
5. Add camera/lidar-like simulated observations and OpenCV perception.
6. Integrate ROS 2 and a physics simulator such as Gazebo; consider CARLA for road-scene research.
7. Explore localization/SLAM, multiple agents, reinforcement learning, or warehouse/drone scenarios as separate follow-on projects.

## K. Troubleshooting

| Symptom | Likely reason | Fix / prevention |
|---|---|---|
| `No module named tkinter` | Dependency installed in another interpreter or venv inactive | Activate `.venv`, then `python -m pip install -r requirements.txt`; run with that same `python` |
| Tkinter install/build issue | Unsupported Python version or stale pip | Use a standard Python installer that includes Tkinter; on python.org Windows installs, Tkinter is normally included |
| Window opens then closes | Launching by double-click hides errors | Run `python main.py` from PowerShell/terminal and read the traceback |
| Display is blank | Window obscured or graphics initialization issue | Bring the Tkinter window forward; run locally with desktop graphics enabled |
| No route found | Start/goal blocked or obstacles partition the map | Check `start`, `goal`, and obstacle layout in `world.py` |
| Rover stops with collision | Map changed but planner/controller assumptions no longer match | Ensure path neighbors use `is_free`; reduce `ROVER_SPEED` if editing update logic |
| Screenshot lacks status text | Saved before the first completed draw | Wait one frame and press **S** again |
| CSV not appearing | Run from a different working directory or goal not reached | Launch from repository root and check the on-screen status |
| `remote origin already exists` | Repository has a configured remote | Inspect `git remote -v`; use `git remote set-url origin ...` if it points to the wrong repository |
| GitHub authentication/push rejected | Credentials, permissions, or remote URL issue | Use GitHub's current HTTPS/browser authentication or SSH setup; verify repository ownership and URL |
| Accidentally staged generated files | Broad `git add .` | Check `git status` before commit; `.gitignore` covers generated output and virtual environments |

## L. Honest scope and claims

Call this a **virtual grid-navigation prototype**. It includes route planning and simple movement in a simulated known map. It does not include image-based object detection, neural networks, hardware drivers, lane detection, SLAM, ROS, or a self-driving car. A future feature should be described as future work until it is implemented and demonstrated.


