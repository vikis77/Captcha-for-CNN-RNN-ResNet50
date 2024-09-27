import streamlit as st

def home_about():
    st.markdown('''
    # 基于ResNet50，CNN，RNN的四位验证码识别''')
    
    st.markdown('''
        本项目github地址：[https://github.com/vikis77/Captcha-for-CNN-RNN-ResNet50](https://github.com/vikis77/Captcha-for-CNN-RNN-ResNet50)
    ''')

    st.image('Snipaste_2024-07-19_17-09-08.png', caption='Example Image 1', use_column_width=True)
    st.image('Snipaste_2024-07-19_17-09-43.png', caption='Example Image 2', use_column_width=True)
    st.image('Snipaste_2024-07-19_17-10-30.png', caption='Example Image 3', use_column_width=True)

    st.markdown('''
    感谢

    [**[Resnet50-for-captche](https://github.com/kevinzhao080/Resnet50-for-captche)**]作者kevinzhao

    [**[RNN-for-captche](https://gitee.com/oceanwang12138/captcha_identify)**]作者: Ocean

    不知名作者 999感冒灵颗粒
    ''')
    