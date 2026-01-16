from sudoku_detector.main import process_sudoku
from sudoku_solver.puzzle import strings_to_puzzle
from sudoku_solver.solver import solve_latin
from sudoku_solver.sudoku_validator import is_valid_sudoku
from sudoku_display.main import solution_to_image
import cv2
img1 = cv2.imread('/Users/paulfomitchev/Documents/Coding/cv-sudokusolver/backend/datasetsudoku/test/images/sudoku_3288_jpg.rf.5aff634f24dfc3f4ceed048be7bee9a9.jpg')

def solve_sudoku_image(img, output_path="solved_sudoku.jpg"):
    puzzle_strings = process_sudoku(img)
    print("Detected puzzle:")
    for row in puzzle_strings:
        print(row)
    puzzle = strings_to_puzzle(puzzle_strings)
    solution = solve_latin(is_valid_sudoku, puzzle)
    if solution is None:
        print("Could not solve puzzle")
        return
    solution_strings = [''.join(map(str, row)) for row in solution]
    solution_to_image(solution_strings, output_path)

solve_sudoku_image(img1)