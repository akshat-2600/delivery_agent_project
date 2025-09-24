import os
import time

class ReplanLogger:
    def _init_(self, log_dir="results", log_file="replan_log.txt"):
        os.makedirs(log_dir, exist_ok=True)
        self.log_path = os.path.join(log_dir, log_file)

        # Start a fresh log file
        with open(self.log_path, "w") as f:
            f.write("=== Replanning Log ===\n")

    def log_replan(self, algorithm, old_path, new_path, cost, nodes, runtime):
        with open(self.log_path, "a") as f:
            f.write(f"\n[Time: {time.strftime('%H:%M:%S')}] Replanning triggered\n")
            f.write(f"Algorithm: {algorithm}\n")
            f.write(f"Previous path length: {len(old_path) if old_path else 0}\n")
            f.write(f"New path length: {len(new_path) if new_path else 0}\n")
            f.write(f"Path cost: {cost}\n")
            f.write(f"Nodes expanded: {nodes}\n")
            f.write(f"Runtime: {runtime:.6f} sec\n")
            f.write("-" * 40 + "\n")

        print(f"\n Replanning occurred using {algorithm}")
        print(f"   Old path length: {len(old_path) if old_path else 0}")
        print(f"   New path length: {len(new_path) if new_path else 0}")
        print(f"   Cost: {cost}, Nodes: {nodes}, Runtime: {runtime:.6f} sec")