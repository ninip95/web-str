# -*- coding:utf-8 -*-

import streamlit as st 
import pandas as pd 

@st.cache_data
def load_data():
    df = pd.read_csv('data/Obesity Classification.csv')

    return df