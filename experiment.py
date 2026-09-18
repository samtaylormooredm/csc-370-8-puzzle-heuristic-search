import random

from astar import astar
from heuristic import h1, h2, h3
from random_boards import RANDOM_SEED, generate_experiment_boards


def run_experiments(experiment_boards):
    """Run A* with each heuristic on all experiment boards."""
    heuristics = {
        "h1": h1,
        "h2": h2,
        "h3": h3,
    }

    results = {}

    for depth, boards in experiment_boards.items():
        results[depth] = {}

        for heuristic_name, heuristic in heuristics.items():
            results[depth][heuristic_name] = []

            for board in boards:
                result = astar(board, heuristic)
                results[depth][heuristic_name].append(result)

    return results


def main():
    """Generate experiment boards and run A* with each heuristic."""
    random.seed(RANDOM_SEED)

    experiment_boards = generate_experiment_boards()
    results = run_experiments(experiment_boards)

    print(results[10]["h2"][0])


if __name__ == "__main__":
    main()