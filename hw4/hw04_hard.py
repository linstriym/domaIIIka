# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

#TODO:
def fraction(st):
    num = []
    numerator = []
    denominator = []
    symb = []
    ln = st.split(' ')
    n = 0
    for i in ln:
        if ln[n] == '+' or ln[n] == '-':
            symb.append(i)
            n += 1
        elif ln[n].find('/') == True:
            if ln[n-1].isdigit() == False:
                a = ln[n].split('/')
                numerator.append(a[0])
                denominator.append(a[1])
                n += 1
            else:
                a = ln[n].split('/')
                numerator.append(int(a[0]) + (int(ln[n-1]) * int(a[1])))
                denominator.append(a[1])
                n += 1
        else:
            if ln[n] != 0:
                num.append(ln[n])
                n += 1
            else:
                num.append(0)
    result_numerator = []
    ind = int(0)
    common_danek = 1
    for i in denominator:
        common_danek = common_danek * int(i)
    for i in numerator:
        result_numerator.append(int(i)*(int(common_danek)/int(denominator[ind])))
        ind += 1
    result = 0
    for i in result_numerator:
        for s in symb:
            if s == '+':
                result += i
            elif s == '-':
                result -= i
            else:
                pass
    total = 0
    def answer(total, result, common_danek):
        if result >= common_danek:
            result -= common_danek
            total += 1
            answer(total, result, common_danek)
        else:
            print(f'{total} {int(result)}/{common_danek}')
    answer(total, result, common_danek)
st = '2 5/6 + 4/7'
fraction(st)

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
