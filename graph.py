# -*- coding:utf-8 -*-
import pandas as pd

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_data

def run_graph():
    df = load_data()
    st.markdown("## 대시보드 개요 \n"
    "본 프로젝트는  를 알려주는 대시보드입니다. "
    "여기에 독자가 넣고 싶은 추가 내용을 더 넣을 수 있습니다.")

    
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("### 연관성 파악을 위한 시각화 ")

   

    tab1, tab2, tab3, tab4 = st.tabs(["나이", "크레아티키나제", "박출계수","사망 조인트"])

    with tab1: #total bill
        fig, ax = plt.subplots()
        st.header("나이-사망 히스토그램")
        # sns.barplot(x='sex', y='ejection_fraction', data=df)
        sns.histplot(x='age', data=df, hue='DEATH_EVENT', kde=True)
       
        st.pyplot(fig)

    with tab2:
        st.header("크레아티키나제-사망 히스토그램")
        fig, ax = plt.subplots(1,1,figsize=(20,10))
        sns.histplot(x='creatinine_phosphokinase', data=df, hue='DEATH_EVENT', kde=True)
        #sns.scatterplot(df, x = 'creatinine_phosphokinase', y = 'DEATH_EVENT')
        # sns.countplot(x='age', hue='DEATH_EVENT', data=df)
        st.pyplot(fig)

    with tab3:
        st.header("박출계수-사망 바이올린프롯")
        fig, ax = plt.subplots()
        sns.violinplot(x='DEATH_EVENT', y='ejection_fraction', data=df)

        #sns.histplot(x='ejection_fraction', data=df, bins=13, hue='DEATH_EVENT', kde=True)

        #sns.boxplot(x='DEATH_EVENT',y='ejection_fraction', data=df, hue='DEATH_EVENT')
        st.pyplot(fig)

    with tab4:
        st.header("박출계수-혈중 크레아틴 레벨-사망 조인트")
        fig, ax = plt.subplots()
        sns.jointplot(x='platelets', y='creatinine_phosphokinase',data=df, kind='kde', hue='DEATH_EVENT')
        #sns.boxplot(x='ejection_fraction', y='creatinine_phosphokinase', data=df, hue='DEATH_EVENT')
        st.pyplot(fig)
        
run_graph()