import streamlit as st
import sys
# sys.path.append('')

def add_animated_bg():
    st.markdown(
        f"""
        <style>
        @keyframes gradient {{
            0% {{
                background-position: 0% 50%;
            }}
            50% {{
                background-position: 100% 50%;
            }}
            100% {{
                background-position: 0% 50%;
            }}
        }}

        .stApp {{
            background: linear-gradient(270deg, #25da32, #b946b0, #86a8e7, #c5db24);
            background-size: 800% 800%;
            animation: gradient 15s ease infinite;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


def home_introduction():

    st.subheader("1 验证码介绍")
    st.markdown("""&emsp;&emsp;CAPTCHA这个词最早是在2002年由卡内基梅隆大学的路易斯·冯·安、Manuel Blum、Nicholas J.Hopper以及IBM的
                John Langford所提出。卡内基梅隆大学曾试图申请此词使其成为注册商标[1]， 但该申请于2008年4月21日被拒绝[2]。一种常用的
                CAPTCHA测试是让用户输入一个扭曲变形的图片上所显示的文字或数字，扭曲变形是为了避免被光学字符识别之类的计算机程序自动识别
                出图片上的文数字而失去效果。由于这个测试是由计算机来考人类，而不是标准图灵测试中那样由人类来考计算机，人们有时称CAPTCHA
                是一种反向图灵测试。 """)
    c1,c2,c3 = st.columns(3)
    with c2:
        st.image('App\Images\路易斯·冯·安.jpg',width=200)
        st.write("&emsp;路易斯·冯·安Luis von Ahn")

    st.markdown('''&emsp;&emsp;全自动区分计算机和人类的图灵测试（英语：Completely Automated Public Turing test to tell Computers and Humans Apart，
                简称CAPTCHA），又称验证码，是一种区分用户是机器或人类的公共全自动程序。在CAPTCHA测试中，作为服务器的计算机会自动生成一个问题
                由用户来解答。这个问题可以由计算机生成并评判，但是必须只有人类才能解答。由于机器无法解答CAPTCHA的问题，回答出问题的用户即可
                视为人类。\n''')
    with st.container():
        # 在页面中使用自定义样式
        st.write("<br><br>市面上部分的Captcha验证码如下所示：",unsafe_allow_html=True)
        c1,c2,c3 = st.columns(3)
        with c1:
            st.image(r'App\Images\896459668.jpg',width=400)
            st.write('早期的Captcha验证码 "smwm" ，由EZ-Gimpy程序产生，使用扭曲的字母和背景颜色梯度')
        with c2:
            st.image(r'App\Images\g878t90.jpg',width=400)
            st.write('一种更现代的CAPTCHA，其不使用扭曲的背景及字母，而是增加一条曲线来使得图像分割（segmentation）更困难。')
        with c3:
            st.image(r'App\Images\g8t8u9.gif',width=400)
            st.write('现代的Captcha验证码 "smwm"由EZ-Gimpy程序产生，使用扭曲的字母和背景颜色梯度')
        c1,c2,c3 = st.columns(3)
        with c1:
            st.image(r'App\Images\435px-12306验证码界面（模拟）.jpg',width=400)
            st.write('<br><br>要求用户识别图片的验证方式，本图为模拟12306网站的验证界面',unsafe_allow_html=True)
        with c2:
            st.image(r'App\Images\34ffef.png',width=400)
            st.write("<br><br><br><br>许多政府机构网站仍使用着要求用户识别图片中的字符的验证方式：本图为国家药品监督管理局的验证界面",unsafe_allow_html=True)
        with c3:
            st.image(r'App\Images\fq4rt.png',width=400)
            st.write('行为式验证码中的障碍躲避，自适应障碍生成和轨迹碰撞算法双重保险，大幅提升安全系数')   


    st.subheader("2 深度学习实现四位验证码的识别介绍")
    st.markdown('''基本思路：\n
        验证码识别的任务是从图片中提取字符，并将它们转换为文本。以下是实现验证码识别的基本步骤：
        1) 数据准备：收集并准备训练数据，包括带标签的验证码图片。
        2) 图像预处理：对图像进行必要的预处理，例如灰度化、归一化和大小调整。
        3) 模型构建：构建 RNN + LSTM 模型以处理序列数据。
        4) 模型训练：使用训练数据对模型进行训练。
        5) 模型评估：使用测试数据评估模型的性能。
        6) 预测：使用训练好的模型进行验证码的识别。''')
    st.subheader("3 模型介绍")
    st.markdown('''3.1 **RNN+LSTM模型**:RNN（循环神经网络）和 LSTM（长短期记忆网络）是处理序列数据的常用模型，
                可以用于许多任务，包括语音识别、语言建模和验证码识别。对于四位验证码的识别任务，LSTM 模型非常适合，
                因为它可以有效地捕获序列中的时间依赖关系。''')
    st.image('RNN\训练结果_4.png',width=1000)
    st.image('RNN\pr.jpg',width=600)

    st.markdown('''3.1 **CNN模型**:RNN（循环神经网络）和 LSTM（长短期记忆网络）是处理序列数据的常用模型，
                可以用于许多任务，包括语音识别、语言建模和验证码识别。对于四位验证码的识别任务，LSTM 模型非常适合，
                因为它可以有效地捕获序列中的时间依赖关系。''')
    st.image('CNN\微信图片_20240719154353.png',width=1000)


    st.markdown('''3.1 **RESNET50模型**:RNN（循环神经网络）和 LSTM（长短期记忆网络）是处理序列数据的常用模型，
                可以用于许多任务，包括语音识别、语言建模和验证码识别。对于四位验证码的识别任务，LSTM 模型非常适合，
                因为它可以有效地捕获序列中的时间依赖关系。''')
    st.image('ResNet50\训练结果1.3.png',width=1000)
    st.image('ResNet50\pr图1.3.png',width=600)