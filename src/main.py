#!/usr/bin/env python
# -*- coding: utf-8 -*-
# main.py

__author__ = "Kamil Rataj"
__credits__ = ["Mateusz Ciszek", "Natalia Martemianow"]
__version__ = "0.0.1"
__maintainer__ = "Kamil Rataj"
__status__ = "Development"

import cv2
import math
import serial
from mediapipe.framework.formats import landmark_pb2
import mediapipe as mp

WIN_NAME = "Inteligentne oswietlenie - IO"
SERIAL_PORT = "/dev/ttyACM1"  # Change this to the correct port


def serial_function(ser, gestue):
    def parse_ctr_value(value_in):
        value_out = "X"
        if value_in == "Thumb_Up":
            value_out = "A"
        elif value_in == "Thumb_Down":
            value_out = "B"
        elif value_in == "Open_Palm":
            value_out = "C"
        elif value_in == "Closed_Fist":
            value_out = "D"
        elif value_in == "Victory":
            value_out = "E"
        elif value_in == "Pointing_Up":
            value_out = "F"
        elif value_in == "ILoveYou":
            value_out = "G"
        else:
            value_out = "X"
        return value_out.encode('utf-8')

    if ser.in_waiting == 0:
        msg = parse_ctr_value(gestue)
        ser.write(msg)
        print(f"Sent: {msg}")
    ser.flush()


def draw_landmarks(image, results):
    if results is None:
        return image
    else:
        mp_hands = mp.solutions.hands
        mp_drawing = mp.solutions.drawing_utils
        mp_drawing_styles = mp.solutions.drawing_styles

        multi_hand_landmarks_list = list(results.hand_landmarks)
        for hand_landmarksA in multi_hand_landmarks_list:
            hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
            hand_landmarks_proto.landmark.extend([
                landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in
                hand_landmarksA
            ])

            mp_drawing.draw_landmarks(
                image,
                hand_landmarks_proto,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())
    return image


def draw_info_text(image, results):
    if results is None:
        return image
    top_gesture = results.gestures[0][0]
    handedness = results.handedness[0][0]
    if top_gesture != "":
        gesture_text = f"Gesture recognized: {top_gesture.category_name} ({format(top_gesture.score, '.1%')})"
        print(gesture_text)
        cv2.putText(image, gesture_text, (5, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 3, cv2.LINE_AA)
    if handedness != "":
        hand_text = f"Handedness: {handedness.category_name} ({format(handedness.score, '.1%')})"
        print(hand_text)
        cv2.putText(image, hand_text, (5, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 3, cv2.LINE_AA)
    return image


def main():
    BaseOptions = mp.tasks.BaseOptions
    GestureRecognizer = mp.tasks.vision.GestureRecognizer
    GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
    VisionRunningMode = mp.tasks.vision.RunningMode

    # Create a gesture recognizer instance with the image mode:
    options = GestureRecognizerOptions(
        base_options=BaseOptions(model_asset_path='gesture_recognizer.task'),
        running_mode=VisionRunningMode.VIDEO,
        num_hands=1,
    )
    ser = serial.Serial()
    ser.port = SERIAL_PORT
    ser.baudrate = 9600
    ser.bytesize = serial.EIGHTBITS
    ser.parity = serial.PARITY_NONE
    ser.stopbits = serial.STOPBITS_ONE
    ser.timeout = 1
    ser.open()

    cv2.namedWindow(WIN_NAME, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(WIN_NAME, 640, 480)
    cap = cv2.VideoCapture(0)

    recognition_result_old = None

    with GestureRecognizer.create_from_options(options) as recognizer:
        # The detector is initialized. Use it here.
        while cap.isOpened():
            # Capture frame-by-frame
            ret, frame = cap.read()
            frame_timestamp_ms = math.floor(cap.get(cv2.CAP_PROP_POS_MSEC))
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Convert the RGB frame to a MediaPipe Image
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)

            recognition_result = recognizer.recognize_for_video(mp_image, frame_timestamp_ms)

            if recognition_result.gestures:
                top_gesture = recognition_result.gestures[0][0]
                recognition_result_old = recognition_result
                if recognition_result.handedness[0][0].category_name == "Right":
                    serial_function(ser, top_gesture.category_name)
            outputImg = draw_landmarks(frame, recognition_result_old)
            cv2.imshow(WIN_NAME, draw_info_text(cv2.flip(outputImg, 1), recognition_result_old))

            if cv2.waitKey(1) & 0xFF == 27 or cv2.getWindowProperty(WIN_NAME, cv2.WND_PROP_VISIBLE) < 1:
                break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
