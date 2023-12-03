image_width, image_height = 1280, 720

# 示例标注数据
label_data = [
    [444, 105, 447, 475], [973, 292, 343, 680],
    [417, 97, 502, 585],  [991, 253, 359, 670]
    # ... 其他标注数据
]

# 转换标注为 YOLOv5 格式的函数
def convert_to_yolov5(label, img_width, img_height):
    x_min, y_min, width, height = label
    x_center = (x_min + width / 2) / img_width
    y_center = (y_min + height / 2) / img_height
    width /= img_width
    height /= img_height
    return [0, x_center, y_center, width, height]  # 假设 class_id 为 0

# 转换所有标注
converted_labels = [convert_to_yolov5(label, image_width, image_height) for label in label_data]

# 打印转换后的标注
for label in converted_labels:
    print(label)