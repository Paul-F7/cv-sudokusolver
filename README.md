# CV Sudoku Solver

A computer vision pipeline that detects, reads, and solves Sudoku puzzles from images using deep learning and constraint satisfaction algorithms.

## How It Works

### Pipeline Overview

```
Image → Grid Detection → Cell Extraction → Digit Recognition → Solver → Solution
         (YOLOv8)          (OpenCV)          (YOLOv8-cls)      (CSP + Backtracking)
```

### 1. Grid Detection (YOLOv8 Object Detection)

A YOLOv8 model trained on ~1000 sudoku images detects and localizes the puzzle grid in any photo.

**Model Performance:**
- mAP50: 99.5%
- Precision: 99.87%
- Recall: 100%

The model handles various conditions: different lighting, paper colors, angles, and both printed and handwritten puzzles.

### 2. Cell Extraction (OpenCV)

Once the grid is detected, OpenCV extracts the 81 individual cells:

```python
# Crop detected region and divide into 9x9 grid
height, width = grid_image.shape[:2]
cell_h, cell_w = height // 9, width // 9

for row in range(9):
    for col in range(9):
        cell = grid_image[row*cell_h:(row+1)*cell_h, col*cell_w:(col+1)*cell_w]
```

Adaptive thresholding handles varying lighting conditions across the image.

### 3. Digit Recognition (YOLOv8 Classification)

A YOLOv8 classification model identifies digits 1-9 in each cell, trained on printed digit datasets. Empty cells are detected by analyzing pixel density in the cell center.

### 4. Sudoku Solver (Constraint Propagation + Backtracking)

The solver uses a combination of constraint satisfaction techniques:

#### Constraint Propagation

The "naked singles" technique propagates constraints through the grid:

```python
def remove_singles(puzzle):
    """When a cell has only one possibility, eliminate that value
    from all cells in the same row and column."""
    while any_satisfy(is_single, puzzle):
        col, row = find_where(is_single, puzzle)
        value = puzzle[row][col][0]

        # Propagate constraint to row and column
        puzzle = remove_from_row(puzzle, row, value)
        puzzle = remove_from_column(puzzle, col, value)
    return puzzle
```

#### Backtracking Search

When constraint propagation alone can't solve the puzzle, depth-first search explores possibilities:

```python
def solve_latin(predicate, puzzle):
    puzzle = remove_singles(puzzle)  # Apply constraints first

    if not has_unsolved_cells(puzzle):
        return puzzle_to_solution(puzzle) if predicate(solution) else None

    if is_invalid(puzzle):  # Dead end - backtrack
        return None

    # Try each possibility for an unsolved cell
    for neighbour in get_neighbours(puzzle):
        solution = solve_latin(predicate, neighbour)
        if solution:
            return solution
    return None
```

#### Sudoku Validation

Sudoku extends Latin square rules with 3x3 block constraints:

```python
def is_valid_sudoku(solution):
    # Extract all nine 3x3 blocks
    for block_row in range(3):
        for block_col in range(3):
            block = extract_3x3_block(solution, block_row, block_col)
            if has_duplicates(block):
                return False
    return True
```

## Tech Stack

| Component | Technology |
|-----------|------------|
| Grid Detection | YOLOv8 (Ultralytics) |
| Cell Extraction | OpenCV |
| Digit Recognition | YOLOv8 Classification |
| Solver Algorithm | Python (CSP + Backtracking) |
| ML Framework | PyTorch |

## Algorithm Complexity

- **Constraint Propagation:** O(n²) per iteration, dramatically reduces search space
- **Backtracking:** O(9^m) worst case where m = empty cells, but pruning makes this tractable
- **Combined:** Most puzzles solve in <100ms due to effective constraint propagation

## Training

### Grid Detection Model
```bash
python backend/sudoku-detector/detect.py
# Trains on Roboflow sudoku-vision dataset
# 100 epochs, 416x416 input size
```

### Digit Classification Model
```bash
python backend/sudoku-detector/train_digits.py
# Trains on printed digit dataset
# 50 epochs, 64x64 input size
```

## Usage

```python
from sudoku_pipeline import SudokuSolver

solver = SudokuSolver()
solution = solver.solve_from_image("sudoku_photo.jpg")

# Returns 9x9 solved grid
for row in solution:
    print(row)
```

## Project Structure

```
backend/
├── sudoku-detector/
│   ├── detect.py           # Grid detection training
│   ├── train_digits.py     # Digit classification training
│   └── models/             # Trained weights
└── sudoku-solver/
    ├── solver.py           # Backtracking search
    ├── constraint_propagation.py  # CSP techniques
    ├── sudoku_validator.py # Validation rules
    └── puzzle.py           # Data structures
```