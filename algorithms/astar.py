import heapq

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(environment):
    start, goal = environment.get_start_goal()
    frontier = [(manhattan(start, goal), 0, start, [start])]  # (f, g, pos, path)
    visited = {}
    nodes_expanded = 0

    while frontier:
        f, g, pos, path = heapq.heappop(frontier)
        nodes_expanded += 1

        if pos == goal:
            return path, g, nodes_expanded

        if pos in visited and visited[pos] <= g:
            continue
        visited[pos] = g

        for neighbor in environment.get_neighbors(pos):
            new_g = g + environment.get_cost(neighbor)
            h = manhattan(neighbor, goal)
            heapq.heappush(frontier, (new_g + h, new_g, neighbor, path + [neighbor]))

    return None, float("inf"), nodes_expanded