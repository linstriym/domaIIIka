# Задание-1:
# Напишите функцию, переводящую км в мили и выводящую информацию на консоль
# т.е функция ничего не возвращает, а выводит на консоль ответ самостоятельно
# Предполагается, что 1км = 1,609 мили
def convert(km):
    print(miles)

#TODO:
def main():
    kilometers = float(input("Enter a distance in kilometers: "))
    cof = 1.609 
    melis = kilometers * cof
    print("The distance in miles is: ", melis)

main()
# Задание-2:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
def my_round(number, ndigits):
    pass


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

#TODO:
def my_round(number, ndigits = 0):
    if ndigits > 0:
        power = 10 ** ndigits
        number = (number * power) + 0.41
        number = (number // 1) / power
    else:
        remainder = number % 1
        number = (number + 1) - remainder if remainder > 0.5 else number - remainder
    return number
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 6))
print(my_round(2.9999967, 5))

# Задание-3:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить, должна возвращать либо True,
# ибо False (если счастливый и несчастливый соответственно)

def lucky_ticket(ticket_number):
    pass


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

#TODO:
def lucky_ticket(ticket_number):
    ticket_len = len(str(ticket_number))
    if ticket_len < 6:
        empty_string = ['0' for x in range(6 - ticket_len)]
        ticket_number = ''.join(empty_string) + str(ticket_number)
    elif ticket_len > 6:
        return False
    left = list(map(int, str(ticket_number)[:3]))
    right = list(map(int, str(ticket_number)[3:]))
    return sum(left) == sum(right)
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
