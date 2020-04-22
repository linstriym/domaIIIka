# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

#TODO:
collection = [1, 2, 4, 0]
n_collection = [x ** 2 for x in collection]
print(n_collection)


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

#TODO:
fruits_a = ['Apple', 'Banana', 'Pineapple', 'Lemon', 'Lime']
fruits_b = ['Apple', 'Fruit1', 'Super Fruit', 'Lemon', 'Lemonade']
result = [fruit for fruit in fruits_a if fruit in fruits_b]
print(result)


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

#TODO:
numbers = [4, 8, 15, 16, 23, 42]
n_numbers = [x for x in numbers if x % 3 == 0 and x > 0 and x % 4 != 0]
print(n_numbers)