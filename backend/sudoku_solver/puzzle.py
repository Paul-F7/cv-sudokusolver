"""
Puzzle representation and conversion utilities.

A Cell is either:
  - An integer (a solved cell)
  - A list of integers (possible values for an unsolved cell)

A Puzzle is a matrix of Cells.
A Solution is a matrix of integers.
"""

from typing import List, Union

Cell = Union[int, List[int]]
Puzzle = List[List[Cell]]
Solution = List[List[int]]

# Convert a list of strings to a puzzle representation.
def strings_to_puzzle(strings: List[str]) -> Puzzle:
    size = len(strings)
    all_values = list(range(1, size + 1))
    
    puzzle = []
    for string in strings:
        row = []
        for char in string:
            if char == '?':
                row.append(all_values.copy())
            else:
                # Convert digit character to integer
                digit = int(char)
                row.append([digit])
        puzzle.append(row)
    
    return puzzle

# Convert a puzzle back to a readable string format for display.
def puzzle_to_string(puzzle: Puzzle) -> str:
    lines = []
    for row in puzzle:
        row_str = []
        for cell in row:
            if isinstance(cell, list):
                if len(cell) == 1:
                    row_str.append(str(cell[0]))
                else:
                    row_str.append('{' + ','.join(map(str, cell)) + '}')
            else:
                row_str.append(str(cell))
        lines.append(' '.join(row_str))
    return '\n'.join(lines)

# Check if a puzzle is a complete solution (all cells are single numbers).
def is_solution(puzzle: Puzzle) -> bool:
    for row in puzzle:
        for cell in row:
            if isinstance(cell, list) and len(cell) != 1:
                return False
    return True

# Convert a completed puzzle to a solution (extract single values).
def puzzle_to_solution(puzzle: Puzzle) -> Solution:
    solution = []
    for row in puzzle:
        sol_row = []
        for cell in row:
            if isinstance(cell, list):
                if len(cell) != 1:
                    raise ValueError(f"Cell has multiple values: {cell}")
                sol_row.append(cell[0])
            else:
                sol_row.append(cell)
        solution.append(sol_row)
    return solution
