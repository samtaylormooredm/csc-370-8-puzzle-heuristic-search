# CSC 370: A* Search for the 8-Puzzle

**Authors:** Samantha Taylormoore and Madeline Shi

This project implements A* search for the 8-puzzle and compares the effect of different admissible heuristics on search performance.

## Heuristics

- **h1:** Misplaced tiles
- **h2:** Manhattan distance
- **h3:** Manhattan distance with linear conflict

## Project Structure

- `board.py` — represents 8-puzzle board states and generates legal neighboring states
- `heuristic.py` — implements and tests the three heuristics
- `bfs.py` — generates solvable puzzle states by exact depth and samples boards for experiments
- `test_board.py` — basic tests for board behavior
- `a_star.py` — implements A* search

## Experiment

The project evaluates A* using 1,200 solvable 8-puzzle instances sampled across even solution depths from 2 through 24. Results are compared across the three heuristics using search cost and effective branching factor.

## Running

```bash
python heuristic.py
python bfs.py
python a_star.py