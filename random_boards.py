import random

from astar import astar
from board import Board
from heuristic import h2

RANDOM_SEED = 100  # Arbitrary fixed seed used for reproducible experiments.
SAMPLES_PER_DEPTH = 100
MAX_DEPTH = 24


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
        attempts = 0

        while len(experiment_boards[target_depth]) < SAMPLES_PER_DEPTH:
            attempts += 1

            board = generate_random_board(target_depth)
            result = astar(board, h2)

            # Only keep boards whose actual solution depth matches the target depth.
            if result["solution_cost"] == target_depth:
                experiment_boards[target_depth].append(board)

        print(
            f"Depth {target_depth}: "
            f"{SAMPLES_PER_DEPTH} boards generated in {attempts} attempts"
        )

    return experiment_boards


def main():
    """Generate experiment boards."""
    random.seed(RANDOM_SEED)

    generate_experiment_boards()

if __name__ == "__main__":
    main()