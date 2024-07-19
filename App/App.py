import sys
sys.path.append('Captcha_GEN')
import streamlit as st
from App_setting import *
from App_functions import *
from my_pages.Home01 import home_page
from my_pages.Home02 import home_introduction
from my_pages.Home03 import home_feature
from my_pages.Home04 import home_about
from my_pages.Home05 import home_use
from my_pages.Sidebar01 import sidebar_a

# 进行页面设置
st.set_page_config(
    page_title='验证码识别', #设置页面标题
    page_icon= "random", #设置页面的icon  使用"random"会随机选择一个emoji作为icon
    layout="wide", #布局对齐效果 centered在当前column中居中  wide相对整个屏幕拉伸
    initial_sidebar_state="auto", #边栏的初始效果 “auto”：在移动设备上收起边栏，在其他设备上展开
    menu_items=None #在一个字典dict中设置页面右上角的菜单内容
)

def main() -> None:
    """
    这是APP的主函数，在运行APP时会被调用。
    根据session_state['menuchoose']的值，决定显示哪一页。
    """
    sidebar_a() #侧边栏
    # 根据session_state['menuchoose']的值，决定显示哪一页
    if session_state['menuchoose'] == '主页':
        home_page()
    elif session_state['menuchoose'] == '介绍':
        home_introduction()
    elif session_state['menuchoose'] == '模型测试':
        home_feature()
    elif session_state['menuchoose'] == '模型使用':
        home_use()
    elif session_state['menuchoose'] == '关于我们':
        home_about()
    else:
        pass    # 如果menuchoose的值不在上述情况中，则不做任何操作

if __name__=='__main__':
    main()

