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