from heapq import heappop, heappush
from itertools import count
from time import perf_counter


def astar(start_board, heuristic):
    """
    Solve an 8-puzzle using A* search.

    Parameters
    ----------
    start_board : Board
        Initial board configuration to solve.
    heuristic : callable
        Heuristic function used to estimate the remaining cost to the goal.

    Returns
    -------
    dict
        Search results containing whether a solution was found, the solution
        cost, number of nodes expanded and generated, and runtime in seconds.
    """

    start_time = perf_counter()
    frontier = []
    tie_breaker = count()

    start_g = 0
    start_f = start_g + heuristic(start_board)

    heappush(frontier, (start_f, start_g, next(tie_breaker), start_board))

    best_g = {start_board.tiles: 0}

    nodes_expanded = 0
    nodes_generated = 1  # The start board already exists in the frontier.

    while frontier:
        f_value, g_value, _, current_board = heappop(frontier)

        # Ignore an old/worse copy of this board in the priority queue.
        if g_value != best_g[current_board.tiles]:
            continue

        # A* removes the goal from the frontier: solution found.
        if current_board.is_goal():
            end_time = perf_counter()

            return {
                "found": True,
                "solution_cost": g_value,
                "nodes_expanded": nodes_expanded,
                "nodes_generated": nodes_generated,
                "runtime_seconds": end_time - start_time,
            }

        nodes_expanded += 1

        for neighbor in current_board.get_neighbors():
            new_g = g_value + 1
            neighbor_key = neighbor.tiles

            if neighbor_key not in best_g or new_g < best_g[neighbor_key]:
                best_g[neighbor_key] = new_g

                new_f = new_g + heuristic(neighbor)

                heappush(frontier, (new_f, new_g, next(tie_breaker), neighbor))

                nodes_generated += 1

    end_time = perf_counter()

    return {
        "found": False,
        "solution_cost": None,
        "nodes_expanded": nodes_expanded,
        "nodes_generated": nodes_generated,
        "runtime_seconds": end_time - start_time,
    }
