#  password = input("Введите пароль:")
#  while password != "easycodeisthebest":
#    password = input("Введите пароль:")
# name = input("Введите ваше имя:")
# promo = input("Введите промокод:")
# count = 0
# while count < 4:
#     if name == "Вася" and promo == "caramel":
#         count +=1
#         print(count)
#     name = input("Введите ваше имя:")
#     promo = input("Введите промокод:")

# a = 0
# for i in range(7):
#     money = int(input("Введите сумму:"))
#     if money > a:
#         a = money
# print(a)

# name = input("Введите имя:")
# last_name = input("Введите фамилию:")
# forbidden_symbols = "!@#$%^&*()-_=+"
# for i in name:
#     if i in forbidden_symbols:
#         print(f"{i} - этот символ запрещено использовать")

name = input("Введите имя:")
last_name = input("Введите фамилию:")
forbidden_symbols = "!@#$%^&*()-_=+"
for symbol in forbidden_symbols:
    if symbol in name or symbol in last_name:
        print(f"{symbol} - этот символ запрещён")
