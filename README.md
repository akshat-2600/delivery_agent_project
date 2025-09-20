# 🚚 Delivery Agent — Grid Pathfinding & Dynamic Replanning

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Algorithms](https://img.shields.io/badge/Algorithms-BFS%20%7C%20UCS%20%7C%20A*-yellow)
![Dynamic Replanning](https://img.shields.io/badge/Dynamic-Replanning-orange)

## Project summary
A compact, well-documented implementation of a delivery agent that finds efficient routes in a 2D grid city.  
It includes static obstacles, varying terrain costs, and dynamic moving obstacles. The project implements and compares:

- *Uninformed search*: BFS (for unit-cost grids), Uniform-Cost Search (UCS)  
- *Informed search: A (Manhattan heuristic)  
- *Local/dynamic replanning: Replanner (uses A/UCS with map updates)  

Outputs are printed to console, saved as visual PNGs, and recorded to results.csv for experiment comparison.

---

## Features
- Grid map loader from plain text files (maps/*.txt)  
- Support for static (X) and dynamic (D) obstacles  
- Terrain costs encoded as integers (1, 2, 3, ...)  
- Agent able to replan when obstacles move (deterministic or random modes)  
- Metrics: *path cost, **nodes expanded, **runtime*  
- ASCII console visualization and Matplotlib graphical plots (PNG)  
- Experiment runner that tests algorithms across multiple maps and saves a results.csv

---

## Project structure

delivery_agent_project/ │── algorithms/ │   ├── bfs.py │   ├── ucs.py │   ├── astar.py │   ├── replanner.py │   └── init.py │ │── maps/ │   ├── small_map.txt │   ├── medium_map.txt │   ├── large_map.txt │   └── dynamic_map.txt │ │── environment.py │── agent.py │── visualize.py │── main.py                # runs experiments, saves results.csv and plots │── test_experiments.py    # optional: alternative runner │── results/               # output PNGs (created at runtime) │── results.csv            # experiment results (created at runtime) │── README.md │── requirements.md │── requirements.txt

---

## Map format
Plain text, rows separated by newline, tokens separated by spaces:

- S → Start  
- G → Goal  
- X → Static obstacle (impassable)  
- D → Dynamic obstacle (moves during simulation)  
- 1,2,3,... → Terrain move cost (integer ≥ 1)  
- . or 1 recommended for plain free cells

Example (5×5):

S . . . G . X . . . . . . X . X . . . . . . . . .

---

## Quick start (local)
1. Clone repo and enter folder:
```bash
git clone https://github.com/<youruser>/delivery_agent_project.git
cd delivery_agent_project

2. Create & activate virtual environment:



python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

3. Install dependencies:



pip install -r requirements.txt

4. Run the whole experiment (runs all maps & algorithms, saves results.csv and PNGs into results/):



python main.py

> If you are running on a headless system (CI/evaluation server), set the environment variable NO_PLOT=1 before running (see requirements.md for details).




---

CLI / automated usage

main.py is intended as the single entry point. It currently runs:

BFS, UCS, A* on every map in maps/

Saves results.csv with rows containing: map, algorithm, cost, nodes_expanded, runtime

Saves per-run PNG visuals to results/<map>_<algorithm>.png

Runs dynamic replanning for maps/dynamic_map.txt and saves the replanned path image


If you prefer or need flags, you can implement an argparse wrapper (suggested flags):

python main.py --maps maps/ --no-gui --out results.csv

(Repository includes main.py that runs everything without extra flags).


---

Output format (expected for grading / evaluation)

CSV: results.csv (header)


map,algorithm,cost,nodes_expanded,runtime
small_map.txt,BFS,5,12,0.000134
small_map.txt,UCS,5,8,0.001248
...

PNG images in results/ e.g. small_map_BFS.png, dynamic_map_Replanner.png.

Console output: human-readable logs that show the ASCII grid, path cost, nodes expanded and runtime.


Automated graders should verify:

results.csv present in repo root after running python main.py

Each algorithm returns a valid path (non-empty) for small/medium/large test maps

Replanner runs on dynamic_map.txt and produces a dynamic_map_Replanner.png file



---

Reproducibility

To reduce nondeterminism when using random dynamic obstacle mode, set a fixed seed:

Edit environment.py to set random.seed(42) or export RANDOM_SEED=42 and read it.


Ensure results/ is writable by the runner and main.py exits with code 0 on success.



---

Troubleshooting & common gotchas

ImportError for algorithms package:

Ensure algorithms/_init_.py exists and exports bfs, ucs, astar, Replanner.


Algorithm function signatures (for automated evaluation) must be:

# Each algorithm returns 4-tuple:
path, cost, nodes_expanded, runtime = algorithm(env)

Environment must accept a map path:

env = Environment("maps/small_map.txt")
start, goal = env.get_start_goal()

Replanner interface (recommended):

planner = Replanner(env, algorithm="astar")
path, cost, nodes_expanded, runtime = planner.replan()

Visualization helper (recommended):

Standalone: plot_path(env, path, save_as="results/small_map_BFS.png")

or viz.plot(path) method inside Visualizer class.




---

What to submit / deliverables (for assignment)

algorithms/ source code (BFS, UCS, A*, replanner) — well documented

environment.py, agent.py, visualize.py, main.py

maps/* — at least 4 maps (small/medium/large/dynamic)

results.csv (sample result after run)

results/ folder with example PNGs

report.pdf (≤6 pages): environment model, agent design, heuristics, experimental tables & plots, analysis & conclusion

demo.mp4 or sequence of screenshots showing dynamic replanning in action



---

Future work / ideas

Add diagonal movement & corresponding admissible heuristics

Implement D* Lite for efficient real-time replanning

Add multiple agents with cooperative planning

GUI with interactive map editing & step-through visualization



---

License & credits

Project licensed under MIT.
Author: Akshat Saxena (adapt the author/maintainer fields).