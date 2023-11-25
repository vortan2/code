#1
# planets = "Меркурий", "Венера", "Земля", "Марс", "Юпитер", "Сатурн", "Уран", "Нептун"
# for i in planets:
#     print(i)



# #2
# coffee = int(input("Введите количество стаканов:"))
# floor = int(input("Введите этаж:"))
# while coffee != -1:
#     if coffee >=1 and coffee <=3 and floor <=100:
#         print("Робот справится")
#         coffee = int(input("Введите количество стаканов:"))
#         floor = int(input("Введите этаж:"))
#     elif coffee >=4 and coffee <=7 and floor <= 50:
#      print("Робот справится")
#      coffee = int(input("Введите количество стаканов:"))
#      floor = int(input("Введите этаж:"))
#     elif coffee >=8 and floor <=2:
#         print("Робот справится")
#         coffee = int(input("Введите количество стаканов:"))
#         floor = int(input("Введите этаж:"))
#     else:
#         print("Робот не справится")
#         coffee = int(input("Введите количество стаканов:"))
#         floor = int(input("Введите этаж:"))
#     if coffee == -1:
#         print("Робот выключился")

#3
# for i in range (1, 101):
#     print(i)

#4
# for i in range(0,101):
#     if i % 2 == 0:
#         print(i)

#5
# a = 0
# for i in range(1,101):
#     a = a + i
#     print(a)

# #6
# text = "abcde"
# text2 = ""
# for i in text:
#     symbol = text[-1]
#     print(symbol)
#     text = text.replace(symbol, "h" )
#     print(text)
    # text2 = i + text2
    # print(text2)

#7
# numbers = [1, 2, 3, 4, 5]
# amount = 0
# for i in numbers:
#     amount = i + amount
#     print(amount)

#8
# alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
# offset = int(input("Величина сдвига:"))
# text = input("Текст для шифровки:").upper()
# result = ""
# for sym in text:
#     index = alphabet.find(sym)
#     new_sym = alphabet[index + offset]
#     result += new_sym
# print(result)

#9
# alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
# offset = 3
# text = "прс"
# result = ""
# index = alphabet.find(text)
# print(index)
# for sym in text:
#     index = alphabet.find(sym)
#     result += alphabet[index - offset]
# print(result)
    
