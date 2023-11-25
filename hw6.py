# list = {"Детская": 5,
#         "Закатное солнце": 20,
#         "Жираф": 31,
#         "Красный дракон": 53,
#         "Кантемир": 100}
# while True:
#         action = input("Введите команду:")
#         if action == "delete":
#                 name = input("Введите название горки:")
#                 if name in list:
#                     del list[name]
#                     print(list)
#         elif action == "add":
#                 name = input("Введите название горки:")
#                 length = int(input("Введите длину горки:"))
#                 list[name] = length
#                 print(list)
#         elif action == "list":
#                new_dict = dict(sorted(list.items()))
#                for keys, value in new_dict.items():
#                       print(f"{keys}-{value}")
#         elif action == "length":
#                 ask = input("Введите название горки:")
#                 if ask in list:
#                     print(f"Протяжённость горки {ask} составляет {list[ask]} метров")

#4

# data = {'year' : '2025','month': '12','day'  : '31',}
# print(f"{data["year"]}-{data["month"]}-{data["day"]}")

#5

# a = set("abcdeabc")
# print(a)

#6

# a = [1,2,3,4,5,6]
# print(a)

#7

# a = {
#     'a': 1,
#     'b': 2,
#     'c': 3, 
#     'd': 4,
# }

# for key in a:
#         a[key] *= 2
# print(a)

#8

# a = '12,34,56'
# numbers = a.split(",")
# print(numbers)
# amount = 0
# for i in numbers:
#     amount += int(i)
# print(amount)

#9
# a = {
#     'a': 1,
#     'b': 2,
#     'c': 3, 
#     'd': 4,
# }
# list = []
# for i in a:
#     list.append(a[i])
# print(list)

# items = list(a.items())
# for i in items:
#         print(i[1])

# b = list(a.keys())
# print(b)

#10
# a = 'abcde'
# result = ''
# for i in a:
#         if i % 2 == 0:
#                 result += a[i].upper()
#         else:
#                 result += a[i]
#         print(result)
    
    

    


