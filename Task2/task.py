# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

x = int(input('input number x '))
y = int(input('input number y '))
z = int(input('input number z '))

leftSide = not (x or y or z)
rightSide = not x and not y and not z
result = leftSide == rightSide

if result == True:
    print('statement is true')
else:
    print('statement is false')

