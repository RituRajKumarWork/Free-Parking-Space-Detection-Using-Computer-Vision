# Free-Parking-Space-Detection-Using-Computer-Vision

### Smart Parking Space Detection System
![image for showing](https://github.com/RituRajKumarWork/Free-Parking-Space-Detection-Using-Computer-Vision/assets/126075558/a449ec6f-4cda-41ab-a99d-ca65ed890fde)

![2](https://github.com/RituRajKumarWork/Free-Parking-Space-Detection-Using-Computer-Vision/assets/126075558/c34849fd-9d0c-4b50-9b75-87077b20d0a8)


#### Ritu Raj Kumar  
**Department of Computer Science and Engineering, India**

---
#### Info Given About Person and Things Could be WRONG>
#### Abstract

Parking space management is an essential aspect of urban infrastructure, influencing traffic flow, congestion, and city planning. This paper presents an innovative approach to parking space detection using advanced image processing techniques. Our research focuses on the development of a reliable, low-cost, and high-accuracy system capable of operating under diverse environmental conditions. The system utilizes machine learning algorithms to recognize and monitor parking space occupancy in real-time, providing significant improvements over traditional methods. The integration of sensor fusion and edge computing is also discussed as a potential advancement in the field.

---

### I. Introduction

The increase in the number of private vehicles in recent years has exacerbated parking challenges in urban areas. Drivers often waste considerable time searching for available parking spots, contributing to traffic congestion and environmental pollution. To address these issues, public parking facilities must inform drivers about available parking spaces and their locations efficiently. Manual management of parking spaces is impractical due to the high workforce and costs involved. Therefore, automated parking space detection systems have become crucial.

Our proposed system aims to enhance driver convenience by automatically detecting available parking spaces and providing real-time updates. This paper explores the underlying principles of computer vision and image processing techniques used in our approach, including object detection and image segmentation. We evaluate various algorithms and their suitability for different scenarios, highlighting the system's robustness and reliability.

---

### II. Literature Survey

Various methods have been proposed to tackle the challenges of parking space detection:

1. **Vehicle Counting at Entry Points**: Ming-Yee Chiu et al. used induction loop sensors embedded under the road surface to count vehicles entering and exiting parking facilities. However, this method could not provide details about specific empty spaces and required significant installation effort.

2. **Sensor-Based Detection**: Ultrasonic, microwave, and infrared sensors have been used to detect vehicles. These sensors are placed in each parking spot, but their effectiveness can be compromised by environmental factors such as temperature, wind, and precipitation.

3. **Vision-Based Systems**: Cameras provide a visual overview of the parking area, enabling the detection of empty spaces. Vision-based systems are cost-effective and easy to install but are heavily dependent on camera placement and environmental conditions. Thomas Fabian proposed an unsupervised parking space detection system using clustering methods, though it struggled with occlusions and shadows.

4. **Color Histogram and Shape Detection**: R. Yusnita and Najmi Hafizi proposed systems using color histograms and vehicle feature detection to identify empty parking slots. While effective in controlled environments, these methods faced challenges in adverse weather conditions.

Our research builds on these approaches by incorporating machine learning techniques to improve detection accuracy and adaptability to varying conditions.

---

### III. Methodology

Our proposed system uses a top-view CCTV camera to capture video footage of the parking area. The key steps involved are:

1. **Data Collection and Annotation**: Images and video data of parking lots are collected. Parking space coordinates are marked manually using a graphical interface.

2. **Image Processing and Feature Extraction**: Frames are extracted from the video feed, and image processing techniques such as Gaussian blur, adaptive thresholding, and morphological operations are applied to identify potential parking spaces.

3. **Parking Space Detection Algorithm**: Predefined parking space positions are analyzed in each frame. A machine learning model is trained to recognize empty spaces based on the number of non-zero pixels within the defined area.

4. **Continuous Monitoring and Evaluation**: The system continuously processes video frames to monitor space occupancy, providing real-time updates on the number of available parking spaces.

---

### IV. Algorithms

The main steps of the proposed algorithm are:

1. **Video Stream Processing**: Capture live video feed and extract frames.

2. **Image Preprocessing**: Convert RGB images to grayscale, apply Gaussian blur, and perform adaptive thresholding.

3. **Parking Space Calibration**: Manually input parking space coordinates and divide the area into virtual blocks.

4. **Occupancy Detection**: Convert blocks to binary images and detect vehicles based on pixel count thresholds.

5. **Real-Time Feedback**: Display the number of available parking spaces and mark occupied and free spots on the video feed.

---

### V. Results

The proposed system was implemented using Python and OpenCV. It was tested on a model parking lot with 69 spaces. The system accurately identified empty and occupied spots, displaying results in real-time with minimal latency. The visual feedback was provided through a user-friendly interface, highlighting available spaces in green and occupied ones in red.

---

### VI. Conclusion

The development of an automated parking space detection system using image processing represents a significant advancement in urban transportation management. Our system leverages computer vision and machine learning to address the challenges of parking space availability, providing real-time updates to drivers and urban planners. The proposed methodology is robust and cost-effective, with potential applications in smart cities to alleviate traffic congestion and improve urban mobility. Future research will explore the integration of sensor fusion and edge computing to enhance system performance further.

---
