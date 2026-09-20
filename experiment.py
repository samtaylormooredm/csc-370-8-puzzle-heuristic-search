import random
import csv

from astar import astar
from heuristic import h1, h2, h3
from random_boards import RANDOM_SEED, generate_experiment_boards


def calculate_effective_branching_factor(nodes_generated, solution_depth):
    """
    Approximate the effective branching factor using binary search.
    """
    if solution_depth == 0:
        return 0.0

    low = 0.0
    high = max(1.0, float(nodes_generated))

    for _ in range(100):
        middle = (low + high) / 2

        estimated_nodes = sum(
            middle**level for level in range(solution_depth + 1)
        )

        if estimated_nodes < nodes_generated:
            low = middle
        else:
            high = middle

    return (low + high) / 2


def run_experiments(experiment_boards):
    """
    Run A* with each heuristic on all experiment boards.

    Parameters
    ----------
    experiment_boards : dict
        Dictionary mapping solution depths to lists of Board objects.

    Returns
    -------
    dict
        Nested dictionary containing A* results for each depth and heuristic.
    """
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
                result["effective_branching_factor"] = (
                    calculate_effective_branching_factor(
                        result["nodes_generated"],
                        result["solution_cost"],
                    )
                )

                results[depth][heuristic_name].append(result)

    return results


def summarize_results(results):
    """Calculate average performance at each depth."""
    summary = []

    for depth, depth_results in results.items():
        for heuristic_name, heuristic_results in depth_results.items():
            number_of_results = len(heuristic_results)

            average_solution_cost = sum(
                result["solution_cost"] for result in heuristic_results
            ) / number_of_results

            average_nodes_expanded = sum(
                result["nodes_expanded"] for result in heuristic_results
            ) / number_of_results

            average_nodes_generated = sum(
                result["nodes_generated"] for result in heuristic_results
            ) / number_of_results

            average_runtime_ms = (
                sum(
                    result["runtime_seconds"]
                    for result in heuristic_results
                )
                / number_of_results
                * 1000
            )

            average_branching_factor = sum(
                result["effective_branching_factor"]
                for result in heuristic_results
            ) / number_of_results

            summary.append(
                {
                    "depth": depth,
                    "heuristic": heuristic_name,
                    "samples": number_of_results,
                    "average_solution_cost": average_solution_cost,
                    "average_nodes_expanded": average_nodes_expanded,
                    "average_nodes_generated": average_nodes_generated,
                    "average_runtime_ms": average_runtime_ms,
                    "average_branching_factor": average_branching_factor,
                }
            )

    return summary


def create_detailed_rows(results):
    """Create one CSV row for every A* search."""
    rows = []

    for depth, depth_results in results.items():
        for heuristic_name, heuristic_results in depth_results.items():
            for result in heuristic_results:
                rows.append(
                    {
                        "depth": depth,
                        "heuristic": heuristic_name,
                        **result,
                    }
                )

    return rows


def save_csv(filename, rows):
    """Save result dictionaries to a CSV file."""
    with open(filename, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=rows[0].keys(),
        )

        writer.writeheader()
        writer.writerows(rows)


def main():
    """Generate experiment boards and run A* with each heuristic."""
    random.seed(RANDOM_SEED)

    experiment_boards = generate_experiment_boards()
    results = run_experiments(experiment_boards)

    summary = summarize_results(results)
    detailed_rows = create_detailed_rows(results)

    save_csv("experiment_results.csv", detailed_rows)
    save_csv("experiment_summary.csv", summary)

    for row in summary:
        print(
            f"Depth {row['depth']:2} | "
            f"{row['heuristic']} | "
            f"expanded: {row['average_nodes_expanded']:8.2f} | "
            f"generated: {row['average_nodes_generated']:8.2f} | "
            f"runtime: {row['average_runtime_ms']:8.3f} ms | "
            f"b*: {row['average_branching_factor']:.4f}"
        )

    print("\nExperiment completed.")
    print(f"Detailed rows: {len(detailed_rows)}")
    print(f"Summary rows: {len(summary)}")


if __name__ == "__main__":
    main()
