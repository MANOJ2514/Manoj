# import streamlit as st
# st.title("Hello World!")
# st.write("<h1>Hello world</h1>",unsafe_allow_html=True)
# #ing colour of test
# st.write("<h1ss style='color:red;'>hello world</h1>",unsafe_allow_html=True)
# st.file_uploader("upload file")
# st.image("
# st.set_page_config("Lay

import streamlit as st
import numpy as np

st.set_page_config(layout="wide")
st.title("Student Management System")
st.sidebar.title("Fee Management System")


st.sidebar.subheader("Add Student")
rollnumber = st.sidebar.number_input("Roll Number")
rollnumber = st.sidebar.number_input("Name")
rollnumber = st.sidebar.number_input("Fees")
rollnumber = st.sidebar.number_input("Add")
