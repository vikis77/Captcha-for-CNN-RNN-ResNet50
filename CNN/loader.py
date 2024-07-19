# loader.py
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from PIL import Image
import torch
import os
from setting import CODE_TYPE, SEED, CHAR_NUMBER, BATCH_SIZE


def one_hot_encode(label, length=CHAR_NUMBER):
    """将固定长度的字符转为独热码向量"""
    if len(label) != length:
        raise ValueError(f"Label '{label}' must be exactly {length} characters long")
    chars = list(label)
    cols = len(SEED)  # 假设 SEED 在这个文件或已导入的模块中定义
    result = torch.zeros((length * cols,), dtype=float)
    for i, char in enumerate(chars):
        if char in SEED:
            j = SEED.index(char)
            result[i * cols + j] = 1.0
        else:
            raise ValueError(f"Invalid character '{char}' in label '{label}'")  # 无效字节在label中
    return result

# ...（与之前相同）

def one_hot_decode(pred_result):
    """将独热码转为字符"""
    pred_result = pred_result.view(-1, len(SEED))
    # print(pred_result)
    index_list = torch.argmax(pred_result, dim=1)
    # print((index_list))
    text = "".join([SEED[i] for i in index_list])
    return text

# ...（与之前相同）

class ImageDataSet(Dataset):
    def __init__(self, dir_path, transform=None):
        super(ImageDataSet, self).__init__()
        self.img_path_list = [f"{dir_path}/{filename}" for filename in os.listdir(dir_path)]
        self.transform = transform

    def __getitem__(self, idx):
        image_path = self.img_path_list[idx]
        image = Image.open(image_path)
        if image.mode == 'RGBA':  # 假设4通道图像是RGBA格式的
            image = image.convert('RGB')  # 转换为RGB格式，丢弃A（alpha）通道
        if self.transform:
            image = self.transform(image)

        label = image_path.split('/')[-1].split('.')[0].split('-')[-1]
        label = one_hot_encode(label, CHAR_NUMBER)

        return image, label

    def __len__(self):
        return len(self.img_path_list)


def get_transform():
    # 注意：这里我们添加了Resize来确保所有图像都是相同的大小
    transform = transforms.Compose([
        transforms.Resize((60, 160)),  # 将图像大小调整为60x160
        transforms.ToTensor(),  # 转换为PyTorch张量
    ])
    return transform


def get_loader(path):
    transform = get_transform()
    dataset = ImageDataSet(path, transform=transform)
    dataloader = DataLoader(dataset, BATCH_SIZE, shuffle=True)
    return dataloader

if __name__ == '__main__':
    train_dataloader = get_loader(r'E:\Python\Captcha_GEN-v1.3\Captcha_GEN\Captcha_GEN\gen_pic')
    test_dataloader = get_loader(r'E:\Python\Captcha_GEN-v1.3\Captcha_GEN\Captcha_GEN\test_1004')
    for X, y in train_dataloader:
        print(X.shape)
        print(y.shape)
        break


