import heapq

def ucs(environment):
    start, goal = environment.get_start_goal()
    frontier = [(0, start, [start])]  # (cost, position, path)
    visited = {}
    nodes_expanded = 0

    while frontier:
        cost, pos, path = heapq.heappop(frontier)
        nodes_expanded += 1

        if pos == goal:
            return path, cost, nodes_expanded

        if pos in visited and visited[pos] <= cost:
            continue
        visited[pos] = cost

        for neighbor in environment.get_neighbors(pos):
            new_cost = cost + environment.get_cost(neighbor)
            heapq.heappush(frontier, (new_cost, neighbor, path + [neighbor]))

    return None, float("inf"), nodes_expanded