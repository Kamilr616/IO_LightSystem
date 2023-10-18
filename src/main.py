# main.py

__author__ = "Kamil Rataj"
__credits__ = ["Mateusz Ciszek", "Natalia Martemianow"]
__version__ = "0.0.1"
__maintainer__ = "Kamil Rataj"
__status__ = "Development"

# import numpy as np
# import math
# import os
from app import *


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
