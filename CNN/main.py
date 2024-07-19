# main.py
import os
import torch
from PIL import Image
from train import NeuralNetWork
from loader import one_hot_decode
from torchvision import transforms
from setting import CODE_TYPE

device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
    
def predict(model, file_path):
    trans = transforms.Compose([
        transforms.Lambda(lambda img: img.convert('RGB') if img.mode == 'RGBA' else img),
        transforms.Resize((60, 160)),  # 确保图像尺寸与训练时一致
        transforms.ToTensor(),  # 转换为PyTorch张量，保持三通道
        # transforms.Normalize((0.25,0.25,0.25),(0.7,0.7,0.7))
        transforms.Normalize((0.001,0.001,0.001),(1,1,1))
    ])
    with torch.no_grad():
        X = trans(Image.open(file_path)).unsqueeze(0)  # 添加批次维度
        X = X.to(device)
        pred = model(X)
        text = one_hot_decode(pred.squeeze(0))  # 移除批次维度并解码
        return text


def main():
    print(device)
    model = NeuralNetWork().to(device)
    # model.load_state_dict(torch.load(f"E:/Python/newtest/new_test/model_{CODE_TYPE}.pth", map_location=torch.device("cpu")))
    model.load_state_dict(torch.load(f"./model_{CODE_TYPE}.pth", map_location=torch.device("cpu")))
    model.eval()

    correct = 0
    test_dir = rf"new_test\train\test_{CODE_TYPE}"
    total = len(os.listdir(test_dir))
    for filename in os.listdir(test_dir):
        file_path = f"{test_dir}/{filename}"
        real_captcha = file_path.split("-")[-1].replace(".png", "")
        pred_captcha = predict(model, file_path)
        if pred_captcha == real_captcha:
            correct += 1
            print(f"{file_path}的预测结果为{pred_captcha}，预测正确")
        else:
            print(f"{file_path}的预测结果为{pred_captcha}，预测错误")
    accuracy = f"{correct / total * 100:.2f}%"
    print(accuracy)


if __name__ == '__main__':
    main()