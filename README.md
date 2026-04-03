# 🚀 Real-Time AI Object Detection Web App

A full-stack computer vision application powered by YOLOv8 and Streamlit. This app allows users to perform state-of-the-art object detection using either static image uploads or real-time continuous video streams directly through the browser via WebRTC.

## ✨ Features
- **Live Video AI:** Zero-lag webcam detection right inside your browser window.
- **Image Scanning:** Upload any JPEG/PNG for instant object mapping and counting.
- **YOLOv8 Engine:** Powered by Ultralytics' fastest state-of-the-art model.
- **Clean UI:** Responsive, minimalist interface built with Streamlit.

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd "object detection"
   ```

2. **Install the dependencies:**
   Make sure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   ```bash
   streamlit run app.py
   ```
   A browser tab will automatically open at `http://localhost:8501`.

## 🖥️ Technologies Used
* **Python** 
* **Streamlit** (UI Framework)
* **YOLOv8 & PyTorch** (Machine Learning & Mathematical Tensors)
* **OpenCV** (Image and bounding-box drawing)
* **Streamlit-WebRTC** (Live video socket transmission)
