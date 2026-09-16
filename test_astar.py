from board import Board
from heuristic import h1, h2
from astar import astar


# Test 1: A* should solve the goal board immediately.
goal = Board([0, 1, 2,
              3, 4, 5,
              6, 7, 8])

goal_result = astar(goal, h1)

print("Test 1: goal board")
print(goal)
print("Solution cost:", goal_result["solution_cost"])  # Should be 0, no moves are needed

assert goal_result["found"] is True
assert goal_result["solution_cost"] == 0


# Test 2: A* using h1 should find the correct shortest path.
two_moves_away = Board([1, 2, 0,
                        3, 4, 5,
                        6, 7, 8])

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


# Test 4: Compare h1 and h2 on the same board.
# Both must find the same optimal solution cost.
# Their numbers of expanded/generated nodes may be different.
print("\nTest 4: compare h1 and h2")
print("h1 solution cost:", h1_result["solution_cost"])
print("h2 solution cost:", h2_result["solution_cost"])
print("h1 nodes expanded:", h1_result["nodes_expanded"])
print("h2 nodes expanded:", h2_result["nodes_expanded"])

assert h1_result["solution_cost"] == h2_result["solution_cost"]


print("\nAll A* tests passed!")