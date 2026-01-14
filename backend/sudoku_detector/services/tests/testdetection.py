from ultralytics import YOLO
import cv2

model = YOLO('models/grid-detect')
img = cv2.imread('test.jpg')
results = model.predict(img, conf=0.1)  # lower confidence threshold

for result in results:
    boxes = result.boxes.cpu().numpy()
    for box in boxes:
        r = box.xyxy[0].astype(int)
        conf = box.conf[0]
        print(f'Found sudoku at {r} with {conf:.2f} confidence')
        
        # Save cropped grid
        cropped = img[r[1]:r[3], r[0]:r[2]]
        cv2.imwrite('cropped.jpg', cropped)
        print('Saved cropped.jpg')