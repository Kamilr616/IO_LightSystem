#!/usr/bin/env python
# -*- coding: utf-8 -*-
# main.py

__author__ = "Kamil Rataj"
__credits__ = ["Mateusz Ciszek"]
__version__ = "0.1.0"
__maintainer__ = "Kamil Rataj"
__status__ = "Development"

import argparse
import sys
import time
import serial

import cv2
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe.framework.formats import landmark_pb2

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Global variables to calculate FPS
COUNTER, FPS = 0, 0
START_TIME = time.time()

WIN_NAME = "Inteligentne oswietlenie - IO"  # Window name
SERIAL_PORT = "COM5"  # Serial port
SERIAL_BAUDRATE = 9600  # Serial baudrate
SERIAL_ENCODOING = 'iso-8859-1'  # Serial encoding
BAR_HEIGHT = 40  # Height of the color bar


def run(model: str, num_hands: int,
        min_hand_detection_confidence: float,
        min_hand_presence_confidence: float, min_tracking_confidence: float,
        camera_id: int, width: int, height: int, control_hand: int, output_mode: int, mirror: int,
        bar_visibility: int) -> None:
    """Continuously run inference on images acquired from the camera.

  Args:
      model: Name of the gesture recognition model bundle.
      num_hands: Max number of hands can be detected by the recognizer.
      min_hand_detection_confidence: The minimum confidence score for hand
        detection to be considered successful.
      min_hand_presence_confidence: The minimum confidence score of hand
        presence score in the hand landmark detection.
      min_tracking_confidence: The minimum confidence score for the hand
        tracking to be considered successful.
      camera_id: The camera id to be passed to OpenCV.
      width: The width of the frame captured from the camera.
      height: The height of the frame captured from the camera.
      control_hand:
      output_mode:
      mirror:
      bar_visibility:
  """

    # Start capturing video input from the camera
    cap = cv2.VideoCapture(camera_id)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    # Visualization parameters
    row_size = 45  # pixels
    left_margin = 24  # pixels
    text_color = (0, 0, 0)  # black
    font_size = 0.8
    font_thickness = 1
    fps_avg_frame_count = 10

    # Label box parameters
    label_text_color = (56, 255, 0)  # white
    label_font_size = 0.8
    label_thickness = 1

    recognition_frame = None
    recognition_result_list = []

    # Initialize the serial port
    if output_mode == 1:
        ser = serial.Serial()
        ser.port = SERIAL_PORT
        ser.baudrate = SERIAL_BAUDRATE
        ser.bytesize = serial.EIGHTBITS
        ser.parity = serial.PARITY_NONE
        ser.stopbits = serial.STOPBITS_ONE
        ser.timeout = 1
        try:
            ser.open()
        except serial.SerialException as e:
            print(f"Could not open serial port: {e}")
            sys.exit(1)

        # Check if the serial port is open
        if not ser.is_open:
            print("Failed to open serial port")
            sys.exit(1)

    def serial_function(serial_com, info):
        def parse_ctr_value(value_in):
            gesture_dict = {
                "Thumb_Up": "A",
                "Thumb_Down": "B",
                "Open_Palm": "C",
                "Closed_Fist": "D",
                "Victory": "E",
                "Pointing_Up": "F",
                "ILoveYou": "G"
            }
            value_out = gesture_dict.get(value_in, "X")
            return value_out.encode(encoding=SERIAL_ENCODOING)

        if serial_com.in_waiting == 0:
            msg = parse_ctr_value(info)
            serial_com.write(msg)
            print(f"Serial: {msg}")
        else:
            print(f"Serial unavailable")
            serial_com.reset_input_buffer()
        serial_com.flush()

    def draw_color_bar(imageA, info):
        bar_height = BAR_HEIGHT  # height of the color bar

        def parse_color(gesture_info):
            gesture_dict = {
                "Thumb_Up": (0, 255, 0),  # Zielony
                "Thumb_Down":(0, 0, 255),  # Czerwony
                "Open_Palm": (255, 0, 0),  # Niebieski
                "Closed_Fist": (0, 255, 255),  # Żółty
                "Victory": (150, 0, 150),  # spring green
                "Pointing_Up": (255, 255, 0),  # Cyjanowy
                "ILoveYou": (255, 255, 0)
            }
            return gesture_dict.get(gesture_info, (255, 255, 255))

        cv2.rectangle(imageA, (0, imageA.shape[0] - bar_height), (imageA.shape[1], imageA.shape[0]), parse_color(info),
                      -1)

    def save_result(result: vision.GestureRecognizerResult,
                    unused_output_image: mp.Image, timestamp_ms: int):
        global FPS, COUNTER, START_TIME

        # Calculate the FPS
        if COUNTER % fps_avg_frame_count == 0:
            FPS = fps_avg_frame_count / (time.time() - START_TIME)
            START_TIME = time.time()

        recognition_result_list.append(result)
        COUNTER += 1

    # Initialize the gesture recognizer model
    base_options = python.BaseOptions(model_asset_path=model)
    options = vision.GestureRecognizerOptions(base_options=base_options,
                                              running_mode=vision.RunningMode.LIVE_STREAM,
                                              num_hands=num_hands,
                                              min_hand_detection_confidence=min_hand_detection_confidence,
                                              min_hand_presence_confidence=min_hand_presence_confidence,
                                              min_tracking_confidence=min_tracking_confidence,
                                              result_callback=save_result)
    recognizer = vision.GestureRecognizer.create_from_options(options)
    # Initialize the window
    cv2.namedWindow(WIN_NAME, cv2.WINDOW_KEEPRATIO)
    # Continuously capture images from the camera and run inference
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            sys.exit(
                'ERROR: Unable to read from webcam. Please verify your webcam settings.'
            )
        if mirror == 1:
            image = cv2.flip(image, 1)
        # Convert the image from BGR to RGB as required by the TFLite model.
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_image)

        # Run gesture recognizer using the model.
        recognizer.recognize_async(mp_image, time.time_ns() // 1_000_000)

        # Show the FPS
        fps_text = 'FPS = {:.1f}'.format(FPS)
        text_location = (left_margin, row_size)
        current_frame = image
        cv2.putText(current_frame, fps_text, text_location, cv2.FONT_HERSHEY_DUPLEX,
                    font_size, text_color, font_thickness, cv2.LINE_AA)

        if recognition_result_list:
            # Draw landmarks and write the text for each hand.
            for hand_index, hand_landmarks in enumerate(
                    recognition_result_list[0].hand_landmarks):
                # Calculate the bounding box of the hand
                x_min = min([landmark.x for landmark in hand_landmarks])
                y_min = min([landmark.y for landmark in hand_landmarks])
                y_max = max([landmark.y for landmark in hand_landmarks])

                # Convert normalized coordinates to pixel values
                frame_height, frame_width = current_frame.shape[:2]
                x_min_px = int(x_min * frame_width)
                y_min_px = int(y_min * frame_height)
                y_max_px = int(y_max * frame_height)

                # Get gesture classification results
                if recognition_result_list[0].gestures:
                    gesture = recognition_result_list[0].gestures[hand_index]
                    category_name = gesture[0].category_name
                    score = round(gesture[0].score, 3)

                    handedness = recognition_result_list[0].handedness[hand_index]
                    handedness_category_name = handedness[0].category_name
                    handedness_score = round(handedness[0].score, 3)

                    result_text = f'{category_name}({format(score, ".1%")})'
                    result_text2 = f'{hand_index} {handedness_category_name}({format(handedness_score, ".1%")})'

                    handedness_index = handedness[0].index

                    # Compute text size
                    text_size = \
                        cv2.getTextSize(result_text, cv2.FONT_HERSHEY_DUPLEX, label_font_size,
                                        label_thickness)[0]
                    text_width, text_height = text_size

                    # Calculate text position (above the hand)
                    text_x = x_min_px - 50 # Adjust this value as needed
                    text_y = y_min_px - 10  # Adjust this value as needed

                    # Make sure the text is within the frame boundaries
                    if text_y < 0:
                        text_y = y_max_px + text_height

                    # Draw the text
                    cv2.putText(current_frame, result_text, (text_x, text_y),
                                cv2.FONT_HERSHEY_DUPLEX, label_font_size,
                                label_text_color, label_thickness, cv2.LINE_AA)
                    cv2.putText(current_frame, result_text2, (text_x, (text_y - text_height - 5)),
                                cv2.FONT_HERSHEY_DUPLEX, label_font_size,
                                label_text_color, label_thickness, cv2.LINE_AA)
                    # Print the text
                    print(f"Hand: {result_text}")

                    # Send the gesture trough serial port
                    if handedness_index == control_hand:
                        if output_mode == 1:
                            serial_function(ser, category_name)
                        if bar_visibility == 1:
                            draw_color_bar(current_frame, category_name)

                # Draw hand landmarks on the frame
                hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
                hand_landmarks_proto.landmark.extend([
                    landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y,
                                                    z=landmark.z) for landmark in
                    hand_landmarks
                ])
                mp_drawing.draw_landmarks(
                    current_frame,
                    hand_landmarks_proto,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

            recognition_frame = current_frame
            recognition_result_list.clear()

        if recognition_frame is not None:
            cv2.imshow(WIN_NAME, recognition_frame)

        # Stop the program if the ESC key is pressed or if the window is closed
        if cv2.waitKey(1) == 27 or cv2.getWindowProperty(WIN_NAME, cv2.WND_PROP_VISIBLE) < 1:
            break

    recognizer.close()
    cap.release()
    cv2.destroyAllWindows()


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '--model',
        help='Name of gesture recognition model.',
        required=False,
        default='gesture_recognizer.task')
    parser.add_argument(
        '--numHands',
        help='Max number of hands that can be detected by the recognizer.',
        required=False,
        default=2)
    parser.add_argument(
        '--minHandDetectionConfidence',
        help='The minimum confidence score for hand detection to be considered '
             'successful.',
        required=False,
        default=0.5)
    parser.add_argument(
        '--minHandPresenceConfidence',
        help='The minimum confidence score of hand presence score in the hand '
             'landmark detection.',
        required=False,
        default=0.5)
    parser.add_argument(
        '--minTrackingConfidence',
        help='The minimum confidence score for the hand tracking to be '
             'considered successful.',
        required=False,
        default=0.5)
    # Finding the camera ID can be very reliant on platform-dependent methods.
    # One common approach is to use the fact that camera IDs are usually indexed sequentially by the OS, starting from 0.
    # Here, we use OpenCV and create a VideoCapture object for each potential ID with 'cap = cv2.VideoCapture(i)'.
    # If 'cap' is None or not 'cap.isOpened()', it indicates the camera ID is not available.
    parser.add_argument(
        '--cameraId', help='Id of camera.', required=False, default=0)
    parser.add_argument(
        '--frameWidth',
        help='Width of frame to capture from camera.',
        required=False,
        default=640)
    parser.add_argument(
        '--frameHeight',
        help='Height of frame to capture from camera.',
        required=False,
        default=480)
    parser.add_argument(
        '--controlHand',
        help='Choose hand, left=1.',
        required=False,
        default=0)
    parser.add_argument(
        '--outputMode',
        help='Output mode, 0=without, 1=serial.',
        required=False,
        default=1)
    parser.add_argument(
        '--mirror',
        help='Mirror image, 0=off, 1=on.',
        required=False,
        default=0)
    parser.add_argument(
        '--barVisibility',
        help='Color bar visibility, 0=off, 1=on.',
        required=False,
        default=1)
    args = parser.parse_args()

    run(args.model, int(args.numHands), args.minHandDetectionConfidence,
        args.minHandPresenceConfidence, args.minTrackingConfidence,
        int(args.cameraId), args.frameWidth, args.frameHeight, int(args.controlHand), int(args.outputMode),
        int(args.mirror), int(args.barVisibility))


if __name__ == '__main__':
    main()
