import numpy as np

class Environment:
    def __init__(self, filename):
        self.grid = []
        self.start = None
        self.goal = None
        self.load_map(filename)

    def load_map(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            row = []
            for j, val in enumerate(line.strip().split()):
                if val == "S":
                    self.start = (i, j)
                    row.append(1)   # start treated as cost=1
                elif val == "G":
                    self.goal = (i, j)
                    row.append(1)   # goal treated as cost=1
                elif val == "X":
                    row.append(-1)  # obstacle
                else:
                    row.append(int(val))
            self.grid.append(row)

        self.grid = np.array(self.grid)

    def display_grid(self):
        print("Grid Map:")
        print(self.grid)

    def get_start_goal(self):
        return self.start, self.goal

    # ✅ Step 3 utilities -----------------------------

    def in_bounds(self, pos):
        """Check if position is inside grid"""
        x, y = pos
        return 0 <= x < self.grid.shape[0] and 0 <= y < self.grid.shape[1]

    def is_passable(self, pos):
        """Check if cell is not an obstacle"""
        x, y = pos
        return self.grid[x][y] != -1

    def get_neighbors(self, pos):
        """Return 4-connected neighbors"""
        x, y = pos
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        valid_neighbors = [
            (nx, ny) for nx, ny in neighbors if self.in_bounds((nx, ny)) and self.is_passable((nx, ny))
        ]
        return valid_neighbors

    def get_cost(self, pos):
        """Return terrain cost of a cell"""
        x, y = pos
        return self.grid[x][y]

    # placeholder for step 5 (dynamic obstacles)
    def update_dynamic_obstacles(self, time_step):
        pass