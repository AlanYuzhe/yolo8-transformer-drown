from scipy.io import loadmat
import pandas as pd
from PIL import Image
import torch
from torch.utils.data import Dataset, DataLoader


mat_data = loadmat('/Users/yuzhewu/PycharmProjects/pythonProject1/gTruth_simple.mat')  # 替换为您的文件路径

# 提取数据
data_source = mat_data['dataSource'].flatten()  # 图像路径数组
label_data = mat_data['labelData']  # 标注数据

# 处理图像路径和标注数据
image_paths = []
labels = []

for index, path in enumerate(data_source):
    image_paths.append(path[0])  # 提取每个图像的路径
    label_row = label_data[index]  # 提取对应的标注数据
    label_list = [tuple(label[0]) for label in label_row if len(label) > 0]
    labels.append(label_list)

# 创建 DataFrame
df = pd.DataFrame({'image_path': image_paths, 'labels': labels})

# 显示 DataFrame 的前几行来验证
print(df.head())

def convert_boxes_to_yolo_format(labels, image_size):
    """
    将边界框坐标转换为 YOLO 格式。
    :param labels: 原始边界框坐标列表，格式为 [(x_min, y_min, width, height), ...]
    :param image_size: 图像尺寸，格式为 (width, height)
    :return: 转换后的标注列表
    """
    converted_labels = []
    im_width, im_height = image_size

    for box in labels:
        x_min, y_min, box_width, box_height = box
        x_center = x_min + box_width / 2
        y_center = y_min + box_height / 2

        # 归一化坐标
        x_center /= im_width
        y_center /= im_height
        box_width /= im_width
        box_height /= im_height

        converted_labels.append([x_center, y_center, box_width, box_height])

    return converted_labels

# 假设您的图像尺寸为 640x640
image_size = (640, 640)

# 对 DataFrame 中的每个标注应用转换
df['yolo_labels'] = df['labels'].apply(lambda x: convert_boxes_to_yolo_format(x, image_size))

# 显示转换后的标注
print(df.head())

class YOLOv5Dataset(Dataset):
    def __init__(self, dataframe, image_size):
        self.dataframe = dataframe
        self.image_size = image_size

    def __len__(self):
        return len(self.dataframe)

    def __getitem__(self, idx):
        # 加载图像
        img_path = self.dataframe.iloc[idx]['image_path']
        image = Image.open(img_path).convert('RGB')

        # 调整图像大小
        image = image.resize(self.image_size)

        # 转换图像为 PyTorch Tensor
        image = transforms.ToTensor()(image)

        # 获取标注数据
        boxes = torch.tensor(self.dataframe.iloc[idx]['yolo_labels'])

        sample = {'image': image, 'bboxes': boxes}

        return sample

# 设置图像大小（例如，YOLOv5s 使用 640x640）
image_size = (640, 640)

dataset = YOLOv5Dataset(df, image_size)

dataloader = DataLoader(dataset, batch_size=4, shuffle=True)
