import cv2
import pickle
import numpy as np
from datetime import datetime

# Video feed
video_capture = cv2.VideoCapture('Parking_Parking_DroneView.mp4')

with open('Parking_points', 'rb') as file:
    parking_positions = pickle.load(file)

spot_width, spot_height = 107, 48


def analyze_parking_spots(processed_image, frame):
    available_spots = 0
    for idx, position in enumerate(parking_positions):
        x, y = position
        cropped_image = processed_image[y:y + spot_height, x:x + spot_width]
        non_zero_count = cv2.countNonZero(cropped_image)
        if non_zero_count < 900:
            rectangle_color = (0, 255, 0)
            line_thickness = 5
            available_spots += 1
            cv2.rectangle(frame, position, (position[0] + spot_width, position[1] + spot_height), rectangle_color,
                          line_thickness)
            cv2.putText(frame, str(idx + 1), (x + 10, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        else:
            rectangle_color = (0, 0, 255)
            line_thickness = 2
            cv2.rectangle(frame, position, (position[0] + spot_width, position[1] + spot_height), rectangle_color,
                          line_thickness)
    cv2.putText(frame, f'Available: {available_spots}/{len(parking_positions)}', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 255, 0), 2)


def draw_futuristic_elements(frame):
    height, width, _ = frame.shape
    # Draw outer rectangle
    cv2.rectangle(frame, (10, 10), (width - 10, height - 10), (0, 255, 255), 2)

    # Draw circles at corners
    radius = 10
    thickness = 2
    cv2.circle(frame, (10, 10), radius, (0, 255, 255), thickness)
    cv2.circle(frame, (width - 10, 10), radius, (0, 255, 255), thickness)
    cv2.circle(frame, (10, height - 10), radius, (0, 255, 255), thickness)
    cv2.circle(frame, (width - 10, height - 10), radius, (0, 255, 255), thickness)

    # Draw futuristic lines
    cv2.line(frame, (10, 10), (width - 10, 10), (0, 255, 255), thickness)
    cv2.line(frame, (10, 10), (10, height - 10), (0, 255, 255), thickness)
    cv2.line(frame, (width - 10, 10), (width - 10, height - 10), (0, 255, 255), thickness)
    cv2.line(frame, (10, height - 10), (width - 10, height - 10), (0, 255, 255), thickness)

    # Display current date and time
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    cv2.putText(frame, current_time, (width - 400, height - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)


while True:
    if video_capture.get(cv2.CAP_PROP_POS_FRAMES) == video_capture.get(cv2.CAP_PROP_FRAME_COUNT):
        video_capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, frame = video_capture.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred_frame = cv2.GaussianBlur(gray_frame, (3, 3), 1)
    threshold_frame = cv2.adaptiveThreshold(blurred_frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,
                                            25, 16)
    median_frame = cv2.medianBlur(threshold_frame, 5)
    kernel = np.ones((3, 3), np.uint8)
    dilated_frame = cv2.dilate(median_frame, kernel, iterations=1)

    analyze_parking_spots(dilated_frame, frame)
    draw_futuristic_elements(frame)

    cv2.imshow("Parking Space Detection", frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
