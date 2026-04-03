from ultralytics import YOLO
import sys

print("Loading model...")
model = YOLO('yolov8n.pt')

print("Saving architecture to text file...")
# PyTorch models can be converted to a giant strings representing all their layers
with open("yolov8_architecture.txt", "w") as f:
    f.write(str(model.model))

print("Done! You can now open yolov8_architecture.txt in your code editor.")
