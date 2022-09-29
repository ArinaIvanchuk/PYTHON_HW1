# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input("input Х: "))
while x == 0:
    x = int(input("input correct number: "))
y = int(input("input Y: "))
while y == 0:
    y = int(input("input correct number: "))
if (x > 0 and y > 0):
    print("\nquarter number: 1.")
elif (x < 0 and y > 0):
    print("\nquarter number: 2.")
elif (x < 0 and y < 0):
    print("\nquarter number: 3.")
else:
    print("\nquarter number: 4.")

