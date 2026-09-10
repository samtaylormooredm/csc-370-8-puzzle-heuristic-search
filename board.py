import random


class Board:
    """
    
    """
    # 0 represents the empty space
    GOAL = (0, 1, 2,
            3, 4, 5,
            6, 7, 8)

    def __init__(self, tiles):
        """
        Tiles should contain the numbers 0-8 exactly once.
        0 represents the blank.
        """
        if len(tiles) != 9:
            raise ValueError("Board must contain exactly 9 positions.")

        if set(tiles) != set(range(9)):
            raise ValueError("Board must contain each value 0-8 exactly once.")

        # Store as tuple so Board states are immutable/hashable
        self.tiles = tuple(tiles)
