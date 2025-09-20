import heapq
import time

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(environment):
    start, goal = environment.get_start_goal()
    frontier = [(0, start)]
    came_from = {start: None}
    cost_so_far = {start: 0}
    nodes_expanded = 0

    start_time = time.time()

    while frontier:
        _, current = heapq.heappop(frontier)
        nodes_expanded += 1

        if current == goal:
            break

        for neighbor in environment.get_neighbors(current):
            new_cost = cost_so_far[current] + environment.get_cost(neighbor)
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current

    path = []
    cost = float("inf")
    if goal in came_from:
        path = []
        node = goal
        cost = 0
        while node is not None:
            path.append(node)
            cost += environment.get_cost(node)
            node = came_from[node]
        path.reverse()

    runtime = time.time() - start_time
    return path, cost, nodes_expanded, runtime