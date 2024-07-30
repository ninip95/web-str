# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_data
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder
import streamlit as st 
import joblib #모델저장 불러올때


def run_model():
    df = load_data()
    st.title("비만도 예측")
    st.header("비만도로 인한 사망률을 예측하기 위한 모델을 만듭니다.")
    st.subheader("기계 학습은 혈청 크레아티닌 및 박출률만으로도 심부전 환자의 생존을 예측할 수 있습니다.")

    st.write("-" * 50) # print()

    st.markdown(""" 

    - 심혈관 질환이 있거나 심혈관 위험이 높은 사람들(고혈압, 당뇨병, 고지혈증 또는 이미 확립된 질병과 같은 하나 이상의 위험 요인의 존재로 인해)은 조기 발견 및 관리가 필요하며 기계 학습 모델이 큰 도움이 될 수 있습니다. 
    - 대부분의 심혈관 질환은 흡연, 건강에 해로운 식단 및 비만, 신체 활동 부족 및 유해한 알코올 사용과 같은 행동 위험 요인을 인구 전체 전략을 사용하여 해결함으로써 예방할 수 있습니다. 
    - 머신러닝 예측을 통해 심부전의 중요한 지표인 박출률로 심장 수축 기능장애 진단에 도움 될 수 있는 결과다. 

                                        """)
        
    st.write(df)
    
        
#     # 연속형 입력 데이터, 범주형 입력 데이터, 출력 데이터로 구분
#     X_num = df[['ID', 'Age','Height', 'Weight', 'BMI']]
   
  

#     # 수치형 입력 데이터를 전처리하고 입력 데이터 통합하기
#     le= LabelEncoder()

#     df['Gender'] = le.fit_transform(df['Gender'])
#     df['Label'] = le.fit_transform(df['Label'])

#     scaler = StandardScaler()
#     scaler.fit(X_num)

#     X = scaler.transform(X_num) 
#     y = df['Label']    

#     #학습, 테스트 데이터 분리s
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

#     #Logistic Regression 모델 생성
#     model = LogisticRegression(max_iter=1000) # 학습 1000번 진행
#     model.fit(X_train, y_train)
#     model.score(X_test, y_test) 

#     pred = model.predict(X_test) # X_test 데이터를 기반으로 y값 예측
#     print(classification_report(y_test, pred)) # 실제 y_test값과 예측된 y값 비교 평가

#     #XGBoost 모델 생성
#     model_xgb = XGBClassifier()
#     model_xgb.fit(X_train, y_train)
#     model_xgb.score(X_test, y_test) # 0.8

#     #학습한 모델을 통한 예측
#     pred = model_xgb.predict(X_test)
#     print(classification_report(y_test, pred))

#     #모델 만들고 내보내기
#     model_file=open('model1.pkl','wb')
#     joblib.dump(model,model_file)
#     model_file.close()


#     #plt.bar(X.columns, model_xgb.feature_importances_)
#     fig, ax = plt.subplots()
#     st.header("비만도 중요 인자")
#     plt.bar(np.array(X.columns), model_xgb.feature_importances_)
#     plt.xticks(rotation=90)
#     st.pyplot(fig)

# run_model()
