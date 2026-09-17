import random

from astar import astar
from board import Board
from heuristic import h2

RANDOM_SEED = 100  # Arbitrary fixed seed used for reproducible experiments.
MAX_DEPTH = 6
SAMPLES_PER_DEPTH = 2


def generate_random_board(num_moves):
    """
    Generate a solvable board by making random legal moves from the goal.

    Parameters
    ----------
    num_moves : int
        Number of random moves to make from the goal state.

    Returns
    -------
    Board
        A randomized, solvable 8-puzzle board.
    """
    current = Board(Board.GOAL)
    previous = None

    for _ in range(num_moves):
        neighbors = current.get_neighbors()

        # Prevent immediately undoing the previous move.
        if previous is not None:
            neighbors = [
                neighbor
                for neighbor in neighbors
                if neighbor.tiles != previous.tiles
            ]

        previous = current
        current = random.choice(neighbors)

    return current


def generate_experiment_boards():
    """
    Generate random boards grouped by solution depth.

    Returns
    -------
    dict
        Randomly generated boards grouped by solution depth.
    """
    experiment_boards = {}

    for target_depth in range(2, MAX_DEPTH + 1, 2):
        experiment_boards[target_depth] = []

        while len(experiment_boards[target_depth]) < SAMPLES_PER_DEPTH:
            board = generate_random_board(target_depth)
            result = astar(board, h2)

            if result["solution_cost"] == target_depth:
                experiment_boards[target_depth].append(board)

    return experiment_boards


def main():
    """Generate and display experiment boards."""
    random.seed(RANDOM_SEED)

    experiment_boards = generate_experiment_boards()

    for depth, boards in experiment_boards.items():
        print(f"\nDepth {depth}:")

        for board in boards:
            print(board)
            print()


if __name__ == "__main__":
    main()