from environment import Environment

if __name__ == "__main__":
    # Load one of the maps
    env = Environment("maps/small_map.txt")
    env.display_grid()
    start, goal = env.get_start_goal()
    print("Start:", start)
    print("Goal:", goal)