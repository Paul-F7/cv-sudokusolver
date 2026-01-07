# CV Sudoku Solver

A computer vision system that photographs a Sudoku puzzle and solves it automatically.

## Pipeline

```
Photo → Detect Grid → Extract Cells → Recognize Digits → Solve
```

## Computer Vision (YOLOv8)

Two neural networks handle the image processing:

**Grid Detection** - A YOLOv8 object detection model locates the Sudoku grid in any photo. Trained on 1000+ images, the model achieves 99.5% mAP with near-perfect precision and recall. It handles varying lighting conditions, different paper colors, camera angles, and works with both printed and handwritten puzzles.

**Digit Recognition** - A YOLOv8 classification model reads the digits (1-9) from each of the 81 cells. Empty cells are identified by analyzing pixel density in the cell center after adaptive thresholding.

## Solving Algorithm

The solver combines two classical AI techniques:

**Constraint Propagation** - When a cell has only one possible value, that value is eliminated from all other cells in the same row, column, and 3x3 block. This process repeats until no more eliminations are possible. For easy and medium puzzles, constraint propagation alone finds the solution without any guessing.

**Backtracking Search** - For harder puzzles where multiple possibilities remain, the algorithm selects an unsolved cell, makes a guess, and recursively attempts to solve the resulting puzzle. If it reaches an invalid state (a cell with no legal values), it backtracks to the last decision point and tries a different value. This depth-first search guarantees finding a solution if one exists.

```
                    [Initial Puzzle]
                          │
                          ▼
               ┌─────────────────────┐
               │     Propagate       │ ◄─────────────────┐
               │    Constraints      │                   │
               └─────────────────────┘                   │
                          │                              │
                          ▼                              │
                ┌───────────────────┐                    │
                │  Solved?          │── Yes ──► Done     │
                └───────────────────┘                    │
                          │ No                           │
                          ▼                              │
                ┌───────────────────┐                    │
                │  Pick unsolved    │                    │
                │  cell, try value  │                    │
                └───────────────────┘                    │
                          │                              │
                          ▼                              │
                ┌───────────────────┐                    │
                │  Valid state?     │── Yes ─────────────┘
                └───────────────────┘
                          │ No
                          ▼
                     Backtrack
```

The combination of constraint propagation (to prune the search space) and backtracking (to handle ambiguity) solves any valid Sudoku puzzle in under 100ms.

## Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Core language for the entire pipeline |
| **PyTorch** | Deep learning framework powering the neural networks |
| **YOLOv8 (Ultralytics)** | State-of-the-art object detection and image classification |
| **OpenCV** | Image preprocessing, thresholding, and cell extraction |