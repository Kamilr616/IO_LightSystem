# Changelog

All notable changes to this project are documented in this file.

The project follows [Semantic Versioning](https://semver.org/).

## [1.1.0] - 2026-07-15

### Added

- Bilingual README and technical documentation.
- Portable CLI tests and GitHub Actions coverage for Python 3.10 and 3.12.
- MIT project license, security policy, release notes and third-party notices.
- Verified MediaPipe Gesture Recognizer model provenance and SHA-256.

### Changed

- Resolved the bundled model path relative to `src/main.py`.
- Updated drawing imports for the MediaPipe Tasks API in version 0.10.35.
- Aligned gesture bytes, serial settings and ESP8266 pin configuration.
- Bounded direct Python dependency versions for reproducible installation.

### Removed

- Generated LPC build output, IDE metadata and the bundled SDK archive.
- Proprietary PKN standards and NXP manuals; official references are retained as links.

## [1.0.0] - 2024-01-24

- Initial gesture-recognition, serial-control and firmware release.
