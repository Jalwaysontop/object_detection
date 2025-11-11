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
src/
 └── auv_vision/
           ├── auv_vision/--- 
                             └──camera_node.py
           ├── package.xml   └──distance_node.py
           ├── resource      └──focal_length_calculate.py
           ├── test          └──operations.py
           └── LICENSE       └──pixel_width_subscriber.py
           └── setup.py      └──__init__.py
           └── setup.cfg
  └──config/pixel_focal_length.yaml

---

⚙️ Build & Run

1️⃣ Clone and build
cd ~/ros2_ws/src
git clone https://github.com/<your-username>/blue_distance_pkg.git
cd ~/ros2_ws
colcon build
source install/setup.bash
2️⃣ Run the nodes
  ros2 run auv_vision webcam
  ros2 run auv_vision operations
  ros2 run auv_vision distance
Note: only run pixel_width_subscriber to find your camera's focal length you can change the object's known width also the objects distance from the camera according to you. Now run this by putting the blue object at the distance in pixel_focal_length.yaml file

🧩 Dependencies
ROS 2 Humble (or newer)
OpenCV (Python)
rclpy and sensor_msgs packages

Install:
sudo apt install ros-${ROS_DISTRO}-cv-bridge python3-opencv
rosdep install --from-paths src --ignore-src -r -y

📜 License
This project is licensed under the Apache 2.0 License — see the LICENSE

🤝 Contributing
Contributions, bug reports, and suggestions are welcome!
Fork this repository, make your changes, and open a pull request.
