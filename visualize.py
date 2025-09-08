from environment import Environment

class Visualizer:
    def __init__(self, environment: Environment):
        self.env = environment

    def display(self, agent_pos=None):
        for i in range(self.env.grid.shape[0]):
            row_str = ""
            for j in range(self.env.grid.shape[1]):
                if (i, j) == self.env.start:
                    row_str += "S "
                elif (i, j) == self.env.goal:
                    row_str += "G "
                elif agent_pos and (i, j) == agent_pos:
                    row_str += "A "
                elif self.env.grid[i][j] == -1:
                    row_str += "X "
                elif self.env.grid[i][j] == -2:
                    row_str += "D "
                else:
                    row_str += ". "
            print(row_str)
        print("\n")