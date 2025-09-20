import time
import csv
import matplotlib.pyplot as plt
import numpy as np

from environment import Environment
from algorithms import bfs, ucs, astar, Replanner

def plot_path(env, path, title="Path"):
    grid = np.array(env.grid)
    plt.imshow(grid, cmap="terrain")

    if path:
        xs, ys = zip(*path)
        plt.plot(ys, xs, marker="o", color="red")

    plt.title(title)
    plt.show()


maps = ["maps/small_map.txt",
        "maps/medium_map.txt",
        "maps/large_map.txt",
        "maps/dynamic_map.txt"]

algorithms = ["bfs", "ucs", "astar"]

results = []


for map_file in maps:
    env = Environment(map_file)
    print(f"\n--- Testing Map: {map_file} ---")

    for algo in algorithms:
        start_time = time.time()

        if algo == "bfs":
            path, cost, nodes = bfs(env)
        elif algo == "ucs":
            path, cost, nodes = ucs(env)
        elif algo == "astar":
            path, cost, nodes = astar(env)

        runtime = round(time.time() - start_time, 6)

        print(f"{algo.upper()} → Cost: {cost}, Nodes Expanded: {nodes}, Time: {runtime} sec")
        results.append({
            "map": map_file,
            "algorithm": algo,
            "cost": cost,
            "nodes_expanded": nodes,
            "runtime": runtime
        })

        if "small" in map_file or "medium" in map_file:
            plot_path(env, path, title=f"{algo.upper()} Path on {map_file}")


with open("results.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["map","algorithm","cost","nodes_expanded","runtime"])
    writer.writeheader()
    writer.writerows(results)

print("\nResults saved to results.csv")


print("\n--- Dynamic Replanning Test ---")
env_dyn = Environment("maps/dynamic_map.txt")
planner = Replanner(env_dyn, algorithm="astar")

replan_result = planner.run()
print("Initial Plan:", replan_result)

env_dyn.update_dynamic_obstacles(mode="random") 

replan_after_change = planner.replan(env_dyn)
print("After Replanning:", replan_after_change)

plot_path(env_dyn, replan_after_change["path"], title="Dynamic Map Replanned Path")