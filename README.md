# 🖐️ Gesture-Based Game Controller for PC Games

Control PC games using **hand gestures** and your **webcam**!  
This project uses **MediaPipe**, **OpenCV**, and **PyAutoGUI**/**Pynput** to detect gestures and simulate keyboard inputs — turning your hand into a virtual game controller.

---

## 🚀 Features

- 🖐️ **One-hand control**: Tilt your hand to steer (left/right), open palm to move forward, fist to brake.
- 👐 **Two-hand steering mode**: Use both hands to mimic a steering wheel — turn left/right based on hand angles.
- 🎮 **Simulated keyboard input**: Works with any PC game that supports keyboard driving.
- 👁️ Real-time video feed with gesture display and FPS counter.
- 🛠️ Easy to customize and extend with new gestures.

---

## 📸 Demo

> Coming Soon – Add a screen recording or GIF here showing the gesture controls in action!

---

## 🧠 How It Works

- Uses **MediaPipe Hands** to track hand landmarks in real-time.
- Classifies gesture using hand landmark positions and angles.
- Simulates corresponding keypress actions using `pynput` or `pyautogui`.
- Loop continues with webcam feed until user presses `q` to quit.

---


---

## ⚙️ Installation

### 🔹 Prerequisites:
- Python 3.8+
- Webcam

### 🔹 Step-by-step Setup:

```bash
# 1. Clone the repository
git clone https://github.com/your-username/gesture-control.git
cd gesture-control

# 2. Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # on Linux/macOS
venv\Scripts\activate     # on Windows

# 3. Install dependencies
pip install -r requirements.txt
# Run the main script
python main.py
opencv-python
mediapipe
pynput
numpy
pyautogui

