# Missionaries and Cannibals Problem with A*

## Problem Description
The Missionaries and Cannibals problem involves transporting a group of missionaries and cannibals from the left bank to the right bank of a river using a boat with limited capacity. The key constraint is that **cannibals must never outnumber missionaries on either bank** (unless there are no missionaries present on that bank).

## Implementation
The solution uses the A* search algorithm to find the most efficient path to the goal state. The implementation consists of three main components:

### `state.py`
- Defines the problem state containing:
  - Number of missionaries/cannibals on each bank
  - Boat position
- Implements heuristic evaluation using:  
```python
minimum_required_trips = (2 * (left_m + left_c) - 1) // (boat_capacity - 1)
```
- Applies penalties for invalid states

### `a_star.py`
- Implements the A* algorithm with:
  - Priority queue for open states
  - Visited state tracking
  - Path reconstruction
- Returns optimal solution path

### `main.py`
- Executes the algorithm with configurable parameters:
  ```python
  N = 3  # Number of missionaries/cannibals
  M = 2  # Boat capacity
  K = 50 # Max allowed trips
  ```
## Heuristic Function
The heuristic combines:
  1. Minimum required trips based on boat capacity
  2. Penalty system for:
    - Invalid states (cannibals > missionaries)
    - Boat capacity violations
    - Negative population counts
Key design choice: Removed explicit constraint checking and instead used penalty terms in heuristic evaluation.

## Execution
To run the solution:
```bash
python main.py
```
