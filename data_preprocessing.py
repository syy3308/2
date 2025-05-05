import json
import os
import cv2
import logging

logging.basicConfig(level=logging.INFO)

def find_image_in_directories(image_id, directories):
    """
    在多个目录中查找图片文件。
    """
    for directory in directories:
        for file in os.listdir(directory):
            # 模糊匹配文件名
            if image_id in file:
                img_path = os.path.join(directory, file)
                print(f"Found image: {img_path}")
                return img_path
    return None

def load_annotations(file_path):
    annotations = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                annotations.append(json.loads(line.strip()))
    except Exception as e:
        logging.error(f"Error loading annotations: {e}")
    return annotations

def preprocess_data(image_dirs, annotation_file):
    annotations = load_annotations(annotation_file)
    data = []
    for anno in annotations:
        # 在多个目录中查找图片
        img_path = find_image_in_directories(anno['ID'], image_dirs)
        if not img_path:
            logging.warning(f"Image not found for ID: {anno['ID']}")
            continue
        logging.info(f"Found image: {img_path}")
        img = cv2.imread(img_path)
        if img is None:
            logging.warning(f"Failed to load image: {img_path}")
            continue
        bboxes = anno.get('gtboxes', [])
        data.append((img, bboxes))
    return data

if __name__ == "__main__":
    # 定义多个图片目录
    image_dirs = [
        "D:/ProgramData/PyCharm Community Edition 2024.3.5/PycharmProjects/PythonProject2/CrowdHuman/CrowdHuman_train01",
        "D:/ProgramData/PyCharm Community Edition 2024.3.5/PycharmProjects/PythonProject2/CrowdHuman/CrowdHuman_train02",
        "D:/ProgramData/PyCharm Community Edition 2024.3.5/PycharmProjects/PythonProject2/CrowdHuman/CrowdHuman_train03"
    ]

    annotation_file = "D:/ProgramData/PyCharm Community Edition 2024.3.5/PycharmProjects/PythonProject2/CrowdHuman/annotation_train.odgt"

    train_data = preprocess_data(image_dirs=image_dirs, annotation_file=annotation_file)
    logging.info(f"Preprocessed {len(train_data)} samples.")