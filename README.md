# YOLO8-Transformer-Drown

An end-to-end deep learning pipeline for detecting drowning persons in images and video by combining YOLOv5/YOLOv8 with a lightweight Transformer head.

---

## Project Overview

**YOLO8-Transformer-Drown** localizes human figures in images or video frames and classifies whether each person is drowning. The project evolves through:

1. YOLOv2 proof of concept  
2. YOLOv5 and SSD / Fast R-CNN benchmarks  
3. YOLOv8 upgrade  
4. YOLOv8 with a custom Transformer head for improved posture discrimination

The final model achieves at least 90% detection confidence on held-out test data.

---

## Key Features

**Model Evolution**  
- Initial experiments with YOLOv2  
- YOLOv5, SSD, and Fast R-CNN training and evaluation  
- YOLOv8 baseline  
- Transformer head integrated into YOLOv8’s feature maps

**Data Handling**  
- MATLAB `.mat` ground-truth annotations (`gTruth.mat`)  
- Example manual labels (`labeled.JPG`)  
- Support for additional test images (`test.jpg`, `dog.jpeg`)

**End-to-End Pipeline**  
- Training scripts (`yolov5.py`, YOLOv8 via Ultralytics CLI)  
- Jupyter notebooks for experiments (`yolo5.ipynb`, `Yolo8.ipynb`)  
- Inference and visualization (`Detection.py`, `1.py`)

**Performance**  
- Detection confidence ≥ 90%  

---

## Project Structure

- `Yolo8.ipynb` – YOLOv8 training and evaluation notebook  
- `Detection.py` – Script for running inference  
- `dataset.yaml` – Dataset configuration for training  
- `yolov8s.pt`, `yolov5s.pt`, `yolov8n.pt` – Pretrained model weights  
- `runs/` – Output directory for detection results  
- `image/` – Sample images for testing  
- `yolo5env/` – YOLOv5 environment setup files  
- `Project1.docx` – Project report and documentation  
- `README.md` – Project description and usage guide

---

## Results

The YOLOv8 + Transformer model achieves strong performance on the drowning detection task, with consistent confidence scores exceeding 90% and real-time inference capability. Detection output is saved under the `runs/` directory.

---

## License

This project is licensed under the MIT License.

## Author

This project was developed by:

- **Yuzhe Wu**  
- **Jiaqi Zhang**  
- **Cheng Qian**
