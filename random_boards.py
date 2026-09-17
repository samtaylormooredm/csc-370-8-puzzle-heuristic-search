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
    current = Board(Board.GOAL)

    for _ in range(num_moves):
        neighbors = current.get_neighbors()
        current = random.choice(neighbors)

    return current


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
    """Generate and display a random board."""
    random.seed(RANDOM_SEED)

    board = generate_random_board(10)

    print("Random board:")
    print(board)

if __name__ == "__main__":
    main()