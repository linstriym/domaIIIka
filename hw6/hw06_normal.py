# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:
def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.
    """
    return (a * b) ** 0.5


a = float(input("a = "))
b = float(input("b = "))
c = avg(a, b)
print("Среднее геометрическое = {:.2f}".format(c))
#TODO:
def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.

    Исключения:
        - ValueError: вычисление не возможно.
    """
    if a * b >= 0:
        return (a * b) ** 0.5
    else:
        raise ValueError("Невозможно определить среднее геометрическое "
                         "введенных чисел.")


try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = avg(a, b)
    print("Среднее геометрическое = {:.2f}".format(c))
except ValueError as err:
    print("Ошибка:", err, ". Проверьте введенные числа.")
except Exception as err:
    print("Ошибка:", err)

# Задача-2:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
#TODO:
from hw6.hw06_easy import create_directory, remove_directory, list_dir
import os

intro_message = """
Welcome!
Actions:
go     - change directory
list   - get content of current directory
remove - remove selected folder
make   - create new folder
"""

print(intro_message)
def go_to(path):
    try:
        os.chdir(path)
        print('Successfully changed directory')
    except:
        print('Error with changing directory')
COMMANDS = {
    'go': go_to,
    'list': list_dir,
    'make': create_directory,
    'remove': remove_directory,
}
def get_command():
    cmd = input("Type command: ")
    if COMMANDS.get(cmd):
        path = os.path.curdir
        action = COMMANDS[cmd]
        if cmd != 'list':
            sub_path = input("Directory path: ")
            path = os.path.join(path, sub_path)
        action(path)
    else:
        print("Invalid command")
    get_command()
get_command()