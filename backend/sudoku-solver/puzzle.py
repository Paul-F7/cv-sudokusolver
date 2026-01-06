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


def strings_to_puzzle(strings: List[str]) -> Puzzle:
    """
    Convert a list of strings to a puzzle representation.
    
    '?' represents an unknown cell (will contain all possible values 1..size)
    Digits represent known cells (will be a single-element list)
    
    Args:
        strings: List of strings, each representing a row of the puzzle
                 Example: ["??3?", "??2?", "?4??", "????"]
    
    Returns:
        A Puzzle where each cell is either a list of possible values
        or a single-element list for known values
    
    Example:
        >>> strings_to_puzzle(["??3", "?3?", "??2"])
        [[[1, 2, 3], [1, 2, 3], [3]], 
         [[1, 2, 3], [3], [1, 2, 3]], 
         [[1, 2, 3], [1, 2, 3], [2]]]
    """
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


def puzzle_to_string(puzzle: Puzzle) -> str:
    """
    Convert a puzzle back to a readable string format for display.
    
    Args:
        puzzle: A Puzzle matrix
    
    Returns:
        A multi-line string representation of the puzzle
    """
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


def is_solution(puzzle: Puzzle) -> bool:
    """
    Check if a puzzle is a complete solution (all cells are single numbers).
    
    Args:
        puzzle: A Puzzle matrix
    
    Returns:
        True if all cells contain exactly one value, False otherwise
    """
    for row in puzzle:
        for cell in row:
            if isinstance(cell, list) and len(cell) != 1:
                return False
    return True


def puzzle_to_solution(puzzle: Puzzle) -> Solution:
    """
    Convert a completed puzzle to a solution (extract single values).
    
    Args:
        puzzle: A Puzzle where all cells should be single-element lists or integers
    
    Returns:
        A Solution matrix of integers
    
    Raises:
        ValueError: If any cell has more than one possible value
    """
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
