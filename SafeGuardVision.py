import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)

cap = cv2.VideoCapture("video538630767234385562.mp4")

def determine_pose(landmarks):

    left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
    right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]
    left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP.value]
    right_hip = landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value]
    left_knee = landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value]
    right_knee = landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value]

    shoulder_mid_y = (left_shoulder.y + right_shoulder.y) / 2
    hip_mid_y = (left_hip.y + right_hip.y) / 2
    knee_mid_y = (left_knee.y + right_knee.y) / 2

    if knee_mid_y > hip_mid_y and hip_mid_y > shoulder_mid_y:
        return "Стоя"
    elif knee_mid_y < hip_mid_y and hip_mid_y < shoulder_mid_y:
        return "Сидя"
    elif abs(knee_mid_y - hip_mid_y) < 0.1 and abs(hip_mid_y - shoulder_mid_y) < 0.1:
        return "Лежа"
    else:
        return "Неизвестно"

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    if not ret:
        break

    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = pose.process(image_rgb)

    image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

    if results.pose_landmarks:
        for idx, pose_landmarks in enumerate(results.pose_landmarks):

            mp_drawing.draw_landmarks(
                image_bgr,
                pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2)
            )

            pose_label = determine_pose(pose_landmarks.landmark)

            cv2.putText(image_bgr, f"Pose {idx + 1}: {pose_label}", (10, 30 + idx * 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('Multi-Person Pose Detection', image_bgr)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()