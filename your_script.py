import cv2
import mediapipe as mp
from signalDanger import send_signal
from redconfig import read_source

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)

mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(read_source())

sended_signal = False

def determine_posture(landmarks):
    global sended_signal
    left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
    right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]
    left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP.value]
    right_hip = landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value]

    shoulder_avg_y = (left_shoulder.y + right_shoulder.y) / 2
    hip_avg_y = (left_hip.y + right_hip.y) / 2





    if abs(shoulder_avg_y - hip_avg_y) < 0.1:
        if sended_signal == False:
            sended_signal = True
            send_signal(state=0)


        return 'Lying down'



    else:
        return 'Standing'


while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    if not ret:
        break

    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = pose.process(image_rgb)

    image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

    if results.pose_landmarks:

        mp_drawing.draw_landmarks(image_bgr, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        posture = determine_posture(results.pose_landmarks.landmark)

        cv2.putText(image_bgr, posture, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('Pose Estimation', image_bgr)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()