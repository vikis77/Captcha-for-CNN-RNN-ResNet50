import streamlit as st

# 定义模型相关的全局静态变量
RNN = 'RNN预测模型'
# RNNPATH = r'RNN\ctc3-1.1.pth'
# RNNPATH = r'RNN\ctc3-1.2.pth'
# RNNPATH = r'RNN\ctc3-1.4.pth'
RNNPATH = r'RNN\ctc3-1.5.pth'
RNNACCPATH = r'RNN\训练结果_4.png'
RNNLOSSPATH = r'RNN\pr.jpg'
RNNACCRATE = '90%'

CNN = 'CNN预测模型'
# CNNPATH = r'CNN\model_1004-1.1.pth'
# CNNPATH = r'CNN\model_1004-1.2.pth' #输入图片大小固定->报错
# CNNPATH = r'CNN\model_1004-1.3.pth'
# CNNPATH = r'CNN\model_1004-1.4.pth'
# CNNPATH = r'CNN\model_1004-1.5.pth'
CNNPATH = r'CNN\model_1004-1.6.pth'
CNNACCPATH = r'CNN\acc.png'
CNNLOSSPATH = r'CNN\loss.png'
CNNACCRATE = '97%'

RESNET50 = 'ResNet50预测模型'
# RESNET50PATH = r'ResNet50\epoch=30-step=12121.ckpt'
RESNET50PATH = r'ResNet50\ResNet_mytrain_weigthts.pth'
RESNET50ACCPATH = r'ResNet50\pr图1.3.png'
RESNET50LOSSPATH = r'ResNet50\训练结果1.3.png'
RESNET50ACCRATE = '91%'

# 初始化会话状态
if 'session_state' not in st.session_state:
    st.session_state.session_state = {
        'acc': 0,
        'total': 50,
        'chose_model': 'RNN预测模型',
        'app_predict_code': '',
        'upload_name': '',
        'showRadio': False,
        'paste_context': '',
        'clipboard_image_exist': False,
        'user_input': '',
        "menuchoose":'主页'
    }
session_state = st.session_state.session_state

# 初始化 session_state 中的计时器状态
if 'start_time' not in st.session_state:
    st.session_state.start_time = None

if 'radio_selection' not in st.session_state:
    st.session_state.radio_selection = 'None'



# 模型路径字典
chose_model_path = {
    RNN: RNNPATH,
    CNN: CNNPATH,
    RESNET50: RESNET50PATH,
    '自定义模型': 'undefined'
}

# 定义时间延迟配置
TIME1 = {'t': 0.001, 'c11': 0.01, 'c12': 0.06, 'c21': 0.005, 'c22': 0.01, 'c32': 0.1, 'c41': 0.05}
TIME2 = {'t': 0.001, 'c11': 0.001, 'c12': 0.006, 'c21': 0.0005, 'c22': 0.005, 'c32': 0.1, 'c41': 0.005}
TIME3 = {'t': 0, 'c11': 0, 'c12': 0, 'c21': 0, 'c22': 0, 'c32': 0, 'c41': 0}
