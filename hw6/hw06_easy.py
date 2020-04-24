
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
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
#TODO:
import os


def create_directory(path):
    if not os.path.exists(path):
        try:
            os.mkdir(path)
            print(f"Successfully created ({path})")
        except:
            print("Error with creating directory")
    else:
        print('Directory already exists')
#remove
def remove_directory(path):
    if os.path.exists(path):
        try:
            os.rmdir(path)
            print(f"Successfully deleted ({path})")
        except:
            print("Error with deleting directory")
    else:
        print('Directory already exists')


# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.
#TODO:
def list_dir(path, only_directories=False):
    try:
        dir_content = os.listdir(path)
        if only_directories:
            dir_content = filter(lambda x: os.path.isdir(x), dir_content)
        print(dir_content)
    except:
        print('Error with listing directory')

# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
#TODO:
def copy_file():
    import shutil
    cur_file = __file__
    shutil.copy(cur_file, f'{cur_file}.copy')
