# 5-Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

coordinate_X1 = int(input('Введите координату Х1: '))
coordinate_Y1 = int(input('Введите координату Y1: '))
coordinate_X2 = int(input('Введите координату Х2: '))
coordinate_Y2 = int(input('Введите координату Y2: '))
result = ((coordinate_X2 - coordinate_X1)**2 + (coordinate_Y2-coordinate_Y1)**2)**(0.5)
print(round(result, 2))