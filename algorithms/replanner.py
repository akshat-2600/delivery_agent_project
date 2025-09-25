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

    def run_once(self):
        start_time = time.time()

        if self.algorithm == "bfs":
            path, cost, nodes_expanded, runtime = bfs(self.env)
        elif self.algorithm == "ucs":
            path, cost, nodes_expanded, runtime = ucs(self.env)
        elif self.algorithm == "astar":
            path, cost, nodes_expanded, runtime = astar(self.env)
        else:
            raise ValueError("Invalid algorithm! Choose bfs, ucs, or astar.")

        runtime = round(time.time() - start_time, 6)
        return path, cost, nodes_expanded, runtime

    def replan(self, new_environment=None, old_path=None):
        if new_environment:
            self.env = new_environment

        path, cost, nodes, runtime = self.run_once()

        self.logger.log_replan(
            algorithm=self.algorithm.upper(),
            old_path=old_path,
            new_path=path,
            cost=cost,
            nodes=nodes,
            runtime=runtime
        )

        return path, cost, nodes, runtime

    @staticmethod
    def replan_agent(environment, algorithm="astar"):
        planner = Replanner(environment, algorithm)
        return planner.run_once()
