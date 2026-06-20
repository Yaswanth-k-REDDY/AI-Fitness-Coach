import cv2
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision


class PoseDetector:

    def __init__(self):

        base_options = python.BaseOptions(
            model_asset_path="models/pose_landmarker.task"
        )

        options = vision.PoseLandmarkerOptions(
            base_options=base_options,
            output_segmentation_masks=False
        )

        self.landmarker = vision.PoseLandmarker.create_from_options(
            options
        )

    def detect_pose(self, frame):

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb_frame
        )

        results = self.landmarker.detect(mp_image)

        return results

    def draw_landmarks(self, frame, results):
        if not results.pose_landmarks:
            return frame

        height, width, _ = frame.shape

        landmarks = results.pose_landmarks[0]

        points = []

        for landmark in landmarks:
            x = int(landmark.x * width)
            y = int(landmark.y * height)

            points.append((x, y))

            cv2.circle(
                frame,
                (x, y),
                5,
                (0, 255, 0),
                -1
            )

        connections = [
            (11, 12),  # shoulders
            (11, 13),
            (13, 15),
            (12, 14),
            (14, 16),
            (11, 23),
            (12, 24),
            (23, 24),
            (23, 25),
            (25, 27),
            (24, 26),
            (26, 28)
        ]

        for start, end in connections:
            cv2.line(
                frame,
                points[start],
                points[end],
                (255, 0, 0),
                2
            )

        return frame