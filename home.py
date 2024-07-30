# -*- coding: utf-8 -*-

import streamlit as st 

def run_home():
    st.title("비만도 예측")
    st.header("사망 사건을 예측하는 12가지 임상적 특징")
    st.subheader("데이터 세트 정보")
    
    st.write("-" * 50) # print()

    st.markdown(""" 
    
    - 심혈관 질환(CVD)은 전 세계 사망 원인 1위로, 매년 약 1,790만 명의 목숨을 앗아가며, 이는 전 세계 사망자의 31%를 차지합니다.
    - 심부전으로 인한 사망률을 예측하는 데 사용할 수 있는 12가지 특징이 포함되어 있습니다.
                """)
   
   


run_home()