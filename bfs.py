from collections import deque
import random

from board import Board


MAX_DEPTH = 24
SAMPLES_PER_DEPTH = 100
RANDOM_SEED = 42


def generate_states_by_depth(max_depth=MAX_DEPTH):
    """
    Generate all reachable board states up to a maximum depth using BFS.

    Breadth-first search begins at the goal state, so the depth assigned
    to each board is its shortest distance from the goal.

    Parameters
    ----------
    max_depth : int, optional
        The maximum BFS depth to explore. Default is ``MAX_DEPTH``.

    Returns
    -------
    dict
        A dictionary mapping each depth to a list of ``Board`` objects
        at exactly that depth.
    dict
        A dictionary mapping each board's tile tuple to its shortest
        distance from the goal.
    """
    goal = Board(Board.GOAL)

    # Queue stores Board objects waiting to be processed.
    queue = deque([goal])

    # We use board.tiles as the dictionary key.
    distance = {
        goal.tiles: 0
    }

    # Group boards by their exact BFS distance.
    states_by_depth = {
        0: [goal]
    }

    while queue:
        current = queue.popleft()
        current_depth = distance[current.tiles]

        if current_depth >= max_depth:
            continue

        # Generate every board reachable in one legal move.
        for neighbor in current.get_neighbors():
            neighbor_key = neighbor.tiles

            # If we have not seen this board before, BFS has found
            # its shortest distance.
            if neighbor_key not in distance:
                neighbor_depth = current_depth + 1

                distance[neighbor_key] = neighbor_depth
                queue.append(neighbor)

                if neighbor_depth not in states_by_depth:
                    states_by_depth[neighbor_depth] = []

                states_by_depth[neighbor_depth].append(neighbor)

    return states_by_depth, distance


def sample_experiment_boards(
    states_by_depth,
    samples_per_depth=SAMPLES_PER_DEPTH
):
    """
    Randomly sample boards from each even search depth.

    Boards are sampled from depths 2, 4, ..., ``MAX_DEPTH``.
    Sampling is performed with replacement, so the same board may
    be selected more than once.

    Parameters
    ----------
    states_by_depth : dict
        A dictionary mapping each depth to a list of ``Board`` objects.
    samples_per_depth : int, optional
        The number of boards to sample from each depth. Default is
        ``SAMPLES_PER_DEPTH``.

    Returns
    -------
    dict
        A dictionary mapping each sampled depth to a list of randomly
        selected ``Board`` objects.

    Raises
    ------
    ValueError
        If no boards are available at one of the requested depths.
    """
    experiment_boards = {}

    # range(2, 25, 2) gives:
    # 2, 4, 6, ..., 24
    for depth in range(2, MAX_DEPTH + 1, 2):
        boards_at_this_depth = states_by_depth[depth]

        if len(boards_at_this_depth) == 0:
            raise ValueError(
                f"No boards found at depth {depth}."
            )

        # choices() samples with replacement.
        # The same board may appear more than once.
        experiment_boards[depth] = random.choices(
            boards_at_this_depth,
            k=samples_per_depth
        )

    return experiment_boards


def main():
    """
    Generate BFS states and sample boards for the experiment.

    The random seed is fixed so that the sampled boards are reproducible.
    """
    random.seed(RANDOM_SEED)

    print("Running BFS...")
    states_by_depth, distance = generate_states_by_depth()

    print("BFS finished.")
    print(f"Number of states stored: {len(distance)}")
    print()

    print("Number of states at each depth:")
    for depth in range(MAX_DEPTH + 1):
        number_of_states = len(states_by_depth.get(depth, []))
        print(f"Depth {depth}: {number_of_states}")

    experiment_boards = sample_experiment_boards(states_by_depth)

    print()
    print("Experiment samples:")
    total_samples = 0

    for depth in experiment_boards:
        number_of_samples = len(experiment_boards[depth])
        total_samples += number_of_samples
        print(f"Depth {depth}: selected {number_of_samples} boards")

    print()
    print(f"Total experiment boards: {total_samples}")


if __name__ == "__main__":
    main()