"""
Latin square solver using backtracking search with constraint propagation.

This module implements a depth-first search algorithm that:
1. Applies constraint propagation (remove-singles)
2. Picks an unsolved cell and tries each possible value
3. Recursively solves the resulting puzzles
4. Validates solutions with a custom predicate
"""

from typing import List, Callable, Optional
from .puzzle import Puzzle, Solution, puzzle_to_solution
from .constraint_propagation import remove_singles, set_cell
from .matrix_utils import any_satisfy, find_where
import copy

# Check if a cell is still a list (unsolved).
def is_list_cell(cell) -> bool:
    return isinstance(cell, list)

# Check if a cell is an empty list (invalid state).
def is_empty_cell(cell) -> bool:
    return isinstance(cell, list) and len(cell) == 0

# Check if the puzzle still has cells with multiple possibilities.
def has_unsolved_cells(puzzle: Puzzle) -> bool:
    return any_satisfy(is_list_cell, puzzle)

# Check if the puzzle is in an invalid state. (zero possibilities)
def is_invalid(puzzle: Puzzle) -> bool:
    return any_satisfy(is_empty_cell, puzzle)

# generate all possible next states (neighbours) from the current puzzle.
def get_neighbours(puzzle: Puzzle) -> List[Puzzle]:
    # If puzzle is invalid or already solved, no neighbours
    if is_invalid(puzzle) or not has_unsolved_cells(puzzle):
        return []
    
    # Find an unsolved cell (one with multiple possibilities)
    col, row = find_where(is_list_cell, puzzle)
    
    # Get the possible values for this cell
    options = puzzle[row][col]
    
    # Create one neighbour for each option
    neighbours = []
    for option in options:
        # Create a new puzzle with this cell set to this option
        new_puzzle = set_cell(puzzle, col, row, [option])
        # Apply constraint propagation
        new_puzzle = remove_singles(new_puzzle)
        neighbours.append(new_puzzle)
    
    return neighbours

# Try to find a solution in a list of puzzle states.
def find_solution_in_list(
    puzzles: List[Puzzle],
    predicate: Callable[[Solution], bool]
) -> Optional[Solution]:
    for puzzle in puzzles:
        solution = solve_latin(predicate, puzzle)
        if solution is not None:
            return solution
    return None

# Solve a Latin square puzzle using backtracking search.
    
def solve_latin(
    predicate: Callable[[Solution], bool],
    puzzle: Puzzle
) -> Optional[Solution]:
    # Apply constraint propagation first
    puzzle = remove_singles(puzzle)
    
    # Base case 1: Puzzle is solved
    if not has_unsolved_cells(puzzle):
        solution = puzzle_to_solution(puzzle)
        if predicate(solution):
            return solution
        else:
            return None
    
    # Base case 2: Puzzle is invalid (some cell has no possibilities)
    if is_invalid(puzzle):
        return None
    
    # Recursive case: Try all possibilities for one unsolved cell
    neighbours = get_neighbours(puzzle)
    return find_solution_in_list(neighbours, predicate)


# Predicate helper functions

def always_true(solution: Solution) -> bool:
    return True


def always_false(solution: Solution) -> bool:
    return False


def diagonal_has_2(solution: Solution) -> bool:
    for i in range(len(solution)):
        if solution[i][i] == 2:
            return True
    return False
