#1
# slides = {"Кантемир": {
#     "length": 100,
#     "min_age": 12,
#     "status": "closed"},
# "Красный дракон": {
#     "length": 53, 
#     "min_age": 16,
#     "status": "open"
# },

# "Детская":{
#     "length": 5,
#     "min_age": 7,
#     "status": "open"
# },
# "Закатное солнце": {
#     "length": 20,
#     "min_age": 16,
#     "status": "fix"
# },
# "Жираф": {
#     "length": 31,
#     "min_age": 16,
#     "status": "open"}}

# while True:
#     choice = input("Введите название горки:")
#     if choice in slides:
#         for info, value in slides[choice].items():
#             print(f"{info}-{value}")
#     else:
#         print("Такой горки нет")

#2
# list = [1.456, 2.125, 3.32, 4.1, 5.34]
# for number in list:
#     print(round(number, 1))

#3
# dict = {"year": "",
#         "month": "",
#         "day": ""
#         }
# date = ('2025-12-31').split("-")
# dict["year"] = date[0]
# dict["month"] = date[1]
# dict["day"] = date[2]
# print(dict)

#4
# a = "fas4312ghsdg52"
# for i in a:
#     if i.isdigit():
#         print(a.find(i))
#         break


#5
# a = "o12402155125fh"
# amount = 0
# for i in a:
#     if not i.isdigit():
#         amount += 1
# if amount <=3:
#     print("Количество букв меньше или равно 3")
# else:
#     print("В строке больше 3 букв")

#6
# text = 'abcde abcde abcde'.split(" ")
# for i in range(len(text)):
#     text[i] = "!" + text[i][1:]
# print(text)
# result = text.replace("a", "!")
# print(result)

#7
# lst1 = [1, 2, 3, [5,7,2]]
# lst2 = [4, 5, 6]
# lst3 = lst1 + lst2
# print(lst3)

#8
# list = [1, 2, 3, 4, 5, 6]
# length = len(list)
# amount = 0
# for i in list:
#     if list.index(i) < length / 2:
#         amount += i
# print(amount)