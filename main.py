# from functions import get_todos, write_todos
import functions
import time

user_prompt = "Type add/new, show, edit, complete or exit: "
user_message = "Enter a Todo: "
user_completedList = "See you later: "
edit_list_Message = "Number of the todo you want to edit: "
modified_todo_Message = "Enter Modified Todo: "
removed_Message = " has been Completed."
invalid_option_message = "This is not a valid option."
invalid_complete_message = "There is no item with that ID."
error_Message = "Your command is not Valid."
complete_Message = "Number of the todo to complete: "
todosList = []

now = time.strftime("%d %b %H:%M:%S")
print("Hi, the time is" ,now)
while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()
    if user_action.startswith('add') or user_action.startswith('new'):
        #This will read all characters from character 4 onwards to remove the add word from the variable.
        todo = user_action[4:]
        todosList = functions.get_todos()
        todosList.append(todo + '\n')

        functions.write_todos(todosList)
        with open('files/todo.txt', 'w') as file:
            file.writelines(todosList)

    elif user_action.startswith('show'):
        todosList = functions.get_todos()
        for index, item in enumerate(todosList):
            # Remove Spacing
            #print(index,'-',item.title())
            # Removes Line Break '\n'
            item = item.strip('\n')
            row = f"{index + 1}-{item.title()}"
            print(row)
        print(f"You have {len(todosList)} items in the ToDoList")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            todosList = functions.get_todos()
            modified_todo = input(modified_todo_Message)
            todosList[number] = modified_todo + "\n"
            functions.write_todos(todosList)
        except ValueError:
            print(error_Message)
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todosList = functions.get_todos()
            index = number - 1
            to_do_removed = todosList[index].strip('\n')
            todosList.pop(index)
            print(f'{to_do_removed.title()}' + removed_Message)
            functions.write_todos(todosList)
        except IndexError:
            print(invalid_complete_message)
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print(invalid_option_message)

print(user_completedList)

