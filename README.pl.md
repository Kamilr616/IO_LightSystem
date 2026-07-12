# 💡 IO LightSystem — oświetlenie sterowane gestami

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-wizja-5C3EE8?logo=opencv&logoColor=white)](https://opencv.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-rozpoznawanie%20gest%C3%B3w-0097A7?logo=google&logoColor=white)](https://developers.google.com/mediapipe)
[![ESP8266](https://img.shields.io/badge/ESP8266-Arduino-000000?logo=espressif&logoColor=white)](https://www.espressif.com/)
[![NXP LPC](https://img.shields.io/badge/NXP-LPCXpresso-EB1700?logo=nxp&logoColor=white)](https://www.nxp.com/)
[![Licencja: MIT](https://img.shields.io/badge/Licencja-MIT-yellow.svg)](LICENSE)

> 🇬🇧 [English version](README.md)

> 🗓️ **Okres realizacji:** 2023–2024

**System oświetlenia sterowany gestami dłoni.** Aplikacja w Pythonie rozpoznaje gesty dłoni z kamery przy użyciu **MediaPipe** i **OpenCV**, a rozpoznany gest wysyła przez **łącze szeregowe (serial)** do mikrokontrolera, który steruje **paskiem LED RGB (NeoPixel)** — machnięcie dłonią zmienia światło.

Projekt powstał jako **projekt z Inżynierii Oprogramowania**, początkowo osadzony wokół inteligentnego oświetlenia (europejska norma oświetlenia drogowego **PN-EN 13201**, dołączona w [`docs/`](docs/), była pierwotną inspiracją) i ewoluował w to demo sterowania kolorem gestami. Był też jedną z inspiracji do pracy inżynierskiej **AI Sign Language Translator**.

## ✨ Funkcje

- ✋ **Rozpoznawanie gestów w czasie rzeczywistym** — MediaPipe Gesture Recognizer (`src/gesture_recognizer.task`) na strumieniu z kamery (OpenCV)
- 🎨 **7 gestów → kolory i komendy** — każdy gest mapuje się na kolor na pasku ekranowym oraz na bajt sterujący wysyłany do sterownika LED
- 🔌 **Sterowanie przez serial** — gesty strumieniowane portem szeregowym (9600 baud, 8N1) do mikrokontrolera
- 🔧 **Dwa warianty firmware** sterownika LED — **ESP8266 (Arduino)** oraz **NXP LPC (LPCXpresso, C++)**, oba sterujące paskiem NeoPixel
- ⚙️ **Konfigurowalność** — kamera (id/rozdzielczość), dłoń sterująca (lewa/prawa), progi detekcji/śledzenia, lustrzane odbicie obrazu, widoczność paska koloru, tryb wyjścia i port szeregowy (flagi CLI)

## 🖐️ Mapa gestów

| Gest | Kolor na ekranie | Bajt serial |
|------|------------------|-------------|
| 👍 `Thumb_Up` | zielony | `A` |
| 👎 `Thumb_Down` | purpurowy | `B` |
| ✋ `Open_Palm` | niebieski | `C` |
| ✊ `Closed_Fist` | żółty | `D` |
| ✌️ `Victory` | spring green | `E` |
| ☝️ `Pointing_Up` | cyjan | `F` |
| 🤟 `ILoveYou` | czerwony | `G` |
| *(brak / nieznany)* | biały | `X` |

## 🧩 Jak to działa

```
Kamera ──▶ Aplikacja Python (OpenCV + MediaPipe GestureRecognizer)
                     │  rozpoznany gest → bajt sterujący
                     ▼
              Port szeregowy (9600 8N1)
                     ▼
     Mikrokontroler  ──▶  pasek LED RGB (NeoPixel)
     (ESP8266 / NXP LPC)
```

## 📂 Struktura repozytorium

| Ścieżka | Opis |
|---------|------|
| `src/main.py` | Aplikacja — obraz z kamery, rozpoznawanie gestów, pasek koloru, wyjście serial |
| `src/gesture_recognizer.task` | Model MediaPipe Gesture Recognizer |
| `src/requirements.txt` | Zależność Pythona (MediaPipe) |
| `embedded/esp_8266_Arduino/` | Firmware sterownika LED NeoPixel na ESP8266 (Arduino) |
| `embedded/IO_LedController_CPP/` | Firmware sterownika LED NeoPixel na NXP LPC (LPCXpresso, C++) |
| `docs/` | Dokumentacja projektu i norma PN-EN 13201 (pierwotna inspiracja) |

## 🚀 Szybki start

### 1. Aplikacja Python

```bash
git clone https://github.com/Kamilr616/IO_LightSystem.git
cd IO_LightSystem
pip install mediapipe opencv-python pyserial
python src/main.py --serialPort COM3        # Windows
# python src/main.py --serialPort /dev/ttyACM0   # Linux
```

Pełna lista opcji: `python src/main.py --help`. Przydatne flagi:

| Flaga | Znaczenie | Domyślnie |
|-------|-----------|-----------|
| `--serialPort` | Port szeregowy sterownika LED | `/dev/ttyACM0` |
| `--outputMode` | `0` = brak, `1` = serial | `1` |
| `--cameraId` | Indeks kamery | `0` |
| `--controlHand` | `0` = prawa, `1` = lewa | `0` |
| `--mirrorImage` | `0` = odbicie, `1` = brak | `0` |
| `--barVisibility` | `0` = pokaż pasek, `1` = ukryj | `1` |
| `--numHands` | Maks. liczba wykrywanych dłoni | `2` |

### 2. Firmware sterownika LED

Wgraj **jeden** ze sterowników na płytkę i podłącz pasek NeoPixel:

- **ESP8266 (Arduino):** otwórz `embedded/esp_8266_Arduino/Led_controller_arduino/Led_controller_arduino.ino` w Arduino IDE i wgraj.
- **NXP LPC (LPCXpresso):** otwórz `embedded/IO_LedController_CPP/` w MCUXpresso IDE i wgraj.

Sterownik odczytuje bajty sterujące z łącza szeregowego i ustawia kolor paska.

## 👥 Zespół

| Osoba | Rola |
|-------|------|
| **Kamil Rataj** | Autor i opiekun — aplikacja gestów, protokół serial, firmware |
| Mateusz Ciszek | Współtwórca |
| Natalia Martemianow | Współtwórczyni |

## 📄 Licencja

Projekt na licencji [MIT](LICENSE).

## 👤 Autor

**Kamil Rataj** — [GitHub](https://github.com/Kamilr616) · [LinkedIn](https://www.linkedin.com/in/kamil-r-153ab7121/)
