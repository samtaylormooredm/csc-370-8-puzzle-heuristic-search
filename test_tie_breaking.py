import random

from astar import astar
from heuristic import h2
from random_boards import RANDOM_SEED, generate_experiment_boards


def main():
    random.seed(RANDOM_SEED)

    experiment_boards = generate_experiment_boards()
    boards = experiment_boards[24]

    methods = ["small_g", "fifo", "large_g"]

    for method in methods:
        generated = []
        expanded = []

        for board in boards:
            result = astar(board, h2, tie_breaking=method)

            generated.append(result["nodes_generated"])
            expanded.append(result["nodes_expanded"])

        avg_generated = sum(generated) / len(generated)
        avg_expanded = sum(expanded) / len(expanded)

        print(
            f"{method:8} | "
            f"generated: {avg_generated:.2f} | "
            f"expanded: {avg_expanded:.2f}"
        )


if __name__ == "__main__":
    main()