while True:
    user_action = input(" type add, show, edit, complete or exit: ")
    user_action = user_action.strip()


    if 'add' in user_action:
        todo = user_action[4:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open(r'C:\Users\seaer\PycharmProjects\pythonProject\todos.txt', 'w') as file:
            file.writelines(todos)

    if "show" in user_action:
        with open(r'C:\Users\seaer\PycharmProjects\pythonProject\todos.txt', 'r') as file:
            todos = file.readlines()

        # list comprehension
        new_todos = [item.strip('\n') for item in todos]
        # list comprehension

        for index, item in enumerate(new_todos):
            row = f"{index + 1}-{item}"
            print(row)

    if 'edit' in user_action:
        number = int(input("Number of the todo to edit: "))
        number = number - 1

        with open(r'C:\Users\seaer\PycharmProjects\pythonProject\todos.txt', 'r') as file:
            todos = file.readlines()
            print('here is todos existing files', todos)
        new_todo = input("enter new todo: ")
        todos[number] = new_todo + '\n'
        with open(r'C:\Users\seaer\PycharmProjects\pythonProject\todos.txt', 'w') as file:
            file.writelines(todos)

    if 'complete' in user_action:

        number = int(input("Number of the todo to complete: "))

        with open(r'C:\Users\seaer\PycharmProjects\pythonProject\todos.txt', 'r') as file:
            todos = file.readlines()

        todos.pop(number - 1)

        with open(r'C:\Users\seaer\PycharmProjects\pythonProject\todos.txt', 'w') as file:
            file.writelines(todos)



    if 'exit' in user_action:
        break

print("bye!")
