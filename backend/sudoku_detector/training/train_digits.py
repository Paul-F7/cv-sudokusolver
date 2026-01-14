from ultralytics import YOLO

# Use MPS (Apple Silicon GPU) if available, otherwise CPU
import torch
if torch.backends.mps.is_available():
    device = "mps"
elif torch.cuda.is_available():
    device = 0
else:
    device = "cpu"

# Load base model
model = YOLO("yolov8n-cls.pt")  # classification model (not detection)

model.train(
    data="../datasetdigits",  # path to digit dataset
    epochs=100,
    imgsz=128,
    device=device,
    batch=32
)
