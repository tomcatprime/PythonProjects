from os import write


def get_todos(filepath="todos.txt"):
    with open(filepath, 'r') as file_local:
         todos_local = file_local.readlines() 
    return todos_local

def write_todos(filepath, todos):
    with open(filepath, 'w') as file:
        file.writelines(todos)



while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()
    

    if user_action.startswith('add'):
            todo = user_action[4:] + '\n'
             
            todos = get_todos()
                 
            todos.append(todo)
             
            write_todos("todos.txt", todos)
     

    elif user_action.startswith('show'):
        todos = get_todos()
                 
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:    
            number = int(user_action[5:])
            number  = number - 1
            
            todos = get_todos()
                 
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'
            
            write_todos("todos.txt", todos)
        except ValueError:
            print("Your command is not valid. ")
            continue
            
    elif user_action.startswith('completed'):
        try:    
            number = int(user_action[9:])
            
            todos = get_todos()
            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)
            
            write("todos.txt", todos)
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is not item with that number.")  
            continue


        
    elif user_action.startswith('exit'):
            break
    else:
        print("Command is not valid")
            
print("Bye!")

