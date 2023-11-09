todos =[]

while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()
    
    match user_action:
        case 'add':
             todo = input("Enter a todo: ") + "\n"
             
             with open('todos.txt', 'r') as file:
                 todos = file.readlines()
                 
             todos.append(todo)
             
             with open('todos.txt', 'w') as file:
                 todos = file.writelines()
    

        case 'show' | 'display':
            with open('todos.txt', 'r') as file:
                 todos = file.readlines()
                 
            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)

        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number  = number - 1
            
            with open('todos.txt', 'r') as file:
                 todos = file.readlines()
                 
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'
            
            with open('todos.txt', 'w') as file:
                 todos = file.writelines()
        
        case 'complete':
            numer = int(input("Number of the todo to complete: "))
            
            with open('todos.txt', 'r') as file:
                 todos = file.readlines()

            todos.pop(number - 1)
            
            with open('todos.txt', 'w') as file:
                 todos = file.writelines()

        case 'exit':
            break
        case not_match:
            print("Hey, you entered and unknown command")
            
print("Bye!")

