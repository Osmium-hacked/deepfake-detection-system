import os
import shutil
import random

FACE_DIR = "data/faces"
OUTPUT_DIR = "data/dataset"
TRAIN_RATIO = 0.8

random.seed(42)  # reproducibility

def prepare_split(label):
    folders = [f for f in os.listdir(FACE_DIR) if f.startswith(label)]
    images = []

    for folder in folders:
        folder_path = os.path.join(FACE_DIR, folder)
        for img in os.listdir(folder_path):
            images.append(os.path.join(folder_path, img))

    random.shuffle(images)
    split_index = int(len(images) * TRAIN_RATIO)

    train_imgs = images[:split_index]
    val_imgs = images[split_index:]

    for img_path in train_imgs:
        shutil.copy(
            img_path,
            os.path.join(OUTPUT_DIR, "train", label)
        )

    for img_path in val_imgs:
        shutil.copy(
            img_path,
            os.path.join(OUTPUT_DIR, "val", label)
        )

    print(f"{label.upper()} → Train: {len(train_imgs)}, Val: {len(val_imgs)}")

prepare_split("real")
prepare_split("fake")
