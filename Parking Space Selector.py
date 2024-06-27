import cv2
import pickle
from datetime import datetime

# Load parking positions if available
try:
    with open('Parking_points', 'rb') as file:
        parking_positions = pickle.load(file)
except FileNotFoundError:
    parking_positions = []

spot_width, spot_height = 107, 48


def handle_mouse_click(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        parking_positions.append((x, y))
    if event == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(parking_positions):
            x1, y1 = pos
            if x1 < x < x1 + spot_width and y1 < y < y1 + spot_height:
                parking_positions.pop(i)
    with open('Parking_points', 'wb') as file:
        pickle.dump(parking_positions, file)


def draw_futuristic_elements(image):
    height, width, _ = image.shape
    # Draw outer rectangle
    cv2.rectangle(image, (10, 10), (width - 10, height - 10), (0, 255, 255), 2)

    # Draw circles at corners
    radius = 10
    thickness = 2
    cv2.circle(image, (10, 10), radius, (0, 255, 255), thickness)
    cv2.circle(image, (width - 10, 10), radius, (0, 255, 255), thickness)
    cv2.circle(image, (10, height - 10), radius, (0, 255, 255), thickness)
    cv2.circle(image, (width - 10, height - 10), radius, (0, 255, 255), thickness)

    # Draw futuristic lines
    cv2.line(image, (10, 10), (width - 10, 10), (0, 255, 255), thickness)
    cv2.line(image, (10, 10), (10, height - 10), (0, 255, 255), thickness)
    cv2.line(image, (width - 10, 10), (width - 10, height - 10), (0, 255, 255), thickness)
    cv2.line(image, (10, height - 10), (width - 10, height - 10), (0, 255, 255), thickness)

    # Display current date and time
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    cv2.putText(image, current_time, (width - 400, height - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)


def draw_text(image, text, position, font_scale=1, thickness=2, color=(255, 255, 255), shadow_color=(0, 0, 0)):
    font = cv2.FONT_HERSHEY_SIMPLEX
    # Draw shadow text
    shadow_offset = 2
    cv2.putText(image, text, (position[0] + shadow_offset, position[1] + shadow_offset), font, font_scale, shadow_color,
                thickness, cv2.LINE_AA)
    # Draw main text
    cv2.putText(image, text, position, font, font_scale, color, thickness, cv2.LINE_AA)


while True:
    image = cv2.imread('Parking_Parking_DroneView_Image.png')
    for idx, pos in enumerate(parking_positions):
        cv2.rectangle(image, pos, (pos[0] + spot_width, pos[1] + spot_height), (255, 0, 255), 2)
        draw_text(image, str(idx + 1), (pos[0] + 10, pos[1] + 30), font_scale=1, thickness=2, color=(255, 255, 255),
                  shadow_color=(0, 0, 0))

    draw_futuristic_elements(image)
    draw_text(image, 'Press "q" to Quit', (10, 30), font_scale=1, thickness=2, color=(0, 255, 0),
              shadow_color=(0, 0, 0))
    draw_text(image, 'Left click to add, Right click to remove', (10, 60), font_scale=1, thickness=2, color=(0, 255, 0),
              shadow_color=(0, 0, 0))

    cv2.imshow("Parking Space Selector", image)
    cv2.setMouseCallback("Parking Space Selector", handle_mouse_click)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
