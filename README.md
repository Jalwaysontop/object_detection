# 📏 Blue Object Distance Estimator (ROS 2 + OpenCV)

## 📖 Overview
This ROS 2 package estimates the **distance of a blue-colored object** from the camera using computer vision and the concept of **focal length calibration**.  
It assumes the object's real-world width is **17–20 cm**, providing accurate results only within that range.

---

## 🧠 How It Works
1. Detects a **blue object** in the camera frame using HSV color thresholds.  
2. Measures its **apparent width (in pixels)** through contour detection.  
3. Calculates the **distance** using the pinhole camera formula:
Distance} = Known Width*Focal Length/Perceived Width
\]

The **focal length** is computed once using a known distance and object width.

---

## 🧱 Workspace Structure
