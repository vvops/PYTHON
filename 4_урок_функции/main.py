HELP = """
help - наечетать справку
add - добавить задачу в список
show - вывести весь спиок здач
exit - выйти
random - добавить случаюную задачу на дату сегодня"""

RANDOM_TASK = "Почистить зубы"

tasks = {

}
run = True

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        date = input("Введите дату для отображения списка задач, для вывода полного списка напишите 'all': ")
        if date in tasks:  # проверка даты списка задач 
            for task in tasks[date]:
                print('-', task )
        elif date == "all":
          print('-', tasks)
        else:
            print("Такой даты в списке задач не существует. Скорее всего на эту дату нет задач.")       
    elif command == "add":
        date = input("Введите дату для добавления задачи: ")
        task = input("Введите название задачи: ")
        if date in tasks: #проверка даты в словаре
          tasks[date].append(task)
        else:
            tasks[date] = []
            tasks[date].append(task)
        print("Задача:", task,"добавлена в дату", date)
    elif command == "exit":
        break
    elif command == "random":
        if "Сегодня" in tasks:
            tasks["Сегодня"].append(RANDOM_TASK)
        else:
            tasks["Сегодня"] = []
            tasks["Сегодня"].append(RANDOM_TASK)
    else:
        print("Неизвестная команнада! Выберете из доступных:" + HELP)
        break
print("Пока-пока!")