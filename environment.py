import numpy as np
import random

class Environment:
    def __init__(self, filename):
        self.grid = []
        self.start = None
        self.goal = None
        self.dynamic_obstacles = []  
        self.time_step = 0
        self.load_map(filename)

    def load_map(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            row = []
            for j, val in enumerate(line.strip().split()):
                if val == "S":
                    self.start = (i, j)
                    row.append(1) 
                elif val == "G":
                    self.goal = (i, j)
                    row.append(1)  
                elif val == "X":
                    row.append(-1)  
                elif val == "D":
                    self.dynamic_obstacles.append({
                        "pos": (i, j),
                        "path": [(i, j)],  
                        "index": 0
                    })
                    row.append(-2)  
                else:
                    row.append(int(val))
            self.grid.append(row)

        self.grid = np.array(self.grid)

    def get_start_goal(self):
        return self.start, self.goal

    def in_bounds(self, pos):
        x, y = pos
        return 0 <= x < self.grid.shape[0] and 0 <= y < self.grid.shape[1]

    def is_passable(self, pos):
        x, y = pos
        return self.grid[x][y] > 0

    def get_neighbors(self, pos):
        x, y = pos
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        valid = [(nx, ny) for nx, ny in neighbors
                 if self.in_bounds((nx, ny)) and self.is_passable((nx, ny))]
        return valid

    def get_cost(self, pos):
        x, y = pos
        return self.grid[x][y] if self.grid[x][y] > 0 else float('inf')

    def update_dynamic_obstacles(self, mode="deterministic"):
        self.time_step += 1

        for obs in self.dynamic_obstacles:
            x, y = obs["pos"]
            self.grid[x][y] = 1  

        for obs in self.dynamic_obstacles:
            if mode == "deterministic":
                directions = [(-1,0), (0,1), (1,0), (0,-1)]
                dx, dy = directions[self.time_step % len(directions)]
                new_x, new_y = obs["pos"][0] + dx, obs["pos"][1] + dy
                if self.in_bounds((new_x, new_y)) and self.grid[new_x][new_y] > 0:
                    obs["pos"] = (new_x, new_y)

            elif mode == "random":
                neighbors = self.get_neighbors(obs["pos"])
                if neighbors:
                    obs["pos"] = random.choice(neighbors)

            x, y = obs["pos"]
            self.grid[x][y] = -2