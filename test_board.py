from board import Board


# Test 1: create and print a board
board = Board([
    1, 2, 3,
    4, 0, 5,
    6, 7, 8
])

print("Board:")
print(board)


# Test 2: check blank location
print("\nBlank index:")
print(board.blank_index())   # should be 4


# Test 3: check goal state
goal = Board([
    0, 1, 2,
    3, 4, 5,
    6, 7, 8
])

print("\nGoal checks:")
print(board.is_goal())   # False
print(goal.is_goal())    # True


# Test 4: check neighbors
print("\nNeighbors:")
neighbors = board.get_neighbors()

print("Number of neighbors:", len(neighbors))  # should be 4

for neighbor in neighbors:
    print()
    print(neighbor)


# Test 5: blank in corner should only have 2 neighbors
corner_board = Board([
    0, 1, 2,
    3, 4, 5,
    6, 7, 8
])

print("\nCorner board neighbors:")
print(len(corner_board.get_neighbors()))  # should be 2


# Test 6: invalid board input
try:
    bad_board = Board([1, 2, 3])
except ValueError as error:
    print("\nCaught expected error:")
    print(error)