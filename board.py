class Board:
    """Represent a single state of the 8-puzzle board."""
    GOAL = (0, 1, 2,
            3, 4, 5,
            6, 7, 8)

    def __init__(self, tiles):
        """
        Initialize an 8-puzzle board with error handling. 
        Tiles should contain the numbers 0-8 exactly once, such
        that 0 represents the blank tile.
        """
        if len(tiles) != 9:
            raise ValueError("Board must contain exactly 9 positions.")

        if set(tiles) != set(range(9)):
            raise ValueError("Board must contain each value 0-8 exactly once.")

        self.tiles = tuple(tiles)

    def __str__(self):

        rows = []

        for i in range(0, 9, 3):
            row = self.tiles[i:i + 3]
            row_string = " ".join("_" if value == 0 else str(value) for value in row)
            rows.append(row_string)

        return "\n".join(rows)
    
    def is_goal(self):
        return self.tiles == Board.GOAL

    def blank_index(self):
        return self.tiles.index(0)
   
    def get_neighbors(self):
        blank = self.blank_index()

        # Convert the blank's 1D index into row and column coordinates.
        row = blank // 3
        col = blank % 3

        neighbors = []

        # Each tuple represents a change in row and column.
        moves = [
            (-1, 0),  # up
            (1, 0),   # down
            (0, -1),  # left
            (0, 1)    # right
        ]

        for row_change, col_change in moves:
            new_row = row + row_change
            new_col = col + col_change

            # Only allow moves that stay within the 3-by-3 board.
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_blank = new_row * 3 + new_col

                # Convert to a list temporarily so the values can be swapped.
                new_tiles = list(self.tiles)

                new_tiles[blank], new_tiles[new_blank] = (
                    new_tiles[new_blank],
                    new_tiles[blank]
                )

                # Create a new Board rather than modifying the current state.
                neighbors.append(Board(new_tiles))

        return neighbors
    