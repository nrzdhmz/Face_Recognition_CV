# Face Recognition with Webcam

This project uses Python, `face_recognition`, and `OpenCV` to recognize a specific person’s face live from a webcam feed. It compares faces detected on the webcam against a base image of that person and labels the video feed accordingly.

## Features

- Load a base image of the authorized person
- Real-time face detection and recognition from webcam video
- Shows a green box and label if the face matches the base image
- Shows a red box and label if the face does not match
- Optimized for smoother video by resizing frames before processing

## Requirements

- Python 3.6+
- face_recognition
- dlib
- OpenCV (`opencv-python`)
- numpy

## Installation

Create a virtual environment and install dependencies:

```bash
python -m venv facevenv
source facevenv/bin/activate  # Linux/macOS
facevenv\Scripts\activate     # Windows

pip install cmake
pip install dlib
pip install face_recognition
pip install opencv-python
pip install numpy
