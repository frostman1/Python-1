# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

day=int(input("Введите число дня недели: "))
if ( day>5 and day<=7):
    print('Да, это выходной день')
elif (day<=5):
    print("Нет, сегодня рабочий день")
else:
    print("Вы ввели что-то не то!")