# -*- coding:utf-8 -*-
import pandas as pd
from utils import load_data
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def run_data():
    df = load_data()
    st.markdown("## 비만도 의료데이터 분석 \n"
                
    "kaggle 데이터를 분석해보자.비만도 데이터 참조 "
    "dataset - heart_failure_clinical_records_dataset.csv"
    )
    
    st.markdown("<hr>", unsafe_allow_html=True)
    st.title("## 데이터 컬럼 내용 ")    
    st.markdown(""" 
            -age: 환자의 나이 
            -anaemia: 환자의 빈혈증 여부 (0: 정상, 1: 빈혈)\n
            -creatinine_phosphokinase: 크레아틴키나제 검사 결과 
            -diabetes: 당뇨병 여부 (0: 정상, 1: 당뇨)
            -ejection_fraction: 박출계수 (%) \n
            -high_blood_pressure: 고혈압 여부 (0: 정상, 1: 고혈압)\n
            -platelets: 혈소판 수 (kiloplatelets/mL) 
            -serum_creatinine: 혈중 크레아틴 레벨 (mg/dL)
            -serum_sodium: 혈중 나트륨 레벨 (mEq/L) \n
            -sex: 성별 (0: 여성, 1: 남성)\n
            -smoking: 흡연 여부 (0: 비흡연, 1: 흡연)
            -time: 관찰 기간 (일) 
            -DEATH_EVENT: 사망 여부 (0: 생존, 1: 사망)   
                 """)

  

   
    tab1, tab2, tab3, tab4 = st.tabs(["상위데이터", "데이터통계", "컬럼데이터", "조건데이터"])

    with tab1:
        dh=df.head(10)
        st.write(dh)

    with tab2:
        dd=df.describe()
        st.write(dd)

    with tab3:
        col=df.columns.tolist()
        col=col[0: ]
        se_col = st.multiselect('select column',col)
        new_df = df.loc[:,se_col]
        st.write(new_df)


    with tab4:
       # col=st.selectbox('select',('age','sex','creatinine_phosphokinase','ejection_fraction','DEATH_EVENT'))
       
        value = st.slider("값 구간을 선택하세요",0.0, 100.0, (25.0, 75.0))
      
        condition=df['age'] < value[1]
    
        c_df=df.loc[condition]

        st.write(value[1])
        
        st.write(c_df)
       # condition = (df["생활인구합계"] >= 1000) & (df["행정동코드"] == 11680610)

run_data()  