# Hand Gesture Game Controller

This project uses your webcam to detect hand gestures and simulates keypresses to control a game like Asphalt 9. It leverages computer vision and gesture recognition to provide a hands-free gaming experience.

## Features
- Detects hand gestures using your webcam
- Maps gestures to game controls (e.g., left, right, accelerate, brake)
- Simulates keypresses to control games

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the main script:
   ```bash
   python main.py
   ```

## Files
- `main.py`: Main entry point, runs webcam loop
- `gesture_utils.py`: Hand gesture detection utilities
- `key_controller.py`: Simulates keypresses based on gestures
- `requirements.txt`: Python dependencies

## Notes
- Actual gesture detection and key simulation logic should be implemented in `gesture_utils.py` and `key_controller.py`.
- For key simulation, you may need to run as administrator on Windows. 