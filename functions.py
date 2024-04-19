FILEPATH = "todos.txt"          #created a variable FILEPATH to indicate file name

# def get_todos(filepath="todos.txt"):
def get_todos(filepath=FILEPATH):    #replaced name of file in each function with variable name
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


#def write_todos(todos_arg, filepath="todos.txt"):
def write_todos(todos_arg, filepath=FILEPATH):   #replaced name of file in each function with variable name
    """ Write a to-do items list in the text file."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":  #will exclude below from being run from any external script file (even practice.py doesn't work)
                                #will only run if the file itself is run
    print("hello from functions")
    print(get_todos())

