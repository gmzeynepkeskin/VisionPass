from ultralytics import YOLO
import cv2

class PersonDetector:
    def __init__(self, model_path="yolov8n.pt"):
        self.model = YOLO(model_path)

    def detect(self, frame):
        results = self.model(frame)
        detections = []

        for result in results:
            for box in result.boxes:
                cls = int(box.cls[0])
                if cls == 0:  # 0 = person class in COCO
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    detections.append((x1, y1, x2, y2))

        return detections
