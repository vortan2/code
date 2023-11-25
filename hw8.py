#1

# import random
# import time
# card_list = []
# def card():
#     number = random.randint(1,2)
#     if not number in card_list:
#         card_list.append(number)
# while True:
#     card()
#     time.sleep(2)
#     print(card_list)

#2
# dct1 = {
#     'a': 1,
#     'b': 2,
# }
# dct2 = {
#     'c': 3, 
#     'd': 4,
# }
# dct1.update(dct2)
# print(dct1)

# word = "abcba"
# reversed_word = ""

# # for i in word[::-1]:
# reversed_word = word[::-1]
# if reversed_word == word:
#         print("Слово читается одинаково с любой стороны")
# else:
#         print("Слово читается по разному")

#3
# numbers = [1,67,125,6,41294]
# # print(numbers)
# # numbers = map(str, numbers)
# # print(list(numbers))
# for i in numbers:
#     print()
# print(numbers)
# # print(type(numbers))
# # print(max(numbers))
# number = 0
# for i in numbers:
#     if i > number:
#         number = i
# print(number)

#4
# dct1 = {4, 512,5125}
# dct2 = {125,512,5125,62}
# # lst1 = [1, 2, 3]
# # lst2 = [4, 5, 6]
# # lst3 = [10,11,12]
# for i,v in zip(dct1, dct2):
#     print(i, v)

#5
# numbers = [12414, 55, 124, 888, 62365, 11]
# new_list = []

# for number in numbers:
#     digits = str(number)
#     unique_digits = set(digits)
#     if len(digits) == len(unique_digits):
#         new_list.append(number)

# numbers = new_list
# print(numbers)


# for i in numbers:
#     if len(set(str(i))) == 1:
#         numbers.remove(i)
# print(numbers)
#6

# a, b = 6,12
# numbers = []
# for i in range(1, min(a,b) + 1):
#     if a % i == 0 and b % i == 0:
#         numbers.append(i)
# print(numbers)

#7
# result = []

# for i in range(3):
#     print(i)
#     row = [i * 3 + 1 + j for j in range(3)]
#     result.append(row)

# print(result)

#8
# a = 'aaa bbb ccc eee fff'.split(" ")
# del a[1::2]
# print(a)

#9
# def bank(a,years):
#     for i in range(years):
#         a = a + (a * 0.1)
#     return a
# a = int(input("Введите сумму вклада:"))
# years = int(input("На сколько лет?"))
# print(bank(a,years))