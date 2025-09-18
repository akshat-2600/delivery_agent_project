from collections import deque

def bfs(environment):
    start, goal = environment.get_start_goal()
    queue = deque([(start, [start])])  # (position, path)
    visited = set([start])
    nodes_expanded = 0

    while queue:
        pos, path = queue.popleft()
        nodes_expanded += 1

        if pos == goal:
            return path, len(path)-1, nodes_expanded  # cost = steps

        for neighbor in environment.get_neighbors(pos):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None, float("inf"), nodes_expanded