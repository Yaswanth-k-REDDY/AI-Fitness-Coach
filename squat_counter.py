import cv2
import time
import pandas as pd
from datetime import datetime

from pose_detector import PoseDetector
from utils import calculate_angle

cap = cv2.VideoCapture(0)

detector = PoseDetector()

counter = 0
stage = None

start_time = time.time()

while True:

    success, frame = cap.read()

    if not success:
        break

    results = detector.detect_pose(frame)

    frame = detector.draw_landmarks(
        frame,
        results
    )

    if results.pose_landmarks:

        landmarks = results.pose_landmarks[0]

        hip = [
            landmarks[24].x,
            landmarks[24].y
        ]

        knee = [
            landmarks[26].x,
            landmarks[26].y
        ]

        ankle = [
            landmarks[28].x,
            landmarks[28].y
        ]

        angle = calculate_angle(
            hip,
            knee,
            ankle
        )

        if angle > 160:
            stage = "UP"

        if angle < 90 and stage == "UP":
            stage = "DOWN"
            counter += 1

        cv2.putText(
            frame,
            f"Knee Angle: {int(angle)}",
            (10, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"Squats: {counter}",
            (10, 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            2
        )

        cv2.putText(
            frame,
            f"Stage: {stage}",
            (10, 150),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

    elapsed_time = int(
        time.time() - start_time
    )

    cv2.putText(
        frame,
        f"Time: {elapsed_time}s",
        (10, 200),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 0),
        2
    )

    cv2.imshow(
        "AI Squat Counter",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

data = {
    "Date": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
    "Exercise": ["Squat"],
    "Reps": [counter],
    "Duration": [elapsed_time]
}

df = pd.DataFrame(data)

df.to_csv(
    "workout_logs.csv",
    mode="a",
    header=False,
    index=False
)

cap.release()
cv2.destroyAllWindows()

print("\nWorkout Saved Successfully!")
print(f"Total Squats: {counter}")
print(f"Duration: {elapsed_time} seconds")