#1
# a = input("Введите первое число:")
# b = input("Введите второе число:")
# first_number_a = a[0]
# first_number_b = b[0]
# if first_number_a == first_number_b:
#     print("Первые цифры совпадают")
# else:
#     print("Первые цифры не совпадают")

#2
# text = input("Введите текст:")
# if len(text) >= 2:
#     print(text[-2])
# else:
#     print("В тексте 1 символ")

#3
# a = int(input("Введите первое число:"))
# b = int(input("Введите второе число:"))
# remains = a % b
# if remains == 0:
#     print("Первое число делится на второе без остатка")
# else:
#     print(f"Первое число делится на второе с остатком {remains}")

#4
# number = input("Введите число")
# print(number[::-1])

#5
# water = int(input("Сколько воды нужно принести?"))
# floor = int(input("Введите этаж:"))
# if water == 1 and floor <= 100:
#     print("Робот справится")
# elif water == 2 and floor <= 99:
#     print("Робот справится")
# elif water == 5 and floor <=53:
#     print("Робот справится")
# else:
#     print("Робот не справится")

#6
# coffee = int(input("Введите количество стаканов:"))
# floor = int(input("Введите этаж:"))
# if coffee >=1 and coffee <=3 and floor <=100:
#     print("Робот справится")
# elif coffee >=4 and coffee <=7 and floor <= 50:
#     print("Робот справится")
# elif coffee >=8 and floor <=2:
#     print("Робот справится")
# else:
#     print("Робот не справится")

#7
# temperature = int(input("Введите температуру:"))
# if temperature < -10:
#     print("Стоит надеть куртку и шапку")
# elif temperature >= -10 and temperature < 0:
#     print("Шапка точно не помешает")
# elif temperature >= 0 and temperature < 10:
#     print("Стоит надеть футболку с толстовкой")
# elif temperature >= 10 and temperature < 20:
#     print("Хватит просто толстовки")
# elif temperature >= 20:
#     print("Одеваемся как летом!")