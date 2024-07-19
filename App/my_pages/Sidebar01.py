import os
import streamlit as st
import sys
sys.path.append('./App')
from streamlit_option_menu import option_menu
from App_functions import *
from App_setting import *

def sidebar_a():
    with st.container():
        with st.sidebar:
            # with st.container():
                # horsecol1,horsecol2 = st.columns([0.2,0.8])
                # with horsecol1:
                #     st.image('App\Images\logo.png',width=320)
                # with horsecol2:
                    # st.header("CAPYCHA👻")
                    # st.header("")
            choose = option_menu("CAPTCHA", ["主页", "介绍", "模型测试", "模型使用", "关于我们"],
                                icons=['house', 'grid', 'kanban', 'book','person lines fill'],
                                menu_icon="tsunami", default_index=0,
                                styles={
                "container": {"padding": "5!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"}, 
                "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#02ab21"}},
                # orientation='horizontal'
                
            )
        session_state['menuchoose'] = choose
        st.sidebar.image("App\Images\Captcha_Recognition.png")
        # main_bg("Images\Captcha_Recognition.png")
        color1 = "#FAEBD7"  # 渐变颜色1
        color2 = "#FFE4E1"  # 渐变颜色2
        color3 = "#E6E6FA"  # 渐变颜色3
        # sidebar_bg_gradient()
        # main_bg_gradient(color1, color2, color3)

        
