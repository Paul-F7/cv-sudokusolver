import cv2
import numpy as np
# Splits the grid and saves the images in the numpy array 
def split_grid(warped_img):
    #Split a warped sudoku image into 81 cells (9x9 grid)
    cells = []
    height, width = warped_img.shape[:2]
    cell_height = height // 9
    cell_width = width // 9
    
    for row in range(9):
        row_cells = []
        for col in range(9):
            # Calculate cell boundaries
            y1 = row * cell_height
            y2 = (row + 1) * cell_height
            x1 = col * cell_width
            x2 = (col + 1) * cell_width
            
            cell = warped_img[y1:y2, x1:x2]
            row_cells.append(cell)
        cells.append(row_cells)
    
    return cells  # 9x9 list of cell images

