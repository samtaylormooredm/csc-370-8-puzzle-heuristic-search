# CSC 370: A* Search for the 8-Puzzle

**Authors:** Samantha Taylormoore and Madeline Shi

This project solves the 8-puzzle with A* search and compares three admissible heuristics. The goal board is `(0, 1, 2, 3, 4, 5, 6, 7, 8)`, where `0` is the blank tile.

## Heuristics

- **h1: Misplaced tiles** counts numbered tiles outside their goal positions.
- **h2: Manhattan distance** sums the row and column distances of numbered tiles from their goal positions.
- **h3: Manhattan distance with linear conflict** adds 2 for each counted non-overlapping pair of tiles in its goal row or column but in the wrong relative order.

## Project structure

| File | Purpose |
| --- | --- |
| `board.py` | Represents a board, checks the goal, and generates legal neighboring boards. |
| `heuristic.py` | Implements `h1`, `h2`, and `h3`. |
| `astar.py` | Implements A* and records solution cost, nodes expanded/generated, and runtime. |
| `random_boards.py` | Generates solvable boards at the requested solution depths. |
| `experiment.py` | Runs the comparison, calculates effective branching factors, and writes the CSV results. |
| `test_board.py`, `test_astar.py` | Check board behavior and A* on example boards. |
| `experiment_results.csv` | One row per board and heuristic (3,600 search results). |
| `experiment_summary.csv` | Mean metrics for each depth and heuristic (36 rows). |

## Experiment

The experiment samples 100 boards at each even solution depth from 2 through 24, for 1,200 boards total. `random_boards.py` makes random legal moves from the goal, avoids immediately reversing a move, and uses A* with Manhattan distance to keep only boards whose *shortest* solution matches the target depth. Boards can repeat within a depth.

`experiment.py` runs all three heuristics on every sampled board. It calculates an effective branching factor for each search from its generated node count and solution depth, then averages the search metrics by depth and heuristic. Generated nodes include the initial board; expanded nodes count boards whose neighbors are examined. Runtime is recorded in seconds in the detailed CSV and reported in milliseconds in the summary CSV.

## Running

From the project directory, use Python 3. No third-party packages are required.

```bash
python test_board.py
python test_astar.py
python experiment.py
```

The experiment uses a fixed random seed (`100`) for reproducible board sampling. Running it prints a summary and overwrites `experiment_results.csv` and `experiment_summary.csv` in the current directory. Runtime measurements can vary by machine and run.

## References

- Russell, S., & Norvig, P. *Artificial Intelligence: A Modern Approach* (3rd ed.).
- Hansson, O., Mayer, A., & Yung, M. (1992). Criticizing solutions to relaxed models yields powerful admissible heuristics. *Information Sciences, 63*(3), 207–227.
