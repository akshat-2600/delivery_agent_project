from environment import Environment
from agent import Agent
from visualize import Visualizer, plot_path
from algorithms import bfs, ucs, astar, Replanner

maps = [
    "maps/small_map.txt",
    "maps/medium_map.txt",
    "maps/large_map.txt",
    "maps/dynamic_map.txt"
]

algorithms = {
    "BFS": bfs,
    "UCS": ucs,
    "ASTAR": astar
}

if __name__ == "__main__":
    for map_file in maps:
        print(f"\n=== Running on Map: {map_file} ===")
        env = Environment(map_file)
        agent = Agent(env)
        viz = Visualizer(env)

        print("Initial Grid:")
        viz.display(agent.position)

        for name, algo in algorithms.items():
            print(f"\n--- {name} ---")
            path, cost, nodes, runtime = algo(env)

            print(f"Path cost: {cost}")
            print(f"Nodes expanded: {nodes}")
            print(f"Runtime: {runtime:.6f} sec")

            viz.display(agent.position, path)
            plot_path(env, path, title=f"{name} on {map_file}")

        if "dynamic_map" in map_file:
            print(f"\n--- REPLANNER ---")
            planner = Replanner(env, algorithm="ASTAR")  
            path, cost, nodes, runtime = planner.replan()

            print(f"Path cost: {cost}")
            print(f"Nodes expanded: {nodes}")
            print(f"Runtime: {runtime:.6f} sec")

            viz.display(agent.position, path)
            plot_path(env, path, title=f"Replanner on {map_file}")



