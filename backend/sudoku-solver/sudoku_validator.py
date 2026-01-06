"""
Sudoku-specific validation.

Sudoku is a Latin square with the additional constraint that
each 3×3 block must also contain no duplicate numbers.
"""

from typing import List
from puzzle import Solution

# Checks if list has any duplicate elements
def has_duplicates(lst: List[int]) -> bool:
    return len(lst) != len(set(lst))

# Extract all 3×3 blocks from a 9×9 Sudoku solution as flattened lists.
def get_sudoku_blocks(solution: Solution) -> List[List[int]]:
    blocks = []
    
    # Iterate through each 3×3 block
    for block_row in range(3):  # 3 rows of blocks
        for block_col in range(3):  # 3 columns of blocks
            block = []
            
            # Extract the 3×3 block
            for row in range(3):
                for col in range(3):
                    actual_row = block_row * 3 + row
                    actual_col = block_col * 3 + col
                    block.append(solution[actual_row][actual_col])
            
            blocks.append(block)
    
    return blocks

# checks if a solution is a valid sudoku solution
def is_valid_sudoku(solution: Solution) -> bool:
    blocks = get_sudoku_blocks(solution)
    
    # Check each block for duplicates
    for block in blocks:
        if has_duplicates(block):
            return False
    
    return True


# checks if a solution is a valid latin square
def is_valid_latin_square(solution: Solution) -> bool:
    n = len(solution)
    
    # Check rows
    for row in solution:
        if has_duplicates(row):
            return False
    
    # Check columns
    for col in range(n):
        column = [solution[row][col] for row in range(n)]
        if has_duplicates(column):
            return False
    
    return True

# Check if a solution is both a valid Latin square AND valid Sudoku.
def is_complete_sudoku(solution: Solution) -> bool:
    return is_valid_latin_square(solution) and is_valid_sudoku(solution)
