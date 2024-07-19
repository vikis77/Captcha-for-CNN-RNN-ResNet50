
import sys
sys.path.append("./RNN")
sys.path.append("./ResNet50")
sys.path.append("./CNN")
import string
import PIL
import torch
import Resnet50_CaptchaDataset
from Model import Model
from CNNLSTM_predict import predict
import train,main
from buildCaptchaModel import CaptchaModel
import model_predict
from App_setting import *

def app_predict(captcha_path,model_name):
    predict_result = ''
    if model_name == "RNN预测模型":
        characters = '-' + string.digits + string.ascii_uppercase
        characters = characters.replace('I','').replace('O','')
        width, height, n_len, n_classes = 192, 64, 4, len(characters)#192 64  
        ctc_model = Model(n_classes, input_shape=(3, height, width))
        ctc_model = torch.load(RNNPATH, map_location='cpu')  
        ctc_model.eval()  # 设置为评估模式 
        if torch.cuda.is_available():
            ctc_model = ctc_model.cuda() 
        prediction = predict(captcha_path, ctc_model)
        predict_result = prediction
    elif model_name == 'CNN预测模型':
        device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
        model = train.NeuralNetWork().to(device)
        model.load_state_dict(torch.load(CNNPATH, map_location=torch.device("cpu")))
        model.eval()
        CNN_captcha = main.predict(model,captcha_path)
        predict_result = CNN_captcha
    elif model_name == 'ResNet50预测模型':
        ckpt_path = RESNET50PATH
        pth_path = ckpt_path
        model = CaptchaModel()
        weights = torch.load(pth_path,map_location='cpu')
        model.load_state_dict(weights)
        predict_result = model_predict.single_predict(model, PIL.Image.open(captcha_path), Resnet50_CaptchaDataset.DECODEDICT)
    return predict_result

if __name__=='__main__':
    app_predict('identify_Code.png','RNN预测模型')