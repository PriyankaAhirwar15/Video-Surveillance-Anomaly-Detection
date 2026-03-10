# 🛡️ AI Surveillance & Anomaly Detection System

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Streamlit-red.svg)](https://streamlit.io/)
[![Deep Learning](https://img.shields.io/badge/Model-YOLOv8--Pose-green.svg)](https://ultralytics.com/)

## 📖 Project Overview
This project is a production-ready **Computer Vision** application designed for automated security monitoring. By leveraging **Deep Learning**, the system identifies human postures and triggers real-time alerts based on crowd density or unauthorized movements.



## 🚀 Key Features
* **Pose Estimation:** Real-time tracking of 17 human joints (Keypoints).
* **Anomaly Logic:** Automated "Crowd Alert" system when person count exceeds threshold.
* **Dual Input:** Seamless processing for both high-resolution images and video streams (.mp4, .avi).
* **Clean UI:** Interactive dashboard for security operators.

## 📁 Project Structure
```text
Anomaly_Detection_AI/
├── data/               # Sample video and image files
├── models/             # Saved AI model weights (.pt files)
├── app.py              # Main Streamlit Web Application
├── requirements.txt    # Project dependencies
└── README.md           # Documentation

🛠️ Installation & Setup
Follow these steps to run the project locally:

Clone the project:

Bash
git clone [https://github.com/PriyankaAhirwar15/Video-Surveillance-Anomaly-Detection.git]
cd Anomaly_Detection_AI
Create a Virtual Environment:

Bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install Dependencies:

Bash
pip install -r requirements.txt
Run the Application:

Bash
streamlit run app.py
🧠 Model Information
This system utilizes the YOLOv8-Pose architecture, which is optimized for high-speed inference on both CPU and GPU. It processes frames at approximately 30-50 FPS, making it suitable for live surveillance.

Author: Priyanka Ahirwar

Role: Data Scientist 