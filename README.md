# 🚚 Delivery Agent — Grid Pathfinding & Dynamic Replanning

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Algorithms](https://img.shields.io/badge/Algorithms-BFS%20%7C%20UCS%20%7C%20A*-yellow)
![Dynamic Replanning](https://img.shields.io/badge/Dynamic-Replanning-orange)

<p align="center">
  <img src="results\banner_logo.png" width="600"/>
</p>


### 🎥 Dynamic Replanning Demo
<p align="center">
  <img src="results\demo_video.gif" width="500"/>
</p>

---

## Project summary
A compact, well-documented implementation of a delivery agent that finds efficient routes in a 2D grid city.  
It includes static obstacles, varying terrain costs, and dynamic moving obstacles. The project implements and compares:

- *Uninformed search*: BFS (for unit-cost grids), Uniform-Cost Search (UCS)  
- *Informed search: A** (Manhattan heuristic)  
- *Local/dynamic replanning: Replanner (uses A/UCS with map updates)  

Outputs are printed to console and also visible as matplotlib visuals.

---

## Features
- Grid map loader from plain text files (maps/*.txt)  
- Support for static (X) and dynamic (D) obstacles  
- Terrain costs encoded as integers (1, 2, 3, ...)  
- Agent able to replan when obstacles move (deterministic or random modes)  
- Metrics: *path cost, **nodes expanded, **runtime*  
- ASCII console visualization and Matplotlib graphical plots (PNG)  

---

## Project structure

delivery_agent_project/

 │── algorithms/ 

    └── init.py 

       ├── astar.py

       ├── bfs.py  

       ├── ucs.py

       ├── replanner.py 

 │── maps/   

    └── dynamic_map.txt 

    ├── large_map.txt 

    ├── medium_map.txt

    ├── small_map.txt

 │── agent.py    

 │── environment.py

 │── main.py

 │── README.md 

 │── replan_logger.py

 │── requirements.txt

 │── visualize.py 
                
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

S . . . G 
. X . . . 
. . . X . 
X . . . . 
. . . . .

---

### 🖼 Sample Visualizations

*Path Planning in BFS on small map*

<img src="results\bfs_small_map.png" width="400"/>

*Path Planning in UCS on small map*

<img src="results\ucs_small_map.png" width="400"/>

*Path Planning in A** on small map*

<img src="results\astar_small_map.png" width="400"/>

## Quick start (local)
1. Clone repo and enter folder:
```bash
git clone https://github.com/<youruser>/delivery_agent_project.git
cd delivery_agent_project
```

2. Create & activate virtual environment:

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the whole experiment (runs all maps & algorithms):

```bash
python main.py
```


### CLI / automated usage

- main.py is the single entry point. It currently runs:

- BFS, UCS, A* on every map in maps/

- Prints human-readable logs to the console, including:

- ASCII grid of the map with the explored path

- Path cost

- Nodes expanded

- Runtime for each algorithm

- Displays a live visualization of the path exploration (via matplotlib).


### Reproducibility

- To reduce nondeterminism when using random dynamic obstacles:

```bash
Edit environment.py to set random.seed(42)
```

Or set an environment variable:

```bash
export RANDOM_SEED=42
```

### Troubleshooting & Common Gotchas

- ImportError for algorithms package:

- Ensure algorithms/_init_.py exists and exports bfs, ucs, astar, Replanner.

- Algorithm function signatures (must return 4-tuple):

- path, cost, nodes_expanded, runtime = algorithm(env)

### Environment usage:

- env = Environment("maps/small_map.txt")
- start, goal = env.get_start_goal()

### Replanner usage (recommended):

- planner = Replanner(env, algorithm="astar")

- path, cost, nodes_expanded, runtime = planner.replan()

### Visualization helper (optional):

- Direct usage: viz.plot(path)


### Future Work 

- Add diagonal movement & corresponding admissible heuristics

- Implement D* Lite for efficient real-time replanning

- Add multiple agents with cooperative planning

- GUI with interactive map editing & step-through visualization


### License & Credits

Licensed under MIT

Author: Akshat Saxena (adapt maintainer fields if needed)