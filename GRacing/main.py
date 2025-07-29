import cv2
import mediapipe as mp
from gesture_utils import detect_gesture
from key_controller import perform_key_action

def main():
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    hands = mp_hands.Hands(static_image_mode=False,
                           max_num_hands=2,
                           min_detection_confidence=0.5,
                           min_tracking_confidence=0.5)

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)
        multi_hand_landmarks = results.multi_hand_landmarks if results.multi_hand_landmarks else []
        if multi_hand_landmarks:
            for handLms in multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

        # Pass all hand landmarks to gesture detection
        gesture = detect_gesture(frame, multi_hand_landmarks)
        if gesture:
            print(f"Detected gesture: {gesture}")
            perform_key_action(gesture)

        cv2.imshow('Game Gesture Control', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    hands.close()

if __name__ == "__main__":
    main() 