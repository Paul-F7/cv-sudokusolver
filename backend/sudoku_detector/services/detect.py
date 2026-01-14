
# detects the sudoku grid and then crops the image
def detect_grid(img, model):
    results = model.predict(img, conf=0.1, verbose=False)

    for result in results:
        boxes = result.boxes.cpu().numpy()

        if len(boxes) > 0:
            best_box = max(boxes, key=lambda b: b.conf[0])
            r = best_box.xyxy[0].astype(int)
            conf = best_box.conf[0]
            print(f'Found sudoku at {r} with {conf:.2f} confidence')

            cropped = img[r[1]:r[3], r[0]:r[2]]
            return cropped

    print("No Sudoku grid found.")
    return None