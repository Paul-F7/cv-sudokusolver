# CV Sudoku Solver

A computer vision system that photographs a Sudoku puzzle and solves it automatically.

## Pipeline

```
Photo → Detect Grid → Extract Cells → Recognize Digits → Solve
```

## Computer Vision (YOLOv8)

Two neural networks handle the image processing:

1. **Grid Detection** - A YOLOv8 object detection model locates the Sudoku grid in any photo. Trained on 1000+ images, achieving 99.5% accuracy across varying lighting, angles, and paper types.

2. **Digit Recognition** - A YOLOv8 classification model reads the digits (1-9) from each of the 81 cells.

## Solving Algorithm

The solver combines two techniques:

**Constraint Propagation** - When a cell has only one possible value, that value is eliminated from all other cells in the same row, column, and 3x3 block. This alone solves most easy/medium puzzles.

**Backtracking Search** - For harder puzzles, the algorithm picks an unsolved cell, tries each possibility, and recursively solves. If it hits a dead end (a cell with no valid options), it backtracks and tries a different path.

This combination solves any valid Sudoku in under 100ms.

## Tech Stack

- **YOLOv8** (Ultralytics) - Object detection and classification
- **OpenCV** - Image processing and cell extraction
- **PyTorch** - ML framework
- **Python** - Solver algorithm