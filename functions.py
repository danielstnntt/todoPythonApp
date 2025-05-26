FILEPATH = "todo.txt"

def get_todos(filepath=FILEPATH):
    """ Reads the Todos text file
    and return a list of to do list
    items """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ This writes a record to the to do list items """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)