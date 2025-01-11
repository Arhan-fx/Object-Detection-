import cv2
from tracker import*

tracker = EuclideanDistanceTracker()

cap = cv2.VideoCapture("los_angeles.mp4")


object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=55)


while True:
    ret, frame = cap.read()
    height, width, _ = frame.shape
    
    
    roi = frame[240: 600,280: 1000]
 
    mask = object_detector.apply(roi)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _= cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detection = []
    for cnt in contours:
         
        area =cv2.contourArea(cnt)
        if area > 100:
           # cv2.drawContours(roi, [cnt], -1, (0,255,0), 2)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(roi, (x,y,), (x+w,y+h), (0,255,0), 3)
            
            detection.append([x, y, w, h])

    print(detection)



    cv2.imshow("roi", roi)
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key=cv2.waitKey(50)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
