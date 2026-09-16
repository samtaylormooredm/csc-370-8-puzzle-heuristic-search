from board import Board

BOARD_SIZE = 3


def h1(board):
    """
    Calculate the number of misplaced numbered tiles.

    The blank tile, represented by 0, is not counted.

    Parameters
    ----------
    board : Board
        The 8-puzzle board to evaluate.

    Returns
    -------
    int
        The number of numbered tiles not in their goal positions.
    """
    misplaced = 0

    for index, tile in enumerate(board.tiles):
        if tile == 0:
            continue

        if tile != Board.GOAL[index]:
            misplaced += 1

    return misplaced


def h2(board):
    """
    Calculate the total Manhattan distance of all numbered tiles.

    The Manhattan distance for a tile is the sum of the absolute
    difference between its current and goal row and column positions.
    The blank tile, represented by 0, is not counted.

    Parameters
    ----------
    board : Board
        The 8-puzzle board to evaluate.

    Returns
    -------
    int
        The sum of the Manhattan distances of all numbered tiles.
    """
    total_distance = 0

    for current_index, tile in enumerate(board.tiles):
        if tile == 0:
            continue

        current_row = current_index // BOARD_SIZE
        current_col = current_index % BOARD_SIZE

        goal_index = Board.GOAL.index(tile)
        goal_row = goal_index // BOARD_SIZE
        goal_col = goal_index % BOARD_SIZE

        tile_distance = abs(current_row - goal_row) + abs(current_col - goal_col)

        total_distance += tile_distance

    return total_distance


def h3(board):
    """
    Calculate Manhattan distance with linear conflict.

    A linear conflict occurs when two tiles are in their goal row
    or goal column but appear in the opposite order from their
    goal positions. Each conflict adds 2 to the Manhattan distance.

    Parameters
    ----------
    board : Board
        The 8-puzzle board to evaluate.

    Returns
    -------
    int
        Manhattan distance plus 2 for each linear conflict.
    """
    manhattan_distance = h2(board)
    conflicts = 0

    # Check each row for linear conflicts.
    for row in range(BOARD_SIZE):
        conflicts += count_row_conflicts(board, row)

    # Check each column for linear conflicts.
    for col in range(BOARD_SIZE):
        conflicts += count_col_conflicts(board, col)

    return manhattan_distance + 2 * conflicts

def count_row_conflicts(board, row):
    """Count non-overlapping linear conflicts in one row."""
    conflicts = 0
    conflicting_tiles = set()

    start = row * BOARD_SIZE
    end = start + BOARD_SIZE

    row_tiles = board.tiles[start:end]

    for first_col in range(BOARD_SIZE):
        first_tile = row_tiles[first_col]

        if first_tile == 0:
            continue

        first_goal_index = Board.GOAL.index(first_tile)
        first_goal_row = first_goal_index // BOARD_SIZE
        first_goal_col = first_goal_index % BOARD_SIZE

        # The tile must belong in this row.
        if first_goal_row != row:
            continue

        for second_col in range(first_col + 1, BOARD_SIZE):
            second_tile = row_tiles[second_col]

            if second_tile == 0:
                continue

            second_goal_index = Board.GOAL.index(second_tile)
            second_goal_row = second_goal_index // BOARD_SIZE
            second_goal_col = second_goal_index % BOARD_SIZE

            # The second tile must also belong in this row.
            if second_goal_row != row:
                continue

            # Current order is first_tile before second_tile,
            # but goal order is reversed.
            if first_goal_col > second_goal_col:
                if (
                    first_tile not in conflicting_tiles
                    and second_tile not in conflicting_tiles
                ):
                    conflicts += 1
                    conflicting_tiles.add(first_tile)
                    conflicting_tiles.add(second_tile)

    return conflicts


def count_col_conflicts(board, col):
    """Count non-overlapping linear conflicts in one column."""
    conflicts = 0
    conflicting_tiles = set()

    col_tiles = [
        board.tiles[row * BOARD_SIZE + col]
        for row in range(BOARD_SIZE)
    ]

    for first_row in range(BOARD_SIZE):
        first_tile = col_tiles[first_row]

        if first_tile == 0:
            continue

        first_goal_index = Board.GOAL.index(first_tile)
        first_goal_row = first_goal_index // BOARD_SIZE
        first_goal_col = first_goal_index % BOARD_SIZE

        # The tile must belong in this column.
        if first_goal_col != col:
            continue

        for second_row in range(first_row + 1, BOARD_SIZE):
            second_tile = col_tiles[second_row]

            if second_tile == 0:
                continue

            second_goal_index = Board.GOAL.index(second_tile)
            second_goal_row = second_goal_index // BOARD_SIZE
            second_goal_col = second_goal_index % BOARD_SIZE

            # The second tile must also belong in this column.
            if second_goal_col != col:
                continue

            if first_goal_row > second_goal_row:
                if (
                    first_tile not in conflicting_tiles
                    and second_tile not in conflicting_tiles
                ):
                    conflicts += 1
                    conflicting_tiles.add(first_tile)
                    conflicting_tiles.add(second_tile)

    return conflicts

if __name__ == "__main__":
    goal = Board([0, 1, 2, 3, 4, 5, 6, 7, 8])

    one_move_away = Board([1, 0, 2, 3, 4, 5, 6, 7, 8])

    two_moves_away = Board([1, 2, 0, 3, 4, 5, 6, 7, 8])

    challenging_board = Board([7, 2, 4, 5, 0, 6, 8, 3, 1])

    row_conflict = Board([0, 2, 1, 3, 4, 5, 6, 7, 8])

    col_conflict = Board([0, 1, 2, 6, 4, 5, 3, 7, 8])

    print("Goal:")
    print(goal)
    print("h1:", h1(goal))  # Expected: 0
    print("h2:", h2(goal))  # Expected: 0
    print("h3:", h3(goal))  # Expected: 0

    print("\nOne move away:")
    print(one_move_away)
    print("h1:", h1(one_move_away))  # Expected: 1
    print("h2:", h2(one_move_away))  # Expected: 1
    print("h3:", h3(one_move_away))  # Expected: 1

    print("\nTwo moves away:")
    print(two_moves_away)
    print("h1:", h1(two_moves_away))  # Expected: 2
    print("h2:", h2(two_moves_away))  # Expected: 2
    print("h3:", h3(two_moves_away))  # Expected: 2

    print("\nChallenging board:")
    print(challenging_board)
    print("h1:", h1(challenging_board))  # Expected: 8
    print("h2:", h2(challenging_board))  # Expected: 18
    print("h3:", h3(challenging_board))

    print("\nRow conflict:")
    print(row_conflict)
    print("h1:", h1(row_conflict))  # Expected: 2
    print("h2:", h2(row_conflict))  # Expected: 2
    print("h3:", h3(row_conflict))  # Expected: 4

    print("\nColumn conflict:")
    print(col_conflict)
    print("h1:", h1(col_conflict))  # Expected: 2
    print("h2:", h2(col_conflict))  # Expected: 2
    print("h3:", h3(col_conflict))  # Expected: 4
