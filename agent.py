from environment import Environment

class Agent:
    def __init__(self, environment: Environment):
        self.env = environment
        self.position = environment.start
        self.goal = environment.goal
        self.path = [self.position]  
        self.total_cost = 0

    def reset(self):
        self.position = self.env.start
        self.path = [self.position]
        self.total_cost = 0

    def move(self, next_pos):
        if next_pos in self.env.get_neighbors(self.position):
            self.position = next_pos
            self.path.append(next_pos)
            self.total_cost += self.env.get_cost(next_pos)
            return True
        return False

    def reached_goal(self):
        return self.position == self.goal

    def get_state(self):
        return {
            "position": self.position,
            "path": self.path,
            "total_cost": self.total_cost,
            "goal": self.goal
        }