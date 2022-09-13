# 4- Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных 
# координат точек в этой четверти (x и y).

number_quarter = int (input('Введите номер четверти: '))
if number_quarter == 1:
    print('диапазон координат: x > 0 and y > 0')
elif number_quarter == 2:
    print('диапазон координат: x < 0 and y > 0')
elif number_quarter == 3:
    print('диапазон координат: x < 0 and y < 0')
elif number_quarter == 4:
    print('диапазон координат: x > 0 and y < 0')
elif number_quarter !=1 or number_quarter != 2 or number_quarter !=3 or number_quarter !=4:
    print ('Такой четверти нет')