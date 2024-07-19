import sys
sys.path.append('Captcha_GEN')

import io 
import streamlit as st
import win32clipboard
import time
import streamlit as st
from PIL import Image
from gen_captcha_QIN import generate_captcha_image
from Predict import app_predict
from App_setting import *


def my_progress(t):
    """显示动态进度条"""
    progress_container = st.empty()
    for percent_complete in range(1, 100):
        time.sleep(t)
        progress_container.progress(percent_complete, '进度')
    time.sleep(0.5)  # 等待0.5秒，确保进度条更新完成后再清除
    progress_container.empty()

def progress_sidebar(t):
    """在侧边栏显示动态进度条"""
    progress_container = st.sidebar.empty()
    my_bar = progress_container.progress(0, '进度')  # 初始值

    for percent_complete in range(100):
        time.sleep(t) # 模拟处理时间
        my_bar.progress(percent_complete + 1, '进度')
    time.sleep(0.1)  # 等待0.5秒，确保进度条更新完成后再清除
    progress_container.empty()

def run_batch_prediction(total_predictions):
    """
    运行批量验证码预测 50次/500次
    参数:
        total_predictions (int): 批量预测的次数
    """
    st.session_state.start_time = time.time()
    acc = 0  # 正确预测的数量
    acc_rate_now, show_acc_rate = 0, 0
    session_state['acc_rate_now'] = acc_rate_now

    # 创建 Streamlit 空白元素，用于动态更新页面内容
    empty1 = st.empty()  # 生成验证码
    empty2 = st.empty()  # 展示验证码
    empty3 = st.empty()  # 预测结果
    empty10 = st.empty() # 正在预测
    empty5 = st.empty()  # 预测正确
    empty6 = st.empty()  # 预测错误
    empty4 = st.empty()  # 正确率
    empty7 = st.empty()  # 用时
    empty9 = st.empty()  # 用时metric
    empty8 = st.empty()  # 预测进度条

    for i in range(1,total_predictions+1):
        elapsed_time = time.time() - st.session_state.start_time  # 计算已用时间
        # identify_code, identifyCode_img_path = gen_captcha_text_and_image()  # 生成验证码及图像路径
        identify_code, identifyCode_img_path = generate_captcha_image()  # 生成验证码及图像路径
        
        session_state['identify_code'] = identify_code
        session_state['identifyCode_img_path'] = identifyCode_img_path
        identifyCode_img_path.save('App\Images\identify_Code.png')  # 保存验证码图像

        empty1.text("生成验证码：")
        empty2.image('App\Images\identify_Code.png', width=200)  # 显示验证码图像
        empty3.text("预测结果：")

        # 清空之前的预测结果显示
        empty5.empty()
        empty6.empty()
        empty10.info("正在预测...")

        hours = int(elapsed_time // 3600)
        minutes = int((elapsed_time % 3600) // 60)
        seconds = int(elapsed_time % 60)

        # 初次显示用时和进度
        if i == 1:
            empty9.metric(f'用时：{hours:02}:{minutes:02}:{seconds:02}', f"进度 {i}/{total_predictions}", f'+正确率：{acc_rate_now}%')

        # 调用模型进行预测
        app_predict_code = app_predict('App\Images\identify_Code.png', session_state['chose_model'])
        with empty8.container():
            my_progress(session_state['TIMEFREE'].get('c22'))  # 显示进度条

        empty3.text(f"预测结果：{app_predict_code}")
        time.sleep(0.3)  # 等待一段时间

        # 判断预测结果是否正确并更新显示
        if session_state['identify_code'] == app_predict_code:
            empty6.empty()
            empty10.empty()
            empty5.success("预测正确")
            acc += 1
        else:
            empty5.empty()
            empty10.empty()
            empty6.error("预测错误")

        # 更新正确率
        acc_rate_now = round(((acc / i) * 100), 2)
        if acc_rate_now>=session_state['acc_rate_now']:
            empty9.metric(f'用时：{hours:02}:{minutes:02}:{seconds:02}',f"进度 {i}/{total_predictions}",f'+正确率：{acc_rate_now}%😲')
        else:
            empty9.metric(f'用时：{hours:02}:{minutes:02}:{seconds:02}',f"进度 {i}/{total_predictions}",f'-正确率：{acc_rate_now}%😟')
        session_state['acc_rate_now'] = acc_rate_now

        time.sleep(1)  # 等待一段时间
        empty3.text("预测结果：")

def run_simgle_prediction(user_input="None",path='App\Images\identify_Code.png'):
    """运行单次验证码预测"""
    empty1 = st.empty()  # 生成验证码
    empty2 = st.empty()  # 展示验证码
    empty3 = st.empty()  # 预测结果
    empty10 = st.empty() # 正在预测
    empty5 = st.empty()  # 预测正确
    empty6 = st.empty()  # 预测错误
    empty8 = st.empty()  # 预测进度条

    if user_input=='None':
        identify_code, identifyCode_img_path = generate_captcha_image()  # 生成验证码及图像路径
    else:
        identify_code, identifyCode_img_path = generate_captcha_image(user_input)

    session_state['identify_code'] = identify_code
    session_state['identifyCode_img_path'] = identifyCode_img_path
    identifyCode_img_path.save('App\Images\identify_Code.png')  # 保存验证码图像

    empty1.text("生成验证码：")
    empty2.image('App\Images\identify_Code.png', width=200)  # 显示验证码图像
    empty3.text("预测结果：")
    empty5.empty()
    empty6.empty()
    empty10.info("正在预测...")

    # 调用模型进行预测
    app_predict_code = app_predict(path, session_state['chose_model'])
    with empty8.container():
        my_progress(session_state['TIMEFREE'].get('c22'))  # 显示进度条

    empty3.text(f"预测结果：{app_predict_code}")
    time.sleep(0.3)  # 等待一段时间

    # 判断预测结果是否正确并更新显示
    if session_state['identify_code'] == app_predict_code:
        empty6.empty()
        empty10.empty()
        empty5.success("预测正确")
    else:
        empty5.empty()
        empty10.empty()
        empty6.error("预测错误")

def run_batch_prediction_fast(total_predictions):
    """
    运行批量验证码预测 50次/500次
    参数:
        total_predictions (int): 批量预测的次数
    """
    st.session_state.start_time = time.time()
    acc = 0  # 正确预测的数量
    acc_rate_now, show_acc_rate = 0, 0
    session_state['acc_rate_now'] = acc_rate_now

    # 创建 Streamlit 空白元素，用于动态更新页面内容
    empty1 = st.empty()  # 生成验证码
    empty2 = st.empty()  # 展示验证码
    empty3 = st.empty()  # 预测结果
    empty10 = st.empty() # 正在预测
    empty5 = st.empty()  # 预测正确
    empty6 = st.empty()  # 预测错误
    empty4 = st.empty()  # 正确率
    empty7 = st.empty()  # 用时
    empty9 = st.empty()  # 用时metric
    empty8 = st.empty()  # 预测进度条

    for i in range(1, total_predictions+1):
        elapsed_time = time.time() - st.session_state.start_time  # 计算已用时间
        # identify_code, identifyCode_img_path = gen_captcha_text_and_image()  # 生成验证码及图像路径
        identify_code, identifyCode_img_path = generate_captcha_image()  # 生成验证码及图像路径
        
        session_state['identify_code'] = identify_code
        session_state['identifyCode_img_path'] = identifyCode_img_path
        identifyCode_img_path.save('App\Images\identify_Code.png')  # 保存验证码图像

        empty1.text("生成验证码：")
        empty2.image('App\Images\identify_Code.png', width=200)  # 显示验证码图像
        empty3.text("预测结果：")

        # 清空之前的预测结果显示
        empty5.empty()
        empty6.empty()
        empty10.info("正在预测...")

        hours = int(elapsed_time // 3600)
        minutes = int((elapsed_time % 3600) // 60)
        seconds = int(elapsed_time % 60)

        # 初次显示用时和进度
        if i == 1:
            empty9.metric(f'用时：{hours:02}:{minutes:02}:{seconds:02}', f"进度 {i}/{total_predictions}", f'+正确率：{acc_rate_now}%')

        # 调用模型进行预测
        app_predict_code = app_predict('App\Images\identify_Code.png', session_state['chose_model'])
        # with empty8.container():
            # my_progress(session_state['TIMEFREE'].get('c22'))  # 显示进度条

        empty3.text(f"预测结果：{app_predict_code}")
        time.sleep(0.3)  # 等待一段时间

        # 判断预测结果是否正确并更新显示
        if session_state['identify_code'] == app_predict_code:
            empty6.empty()
            empty10.empty()
            empty5.success("预测正确")
            acc += 1
        else:
            empty5.empty()
            empty10.empty()
            empty6.error("预测错误")

        # 更新正确率
        acc_rate_now = round(((acc / i) * 100), 2)
        if acc_rate_now>=session_state['acc_rate_now']:
            empty9.metric(f'用时：{hours:02}:{minutes:02}:{seconds:02}',f"进度 {i}/{total_predictions}",f'+正确率：{acc_rate_now}%😲')
        else:
            empty9.metric(f'用时：{hours:02}:{minutes:02}:{seconds:02}',f"进度 {i}/{total_predictions}",f'-正确率：{acc_rate_now}%😟')
        session_state['acc_rate_now'] = acc_rate_now

        # time.sleep(1)  # 等待一段时间
        empty3.text("预测结果：")

def run_simgle_prediction_fast(user_input="None",path='App\Images\identify_Code.png'):
    """运行单次验证码预测"""
    empty1 = st.empty()  # 生成验证码
    empty2 = st.empty()  # 展示验证码
    empty3 = st.empty()  # 预测结果
    empty10 = st.empty() # 正在预测
    empty5 = st.empty()  # 预测正确
    empty6 = st.empty()  # 预测错误

    if user_input=='None':
        identify_code, identifyCode_img_path = generate_captcha_image()  # 生成验证码及图像路径
    else:
        identify_code, identifyCode_img_path = generate_captcha_image(user_input)

    session_state['identify_code'] = identify_code
    session_state['identifyCode_img_path'] = identifyCode_img_path
    identifyCode_img_path.save('App\Images\identify_Code.png')  # 保存验证码图像

    empty1.text("生成验证码：")
    empty2.image('App\Images\identify_Code.png', width=200)  # 显示验证码图像
    empty3.text("预测结果：")
    empty5.empty()
    empty6.empty()
    empty10.info("正在预测...")

    # 调用模型进行预测
    app_predict_code = app_predict(path, session_state['chose_model'])
    empty3.text(f"预测结果：{app_predict_code}")

    # 判断预测结果是否正确并更新显示
    if session_state['identify_code'] == app_predict_code:
        empty6.empty()
        empty10.empty()
        empty5.success("预测正确")
    else:
        empty5.empty()
        empty10.empty()
        empty6.error("预测错误")

def change_selection(option):
    """回调函数，改变单选按钮的选择"""
    st.session_state.radio_selection = option

def get_clipboard_image():
    """获取剪切板中的图像数据"""
    win32clipboard.OpenClipboard()
    try:
        if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_DIB):
            data = win32clipboard.GetClipboardData(win32clipboard.CF_DIB)
            image_bytes = io.BytesIO(data)
            image = Image.open(image_bytes)
            return image
        else:
            return None
    finally:
        win32clipboard.CloseClipboard()


def sidebar_bg_gradient():
    """侧边栏背景颜色渐变"""
    st.markdown(
        st.markdown(
            f"""
            <style>
            [data-testid="stSidebar"] > div:first-child {{
                background: linear-gradient(135deg, '#FAEBD7', '#E6E6FA');
                background-size: cover;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    )

def main_bg_gradient(color1, color2, color3):
    st.markdown(
        f"""
         <style>
         .stApp {{
             background: linear-gradient(135deg, {color1}, {color2}, {color3});
             background-size: cover;
         }}
         </style>
         """,
        unsafe_allow_html=True
    )
    