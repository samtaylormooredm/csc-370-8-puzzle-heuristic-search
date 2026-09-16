from astar import astar
from board import Board
from heuristic import h1, h2, h3

# Test 1: A* should solve the goal board immediately.
# The solution cost should be 0 because no moves are needed.
goal = Board([0, 1, 2, 3, 4, 5, 6, 7, 8])

goal_result = astar(goal, h1)

print("Test 1: goal board")
print(goal)
print("Solution cost:", goal_result["solution_cost"])  # Should be 0

assert goal_result["found"] is True
assert goal_result["solution_cost"] == 0


# This board is exactly 2 moves away from the goal.
two_moves_away = Board([1, 2, 0, 3, 4, 5, 6, 7, 8])


# Test 2: A* using h1 should find the correct shortest path.
h1_result = astar(two_moves_away, h1)

print("\nTest 2: two-moves-away board using h1")
print(two_moves_away)
print("Solution cost:", h1_result["solution_cost"])  # Should be 2
print("Nodes expanded:", h1_result["nodes_expanded"])
print("Nodes generated:", h1_result["nodes_generated"])

assert h1_result["found"] is True
assert h1_result["solution_cost"] == 2


# Test 3: A* using h2 should also find the correct shortest path.
h2_result = astar(two_moves_away, h2)

print("\nTest 3: two-moves-away board using h2")
print(two_moves_away)
print("Solution cost:", h2_result["solution_cost"])  # Should be 2
print("Nodes expanded:", h2_result["nodes_expanded"])
print("Nodes generated:", h2_result["nodes_generated"])

assert h2_result["found"] is True
assert h2_result["solution_cost"] == 2


# Test 4: A* using h3 should also find the correct shortest path.
# h3 is Manhattan distance plus linear conflict.
h3_result = astar(two_moves_away, h3)

print("\nTest 4: two-moves-away board using h3")
print(two_moves_away)
print("Solution cost:", h3_result["solution_cost"])  # Should be 2
print("Nodes expanded:", h3_result["nodes_expanded"])
print("Nodes generated:", h3_result["nodes_generated"])

assert h3_result["found"] is True
assert h3_result["solution_cost"] == 2


# Test 5: Check A* on a board where h3 detects a linear conflict.
# For this board, h3 should be stronger than h2.
linear_conflict_board = Board([0, 1, 2, 5, 4, 8, 3, 6, 7])

print("\nTest 5: linear-conflict board")
print(linear_conflict_board)
print("h2 value:", h2(linear_conflict_board))  # Should be 6
print("h3 value:", h3(linear_conflict_board))  # Should be 8

assert h2(linear_conflict_board) == 6
assert h3(linear_conflict_board) == 8
assert h3(linear_conflict_board) > h2(linear_conflict_board)

linear_h1_result = astar(linear_conflict_board, h1)
linear_h2_result = astar(linear_conflict_board, h2)
linear_h3_result = astar(linear_conflict_board, h3)

# Different heuristics may explore different numbers of nodes,
# but all admissible heuristics must find the same optimal cost.
assert linear_h1_result["solution_cost"] == linear_h2_result["solution_cost"]
assert linear_h2_result["solution_cost"] == linear_h3_result["solution_cost"]

print("All three heuristics found the same solution cost:")
print("Solution cost:", linear_h3_result["solution_cost"])
print("h1 nodes expanded:", linear_h1_result["nodes_expanded"])
print("h2 nodes expanded:", linear_h2_result["nodes_expanded"])
print("h3 nodes expanded:", linear_h3_result["nodes_expanded"])


print("\nAll A* tests passed!")
