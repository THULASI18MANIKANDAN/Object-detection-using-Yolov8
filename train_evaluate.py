from ultralytics import YOLO
import os

def train_and_evaluate(epochs=5, dataset_yaml="coco8.yaml"):
    """
    Trains a YOLO model and evaluates its accuracy.
    It automatically generates detailed charts (F1, Precision-Recall curves, Confusion Matrices).
    """
    # 1. Load a pretrained model (used as a starting point for transfer learning)
    print("Loading pretrained YOLOv8 model for fine-tuning...")
    model = YOLO("yolov8n.pt")  # Start with the nano variant
    
    # 2. Train the model on your dataset
    # Note: YOLO automatically saves rich charting data in the "runs/detect/train" folder.
    print(f"\n==============================================")
    print(f"   Starting Training on dataset: {dataset_yaml}")
    print(f"==============================================")
    model.train(
        data=dataset_yaml, 
        epochs=epochs, 
        imgsz=640, 
        plots=True,   # Tells YOLO to save detailed plot/chart images
        val=True,     # Run validation iteratively to track accuracy
        batch=4       # Lower batch size since we're assuming basic hardware
    )
    
    # 3. Test/Evaluate the Model on the Validation Split
    print("\n==============================================")
    print("   Evaluating Model Accuracy                  ")
    print("==============================================")
    metrics = model.val()
    
    # Output detailed numeric accuracy map
    print("\n--- DETAILED ACCURACY METRICS ---")
    print(f"Mean Average Precision (mAP@50-95): {metrics.box.map:.4f}")
    print(f"mAP@50 (Standard Benchmark):        {metrics.box.map50:.4f}")
    print(f"mAP@75:                             {metrics.box.map75:.4f}")
    
    # 4. Predict on a test image to visualize the trained model's performance
    print("\n==============================================")
    print("   Running Prediction Test                    ")
    print("==============================================")
    
    # Sample image included in Ultralytics to verify prediction
    test_image_url = "https://ultralytics.com/images/bus.jpg" 
    
    # Running prediction
    model.predict(source=test_image_url, save=True, show=True)
    
    print("\n=======================================================")
    print("✅ TRAINING AND EVALUATION COMPLETE!")
    print("All Prediction Charts, Confusion Matrices, and Loss Graphs")
    print("have been automatically saved to your 'runs/detect/train' folder.")
    print("=======================================================")

if __name__ == "__main__":
    print("This script will train an object detection model.")
    print("For demonstration, it defaults to a micro-dataset ('coco8.yaml') with 8 images.")
    
    print("Starting the training process with the demo dataset (epochs=5)...")
    train_and_evaluate(epochs=5, dataset_yaml="coco8.yaml")
