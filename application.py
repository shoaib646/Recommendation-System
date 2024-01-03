import os
import pickle
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests

content_list = pickle.load(open('content.pkl','rb'))
content_similarity = pickle.load(open('content_sim.pkl','rb'))


def recommend(course):
    index = content_list[content_list['course_name'] == course].index[0]
    distances = sorted(list(enumerate(content_similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_course_names = []
    for i in distances[1:7]:
        course_name = content_list.iloc[i[0]].course_name
        recommended_course_names.append(course_name)

    return recommended_course_names




st.markdown("<h2 style='text-align: center; color: blue;'>Recommendation System for e-learning courses</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: green;'>Author: Shoaib Ahmed</h4>", unsafe_allow_html=True)


selected_course = st.selectbox(
    "Type or select a course you like :",
    content_list
)


if st.button('Show Recommended Courses'):
    st.write("Recommended Courses based on your selection are :")
    recommended_course_names = recommend(selected_course)
    st.text(recommended_course_names[0])
    st.text(recommended_course_names[1])
    st.text(recommended_course_names[2])
    st.text(recommended_course_names[3])
    st.text(recommended_course_names[4])
    st.text(recommended_course_names[5])
    st.text(" ")