import cv2
import os

FRAME_DIR = "data/frames"
FACE_DIR = "data/faces"

os.makedirs(FACE_DIR, exist_ok=True)

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def detect_and_save_faces(frame_path, output_dir):
    img = cv2.imread(frame_path)
    if img is None:
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    for i, (x, y, w, h) in enumerate(faces):
        face = img[y:y+h, x:x+w]
        face_filename = f"face_{i}.jpg"
        cv2.imwrite(os.path.join(output_dir, face_filename), face)

for video_folder in os.listdir(FRAME_DIR):
    video_frame_path = os.path.join(FRAME_DIR, video_folder)
    output_face_path = os.path.join(FACE_DIR, video_folder)

    os.makedirs(output_face_path, exist_ok=True)

    for frame in os.listdir(video_frame_path):
        frame_path = os.path.join(video_frame_path, frame)
        detect_and_save_faces(frame_path, output_face_path)

    print(f"Processed faces for {video_folder}")
