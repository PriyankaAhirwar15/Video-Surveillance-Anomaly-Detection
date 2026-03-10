import streamlit as st
from ultralytics import YOLO
import cv2
import tempfile
import numpy as np
from PIL import Image

st.title("🛡️ AI Surveillance Anomaly Detection")

# 1. Load the AI Model
model = YOLO('yolov8n-pose.pt')

# 2. Let the user choose between Image or Video
choice = st.radio("Pick your input type:", ["Image", "Video"])

# --- IMAGE SECTION ---
if choice == "Image":
    uploaded_img = st.file_uploader("Upload a photo...", type=['jpg', 'jpeg', 'png'])
    if uploaded_img is not None:
        image = Image.open(uploaded_img).convert("RGB")
        results = model(np.array(image))
        
        # --- NEW PROFESSIONAL LOGIC ---
        # Count how many people the AI found
        person_count = len(results[0].keypoints) 
        
        st.subheader(f"People Detected: {person_count}")
        
        # If more than 3 people, show a Security Alert
        if person_count > 3:
            st.error("🚨 SECURITY ALERT: Crowd Detected in Restricted Area!")
        else:
            st.success("Area Secure: Normal Activity.")
        # ------------------------------
        
        st.image(results[0].plot(), caption="Pose Detection", use_container_width=True)

# --- VIDEO SECTION ---
else:
    uploaded_video = st.file_uploader("Upload a surveillance clip...", type=['mp4', 'mov', 'avi'])
    
    if uploaded_video is not None:
        # Streamlit needs to save the video to a temporary file to read it
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_video.read())
        
        vf = cv2.VideoCapture(tfile.name)
        st_frame = st.empty() # This creates a spot for the video to play

        while vf.isOpened():
            ret, frame = vf.read()
            if not ret:
                break
            
            # Run AI on the video frame
            results = model(frame)
            
            # Draw the skeleton
            annotated_frame = results[0].plot()
            
            # Show it on the website
            st_frame.image(annotated_frame, channels="BGR")
        
        vf.release()
        st.success("Video processing finished!")