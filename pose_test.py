import cv2
from ultralytics import YOLO

model = YOLO('yolov8n-pose.pt')
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    results = model(frame)
    annotated_frame = results[0].plot()

    cv2.imshow("AI Anomaly Detection - Pose", annotated_frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q") or key == 27:  ## q OR ESC to stop
        break

cap.release()
cv2.destroyAllWindows()