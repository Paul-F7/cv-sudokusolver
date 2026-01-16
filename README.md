# CV Sudoku Solver

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![YOLO](https://img.shields.io/badge/YOLOv8-00FFFF?style=for-the-badge&logo=yolo&logoColor=black)

Photograph a Sudoku puzzle and get the solution instantly.

---

## Model Performance

### Grid Detection
- **99.5% mAP50** — mean average precision at 50% IoU threshold
- **99.9% Precision** — minimal false positives
- **100% Recall** — detects every grid

### Digit Recognition
- **99.0% Top-1 Accuracy** — correct digit on first prediction
- **100% Top-5 Accuracy** — correct digit always in top 5 predictions
- **10-class classifier** — digits 1-9 plus empty cells

### Robustness
- Printed and handwritten puzzles
- Varying lighting and exposure
- Skewed camera angles
- Any paper color or background

---

## Models

### Grid Detection Model

YOLOv8 Nano object detection trained on 500+ images from Roboflow.

**Training Results**

<table>
<tr>
<td width="50%">

**Training Curves**

![Results](backend/models/results/detect/results.png)

</td>
<td width="50%">

**Precision-Recall Curve**

![PR Curve](backend/models/results/detect/BoxPR_curve.png)

</td>
</tr>
<tr>
<td>

**Confusion Matrix**

![Confusion Matrix](backend/models/results/detect/confusion_matrix_normalized.png)

</td>
<td>

**Validation Predictions**

![Validation](backend/models/results/detect/val_batch0_pred.jpg)

</td>
</tr>
</table>

---

### Digit Classification Model

YOLOv8 Nano classifier trained on 4,400+ cell images to recognize digits 1-9 and empty cells.

**Training Results**

<table>
<tr>
<td width="50%">

**Training Curves**

![Results](backend/models/results/classify/results.png)

</td>
<td width="50%">

**Confusion Matrix**

![Confusion Matrix](backend/models/results/classify/confusion_matrix_normalized.png)

</td>
</tr>
<tr>
<td colspan="2" align="center">

**Validation Samples**

<img src="backend/models/results/classify/val_batch0_labels.jpg" width="400">

</td>
</tr>
</table>

---

## How It Works

1. **Detect** — YOLOv8 locates the Sudoku grid in your photo
2. **Warp** — OpenCV corrects perspective to create a perfect square
3. **Split** — Grid is divided into 81 individual cells
4. **Recognize** — YOLOv8 classifier identifies each digit
5. **Solve** — Constraint propagation + backtracking finds the solution
6. **Render** — Solution is drawn onto a clean grid image

---

## Solving Algorithm

Uses a hybrid approach:

1. **Constraint Propagation** — Eliminates impossible values by checking rows, columns, and 3x3 blocks. Solves most puzzles without guessing.

2. **Backtracking Search** — For harder puzzles, tries possibilities and backtracks when stuck. Guarantees a solution if one exists.

Solves any valid Sudoku in under 100ms.

---

## Project Structure

```
backend/
├── sudoku_detector/     # Computer vision pipeline
│   ├── services/        # Detection, warping, recognition
│   ├── training/        # Model training scripts
│   └── models/          # Trained weights (.pt files)
├── sudoku_solver/       # Solving algorithms
└── sudoku_display/      # Solution rendering
```

---

## Getting Started

```bash
# Clone the repo
git clone https://github.com/yourusername/cv-sudokusolver.git
cd cv-sudokusolver

# Install dependencies
pip install -r requirements.txt

# Run on an image
cd backend
python -c "import cv2; from main import solve_sudoku_image; solve_sudoku_image(cv2.imread('path/to/sudoku.jpg'))"
```

Output is saved to `solved_sudoku.jpg`.