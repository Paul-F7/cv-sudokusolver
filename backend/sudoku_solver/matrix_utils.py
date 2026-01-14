"""
Matrix utility functions for working with 2D lists.

These functions operate on matrices (list of lists) and provide
predicate checking and element finding functionality.
"""

from typing import List, Callable, Tuple, TypeVar, Any

T = TypeVar('T')
Matrix = List[List[T]]

# Check if every element in the matrix satisfies the predicate.
def all_satisfy(pred: Callable[[T], bool], matrix: Matrix[T]) -> bool:
    for row in matrix:
        for elem in row:
            if not pred(elem):
                return False
    return True

# Check if any element in the matrix satisfies the predicate.
def any_satisfy(pred: Callable[[T], bool], matrix: Matrix[T]) -> bool:
    for row in matrix:
        for elem in row:
            if pred(elem):
                return True
    return False

# Find the (column, row) coordinates of the first element satisfying the predicate.
def find_where(pred: Callable[[T], bool], matrix: Matrix[T]) -> Tuple[int, int]:
    for row_idx, row in enumerate(matrix):
        for col_idx, elem in enumerate(row):
            if pred(elem):
                return (col_idx, row_idx)
    
    raise ValueError("No element in matrix satisfies the predicate")
