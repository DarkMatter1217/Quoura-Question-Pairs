
import streamlit as st
import pickle 
import helper


model = pickle.load(open('model_300000.pkl','rb'))

st.header("Duplicate Question Pairs")


q1=st.text_input("Question 1")
q2=st.text_input("Question 2")

if st.button("Find"):
    query=helper.query_point_creator(q1,q2)
    result=model.predict(query)[0]
    if result:
        st.header("The Questions are Duplicate")
    else:
        st.header("The Questions are Not Duplicate")