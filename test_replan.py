from environment import Environment
from algorithms import Replanner

# Load a map
env = Environment("maps/small_map.txt")

# Run A*
planner = Replanner(env, algorithm="astar")
result = planner.run()

print(result)

# Suppose the map changes → run replanning
new_env = Environment("maps/small_map_changed.txt")
replan_result = planner.replan(new_env)

print("After replanning:", replan_result)