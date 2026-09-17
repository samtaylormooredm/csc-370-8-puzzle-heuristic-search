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