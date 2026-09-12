from board import Board

BOARD_SIZE = 3

def h1(board):
    """
    h1: the number of misplaced numbered tiles.

    The blank tile, represented by 0, is not counted.
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
    h2: the sum of the Manhattan distances of all numbered tiles
    from their goal positions.

    Manhattan distance:
        absolute row difference + absolute column difference
    """

    total_distance = 0

    for current_index, tile in enumerate(board.tiles):
        if tile == 0:
            continue

        current_row = current_index // 3
        current_col = current_index % 3

        goal_index = Board.GOAL.index(tile)
        goal_row = goal_index // 3
        goal_col = goal_index % 3

        tile_distance = (
            abs(current_row - goal_row)
            + abs(current_col - goal_col)
        )

        total_distance += tile_distance

    return total_distance


if __name__ == "__main__":
    goal = Board([0, 1, 2, 3, 4, 5, 6, 7, 8])

    one_move_away = Board([1, 0, 2, 3, 4, 5, 6, 7, 8])

    two_moves_away = Board([1, 2, 0, 3, 4, 5, 6, 7, 8])

    challenging_board = Board([7, 2, 4, 5, 0, 6, 8, 3, 1])

    print("Goal:")
    print(goal)
    print("h1:", h1(goal))  # Expected: 0
    print("h2:", h2(goal))  # Expected: 0

    print("\nOne move away:")
    print(one_move_away)
    print("h1:", h1(one_move_away))  # Expected: 1
    print("h2:", h2(one_move_away))  # Expected: 1

    print("\nTwo moves away:")
    print(two_moves_away)
    print("h1:", h1(two_moves_away))  # Expected: 2
    print("h2:", h2(two_moves_away))  # Expected: 2

    print("\nChallenging board:")
    print(challenging_board)
    print("h1:", h1(challenging_board))  # Expected: 8
    print("h2:", h2(challenging_board))  # Expected: 18