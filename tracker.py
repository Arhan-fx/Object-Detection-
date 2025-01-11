import cv2
import numpy as np
import math

class EuclideanDistanceTracker:
    def __init__(self):
        self.tracking_objects = {}
        self.track_id = 0

    def update(self, center_points_prev_frame, center_points_cur_frame):
        updated_tracking_objects = self.tracking_objects.copy()
        new_centers = []

        for object_id, prev_center in updated_tracking_objects.items():
            object_exists = False
            for pt in center_points_cur_frame:
                distance = math.hypot(prev_center[0] - pt[0], prev_center[1] - pt[1])

                if distance < 20:
                    self.tracking_objects[object_id] = pt
                    object_exists = True
                    new_centers.append(pt)
                    center_points_cur_frame.remove(pt)
                    break

            if not object_exists:
                self.tracking_objects.pop(object_id)

        for pt in center_points_cur_frame:
            self.tracking_objects[self.track_id] = pt
            self.track_id += 1

        return self.tracking_objects, center_points_cur_frame


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture("los_angeles.mp4")

count = 0
center_points_prev_frame = []

tracker = EuclideanDistanceTracker()

while True:
    ret, frame = cap.read()
    count += 1
    if not ret:
        break

    center_points_cur_frame = []

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cx = int((x + x + w) / 2)
        cy = int((y + y + h) / 2)
        center_points_cur_frame.append((cx, cy))
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    tracking_objects, updated_center_points = tracker.update(center_points_prev_frame, center_points_cur_frame)

    for object_id, pt in tracking_objects.items():
        cv2.circle(frame, pt, 5, (0, 0, 255), -1)
        cv2.putText(frame, str(object_id), (pt[0], pt[1] - 7), 0, 1, (0, 0, 255), 2)

    print("Tracking objects")
    print(tracking_objects)

    print("CUR FRAME LEFT PTS")
    print(updated_center_points)

    cv2.imshow("Frame", frame)

    center_points_prev_frame = updated_center_points.copy()

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
