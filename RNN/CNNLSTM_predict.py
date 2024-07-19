import torch
import numpy as np
from PIL import Image  
import torchvision.transforms as transforms  
import string

from Model import Model
from pathlib import Path  

characters = '-' + string.digits + string.ascii_uppercase
characters = characters.replace('I','').replace('O','')
width, height, n_len, n_classes = 160, 60, 4, len(characters)#192 64  

def decode(sequence):
    a = ''.join([characters[x] for x in sequence])
    s = ''.join([x for j, x in enumerate(a[:-1]) if x != characters[0] and x != a[j+1]])
    if len(s) == 0:
        return ''
    if a[-1] != characters[0] and s[-1] != a[-1]:
        s += a[-1]
    return s

def decode_target(sequence):
    return ''.join([characters[x] for x in sequence]).replace(' ', '')

def calc_acc(target, output):
    output_argmax = output.detach().permute(1, 0, 2).argmax(dim=-1)
    target = target.cpu().numpy()
    output_argmax = output_argmax.cpu().numpy()
    a = np.array([decode_target(true) == decode(pred) for true, pred in zip(target, output_argmax)])
    return a.mean()


  

  
# 定义图片预处理函数  
def preprocess_image(image_path):  
    image = Image.open(image_path).convert('RGB')  
    transform = transforms.Compose([  
        transforms.Resize((height, width)),  
        transforms.ToTensor(),  
        # transforms.Normalize(mean=[0.620, 0.620, 0.620], std=[0.270, 0.270, 0.270])  
        # transforms.Normalize(mean=[0.700, 0.700, 0.700], std=[0.900, 0.900, 0.900])  
        # transforms.Normalize(mean=[0.200, 0.200, 0.200], std=[0.700, 0.700, 0.700])  
        transforms.Normalize(mean=[0.250, 0.250, 0.250], std=[0.600, 0.600, 0.600])  
    ])  
    image = transform(image).unsqueeze(0)  # 增加批次维度  
    return image  
  
# 定义预测函数  
def predict(image_path, model):  
    image = preprocess_image(image_path)  
    if torch.cuda.is_available():  
        image = image.cuda()  
    with torch.no_grad():  
        output = model(image)  
    output_argmax = output.detach().permute(1, 0, 2).argmax(dim=-1)  
    prediction = decode(output_argmax[0])  
    return prediction


if __name__=='__main__':
    # 使用示例  
    # 加载模型
    width, height, n_len, n_classes = 192, 64, 4, len(characters)#192 64  
    model = Model(n_classes, input_shape=(3, height, width))
    model = model.cuda()
    model = torch.load('ctc3.pth')  
    model.eval()  # 设置为评估模式  
    folder_path = 'test_img'
    # prediction = predict('./test_img/0C60.png', model)
    # print(f'Predicted captcha:{prediction}')

    total=0
    a=0
    for path in Path(folder_path).rglob('*'):  
        if path.is_file():  
            total+=1
            prediction = predict(f'./test_img/{path.name}', model)
            if 'V' in prediction and len(prediction)==5:
                prediction = prediction.replace('V', '', 1)
            if 'Y' in prediction and len(prediction)==5:
                prediction = prediction.replace('Y', '', 1)
            if 'T' in prediction and len(prediction)==5:
                prediction = prediction.replace('T', '', 1)
            if prediction == path.name[:4]:
                print(f'真实结果：{path.name[:4]} 预测结果:{prediction}  True')
                a+=1
            else:
                print(f'真实结果：{path.name[:4]} 预测结果:{prediction}  False')
    print(f'正确率：{a/total}')
    

    