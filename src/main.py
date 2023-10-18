# main.py

__author__ = "Kamil Rataj"
__credits__ = ["Mateusz Ciszek", "Natalia Martemianow"]
__version__ = "0.0.1"
__maintainer__ = "Kamil Rataj"
__status__ = "Development"

import cv2
import mediapipe as mp
# import numpy as np
# import math
# import os
# from app import *

class HandTracker:
    def __init__(self, mode=False, max_hands=2, detection_con=0.5, model_complexity=1, track_con=0.5):
        # Inicjalizacja parametrów śledzenia dłoni
        self.mode = mode
        self.max_hands = max_hands
        self.detection_con = detection_con
        self.model_complexity = model_complexity
        self.track_con = track_con
        # Inicjalizacja modułów MediaPipe
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.mode, self.max_hands, self.model_complexity,
                                         self.detection_con, self.track_con)
        self.mp_draw = mp.solutions.drawing_utils

    def find_hands(self, image, draw=True):
        # Przetwarzanie obrazu w poszukiwaniu dłoni
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(image_rgb)

        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                if draw:
                    # Rysowanie punktów i połączeń dłoni
                    self.mp_draw.draw_landmarks(image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
        return image

    def find_positions(self, image, hand_no=0, draw=True):
        # Znajdowanie pozycji (landmarków) dłoni
        lm_list = []
        if self.results.multi_hand_landmarks:
            hand = self.results.multi_hand_landmarks[hand_no]
            for id, lm in enumerate(hand.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append([id, cx, cy])
                if draw:
                    # Rysowanie okręgów wokół landmarków
                    cv2.circle(image, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
        return lm_list


def main():
    cap = cv2.VideoCapture(0)
    tracker = HandTracker()
    window_open = True  # Zmienna śledząca, czy okno jest otwarte czy zamknięte
    print('Inżynieria oprogramowania')

    while window_open:
        success, image = cap.read()

        image = cv2.flip(image, 1)
        image = tracker.find_hands(image)
        lm_list = tracker.find_positions(image)

        if len(lm_list) != 0:
            print(lm_list[4])

        cv2.imshow("Hand Tracking", image)

        # Zamknięcie okna po naciśnięciu klawisza 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            window_open = False  # Zmiana wartości zmiennej na False, aby przerwać pętlę

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
