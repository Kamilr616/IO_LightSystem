# Third-Party Notices

This file records third-party material bundled with or directly required by IO LightSystem v1.1.0. The project-level MIT license does not replace the licenses listed here.

## Bundled components

### MediaPipe Gesture Recognizer model

- File: `src/gesture_recognizer.task`
- Upstream: [MediaPipe Gesture Recognizer float16 model](https://storage.googleapis.com/mediapipe-models/gesture_recognizer/gesture_recognizer/float16/1/gesture_recognizer.task)
- Verification: SHA-256 `97952348cf6a6a4915c2ea1496b4b37ebabc50cbbf80571435643c455f2b0482`
- Copyright: The MediaPipe Authors / Google LLC
- License: Apache License 2.0; see [`LICENSES/Apache-2.0.txt`](LICENSES/Apache-2.0.txt)

The hash matches the model downloaded by the official [MediaPipe Gesture Recognizer Python sample](https://github.com/google-ai-edge/mediapipe-samples/blob/main/examples/gesture_recognizer/python/gesture_recognizer.ipynb).

### Arm CMSIS headers

- Files: `embedded/IO_LedController_CPP/CMSIS/`
- Upstream: [Arm CMSIS 5](https://github.com/ARM-software/CMSIS_5)
- Copyright: Arm Limited
- License: Apache License 2.0; see [`LICENSES/Apache-2.0.txt`](LICENSES/Apache-2.0.txt)

### NXP legacy MCUXpresso SDK 2.x sources

- Files: NXP/Freescale-authored files under `embedded/IO_LedController_CPP/` outside the `CMSIS/` directory
- Upstream: [NXP legacy MCUXpresso SDK](https://github.com/nxp-mcuxpresso/legacy-mcux-sdk)
- Copyright: NXP, Freescale Semiconductor, Inc. and Code Red Technologies Ltd., as retained in individual source headers
- License: BSD 3-Clause; see [`LICENSES/BSD-3-Clause.txt`](LICENSES/BSD-3-Clause.txt)

### ESP8266 sketch based on Adafruit NeoPixel example code

- File: `embedded/esp_8266_Arduino/Led_controller_arduino/Led_controller_arduino.ino`
- Upstream: [Adafruit NeoPixel `buttoncycler` example](https://github.com/adafruit/Adafruit_NeoPixel/blob/master/examples/buttoncycler/buttoncycler.ino)
- Copyright: Adafruit Industries, Phil Burgess and contributors; IO LightSystem modifications by Kamil Rataj and contributors
- License: LGPL-3.0-or-later; see [`LICENSES/LGPL-3.0-or-later.txt`](LICENSES/LGPL-3.0-or-later.txt)

### Demonstration screenshot source image

- File: `docs/gesture-recognition.png`
- Source asset: the `victory.jpg` test image downloaded by the official [MediaPipe sample notebook](https://github.com/google-ai-edge/mediapipe-samples/blob/main/examples/gesture_recognizer/python/gesture_recognizer.ipynb)
- Original image source attribution: Pixabay, as recorded by the upstream notebook
- Terms: [Pixabay Content License](https://pixabay.com/service/license-summary/)

The bundled file is a transformed application screenshot with overlays, not a standalone redistribution of the source photograph.

## Direct dependencies not bundled

Installed distributions include their own license metadata and any transitive notices.

| Component | Required version | License | Upstream |
|---|---:|---|---|
| MediaPipe | `0.10.35` | Apache-2.0 | [google-ai-edge/mediapipe](https://github.com/google-ai-edge/mediapipe) |
| OpenCV Contrib Python | `>=4.9,<6` | Apache-2.0 for OpenCV 4.5+ | [opencv/opencv-python](https://github.com/opencv/opencv-python) |
| pySerial | `>=3.5,<4` | BSD-3-Clause | [pyserial/pyserial](https://github.com/pyserial/pyserial) |
| Adafruit NeoPixel | Arduino build dependency | LGPL-3.0-or-later | [adafruit/Adafruit_NeoPixel](https://github.com/adafruit/Adafruit_NeoPixel) |

## External proprietary references

PKN standards, NXP manuals, data sheets and board schematics are not bundled with the release. Official links and the reason for exclusion are documented in [`docs/REFERENCES.md`](docs/REFERENCES.md).
