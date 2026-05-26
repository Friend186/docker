import os
import kaggle
from ultralytics import YOLO


# --- 1. KAGGLE DOWNLOAD ---
dataset_name = "nardengerges/accident-detection" 
extract_folder = "/workspace/dataset"

print(f"Fetching {dataset_name} directly from Kaggle...")
kaggle.api.authenticate()
kaggle.api.dataset_download_cli(dataset_name, unzip=True, path=extract_folder)
print("✅ Download complete!")

yaml_path = "/workspace/docker_data.yaml"

# Mapping the exact folder from your screenshot
dataset_folder = f"{extract_folder}/Car Accident.v3-car-accident-v5.yolov8"

print("Generating  YAML...")
yaml_content = f"""
train: {dataset_folder}/train/images
val: {dataset_folder}/valid/images
test: {dataset_folder}/test/images

nc: 2
names:
  0: Accident
  1: Non Accident
"""

with open(yaml_path, 'w') as f:
    f.write(yaml_content)

# --- 3. YOLO TRAINING ---
print("Loading Model...")
model = YOLO('yolo11n.pt') 

print("🔥 Starting Training...")
results = model.train(
    data=yaml_path,
    epochs=300,
    imgsz=640,
    device=0, # <--- THIS IS THE ONLY CHANGE! Forces GPU usage.
    batch=16,
    project="/workspace/docker_runs", 
    name='accident_model'
)
print("✅ Training Complete!")

# docker run --pull always \
#   -e KAGGLE_USERNAME="accident" \
#   -e KAGGLE_KEY="KGAT_1ad0dfe246daa7d8b688b0632ee231c3" \
#   -v $(pwd):/workspace/docker_runs \
#   theerachotounlum2/test:latest

# docker run --gpus all --pull always \
#   -e KAGGLE_USERNAME="accident" \
#   -e KAGGLE_KEY="KGAT_1ad0dfe246daa7d8b688b0632ee231c3" \
#   -v $(pwd):/workspace/docker_runs \
#   theerachotounlum2/test:latest