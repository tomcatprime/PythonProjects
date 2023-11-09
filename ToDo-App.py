todos =[]

while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()
    

    if 'add' in user_action or 'new' in user_action:
            todo = user_action[4:] + '\n'
             
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
                 
            todos.append(todo)
             
            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)
     

    elif 'show' | 'display':
        with open('todos.txt', 'r') as file:
                todos = file.readlines()
                 
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif 'edit' in user_action:
        number = int(user_action[5:])
        number  = number - 1
            
        with open('todos.txt', 'r') as file:
                todos = file.readlines()
                 
        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + '\n'
            
        with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)
        
    elif 'complete' in user_action:
        number = int(user_action[9:])
            
        with open('todos.txt', 'r') as file:
                todos = file.readlines()
        todo_to_remove = todos[number - 1].strip('\n')
        todos.pop(number - 1)
            
        with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)
        message = f"Todo {todo_to_remove} was removed from the list."
        print(message)     
    elif 'exit':
            break
    else:
        print("Command is not valid")
            
print("Bye!")

