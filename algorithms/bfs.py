import time
from collections import deque

def bfs(environment):
    start, goal = environment.get_start_goal()
    frontier = deque([start])
    came_from = {start: None}
    nodes_expanded = 0

    start_time = time.time()

    while frontier:
        current = frontier.popleft()
        nodes_expanded += 1

        if current == goal:
            break

        for neighbor in environment.get_neighbors(current):
            if neighbor not in came_from:
                frontier.append(neighbor)
                came_from[neighbor] = current

    path = []
    cost = 0
    if goal in came_from:
        node = goal
        while node is not None:
            path.append(node)
            cost += environment.get_cost(node)
            node = came_from[node]
        path.reverse()

    runtime = time.time() - start_time
    return path, cost, nodes_expanded, runtime