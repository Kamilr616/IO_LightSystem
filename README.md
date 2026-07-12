# 💡 IO LightSystem — Gesture-Controlled Lighting

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-vision-5C3EE8?logo=opencv&logoColor=white)](https://opencv.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-gesture%20recognition-0097A7?logo=google&logoColor=white)](https://developers.google.com/mediapipe)
[![ESP8266](https://img.shields.io/badge/ESP8266-Arduino-000000?logo=espressif&logoColor=white)](https://www.espressif.com/)
[![NXP LPC](https://img.shields.io/badge/NXP-LPCXpresso-EB1700?logo=nxp&logoColor=white)](https://www.nxp.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> 🇵🇱 [Wersja polska](README.pl.md)

> 🗓️ **Project period:** 2023–2024

A **hand-gesture–controlled lighting system**. A Python app recognizes hand gestures from a webcam using **MediaPipe** and **OpenCV**, and sends the recognized gesture over a **serial link** to a microcontroller that drives an **RGB NeoPixel LED strip** — so a wave of the hand changes the light.

The project started as a **Software Engineering course project** framed around intelligent lighting (the European road-lighting standard **PN-EN 13201**, included in [`docs/`](docs/), was the initial inspiration) and evolved into this gesture-controlled RGB demo. It was also one of the inspirations for the engineering thesis **AI Sign Language Translator**.

## ✨ Features

- ✋ **Real-time hand-gesture recognition** — MediaPipe Gesture Recognizer (`src/gesture_recognizer.task`) over an OpenCV camera stream
- 🎨 **7 gestures → colors & commands** — each recognized gesture maps to a color on an on-screen bar and to a control byte sent to the LED controller
- 🔌 **Serial control** — gestures are streamed over a serial port (9600 baud, 8N1) to the microcontroller
- 🔧 **Two firmware options** for the LED controller — **ESP8266 (Arduino)** and **NXP LPC (LPCXpresso, C++)**, both driving a NeoPixel strip
- ⚙️ **Configurable** — camera id/resolution, controlling hand (left/right), detection/tracking confidence, image mirroring, color-bar visibility, output mode and serial port (all via CLI flags)

## 🖐️ Gesture map

| Gesture | On-screen color | Serial byte |
|---------|-----------------|-------------|
| 👍 `Thumb_Up` | Green | `A` |
| 👎 `Thumb_Down` | Magenta | `B` |
| ✋ `Open_Palm` | Blue | `C` |
| ✊ `Closed_Fist` | Yellow | `D` |
| ✌️ `Victory` | Spring green | `E` |
| ☝️ `Pointing_Up` | Cyan | `F` |
| 🤟 `ILoveYou` | Red | `G` |
| *(none / unknown)* | White | `X` |

## 🧩 How it works

```
Webcam ──▶ Python app (OpenCV + MediaPipe GestureRecognizer)
                     │  recognized gesture → control byte
                     ▼
              Serial port (9600 8N1)
                     ▼
     Microcontroller  ──▶  NeoPixel RGB LED strip
     (ESP8266 / NXP LPC)
```

## 📂 Repository structure

| Path | Description |
|------|-------------|
| `src/main.py` | Application — camera capture, gesture recognition, color bar, serial output |
| `src/gesture_recognizer.task` | MediaPipe Gesture Recognizer model bundle |
| `src/requirements.txt` | Python dependency (MediaPipe) |
| `embedded/esp_8266_Arduino/` | ESP8266 (Arduino) NeoPixel LED-controller firmware |
| `embedded/IO_LedController_CPP/` | NXP LPC (LPCXpresso, C++) NeoPixel LED-controller firmware |
| `docs/` | Course documentation and the PN-EN 13201 road-lighting standard (initial inspiration) |

## 🚀 Getting started

### 1. Python app

```bash
git clone https://github.com/Kamilr616/IO_LightSystem.git
cd IO_LightSystem
pip install mediapipe opencv-python pyserial
python src/main.py --serialPort COM3        # Windows
# python src/main.py --serialPort /dev/ttyACM0   # Linux
```

Run `python src/main.py --help` for all options. Useful flags:

| Flag | Meaning | Default |
|------|---------|---------|
| `--serialPort` | Serial port of the LED controller | `/dev/ttyACM0` |
| `--outputMode` | `0` = none, `1` = serial | `1` |
| `--cameraId` | Camera index | `0` |
| `--controlHand` | `0` = right, `1` = left | `0` |
| `--mirrorImage` | `0` = mirror, `1` = no | `0` |
| `--barVisibility` | `0` = show color bar, `1` = hide | `1` |
| `--numHands` | Max hands to detect | `2` |

### 2. LED controller firmware

Flash **one** of the controllers to your board and wire a NeoPixel strip:

- **ESP8266 (Arduino):** open `embedded/esp_8266_Arduino/Led_controller_arduino/Led_controller_arduino.ino` in the Arduino IDE and upload.
- **NXP LPC (LPCXpresso):** open `embedded/IO_LedController_CPP/` in MCUXpresso IDE and flash.

The controller reads the control bytes from the serial link and sets the strip color accordingly.

## 👥 Team

| Member | Role |
|--------|------|
| **Kamil Rataj** | Author & maintainer — gesture app, serial protocol, firmware |
| Mateusz Ciszek | Contributor |
| Natalia Martemianow | Contributor |

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 👤 Author

**Kamil Rataj** — [GitHub](https://github.com/Kamilr616) · [LinkedIn](https://www.linkedin.com/in/kamil-r-153ab7121/)
