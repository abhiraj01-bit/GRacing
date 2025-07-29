import math

def calculate_angle(p1, p2):
    x_diff = p2.x - p1.x
    y_diff = p2.y - p1.y
    return math.degrees(math.atan2(y_diff, x_diff))

def detect_gesture(frame, multi_hand_landmarks):
    """
    Detects hand gesture from MediaPipe multi_hand_landmarks.
    Returns one of: 'forward', 'brake', 'left', 'right', or None if no gesture detected.
    """
    if not multi_hand_landmarks:
        return None

    # Single hand logic
    if len(multi_hand_landmarks) == 1:
        hand_landmarks = multi_hand_landmarks[0]
        lm = hand_landmarks.landmark
        TIP_IDS = [8, 12, 16, 20]  # Index, Middle, Ring, Pinky tips
        MCP_IDS = [5, 9, 13, 17]   # Index, Middle, Ring, Pinky MCPs
        INDEX_ID = 5
        PINKY_ID = 17

        open_fingers = 0
        for tip, mcp in zip(TIP_IDS, MCP_IDS):
            if lm[tip].y < lm[mcp].y:
                open_fingers += 1
        hand_open = open_fingers == 4
        hand_closed = open_fingers == 0

        index_x = lm[INDEX_ID].x
        pinky_x = lm[PINKY_ID].x

        if hand_open:
            return "forward"
        elif hand_closed:
            return "brake"
        elif index_x < pinky_x:
            return "left"
        elif index_x > pinky_x:
            return "right"

    # Two hand logic
    elif len(multi_hand_landmarks) == 2:
        lm1 = multi_hand_landmarks[0].landmark
        lm2 = multi_hand_landmarks[1].landmark
        wrist1 = lm1[0]
        wrist2 = lm2[0]
        angle = calculate_angle(wrist1, wrist2)
        # Normalize angle to [-180, 180]
        if angle > 180:
            angle -= 360
        elif angle < -180:
            angle += 360
        # Distance between wrists
        dist = math.hypot(wrist2.x - wrist1.x, wrist2.y - wrist1.y)
        if dist < 0.08:  # Threshold for 'brake' (wrists very close)
            return "brake"
        if angle > 15:
            return "right"
        elif angle < -15:
            return "left"
        elif abs(angle) <= 15:
            return "forward"

    return None 