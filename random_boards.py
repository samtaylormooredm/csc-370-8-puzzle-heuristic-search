import random

from board import Board

RANDOM_SEED = 100  # Arbitrary fixed seed used for reproducible experiments.


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
    pass


def generate_experiment_boards():
    """
    Generate the random boards used in the experiment.

    Returns
    -------
    dict
        Randomly generated boards grouped by solution depth.
    """
    pass


def main():
    """Generate and display random experiment boards."""
    random.seed(RANDOM_SEED)

    experiment_boards = generate_experiment_boards()

    # TODO: Display or summarize generated boards.


if __name__ == "__main__":
    main()