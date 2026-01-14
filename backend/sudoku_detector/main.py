import cv2
import os
os.environ['YOLO_VERBOSE'] = 'False'
from ultralytics import YOLO
from .services.detect import detect_grid
from .services.recognizegrid import recognize_grid
from .services.warpimage import warp_image
from .services.splitgrid import split_grid

CROPMODEL = YOLO('models/grid-detect.pt')
DIGITMODEL = YOLO('models/digit-classify.pt')

# Fully ties entire sudoku grid
def process_sudoku(img):
    cropped = detect_grid(img, CROPMODEL)
    warped = warp_image(cropped)
    cells = split_grid(warped)
    textsudoku = recognize_grid(cells, DIGITMODEL)
    return textsudoku




