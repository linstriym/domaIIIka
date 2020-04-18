# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    pass
#TODO:
def fibonacci(n, m):
    current, next_item = 1, 1
    numbers = []
    for x in range(1, m + 1):
        if x >= n:
            numbers.append(current)
        current, next_item = next_item, current + next_item
    return numbers
print(fibonacci(10, 20))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()



def sort_to_max(origin_list):
    pass

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

#TODO:
def sort_to_max(origin_list):
    n = 1
    while n < len (origin_list):
        for i in range(len(origin_list) - n):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
        n += 1
    return origin_list
print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

#TODO:
lost = [99,99, 99,99,4, 2, 10, -12, 101, 2.5, 20, 7, 3, -11,4,4,4,0]
def filt(arg, obj):
    print (obj)
    print ('='*60)
    lst = []
    for i in obj : 
        if i != arg : 
            lst.append(i)
    print (lst)
filt(4, lost)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.def check_parall(x1, y1, x2, y2, x3, y3, x4, y4):

#TODO:
def check_parallelogramm(x1, y1, x2, y2, x3, y3, x4, y4):
    side1 = y2 - y1
    side2 = x3 - x2
    side3 = y3 - y4
    side4 = x4 - x1
    if side1 == side3 and side2 == side4:
        print('Это параллелограмм')
    else:
        print('Не параллелограмм')
    pass
check_parallelogramm(1, 1, 1, 4, 4, 4, 4, 1)

