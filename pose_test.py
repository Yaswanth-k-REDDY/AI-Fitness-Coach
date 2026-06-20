import cv2
import time
import pandas as pd
from datetime import datetime

from pose_detector import PoseDetector
from utils import calculate_angle
from voice import speak
cap = cv2.VideoCapture(0)

detector = PoseDetector()

counter = 0
stage = None
last_spoken = 0
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

        # LEFT ARM
        left_shoulder = [landmarks[11].x, landmarks[11].y]
        left_elbow = [landmarks[13].x, landmarks[13].y]
        left_wrist = [landmarks[15].x, landmarks[15].y]

        # RIGHT ARM
        right_shoulder = [landmarks[12].x, landmarks[12].y]
        right_elbow = [landmarks[14].x, landmarks[14].y]
        right_wrist = [landmarks[16].x, landmarks[16].y]

        left_angle = calculate_angle(
            left_shoulder,
            left_elbow,
            left_wrist
        )

        right_angle = calculate_angle(
            right_shoulder,
            right_elbow,
            right_wrist
        )

        # Active arm
        angle = min(left_angle, right_angle)

        if angle > 160:
            stage = "DOWN"

        if angle < 40 and stage == "DOWN":
            stage = "UP"
            counter += 1
            if counter == 5 and counter != last_spoken:
                #speak("5 reps completed")
                last_spoken = counter

            elif counter > 5 and (counter - 5) % 10 == 0 and counter != last_spoken:
                speak(f"{counter} reps completed")
                last_spoken = counter

        cv2.putText(
            frame,
            f"Left Angle: {int(left_angle)}",
            (10, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2
        )

        cv2.putText(
            frame,
            f"Right Angle: {int(right_angle)}",
            (10, 90),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"Reps: {counter}",
            (10, 130),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            2
        )

        cv2.putText(
            frame,
            f"Stage: {stage}",
            (10, 170),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

    elapsed_time = int(time.time() - start_time)

    cv2.putText(
        frame,
        f"Time: {elapsed_time}s",
        (10, 210),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("AI Fitness Coach", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

# Save Workout Log

data = {
    "Date": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
    "Exercise": ["Bicep Curl"],
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
speak("Workout completed. Great job!")
cap.release()
cv2.destroyAllWindows()

print("\nWorkout Saved Successfully!")
print(f"Total Reps: {counter}")
print(f"Duration: {elapsed_time} seconds")