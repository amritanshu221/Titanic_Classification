import streamlit as st
import pickle
import pandas as pd

st.markdown("<h1 style='text-align: center;'>Bharat Intern Titanic Classification Model </h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Uses Random Forest Algorithm </h2>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'> Created By Amritanshu Bathre </h2>", unsafe_allow_html=True)

Sex=[0,1]
Pclass=[1,2,3]
SibSp=[1,2,3,4,5,6,7,8]
Parch=[0,1,2,3,4,5,6]
q=[0,1]

st.write("Male =0, Female=1")
pipe=pickle.load(open('pipe.pkl','rb'))

col1,col2=st.columns(2)
with col1:
    Sex_p=st.selectbox('select your gender',Sex)
with col2:
    P_class=st.selectbox('select your class',Pclass)

age=st.number_input('Age',min_value=0, max_value=100)

col3,col4=st.columns(2)
with col3:
    Pa_rch=st.selectbox('select  Parch',Parch)
with col4:
    Sib_Sp=st.selectbox('select your Siblings',SibSp)

Fare=st.number_input('Total Fare',min_value=0, max_value=100)


col5,col6=st.columns(2)
with col5:
    E_mbarked_q = st.selectbox('Embarked status Q', q)
with col6:
    E_mbarked_s=st.selectbox('Embarked status S',q)

if st.button('Predict satisfaction'):
    pass



input_df=pd.DataFrame({'Sex':[Sex_p],'Pclass':[P_class],'Age':[age],'Sibsp':[Sib_Sp]
                       ,'Parch':[Pa_rch],'Fare':[Fare],'Embarked_Q':[E_mbarked_q],'Embarked_S':[E_mbarked_s]})

st.header("Result is :")

result=pipe.predict(input_df)
st.header(result)


def display_chance_of_survival(result):
    if result == 1:
        st.write("Congratulations! Your chance of survival is high.")
    else:
        st.write("The chance of survival is low.")

display_chance_of_survival(result)


