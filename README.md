# Face and Object Detection with Euclidean Distance Tracker

This repository contains Python code for detecting and tracking objects in video frames using OpenCV. The code uses a combination of face detection and background subtraction to track objects based on their Euclidean distance from previous frames.

## Requirements

Ensure you have the following Python packages installed:

- `opencv-python`
- `numpy`

You can install these dependencies using pip:

```bash
pip install opencv-python numpy
```

## Files

### 1. **Face and Object Detection with Euclidean Distance Tracker**
   - This script uses the **Haar Cascade** face detector and a custom **Euclidean Distance Tracker** to track moving faces or objects across multiple video frames.

   **Usage:**
   - This script reads from a video file (e.g., "los_angeles.mp4") and applies face detection to locate faces in the frame.
   - The **Euclidean Distance Tracker** is then used to track the positions of these faces across consecutive frames.
   - Object IDs are assigned to each detected face, and the program visualizes the tracked objects using circles and ID labels.

   **Key Features:**
   - Face detection using OpenCV's Haar Cascade Classifier.
   - Custom tracking of object positions using Euclidean distance.
   - Real-time tracking and visualization of objects in video frames.

   **How to run:**
   - Run the script in your Python environment with the video file path correctly set:
     ```bash
     python tracker.py
     ```
   - Make sure to update the video file name in `cv2.VideoCapture("los_angeles.mp4")` if needed.

---

### 2. **Background Subtraction and Contour Detection**
   - This script uses the **Background Subtractor MOG2** method to detect moving objects and applies **contour detection** to highlight areas of interest.

   **Usage:**
   - The video is cropped to a Region of Interest (ROI) to focus on the relevant portion of the frame.
   - The **Background Subtractor MOG2** creates a mask of the moving objects, and the **contours** of these objects are drawn on the frame.
   - The contours of significant areas are highlighted, and bounding boxes are drawn around them.

   **Key Features:**
   - Background subtraction using OpenCV's `createBackgroundSubtractorMOG2`.
   - Contour detection to identify and highlight moving objects.
   - Bounding boxes around detected objects.

   **How to run:**
   - Run the script in your Python environment with the video file path correctly set:
     ```bash
     python background_subtraction.py
     ```
   - Update the video file path in `cv2.VideoCapture("los_angeles.mp4")` to match your file location.

---

## How to Use

1. Clone the repository or download the scripts to your local machine.
2. Ensure you have the required dependencies installed as listed above.
3. Place a video file (e.g., "los_angeles.mp4") in the project directory or update the file path in the script accordingly.
4. Run the appropriate Python script (as mentioned above) to process the video and visualize the object tracking or background subtraction in real-time.
5. Press `ESC` to stop the script while the video is being processed.

## Example

### Face Detection and Tracking:

```python
python tracker.py
```

This will detect and track faces in the video, showing the tracked objects' positions in real-time.

### Background Subtraction and Contour Detection:

```python
python background_subtraction.py
```

This will detect and highlight moving objects using background subtraction, showing the contours and bounding boxes in real-time.

## License

This project is open-source and available under the [MIT License](LICENSE).

 
