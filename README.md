# Hand Tracking Mouse Controller

This project uses `OpenCV`, `Mediapipe`, and `PyAutoGUI` to detect hand movements via a webcam and control the mouse cursor based on finger positions. It also allows for mouse clicks using specific hand gestures.

## Features
- **Hand Tracking**: Uses Mediapipe to detect hand landmarks.
- **Mouse Movement**: Controls the mouse cursor based on the position of a specific finger.
- **Mouse Click**: Simulates a mouse click when a particular gesture is recognized (finger pinch).

## Requirements
Before running the project, ensure you have the following Python libraries installed:
- `opencv-python`
- `mediapipe`
- `pyautogui`

You can install them using pip:
```bash
pip install opencv-python mediapipe pyautogui
```

## How It Works
The script captures video from the webcam.
It processes the video frame to detect hand landmarks using Mediapipe's hand detection model.
The position of the index finger (landmark 7) is mapped to the screen coordinates to control the mouse.
When the distance between the thumb (landmark 3) and the index finger (landmark 7) is small (less than 20 pixels), a mouse click is triggered.

## Usage
1. Ensure your webcam is connected.
2. Run the script:
```
python hand_tracking_mouse.py
```
3. Use your hand in front of the webcam. The mouse cursor will move according to your index finger.
4. To click, bring your thumb and index finger close together.
