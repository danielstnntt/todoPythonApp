#Run Command in Pycharm to build code
    # & "C:\Users\Daniel.Stennett\AppData\Local\Programs\Python\Python313\python.exe" -m streamlit run "C:\Users\Daniel.Stennett\OneDrive - farsound aviation\Documents\Training\Python Training\todo_app\webgui.py"
#Check URL to see if the changes were successful
    #  Local URL: http://localhost:8501
    #  Network URL: http://192.168.1.65:8501

import functions
import streamlit as st

todos = functions.get_todos()

def add_todo():
    #session_state is a dictionary that stores the value on the user's session
    #e.g from below: { new_todo: "Fix Computer" }
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")

st.text_input(label="Please add a ToDo Item to the list",
              placeholder="Right Here...",
              on_change=add_todo,
              key="new_todo")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        #This manually trigger a rerun of your Streamlit app
        st.rerun()

#When the page is loaded, it shows all components and there values on the page dynamically
st.session_state