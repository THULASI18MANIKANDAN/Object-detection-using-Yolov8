import streamlit as st
from ultralytics import YOLO
import cv2
import av
import numpy as np
from PIL import Image
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration

st.set_page_config(page_title="Real-Time Web AI Detection", page_icon="🎥", layout="wide")
st.title("🎥 Live Full-Motion AI Object Detection")

@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")

model = load_model()

# Create a clean sidebar to toggle views
st.sidebar.title("App Navigation")
app_mode = st.sidebar.radio("Choose detection format:", ["Live Webcam", "Upload Static Image"])

if app_mode == "Upload Static Image":
    st.subheader("Image Upload Detection")
    st.write("Upload any picture from your computer, and the AI will analyze it!")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "webp"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        # Display the uploaded image
        st.image(image, caption="Original Image", width=640)
        
        # Action button to start detection
        if st.button("Detect Objects", type="primary"):
            with st.spinner("Analyzing..."):
                img_array = np.array(image.convert("RGB"))
                
                # Inference
                results = model.predict(source=img_array, conf=0.25)
                
                # Draw boxes
                annotated_img = results[0].plot()
                
                # Convert from OpenCV BGR to Web RGB
                annotated_img_rgb = cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB)
                
                st.success("✅ Detection Complete!")
                st.image(annotated_img_rgb, caption="Predicted Image with Bounding Boxes", width=640)
                
                # Print out text summary of what it found
                st.subheader("Detected Objects Summary:")
                detected_classes = [model.names[int(box.cls)] for box in results[0].boxes]
                if detected_classes:
                    item_counts = {item: detected_classes.count(item) for item in set(detected_classes)}
                    for item, count in item_counts.items():
                        st.write(f"- **{item.capitalize()}**: {count}")
                else:
                    st.write("No objects detected.")

# Webcam Mode
else:
    st.subheader("Live Real-Time Tracker")
    st.write("Watch the YOLOv8 AI track objects continuously directly through your browser!")
    
    # Configuration for WebRTC connecting to local webcam
    RTC_CONFIGURATION = RTCConfiguration(
        {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
    )

    def video_frame_callback(frame: av.VideoFrame) -> av.VideoFrame:
        # Convert incoming browser frame to OpenCV format
        img = frame.to_ndarray(format="bgr24")
        
        # Perform object detection mathematically without printing logs to console
        results = model.predict(source=img, conf=0.25, verbose=False)
        
        # Draw boxes
        annotated_img = results[0].plot()
        
        # Return processed frame back to the browser in real-time
        return av.VideoFrame.from_ndarray(annotated_img, format="bgr24")

    st.write("Click 'Start' below to turn on the continuous live video feed!")

    # The WebRTC stream component
    webrtc_streamer(
        key="yolov8-detection",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration=RTC_CONFIGURATION,
        video_frame_callback=video_frame_callback,
        media_stream_constraints={"video": True, "audio": False},
        async_processing=True,
        video_html_attrs={
            "style": {"width": "640px", "margin": "0 auto", "display": "block", "border": "2px solid #333", "border-radius": "8px"},
            "controls": False,
            "autoPlay": True,
        }
    )
