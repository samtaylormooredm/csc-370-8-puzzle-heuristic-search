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

        # Store the board as an immutable tuple.
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
        # Represent as psuedocode for now
            # locate blank
            # determine blank row and column

            # for each direction (up, down, left, right):
            #     calculate destination position

            #     if destination is valid:
            #         copy board
            #         swap blank with destination tile
            #         add resulting board to neighbors

            # return neighbors
        return 0
    
    
