import scipy.io
import os

# 加载 .mat 文件的路径
mat_file_path = '/Users/yuzhewu/PycharmProjects/pythonProject1/gTruth_simple.mat'

# 输出标注文件的目录
output_dir = '/Users/yuzhewu/PycharmProjects/pythonProject1'

# 加载 .mat 文件
mat_data = scipy.io.loadmat(mat_file_path)
label_data = mat_data['labelData']
data_source = mat_data['dataSource']

# 图像的尺寸为 224x224 像素
img_width, img_height = 224, 224

for idx, path in enumerate(data_source):
    img_labels = label_data[idx]
    # 提取文件名（这里只需要文件名，不包括任何路径）
    base_name = os.path.basename(path)
    # 创建 .txt 文件名
    txt_filename = os.path.splitext(base_name)[0] + '.txt'
    txt_path = os.path.join(output_dir, txt_filename)

    with open(txt_path, 'w') as file:
        for cell in img_labels:
            if cell.size > 0:
                label = cell[0]
                x_min, y_min, width, height = label
                x_center = (x_min + width / 2) / img_width
                y_center = (y_min + height / 2) / img_height
                width /= img_width
                height /= img_height
                # 假设 class_id 为 0，如果有多个类别，这里需要相应地进行修改
                file.write(f"0 {x_center} {y_center} {width} {height}\n")
        print(f"File saved: {txt_path}")  # 打印保存的文件路径
