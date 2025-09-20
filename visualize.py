from environment import Environment
import matplotlib.pyplot as plt
import numpy as np

class Visualizer:
    def __init__(self, environment: Environment):
        self.env = environment

    def display(self, agent_pos=None, path=None, title="Grid"):
        grid = self.env.grid.copy()

        if path:
            for (i, j) in path:
                if (i, j) != self.env.start and (i, j) != self.env.goal:
                    grid[i][j] = 2  

        for i in range(self.env.grid.shape[0]):
            row_str = ""
            for j in range(self.env.grid.shape[1]):
                if (i, j) == self.env.start:
                    row_str += "S "
                elif (i, j) == self.env.goal:
                    row_str += "G "
                elif agent_pos and (i, j) == agent_pos:
                    row_str += "A "
                elif grid[i][j] == -1:
                    row_str += "X "
                elif grid[i][j] == -2:
                    row_str += "D "
                elif grid[i][j] == 2:
                    row_str += "o "
                else:
                    row_str += ". "
            print(row_str)
        print("\n")

    def plot(self, path=None, title="Path Visualization"):
        grid = self.env.grid.copy()
        plt.figure(figsize=(6, 6))
        plt.title(title)

        cmap = plt.cm.gray
        plt.imshow(grid == -1, cmap=cmap, origin="upper")

        if path:
            path_y, path_x = zip(*path)
            plt.plot(path_x, path_y, color="red", linewidth=2, marker="o")

        sy, sx = self.env.start
        gy, gx = self.env.goal
        plt.plot(sx, sy, "go", markersize=12, label="Start")
        plt.plot(gx, gy, "bo", markersize=12, label="Goal")

        plt.legend()
        plt.show()


def plot_path(env, path, title="Path Visualization"):
    viz = Visualizer(env)
    viz.plot(path=path, title=title)