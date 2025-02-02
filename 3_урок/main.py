HELP = """
help - наечетать справку
add - добавить задачу в список
show - вывести весь спиок здач"""

tasks = []
run = True


while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print(tasks)
    elif command == "add":
        task = input("Введе название задачи: ")
        tasks.append(task)
        print("Задача добавлена!")
    else:
        print("Неизвестная команнада! Выберете из доступных:" + HELP)
        run = False # 1 вариант завершения
        break
print("Пока-пока!")