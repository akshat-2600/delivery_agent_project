import numpy as np

class Environment:
    def _init_(self, filename):
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
                    row.append(1)   # start = cost 1
                elif val == "G":
                    self.goal = (i, j)
                    row.append(1)   # goal = cost 1
                elif val == "X":
                    row.append(-1)  # static obstacle
                else:
                    row.append(int(val))  # terrain cost
            self.grid.append(row)

        self.grid = np.array(self.grid)

    def display_grid(self):
        print("Grid Map:")
        print(self.grid)

    def get_start_goal(self):
        return self.start, self.goal