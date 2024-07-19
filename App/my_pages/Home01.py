import base64
import streamlit as st

# 使用自定义md三级标题样式
md_h3_css = """
    <style>
    [data-testid="stMarkdownContainer"] h3 {
        color: white;
    }
    </style>
    """

# 设置背景颜色和Markdown字体颜色的CSS代码
page_bg_css = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #000D2D; /* 设置背景颜色*/
}

[data-testid="stMarkdownContainer"] p {
    color: white; /* 设置Markdown字体颜色为白色 */
}
</style>
"""

def home_page():
    # 将CSS代码注入到Streamlit应用中
    st.markdown(page_bg_css, unsafe_allow_html=True)
    st.markdown(md_h3_css, unsafe_allow_html=True)

    # st.markdown('### 项目内容')
    # st.markdown('本项目旨在实现四位验证码的识别，通过设计和实现 **三种不同的神经网络模型（RNN、CNN和ResNet50）**，以及前端页面构建一个完整的系统，提供验证码生成、识别和测试功能。项目内容包括模型设计与实现、前端页面设计与实现、验证码数据设计与生成、模型训练与测试、前端系统集成以及前端可视化页面实现。模型设计与实现部分将开发并优化RNN、CNN和ResNet50三种神经网络模型，以提升验证码识别的准确率。前端页面设计与实现部分将设计用户友好的前端页面，提供验证码生成和识别的界面。验证码数据设计与生成部分将设计并生成用于训练和测试的验证码数据集。模型训练与测试部分对不同的神经网络模型进行训练和测试，评估其性能。前端系统集成部分将前端页面与后端识别系统集成，确保功能的完整性和稳定性。前端可视化页面实现部分将实现验证码识别结果的可视化展示，提升用户体验。通过上述步骤，最终实现一个高效、准确的验证码识别系统。')
    # st.markdown('验证码是一种图灵测试手段,旨在识别出哪些操作是由人类执行的,哪些操作是由计算机程序执行。这种测试通常用在用户注册、登录、信息验证等阶段,用于保障互联网中人机交互的安全。由于字符验证码具有制作简单、易于维护等特点,因此成为众多验证码种类中最常用的一种验证码。对字符验证码的识别研究,能够发现字符验证码在设计过程中存在的缺陷,从而完善其设计机制,从而增强网站抵御非法入侵的能力,保护用户的网络隐私,使用户有一个安全的网络环境。目前研究者在针对字符验证码的研究上,提出了许多方法,有基于深度学习的字符验证码识别方法也有基于分割算法的字符验证码识别方法,但是基于深度学习的方法使用的神经网络模型较为复杂,而基于传统分割算法的方法又存在着分割准确率低,或者是识别结果不如人意的问题,因此针对上述的问题,我们设计和实现三种不同的神经网络模型（RNN、CNN和ResNet50），构建一个完整的系统，提供验证码生成、识别和测试功能。')
    st.image(r'App\Images\vw44fw.png')
    st.image(r'App\Images\f44t4er.png')
    st.image(r'App\Images\54gs8.png')
    # st.image(r'App\Images\32rewf.png')
