import cv2
import os

VIDEO_DIR = "data/videos"
FRAME_DIR = "data/frames"

os.makedirs(FRAME_DIR, exist_ok=True)

def extract_frames(video_path, output_dir, every_n=10):
    cap = cv2.VideoCapture(video_path)
    count = 0
    saved = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if count % every_n == 0:
            frame_name = f"frame_{saved}.jpg"
            cv2.imwrite(os.path.join(output_dir, frame_name), frame)
            saved += 1

        count += 1

    cap.release()
    print(f"Extracted {saved} frames from {video_path}")

for video in os.listdir(VIDEO_DIR):
    video_path = os.path.join(VIDEO_DIR, video)
    video_name = os.path.splitext(video)[0]
    output_path = os.path.join(FRAME_DIR, video_name)

    os.makedirs(output_path, exist_ok=True)
    extract_frames(video_path, output_path)
