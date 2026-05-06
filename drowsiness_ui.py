# enhanced_drowsiness_ui.py
import cv2
import mediapipe as mp
import numpy as np
import streamlit as st
from threading import Thread
from playsound import playsound
import time


def play_alarm():
    try:
        playsound("alarm.wav")
    except:
        pass


def eye_aspect_ratio(eye):
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
    C = np.linalg.norm(eye[0] - eye[3])
    return (A + B) / (2.0 * C)


mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1)
mp_drawing = mp.solutions.drawing_utils

st.set_page_config(layout="wide")
st.title("🚗 Driver Drowsiness Detection")
st.write("Monitor your eyes and alert if drowsy!")

col1, col2 = st.columns([3, 1])
frame_placeholder = col1.empty()
start_button = col2.button("Start Detection")
stop_button = col2.button("Stop Detection")

EAR_THRESHOLD = 0.25
CONSEC_FRAMES = 15

run_detection = False
counter = 0
ear_list = []

# Webcam
cap = cv2.VideoCapture(0)

while True:
    if start_button:
        run_detection = True
        start_button = False
    if stop_button:
        run_detection = False
        stop_button = False

    if run_detection:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb_frame)

        h, w, _ = frame.shape
        alert = False

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                # Eye landmarks
                left_eye_idx = [33, 160, 158, 133, 153, 144]
                right_eye_idx = [362, 385, 387, 263, 373, 380]

                left_eye = np.array(
                    [
                        (
                            int(face_landmarks.landmark[i].x * w),
                            int(face_landmarks.landmark[i].y * h),
                        )
                        for i in left_eye_idx
                    ]
                )
                right_eye = np.array(
                    [
                        (
                            int(face_landmarks.landmark[i].x * w),
                            int(face_landmarks.landmark[i].y * h),
                        )
                        for i in right_eye_idx
                    ]
                )

                leftEAR = eye_aspect_ratio(left_eye)
                rightEAR = eye_aspect_ratio(right_eye)
                ear = (leftEAR + rightEAR) / 2.0
                ear_list.append(ear)

                for x, y in np.concatenate((left_eye, right_eye)):
                    cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

                if ear < EAR_THRESHOLD:
                    counter += 1
                    if counter >= CONSEC_FRAMES:
                        cv2.putText(
                            frame,
                            "DROWSINESS ALERT!",
                            (50, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1.5,
                            (0, 0, 255),
                            3,
                        )
                        alert = True
                        Thread(target=play_alarm).start()
                else:
                    counter = 0

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame_rgb, channels="RGB")

        col2.markdown(
            f"**Current EAR:** {ear_list[-1]:.2f}" if ear_list else "**Current EAR:** 0"
        )
        col2.markdown(f"**Drowsiness Counter:** {counter}")
        col2.markdown("⚠️ Alert!" if alert else "✅ Safe")

    time.sleep(0.01)  # small delay to reduce CPU usage

cap.release()
