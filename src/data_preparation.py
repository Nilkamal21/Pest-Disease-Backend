import os
import random
import shutil
from glob import glob
RAW_DIR = r'C:\Users\adhik\OneDrive\Desktop\pest_disease_detection\data\raw_images'
PROCESSED_TRAIN_DIR = r'C:\Users\adhik\OneDrive\Desktop\pest_disease_detection\data\processed\train'
PROCESSED_VAL_DIR = r'C:\Users\adhik\OneDrive\Desktop\pest_disease_detection\data\processed\val'

VAL_SPLIT_RATIO = 0.2

os.makedirs(PROCESSED_TRAIN_DIR, exist_ok=True)
os.makedirs(PROCESSED_VAL_DIR, exist_ok=True)

def prepare_data():
    class_folders = [f for f in os.listdir(RAW_DIR) if os.path.isdir(os.path.join(RAW_DIR, f))]
    for class_name in class_folders:
        src_class_folder = os.path.join(RAW_DIR, class_name)
        images = glob(os.path.join(src_class_folder, '*.jpg')) + glob(os.path.join(src_class_folder, '*.png'))
        random.shuffle(images)

        val_count = int(len(images) * VAL_SPLIT_RATIO)
        train_images = images[val_count:]
        val_images = images[:val_count]

        train_class_folder = os.path.join(PROCESSED_TRAIN_DIR, class_name)
        val_class_folder = os.path.join(PROCESSED_VAL_DIR, class_name)
        os.makedirs(train_class_folder, exist_ok=True)
        os.makedirs(val_class_folder, exist_ok=True)

        # Copy train images
        for img_path in train_images:
            shutil.copy(img_path, train_class_folder)

        # Copy val images
        for img_path in val_images:
            shutil.copy(img_path, val_class_folder)

        print(f'Class {class_name}: {len(train_images)} train, {len(val_images)} val')

if __name__ == "__main__":
    prepare_data()
