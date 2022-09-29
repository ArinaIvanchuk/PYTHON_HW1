# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных 
# координат точек в этой четверти (x и y).

quarter = int(input("input quarter number: "))
while quarter > 4 or quarter < 1:
    quarter = int(input("input correct quarter number: "))
if quarter == 1:
    print('x > 0; y > 0')
elif quarter == 2:
    print('x < 0; y > 0')
elif quarter == 3:
    print('x < 0; y < 0')
else:
    print('x > 0; y < 0')