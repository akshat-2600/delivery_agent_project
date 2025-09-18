import time
from algorithms.bfs import bfs
from algorithms.ucs import ucs
from algorithms.astar import astar

class Replanner:
    def _init_(self, environment, algorithm="astar"):
        self.env = environment
        self.algorithm = algorithm.lower()

    def run(self):
        """Run the chosen algorithm and return results"""
        start_time = time.time()

        if self.algorithm == "bfs":
            path, cost, nodes_expanded = bfs(self.env)
        elif self.algorithm == "ucs":
            path, cost, nodes_expanded = ucs(self.env)
        elif self.algorithm == "astar":
            path, cost, nodes_expanded = astar(self.env)
        else:
            raise ValueError("Invalid algorithm! Choose bfs, ucs, or astar.")

        runtime = round(time.time() - start_time, 6)

        return {
            "algorithm": self.algorithm.upper(),
            "path": path,
            "cost": cost,
            "nodes_expanded": nodes_expanded,
            "runtime": runtime
        }

    def replan(self, new_environment):
        """Replan in case the environment changes dynamically"""
        self.env = new_environment
        return self.run()
    
    def replan_agent(environment, algorithm="astar"):
        planner = Replanner(environment, algorithm)
        return planner.run()