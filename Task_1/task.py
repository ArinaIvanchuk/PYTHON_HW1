
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input('input number: '))
if day == 6 or day == 7:
    print(day, '-> yes')
else:
    print(day, '-> no')