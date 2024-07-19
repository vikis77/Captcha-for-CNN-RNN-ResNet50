import sys
import pyperclip
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from App_functions import *
from App_setting import *
import time
sys.path.append('Captcha_GEN')

def home_use():
    with st.expander("模型使用",icon='🚨',expanded=True):
        with st.container(height=650):
            c1,c2=st.columns([1,2])
            with c1:
                with st.container(height=600):
                    st.write('1.上传验证码进行预测')
                    content_file = st.file_uploader('请上传验证码图片', type=["png"])
                    if content_file is not None:
                        emp1 = st.empty()
                        with open("App/Images/upload_code.png", 'wb') as f:  
                            f.write(content_file.getbuffer())  
                        emp1.image('App/Images/upload_code.png', width=200)
                        t2 = st.empty()
                        t22 = st.empty()
                        t23 = st.empty()
                        t1 = st.empty()
                        if session_state['upload_name'] == content_file.name:
                            code=session_state['app_predict_code']
                        else:
                            session_state['app_predict_code']=''
                            code = ''
                        t2.success(f"预测结果：{code}")
                        # 点击预测按钮时，开始调用app_predict函数进行预测，并显示预测结果
                        if t1.button("点击预测",type="primary",on_click=change_selection, args=('None',)):
                            session_state['showRadio'] = True
                            res1=None
                            emp2 = st.empty()
                            # RNN模型预测
                            RNN_app_predict_code = app_predict('App/Images/upload_code.png', RNN)
                            session_state['RNN_app_predict_code'] = RNN_app_predict_code
                            t2.info('RNN正在预测...')
                            with emp2.container():
                                my_progress(session_state['TIMEFREE'].get('c41')) #进度条
                            t2.success(f"RNN预测结果：{RNN_app_predict_code}")
                            # CNN模型预测
                            CNN_app_predict_code = app_predict('App/Images/upload_code.png', CNN)
                            session_state['CNN_app_predict_code'] = CNN_app_predict_code
                            t22.info('CNN正在预测...')
                            with emp2.container():
                                my_progress(session_state['TIMEFREE'].get('c41')) #进度条
                            t22.success(f"CNN预测结果：{CNN_app_predict_code}")
                            # RESNET50模型预测
                            RESNET50_app_predict_code = app_predict('App/Images/upload_code.png', RESNET50)
                            session_state['RESNET50_app_predict_code'] = RESNET50_app_predict_code
                            t23.info('RESNET50正在预测...')
                            with emp2.container():
                                my_progress(session_state['TIMEFREE'].get('c41')) #进度条
                            t23.success(f"RESNET50预测结果：{RESNET50_app_predict_code}")
                        session_state['upload_name'] = content_file.name
                # with col2:
                    if session_state['showRadio']:
                        res1 = st.radio('结果是否正确？',['None', '👍', '👎'],key='radio_selection')
                        if res1 =='👍':
                            st.balloons()
                        elif res1 == '👎':
                            st.snow()   
            with c2:
                with st.container(height=600):
                    st.write('2.读取剪切板图片进行预测')
                    col1,col2 = st.columns(2)
                    session_state['paste_context'] = ''
                    predict_button = False
                    predice_done = False
                    with col1:
                        with st.container():
                            if st.button("2.1.点击读取\n\n剪切板"):
                                paste_context = ''
                                session_state['clipboard_image_exist'] = False
                                # 检查剪切板中是否有文本数据
                                clipboard_text = pyperclip.paste()
                                if clipboard_text:
                                    paste_context = clipboard_text
                                else:
                                    paste_context = '剪切板中没有文本数据'
                                session_state['paste_context'] = paste_context

                                # 检查剪切板中是否有图片数据
                                clipboard_image = get_clipboard_image()
                                if clipboard_image:
                                    # Save the image to a file
                                    clipboard_image.save("App\Images\clipboard_image.png")
                                    session_state['clipboard_image_exist'] = True

                            empty11 = st.empty()
                            if st.button("2.2点击预测"):
                                predict_button = True
                                empty1 = st.empty()  # 生成验证码
                                empty2 = st.empty()  # 展示验证码
                                empty3 = st.empty()  # 预测结果
                                empty32 = st.empty()  # 预测结果
                                empty33 = st.empty()  # 预测结果
                                empty10 = st.empty() # 正在预测
                                empty5 = st.empty()  # 预测正确
                                empty6 = st.empty()  # 预测错误
                                empty8 = st.empty()  # 预测进度条

                                if session_state['clipboard_image_exist']:
                                    if predict_button:
                                        # 调用模型进行预测
                                        empty10.info("正在预测...")
                                        RNN_app_predict_code = app_predict('App\Images\clipboard_image.png', RNN)
                                        print(RNN_app_predict_code)
                                        with empty8.container():
                                            my_progress(session_state['TIMEFREE'].get('c22'))  # 显示进度条
                                        empty10.empty()
                                        empty11.empty()
                                        predice_done = True
                                        empty3.success(f"RNN预测结果：{RNN_app_predict_code}")
                                        time.sleep(0.1)  # 等待一段时间

                                        CNN_app_predict_code = app_predict('App\Images\clipboard_image.png', CNN)
                                        print(CNN_app_predict_code)
                                        with empty8.container():
                                            my_progress(session_state['TIMEFREE'].get('c22'))  # 显示进度条
                                        empty10.empty()
                                        empty11.empty()
                                        predice_done = True
                                        empty32.success(f"CNN预测结果：{CNN_app_predict_code}")
                                        time.sleep(0.1)  # 等待一段时间

                                        RESNET50_app_predict_code = app_predict('App\Images\clipboard_image.png', RESNET50)
                                        print(RESNET50_app_predict_code)
                                        with empty8.container():
                                            my_progress(session_state['TIMEFREE'].get('c22'))  # 显示进度条
                                        empty10.empty()
                                        empty11.empty()
                                        predice_done = True
                                        empty33.success(f"RESNET50预测结果：{RESNET50_app_predict_code}")
                                        time.sleep(0.1)  # 等待一段时间
                    with col2:
                        if session_state['clipboard_image_exist']:
                            if predice_done:
                                empty11.empty()
                            else:
                                empty11.success('图片已读取，请预测')
                            st.image('App/Images/clipboard_image.png', caption='剪切板中的图片')
                        else:
                            st.info('剪切板中没有图片数据或无法读取图片，请重新复制图片到剪切板！')