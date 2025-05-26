import functions
import FreeSimpleGUI as gui

label = gui.Text("Type in a To-Do")
input_Box = gui.InputText(tooltip="Enter A To Do", key="todo")
add_button = gui.Button("Add")
current_label = gui.Text("List of Current Todos")
list_box = gui.Listbox(values=functions.get_todos(),
                       key="todos",
                       enable_events=True,
                       size=[45, 10])
edit_button = gui.Button("Edit")
complete_button = gui.Button("Complete")
exit_button = gui.Button("Exit")

window = gui.Window('My To Do App',
                    layout=[[label],
                            [input_Box, add_button],
                            [current_label],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                    font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values["todos"])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            selected_todo = values["todos"][0]
            updated_todo = values["todo"]
            todos = functions.get_todos()
            position = todos.index(selected_todo)
            todos[position] = updated_todo
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "Complete":
            complete_todo = values["todos"][0]
            todos = functions.get_todos()
            todos.remove(complete_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value='')
        case "Exit":
            break
        case "todos":
            window["todo"].update(values["todos"][0])
        case gui.WINDOW_CLOSED:
            break

window.close()