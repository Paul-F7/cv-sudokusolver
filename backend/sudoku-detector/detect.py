import torch
from ultralytics import YOLO

# Use MPS (Apple Silicon GPU) if available, otherwise CPU
if torch.backends.mps.is_available():
    device = "mps"
elif torch.cuda.is_available():
    device = 0  # CUDA GPU
else:
    device = "cpu"
# Load a model
model = YOLO("yolov8n.pt")  # nano model - faster to download and train usually its l

# Train the model
model.train(data="../datasetsudoku/data.yaml", epochs=100, imgsz=416, device=device)


''''
# Run inference on an image
results = model('image.jpg')

# Display results
results[0].show()

# Get detections
for r in results:
    boxes = r.boxes  # bounding boxes
    for box in boxes:
        cls = int(box.cls[0])  # class id
        conf = float(box.conf[0])  # confidence
        xyxy = box.xyxy[0].tolist()  # coordinates
        print(f"Detected {model.names[cls]} with {conf:.2f} confidence")
'''