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

The combination of constraint propagation (to prune the search space) and backtracking (to handle ambiguity) solves any valid Sudoku puzzle in under 100ms.

## Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Core language for the entire pipeline |
| **PyTorch** | Deep learning framework powering the neural networks |
| **YOLOv8 (Ultralytics)** | State-of-the-art object detection and image classification |
| **OpenCV** | Image preprocessing, thresholding, and cell extraction |

### Why YOLOv8?

YOLO (You Only Look Once) performs detection in a single forward pass through the network, making it fast enough for real-time applications. The v8 architecture from Ultralytics provides an excellent balance of accuracy and speed, with built-in support for both object detection (locating the grid) and classification (reading digits).

### Why Constraint Propagation + Backtracking?

Pure brute force would need to check up to 9^81 combinations. Constraint propagation dramatically reduces this by eliminating impossible values early. Most cells get resolved without any guessing, and backtracking only kicks in for the truly ambiguous cases. This makes the solver both correct (guaranteed to find a solution) and fast (typically milliseconds).