import random
#1
# a = [1, 2, 3, 4, 5, 6]
# print(a[4:6])

#2
# a = [1, 2, -3, 4, -5]
# amount = 0
# for i in a:
#     if i > 0:
#         amount = i + amount
# print(amount)

#3
# text = "abcde"
# for i in text[::-1]:
#     print(i)
    
4
a = "abcdef"
result = ""
for i in range(len(a)):
    if i % 2 == 0:
        result += a[i]
print(result)
print(a[::2])


#5
# list = ["http://asdfasf", "asfsagoewg", "http://-q0pwr[qwrq]", 'asfasf', 'http://pqwrqwpgklqpg']
# for i in list:
#     if "http://" in i:
#         print(i)
#     else:
#         list.remove(i)
# print(list)

#6
# text = "fasojg0ewgwejg"
# zero = text.find("0")
# print(zero)

#7
# for i in range(10,1001):
#     number = str(i)
#     if int(number[0]) + int(number[1]) == 5:
#         print(number)

#8


#9
# list = [1, -5, 5, -2 , -6, 4, 8, -1, -9]
# amount = 0
# for i in list:
#     if i < 0:
#         amount +=1
# print(amount)

#10
# movies = ["asfasg", "asfgasgas"]
# while True:
#     movie = input("Введите название фильма:")
#     if movie == "stop":
#         break
#     elif movie in movies:
#         print("Такой фильм уже имеется")
#     else:
#         movies.append(movie)

# while True:
#         print("1. Вывести список фильмов") 
#         print("2. Добавить фильм") 
#         print("3. Удалить фильм по названию") 
#         print("4. Удалить фильм по номеру") 
#         print("5. Показать фильм по названию") 
#         print("6. Показать случайный фильм в случайной комнате") 
#         choice = int(input("Введите действие:"))
#         if choice == 1:
#              print(movies)
#         elif choice == 2:
#              movie = input("Введите название фильма:")
#              movies.append(movie)
#         elif choice == 3:
#              movie = input("Введите название фильма:")
#              if movie in movies:
#                   movies.remove(movie)
#         elif choice == 4:
#              number = int(input("Введите номер фильма:"))
#              movies.pop(number)
#         elif choice == 5:
#              movie = input("Введите название фильма:")
#              print(f"В зале #{random.randint(1,10)} показывают фильм {movie}")
#         elif choice == 6:
#              print(f"В зале #{random.randint(1,10)} показывают фильм {movies[random.randint(0,len(movies) - 1)]}")
#         elif choice == 0:
#              break
#         else:
#              print("Неправильное действие")

#0
# actions = ["камень", "ножницы", "бумага"]
# bot_action = random.choice(actions)
# action = input("Выберите, камень, ножницы или бумага?").lower()
# if action == bot_action:
#     print("Ничья!")
# elif action == "камень":
#     if bot_action == "ножницы":
#         print(f"Вы выбрали {action}, компьютер выбрал {bot_action}. Вы победили!")
#     else:
#         print(f"Вы выбрали {action}, компьютер выбрал {bot_action}. Вы проиграли!")
# elif action == "ножницы":
#     if bot_action == "камень":
#         print(f"Вы выбрали {action}, компьютер выбрал {bot_action}. Вы проиграли!")
#     else:
#         print(f"Вы выбрали {action}, компьютер выбрал {bot_action}. Вы победили!")
# elif action == "бумага":
#     if bot_action == "камень":
#         print(f"Вы выбрали {action}, компьютер выбрал {bot_action}. Вы победили!")
#     else:
#         print(f"Вы выбрали {action}, компьютер выбрал {bot_action}. Вы проиграли!")

#11
# cache = [3, 4, 6, 3]
# for i in range(3):
#     add = int(input("Введите 3 значения:"))
#     cache.append(add)
# while len(cache) > 5:
#     cache.pop(0)
# print(len(cache))
# print(cache)
