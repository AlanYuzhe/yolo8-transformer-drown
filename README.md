# Project_1
# Using Yolov5 and Yolov8 to primarily train the model to detect the drowning people. To combine transformer with Yolov8 to improve the model.
#For this project, we first used YOLOv2 model for idea validation, and then gradually upgraded the YOLO version to v8. Then we found that YOLOv8+transformer works relatively well after training with Fast R-CNN and SSD models respectively. So this program was adopted.
#When we trained the model, we only trained to find the person and then recognize whether he is drowning or not, and we didn't do how to find the person from the big image, so we can only intercept the person for him to recognize. Then for the sake of clarity and visualization, so we extracted the results and drew them on a diagram of the poster.According to the running results can be obtained, the detection confidence is basically more than 90%.
![image](https://github.com/AlanYuzhe/Project_1/assets/77837061/0c33cd07-6280-4fb8-8a2d-acf44f26575b)
<img width="1035" alt="31ea8849ab8daca31fef87ed01b453d" src="https://github.com/AlanYuzhe/Project_1/assets/77837061/7fb20e01-2d9e-446d-8764-cace8d1b5e15">
