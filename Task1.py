# 1-Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным.
# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет

weekend_day = int(input ('Введите день недели: '))
if weekend_day == 6 or weekend_day == 7:
    print ('да')
else:
    print ('нет')
