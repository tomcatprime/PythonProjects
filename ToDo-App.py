todos =[]

while True:
    user_action = input("Type add, show, edit, or exit:")
    user_action = user_action.strip()
    
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
            file = open('todos.txt', 'w')
            file.writelines(todos)
        case 'show' | 'display':
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number  = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        
        case 'complete':
            numer = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        
        case 'exit':
            break
        case not_match:
            print("Hey, you entered and unknown command")
            
print("Bye!")

