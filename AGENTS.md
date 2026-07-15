# AGENTS.md

Guidance for AI coding agents working in this repository.

## Project
**Hand-gesture → LED-strip** controller. A Python app (OpenCV + MediaPipe) recognizes
hand gestures from the webcam and sends a byte over **serial/USB** to firmware that
lights an addressable LED strip. Firmware exists for **ESP8266 (Arduino)** and
**NXP LPC (C++)**. (Street-lighting norm PN-EN 13201 was only an inspiration.)

## Layout
- `src/main.py` — gesture recognition + serial control (argparse CLI).
- `src/gesture_recognizer.task` — bundled MediaPipe model.
- `embedded/esp_8266_Arduino/…` — Arduino firmware · `embedded/IO_LedController_CPP/` — LPC firmware.
- `tests/test_cli.py` — CLI tests · `docs/` — reference PDFs.

## Build / run / test
- Run: `python src/main.py` (see `--serialPort`, e.g. `COM3` on Windows / `/dev/ttyACM0`
  on Linux; other flags documented in README).
- Tests: `python -m unittest discover -s tests`.
- Serial link is **9600 8N1**; the firmware must be flashed to the board separately.

## Conventions & good practices
- Keep paths **portable** — resolve the model relative to the script, don't hardcode
  absolute paths or COM ports (make them CLI-configurable).
- Commit firmware **source** only; never commit build output (`Debug/`, `*.o`, `*.axf`).
- MediaPipe 0.10.35 drawing uses `mediapipe.tasks.python.vision.drawing_utils` with
  Tasks landmarks and `HandLandmarksConnections`; verify imports when changing the
  dependency version because older releases exposed the legacy `mp.solutions` API.
- Update **both** `README.md` and `README.pl.md` together.

## Documentation
- [README.md](README.md) · [README.pl.md](README.pl.md)
- [Technical documentation](docs/TECHNICAL_DOCUMENTATION.md) · [Polski](docs/TECHNICAL_DOCUMENTATION.pl.md)
- License: **MIT** — see [LICENSE](LICENSE).

_Educational / portfolio project._
