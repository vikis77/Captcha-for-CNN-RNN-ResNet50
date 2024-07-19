import os
import pyperclip
import streamlit as st
from Predict import app_predict
from App_functions import *
from App_setting import *
import sys
sys.path.append('Captcha_GEN')

def home_feature():
    with st.container():
        with st.expander("模型测试（点击展开/收起）",icon='🚨',expanded=True):
            with st.container(height=600):
                chose_model = session_state['chose_model']
                c1,c2=st.tabs([f'1.选择测试模型（当前已选{chose_model}）','2.模型测试'])
                with c1:
                    new_chose_model = st.selectbox('选择测试模型？',list(chose_model_path.keys()))  # 侧边栏添加下拉选择框
                    if new_chose_model != chose_model:
                        session_state['chose_model'] = new_chose_model
                        st.experimental_rerun()
                    if chose_model != session_state['chose_model']:
                        with st.spinner('加载中...'):
                            my_progress(0.01)
                    speed = st.select_slider(label='预测速度', options=[1,2,3], value=3, help="wu..")
                    if speed == 1:
                        session_state['TIMEFREE'] = TIME1
                    elif speed == 2:
                        session_state['TIMEFREE'] = TIME2
                    elif speed ==3:
                        session_state['TIMEFREE'] = TIME3
                    session_state['chose_model'] = chose_model

                    # 获取模型路径
                    model_path = chose_model_path[chose_model]

                    # 提示模型文件是否存在
                    if os.path.exists(model_path):
                        if chose_model == RNN:
                            st.success(f'* 模型已导入\n\n    训练准确率约为：92.0%  \n\n     预测500张图用时：00:03:35\n\n     实际预测正确率：94.2%')
                        elif chose_model == CNN:
                            st.success(f'* 模型已导入\n\n    训练准确率约为：90.3%  \n\n     预测500张图用时：00:05:56\n\n     实际预测正确率：63.8%')
                        elif chose_model == RESNET50:
                            st.success(f'* 模型已导入\n\n    训练准确率约为：94.5%  \n\n     预测500张图用时：00:06:28\n\n     实际预测正确率：94.0%')
                    else:
                        st.warning('* 路径不存在，请重新确认后输入')

                with c2:
                    c1,c2=st.columns([1,2])
                    with c1:
                        with st.container(height=500):
                            st.write('模型测试1：输入验证码进行预测')
                            col1,col2 = st.columns(2)
                            emp_text1 =st.empty()
                            user_input = emp_text1.text_input('请输入四位验证码：',value=session_state['user_input'],placeholder="不区分大小写",key='text_input')  
                            session_state['user_input'] = user_input
                            emp_btn1 =st.empty()
                            if emp_btn1.button("点我预测",key='btn01'):
                                if len(user_input)<0:
                                    st.error("输入长度错误，请检查确认！！")
                                else:
                                    user_input = user_input.upper()
                                    run_simgle_prediction(user_input=user_input,path='App\Images\identify_Code.png')
                    with c2:
                        with st.container(height=500):
                            st.write('模型测试2：生成验证码并预测')
                            if st.checkbox('极速模式'):
                                col1, col2,col3 = st.columns(3)
                                with col1:
                                    if st.button("点击生成（单次）"):
                                        run_simgle_prediction_fast(path='App\Images\identify_Code.png')

                                with col2:
                                    if st.button("批量预测（50次）"):
                                        run_batch_prediction_fast(total_predictions=50)
                                    
                                with col3:
                                    if st.button("批量预测（500次）"):
                                        run_batch_prediction_fast(total_predictions=500)
                            else:
                                col1, col2,col3 = st.columns(3)
                                with col1:
                                    if st.button("点击生成（单次）"):
                                        run_simgle_prediction(path='App\Images\identify_Code.png')

                                with col2:
                                    if st.button("批量预测（50次）"):
                                        run_batch_prediction(total_predictions=50)
                                    
                                with col3:
                                    if st.button("批量预测（500次）"):
                                        run_batch_prediction(total_predictions=500)
    

