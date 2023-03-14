while True:
    user_action = input(" type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        with open(r'C:\Users\seaer\PycharmProjects\pythonProject\todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo + '\n')

        with open(r'C:\Users\seaer\PycharmProjects\pythonProject\todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        with open(r'C:\Users\seaer\PycharmProjects\pythonProject\todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            with open(r'C:\Users\seaer\PycharmProjects\pythonProject\todos.txt', 'r') as file:
                todos = file.readlines()
                print('here is todos existing files', todos)
            new_todo = input("enter new todo: ")
            todos[number] = new_todo + '\n'
            with open(r'C:\Users\seaer\PycharmProjects\pythonProject\todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Not a valid command")
            continue

    elif user_action.startswith("complete"):
        number = int(user_action[9:])

        with open(r'C:\Users\seaer\PycharmProjects\pythonProject\todos.txt', 'r') as file:
            todos = file.readlines()

        todos.pop(number - 1)

        with open(r'C:\Users\seaer\PycharmProjects\pythonProject\todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'exit' in user_action:
        break
    else:
        print("What?")

print("bye!")
