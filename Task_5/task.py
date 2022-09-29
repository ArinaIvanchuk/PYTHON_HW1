#  Напишите программу, которая принимает на вход координаты двух точек и находит 
# расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


from math import*


A1 = float(input('input coordinate A1: '))
B1 = float(input('input coordinate B1: '))
A2 = float(input('input coordinate A2: '))
B2 = float(input('input coordinate B2: '))
num = (A2 - A1)**2 + (B2 - B1)**2
sqr = sqrt(num)

print(float(round(sqr, 3)))