import functions
import FreeSimpleGUI as gui

label = gui.Text("Type in a To-Do")
input_Box = gui.InputText(tooltip="Enter A To Do", key="todo")
add_button = gui.Button("Add")

window = gui.Window('My To Do App',
                    layout=[[label], [input_Box, add_button]],
                    font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case gui.WINDOW_CLOSED:
            break

window.close()