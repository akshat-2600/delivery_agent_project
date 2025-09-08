# from environment import Environment

# if __name__ == "__main__":
#     # Load one of the maps
#     env = Environment("maps/small_map.txt")
#     env.display_grid()
#     start, goal = env.get_start_goal()
#     print("Start:", start)
#     print("Goal:", goal)

from environment import Environment
from agent import Agent
from visualize import Visualizer

env = Environment("maps/dynamic_map.txt")
agent = Agent(env)
viz = Visualizer(env)

print("Initial Map:")
viz.display(agent.position)

# simulate moves
moves = [(0,1),(0,2)]
for step, move in enumerate(moves, start=1):
    agent.move(move)
    env.update_dynamic_obstacles(mode="deterministic")
    print(f"Step {step}:")
    viz.display(agent.position)