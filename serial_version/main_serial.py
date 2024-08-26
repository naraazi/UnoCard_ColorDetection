import cv2
import numpy as np
import serial
import time

# -- you can change the port here
ser = serial.Serial('/dev/ttyUSB0', 9600)
time.sleep(2)

color_ranges = {
    "red": [(0, 100, 100), (10, 255, 255)],
    "yellow": [(20, 150, 150), (30, 255, 255)],
    "green": [(40, 100, 100), (80, 255, 255)],
    "blue": [(90, 100, 100), (130, 255, 255)]
}

colors_state = {color: False for color in color_ranges}


def process_frame(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    result = np.full_like(frame, 255)
    colors_detected = {}

    for color, (lower, upper) in color_ranges.items():
        mask = cv2.inRange(hsv, np.array(lower), np.array(upper))
        color_pixels = cv2.countNonZero(mask)

        if color_pixels > 500:
            colors_detected[color] = color_pixels

            average_hue = (lower[0] + upper[0]) // 2
            average_color_hsv = np.uint8([[[average_hue, 255, 255]]])
            average_color_bgr = cv2.cvtColor(average_color_hsv, cv2.COLOR_HSV2BGR)[0, 0, :]
            result[mask > 0] = average_color_bgr

    if len(colors_detected) == len(color_ranges):
        if not all(colors_state.values()):
            ser.write(b'a')
            for color in colors_state:
                colors_state[color] = True
        return result, "All the colors!"

    elif colors_detected:
        predominant_color = max(colors_detected, key=colors_detected.get)
        if not colors_state[predominant_color]:
            ser.write(predominant_color[0].encode())
            colors_state[predominant_color] = True
        return result, predominant_color

    else:
        for color in colors_state:
            colors_state[color] = False
        return result, "No colors!"


def main():
    cap = cv2.VideoCapture(2)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        result, color_status = process_frame(frame)
        cv2.putText(result, color_status, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.imshow("Window", result)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    ser.close()


if __name__ == "__main__":
    main()
