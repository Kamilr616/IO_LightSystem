# main.py

__author__ = "Kamil Rataj"
__credits__ = ["Mateusz Ciszek", "Natalia Martemianow"]
__version__ = "0.0.1"
__maintainer__ = "Kamil Rataj"
__status__ = "Development"

# import math
# import os
# from app import *
import serial
# import time

from tracker import *

WIN_NAME = "Inteligentne oswietlenie - IO"
SERIAL_PORT = "/dev/ttyACM1"  # Change this to the correct port


def serial_function(ser, value):
    if ser.in_waiting == 0:
        # time.sleep(2)
        ser.write(value.encode())
    ser.flush()


def main():
    # Inicjalizacja kamery i klasy śledzącej dłonie
    cap = cv2.VideoCapture(0)
    tracker = HandTracker()
    window_open = True  # Zmienna śledząca, czy okno jest otwarte czy zamknięte
    position_info = "pozycja nieznana"
    print(WIN_NAME)

    ser = serial.Serial()
    ser.port = SERIAL_PORT
    ser.baudrate = 9600
    ser.bytesize = serial.EIGHTBITS
    ser.parity = serial.PARITY_NONE
    ser.stopbits = serial.STOPBITS_ONE
    ser.timeout = 1
    mapped_value_old = 0
    ser.open()

    while window_open:
        success, image = cap.read()
        image = cv2.flip(image, 1)
        image = tracker.find_hands(image)
        lm_list = tracker.find_positions(image)

        if len(lm_list) != 0:
            hand_x, hand_y = lm_list[9][1], lm_list[9][2]
            position_info = f"Pozycja dłoni: x = {hand_x} | y = {hand_y}|"

            cv2.circle(image, (hand_x, hand_y), 30, (0, 255, 0), cv2.FILLED)
            cv2.rectangle(image, (hand_x - 20, 460), (hand_x + 20, 500), (0, 255, 255), cv2.FILLED)

            print("\r" + position_info, end="", flush=True)
            mapped_value = int((hand_x / 640) * 9)  # Map hand_x to a value between 0 and 9
            if mapped_value != mapped_value_old:
                mapped_value_old = mapped_value
                serial_function(ser, str(mapped_value))

        else:
            # W przypadku braku pozycji dłoni
            print("\rNie wykryto dłoni! Ostatnia " + position_info, end="", flush=True)

        cv2.imshow(WIN_NAME, image)

        # Zamknięcie okna po naciśnięciu klawisza 'esc'
        if cv2.waitKey(1) & 0xFF == 27 or cv2.getWindowProperty(WIN_NAME, cv2.WND_PROP_VISIBLE) < 1:
            window_open = False  # Zmiana wartości zmiennej na False, aby przerwać pętlę

    cap.release()
    cv2.destroyAllWindows()
    ser.close()


if __name__ == "__main__":
    main()
