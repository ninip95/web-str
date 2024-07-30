# -*- coding:utf-8 -*-
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
from home import run_home
from data import run_data
from graph import run_graph
from model import run_model

def main():
    st.title('비만도 웹 대시보드 프로젝트')

    with st.sidebar:
        selected = option_menu("대시보드 메뉴", ['홈', '데이터분석', '시각화','머신러닝보고서'], 
                                default_index=0)
    if selected == "홈":
       run_home()
    elif selected == "데이터분석":
       run_data()
    elif selected == "시각화":
       run_graph()
    elif selected == "머신러닝보고서":
       run_model()
    else:
       print("error..")
        
if __name__ == "__main__":
    
    main()   #  메인 실행 파일인지 확인하는 코드