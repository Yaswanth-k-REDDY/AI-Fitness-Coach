import mediapipe as mp

print("MediaPipe Version:", mp.__version__)

try:
    from mediapipe.tasks.python import vision
    print("Tasks API Available ✅")
except Exception as e:
    print("Error:", e)