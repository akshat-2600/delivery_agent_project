# Requirements

## 1. Python Version

- Python **3.8 or higher**


## 2. Dependencies

Install required libraries:

```bash
pip install -r requirements.txt
```

Or install manually:

matplotlib

numpy


## 3. Running the Project

Run the entry point:

```bash
python main.py
```

This will:

- Execute BFS, UCS, A* on all maps in maps/

- Display console logs (ASCII grid, cost, nodes expanded, runtime)

- Show live visualization of explored path and solution

- Run dynamic replanning on maps/dynamic_map.txt


## 4. Output

- All results are displayed in the console and via live visualization


## 5. Special Notes

Ensure the maps/ folder exists and contains at least:

- small_map.txt

- medium_map.txt

- large_map.txt

- dynamic_map.txt


For reproducibility with dynamic obstacles, set a random seed:

```bash
export RANDOM_SEED=42
```