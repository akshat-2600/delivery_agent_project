import time
from algorithms.bfs import bfs
from algorithms.ucs import ucs
from algorithms.astar import astar
from replan_logger import ReplanLogger

class Replanner:
    def __init__(self, environment, algorithm="astar"):
        self.env = environment
        self.algorithm = algorithm.lower()
        self.logger = ReplanLogger()

    def run(self):
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

    def replan(self, new_environment, old_path=None):
        self.env = new_environment
        result = self.run()
        self.logger.log_replan(
            algorithm=result["algorithm"],
            old_path=old_path,
            new_path=result["path"],
            cost=result["cost"],
            nodes=result["nodes_expanded"],
            runtime=result["runtime"]
        )
        return result
    
    def replan_agent(environment, algorithm="astar"):
        planner = Replanner(environment, algorithm)
        return planner.run()

