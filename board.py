class Board:
    """Represent a single state of the 8-puzzle board."""

    GOAL = (0, 1, 2, 3, 4, 5, 6, 7, 8)

    def __init__(self, tiles):
        """
        Initialize an 8-puzzle board.

        Parameters
        ----------
        tiles : iterable of int
            The 9 board values in row-major order. Values must contain each
            integer from 0 through 8 exactly once. The value 0 represents
            the blank tile.

        Raises
        ------
        ValueError
            If the board does not contain exactly 9 values or does not contain
            each value from 0 through 8 exactly once.
        """
        if len(tiles) != 9:
            raise ValueError("Board must contain exactly 9 positions.")

        if set(tiles) != set(range(9)):
            raise ValueError("Board must contain each value 0-8 exactly once.")

        self.tiles = tuple(tiles)

    def __str__(self):
        """
        Return the board as a formatted 3-by-3 string.

        Returns
        -------
        str
            String representation of the board, with 0 displayed as "_".
        """
        rows = []

        for i in range(0, 9, 3):
            row = self.tiles[i : i + 3]
            row_string = " ".join("_" if value == 0 else str(value) for value in row)
            rows.append(row_string)

        return "\n".join(rows)

    def is_goal(self):
        """
        Check whether the board is the goal state.

        Returns
        -------
        bool
            True if the board matches the goal state, otherwise False.
        """
        return self.tiles == Board.GOAL

    def blank_index(self):
        """
        Return the index of the blank tile.

        Returns
        -------
        int
            Index of the blank tile in the flattened board.
        """
        return self.tiles.index(0)

    def get_neighbors(self):
        """
        Generate all board states reachable in one legal move.

        Returns
        -------
        list of Board
            Neighboring board states produced by moving the blank up, down,
            left, or right when legal.
        """
        blank = self.blank_index()

        # Convert the blank's 1D index into row and column coordinates.
        row = blank // 3
        col = blank % 3

        neighbors = []

        # Each tuple represents a change in row and column.
        moves = [
            (-1, 0),  # up
            (1, 0),  # down
            (0, -1),  # left
            (0, 1),  # right
        ]

        for row_change, col_change in moves:
            new_row = row + row_change
            new_col = col + col_change

            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_blank = new_row * 3 + new_col

                # Convert to a list temporarily so the values can be swapped.
                new_tiles = list(self.tiles)

                new_tiles[blank], new_tiles[new_blank] = (
                    new_tiles[new_blank],
                    new_tiles[blank],
                )

                # Create a new Board rather than modifying the current state.
                neighbors.append(Board(new_tiles))

        return neighbors
