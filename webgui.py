#Run Command in Pycharm to build code
    # & "C:\Users\Daniel.Stennett\AppData\Local\Programs\Python\Python313\python.exe" -m streamlit run "C:\Users\Daniel.Stennett\OneDrive - farsound aviation\Documents\Training\Python Training\todo_app\webgui.py"
#Check URL to see if the changes were successful
    #  Local URL: http://localhost:8501
    #  Network URL: http://192.168.1.65:8501

import functions
import streamlit as st

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("Please add a ToDo Item to the list")
st.text_input(label="", placeholder="Right Here...")

for item in todos:
    st.checkbox(item)




