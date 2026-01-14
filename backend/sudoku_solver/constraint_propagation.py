"""
Constraint propagation for puzzle solving.

This module implements the 'remove-singles' technique:
When a cell has only one possible value (a "single"), that value
is removed from all other cells in the same row and column.
"""

from typing import List
from .puzzle import Puzzle, Cell
from .matrix_utils import any_satisfy, find_where
import copy

# Check if a cell is a single (list with exactly one element).
def is_single(cell: Cell) -> bool:
    return isinstance(cell, list) and len(cell) == 1

# Get the cell at the specified position.
def get_cell(puzzle: Puzzle, col: int, row: int) -> Cell:
    return puzzle[row][col]

# reate a new puzzle with the cell at (col, row) set to value.
def set_cell(puzzle: Puzzle, col: int, row: int, value: Cell) -> Puzzle:
    new_puzzle = copy.deepcopy(puzzle)
    new_puzzle[row][col] = value
    return new_puzzle

#  Remove a value from a cell's possibilities.
def remove_value_from_cell(cell: Cell, value: int) -> Cell:
    if isinstance(cell, list):
        return [v for v in cell if v != value]
    return cell

# Remove a value from all cells in the specified row.
def remove_from_row(puzzle: Puzzle, row: int, value: int) -> Puzzle:
    new_puzzle = copy.deepcopy(puzzle)
    new_puzzle[row] = [remove_value_from_cell(cell, value) for cell in new_puzzle[row]]
    return new_puzzle

# Remove a value from all cells in the specified column.
def remove_from_column(puzzle: Puzzle, col: int, value: int) -> Puzzle:
    new_puzzle = copy.deepcopy(puzzle)
    for row_idx in range(len(new_puzzle)):
        new_puzzle[row_idx][col] = remove_value_from_cell(
            new_puzzle[row_idx][col], value
        )
    return new_puzzle

# Convert a single-element list to just its value (e.g., [3] -> 3). (solved)
def make_cell_a_number(puzzle: Puzzle, col: int, row: int) -> Puzzle:
    cell = puzzle[row][col]
    if isinstance(cell, list) and len(cell) == 1:
        return set_cell(puzzle, col, row, cell[0])
    return puzzle

# Perform one iteration of singles removal.
def remove_singles_once(puzzle: Puzzle) -> Puzzle:
    # Check if there are any singles in the puzzle
    if not any_satisfy(is_single, puzzle):
        return puzzle
    
    # Find the first single
    col, row = find_where(is_single, puzzle)
    
    # Get the value from the single
    cell = get_cell(puzzle, col, row)
    value = cell[0]
    
    # Step 1: Make this cell a number (not a list)
    puzzle = make_cell_a_number(puzzle, col, row)
    
    # Step 2: Remove the value from all cells in the same row
    puzzle = remove_from_row(puzzle, row, value)
    
    # Step 3: Remove the value from all cells in the same column
    puzzle = remove_from_column(puzzle, col, value)
    
    return puzzle

#  Repeatedly apply singles removal until no more singles exist.
def remove_singles(puzzle: Puzzle) -> Puzzle:
    while any_satisfy(is_single, puzzle):
        puzzle = remove_singles_once(puzzle)
    return puzzle
