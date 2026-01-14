"""
Main script demonstrating the Sudoku/Latin Square solver.

This file contains examples and tests from the original Racket code.
"""

from puzzle import strings_to_puzzle, puzzle_to_string, puzzle_to_solution
from constraint_propagation import remove_singles
from solver import solve_latin, always_true, diagonal_has_2, always_false
from sudoku_validator import is_valid_sudoku
from matrix_utils import all_satisfy, any_satisfy, find_where


def print_puzzle(puzzle, title="Puzzle"):
    """Pretty print a puzzle."""
    print(f"\n{title}:")
    print(puzzle_to_string(puzzle))


def print_solution(solution, title="Solution"):
    """Pretty print a solution."""
    print(f"\n{title}:")
    for row in solution:
        print(' '.join(map(str, row)))


def test_matrix_utils():
    """Test the matrix utility functions."""
    print("\n" + "="*60)
    print("TESTING MATRIX UTILITIES")
    print("="*60)
    
    # Test all_satisfy
    matrix1 = [[2, 3, 4], [5, 6, 7]]
    matrix2 = [[2, 3, 4], [5, 'six', 7]]
    
    print("\nTesting all_satisfy with integers:")
    print(f"Matrix: {matrix1}")
    print(f"All integers? {all_satisfy(lambda x: isinstance(x, int), matrix1)}")  # Should be True
    
    print(f"\nMatrix: {matrix2}")
    print(f"All integers? {all_satisfy(lambda x: isinstance(x, int), matrix2)}")  # Should be False
    
    # Test any_satisfy
    print("\nTesting any_satisfy with symbols:")
    print(f"Matrix: {matrix1}")
    print(f"Any strings? {any_satisfy(lambda x: isinstance(x, str), matrix1)}")  # Should be False
    
    print(f"\nMatrix: {matrix2}")
    print(f"Any strings? {any_satisfy(lambda x: isinstance(x, str), matrix2)}")  # Should be True
    
    # Test find_where
    where_matrix = [[1, 2, 3, 4],
                    [4, 5, [3, 6], [1, 2]],
                    [[7], 8, 9, []]]
    
    print(f"\nTesting find_where:")
    print(f"Matrix: {where_matrix}")
    print(f"First list: {find_where(lambda x: isinstance(x, list), where_matrix)}")  # (2, 1)
    print(f"First empty: {find_where(lambda x: isinstance(x, list) and len(x) == 0, where_matrix)}")  # (3, 2)
    print(f"First integer: {find_where(lambda x: isinstance(x, int), where_matrix)}")  # (0, 0)


def test_strings_to_puzzle():
    """Test puzzle string conversion."""
    print("\n" + "="*60)
    print("TESTING PUZZLE CONVERSION")
    print("="*60)
    
    # Test 3x3 puzzle
    puzzle1 = strings_to_puzzle(["???", "?3?", "??2"])
    print("\nInput: ['???', '?3?', '??2']")
    print_puzzle(puzzle1, "Converted Puzzle")
    
    # Test 4x4 puzzle
    puzzle2 = strings_to_puzzle(["??3?", "??2?", "?4??", "????"])
    print("\n\nInput: ['??3?', '??2?', '?4??', '????']")
    print_puzzle(puzzle2, "Converted Puzzle")


def test_remove_singles():
    """Test constraint propagation."""
    print("\n" + "="*60)
    print("TESTING CONSTRAINT PROPAGATION")
    print("="*60)
    
    # Test 4x4 puzzle
    puzzle = strings_to_puzzle(["??3?", "??2?", "?4??", "????"])
    print("\nInitial puzzle:")
    print_puzzle(puzzle)
    
    result = remove_singles(puzzle)
    print("\nAfter remove_singles:")
    print_puzzle(result)
    
    # Test 3x3 puzzle that solves completely
    puzzle2 = strings_to_puzzle(["???", "?3?", "??2"])
    print("\n\nInitial puzzle:")
    print_puzzle(puzzle2)
    
    result2 = remove_singles(puzzle2)
    print("\nAfter remove_singles:")
    print_puzzle(result2)


def test_solver():
    """Test the Latin square solver."""
    print("\n" + "="*60)
    print("TESTING SOLVER")
    print("="*60)
    
    # Test 3x3 puzzle
    print("\n3x3 Puzzle: ['???', '?3?', '??2']")
    puzzle1 = strings_to_puzzle(["???", "?3?", "??2"])
    solution1 = solve_latin(always_true, puzzle1)
    if solution1:
        print_solution(solution1, "Solution (any valid solution)")
    
    # Test 4x4 puzzle
    print("\n\n4x4 Puzzle: ['??3?', '??2?', '?4??', '????']")
    puzzle2 = strings_to_puzzle(["??3?", "??2?", "?4??", "????"])
    
    print("\nSolving with 'always_true' predicate:")
    solution2 = solve_latin(always_true, puzzle2)
    if solution2:
        print_solution(solution2)
    
    print("\nSolving with 'diagonal_has_2' predicate:")
    solution3 = solve_latin(diagonal_has_2, puzzle2)
    if solution3:
        print_solution(solution3)
        print(f"Diagonal: {[solution3[i][i] for i in range(len(solution3))]}")
    
    print("\nSolving with 'always_false' predicate (should fail):")
    solution4 = solve_latin(always_false, puzzle2)
    if solution4 is None:
        print("No solution found (as expected)")


def test_sudoku_validator():
    """Test Sudoku validation."""
    print("\n" + "="*60)
    print("TESTING SUDOKU VALIDATOR")
    print("="*60)
    
    # Valid Sudoku
    valid_sudoku = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 6, 5, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [7, 8, 9, 1, 2, 3, 6, 5, 4],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [3, 2, 1, 4, 5, 6, 7, 8, 9]
    ]
    
    print("\nTesting valid Sudoku:")
    print(f"Is valid Sudoku? {is_valid_sudoku(valid_sudoku)}")  # Should be True
    
    # Invalid Sudoku (has duplicate in bottom-left 3x3 block)
    invalid_sudoku = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [7, 8, 9, 1, 2, 3, 4, 5, 7],  # Last element is 7 (duplicate)
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]
    
    print("\nTesting invalid Sudoku (duplicate in block):")
    print(f"Is valid Sudoku? {is_valid_sudoku(invalid_sudoku)}")  # Should be False


def solve_example_puzzles():
    """Solve some example puzzles."""
    print("\n" + "="*60)
    print("SOLVING EXAMPLE PUZZLES")
    print("="*60)
    
    examples = [
        (["???", "?3?", "??2"], "3x3 Latin Square"),
        (["??3?", "??2?", "?4??", "????"], "4x4 Latin Square"),
        (["?3??", "????", "??2?", "???1"], "4x4 with corners"),
    ]
    
    for puzzle_strings, description in examples:
        print(f"\n\n{description}")
        print(f"Input: {puzzle_strings}")
        
        puzzle = strings_to_puzzle(puzzle_strings)
        print_puzzle(puzzle, "Initial Puzzle")
        
        solution = solve_latin(always_true, puzzle)
        if solution:
            print_solution(solution, "Solution")
        else:
            print("No solution found!")


def main():
    """Run all tests and examples."""
    print("="*60)
    print("SUDOKU/LATIN SQUARE SOLVER")
    print("Converted from Racket to Python")
    print("="*60)
    
    test_matrix_utils()
    test_strings_to_puzzle()
    test_remove_singles()
    test_solver()
    test_sudoku_validator()
    solve_example_puzzles()
    
    print("\n" + "="*60)
    print("ALL TESTS COMPLETE")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
